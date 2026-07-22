#!/usr/bin/env python3
"""CRP 项目打包工具（uniontech-crp-pack）- 完全独立，不依赖其他 skill 模块。

首次运行需在终端输入 OA/LDAP 账号密码，认证成功后缓存到本地。

用法:
  python3 crp_pack.py auth [--force] [--loginid UT003649]
  python3 crp_pack.py config [--force]
  python3 crp_pack.py test --topic DDE-V25-20260416 --project deepin-terminal-v25
  python3 crp_pack.py pack --topic DDE-V25-20260416 --project deepin-terminal-v25 [--branch upstream/master] [--tag 6.0.1-1]
  python3 crp_pack.py instances --topic DDE-V25-20260416
   python3 crp_pack.py topics --topic DDE-V25
   python3 crp_pack.py projects --project deepin-terminal
   python3 crp_pack.py branches snipe
"""
from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
import rsa
from cryptography.fernet import Fernet

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------

CRP_BASE_URL = "https://crp.uniontech.com"
_HEADERS_JSON = {"Content-Type": "application/json"}

_CRP_RSA_PUBKEY_PEM = b"""-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCkA9WqirWQII3D8/M9UG8X8ybQ
Ou+cPSNTgR9b4HenJ7A5zSfkXZnetb5q6MmKTJLGCl9MSsHveQPHmLGDG+xw2MlB
w3Yefd/jJ1Cg8pP69wlHRX+wiyh5p8KY55ehFNsQLm3kDGXgVJdtrZn/MiBOlCtE
fe9YvvT0lqy2BtBpaQIDAQAB
-----END PUBLIC KEY-----"""

_DEFAULT_CFG: Dict[str, Any] = {
    "archs":          "amd64;arm64;loong64;sw64;mips64el",
    "topic_type":     "test",
    "branch_id":      123,
    "default_branch": "upstream/master",
}

# ---------------------------------------------------------------------------
# 代理清理
# ---------------------------------------------------------------------------

def _clear_proxy() -> None:
    for k in ["https_proxy", "http_proxy", "ftp_proxy", "all_proxy",
              "HTTPS_PROXY", "HTTP_PROXY", "FTP_PROXY", "ALL_PROXY"]:
        os.environ.pop(k, None)

# ---------------------------------------------------------------------------
# 凭证存储（加密，与 uniontech-oa-lib 共享同一目录，不添加额外字段）
# ---------------------------------------------------------------------------

def _cred_dir() -> Path:
    env = os.getenv("UNIONTECH_OA_CONFIG_DIR")
    p = Path(env) if env else Path.home() / ".config" / "uniontech-oa"
    p.mkdir(parents=True, exist_ok=True)
    return p


def _fernet() -> Fernet:
    key_file = _cred_dir() / "key.bin"
    if key_file.exists():
        key = key_file.read_bytes()
    else:
        key = Fernet.generate_key()
        key_file.write_bytes(key)
        key_file.chmod(0o600)
    return Fernet(key)


def _save_creds(loginid: str, password: str) -> None:
    f = _fernet()
    data = {
        "loginid": loginid,
        "password_encrypted": f.encrypt(password.encode()).decode(),
        "saved_at": datetime.now().isoformat(),
        "metadata": {},
    }
    cred_file = _cred_dir() / "default.json"
    cred_file.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    cred_file.chmod(0o600)


def _load_creds() -> Optional[Dict[str, str]]:
    cred_file = _cred_dir() / "default.json"
    if not cred_file.exists():
        return None
    try:
        data = json.loads(cred_file.read_text())
        pwd = _fernet().decrypt(data["password_encrypted"].encode()).decode()
        return {"loginid": data["loginid"], "password": pwd}
    except Exception:
        return None

# ---------------------------------------------------------------------------
# CRP 专属配置（独立文件，明文，~/.config/uniontech-crp-pack/config.json）
# ---------------------------------------------------------------------------

def _crp_cfg_file() -> Path:
    p = Path.home() / ".config" / "uniontech-crp-pack"
    p.mkdir(parents=True, exist_ok=True)
    return p / "config.json"


def _load_crp_cfg() -> Dict[str, Any]:
    f = _crp_cfg_file()
    if f.exists():
        try:
            return {**_DEFAULT_CFG, **json.loads(f.read_text())}
        except Exception:
            pass
    return dict(_DEFAULT_CFG)


def _save_crp_cfg(cfg: Dict[str, Any]) -> None:
    _crp_cfg_file().write_text(json.dumps(cfg, ensure_ascii=False, indent=2))

# ---------------------------------------------------------------------------
# CRP 认证
# ---------------------------------------------------------------------------

def _encrypt_password(plain: str) -> str:
    pub = rsa.PublicKey.load_pkcs1_openssl_pem(_CRP_RSA_PUBKEY_PEM)
    return base64.b64encode(rsa.encrypt(plain.encode(), pub)).decode()


def _fetch_auth(loginid: str, password: str) -> str:
    resp = requests.post(
        f"{CRP_BASE_URL}/api/login",
        headers=_HEADERS_JSON,
        json={"userName": loginid, "password": _encrypt_password(password)},
        timeout=30,
    )
    resp.raise_for_status()
    token = resp.json().get("Token", "")
    if not token:
        raise RuntimeError("CRP 登录失败：服务器未返回 Token")
    return token


def _ensure_auth(force: bool = False, loginid_hint: str = "") -> Dict[str, str]:
    """返回 {loginid, password, token}，无缓存或 force=True 时终端交互输入。"""
    if not force:
        creds = _load_creds()
        if creds:
            try:
                token = _fetch_auth(creds["loginid"], creds["password"])
                return {**creds, "token": token}
            except Exception:
                pass

    cached = _load_creds() or {}
    default_id = loginid_hint or cached.get("loginid", "")
    prompt = f"OA/LDAP loginid [{default_id}]: " if default_id else "OA/LDAP loginid: "
    loginid = input(prompt).strip() or default_id
    if not loginid:
        raise RuntimeError("未输入 loginid")
    password = getpass.getpass("OA/LDAP password: ")
    if not password:
        raise RuntimeError("未输入密码")

    token = _fetch_auth(loginid, password)
    _save_creds(loginid, password)
    return {"loginid": loginid, "password": password, "token": token}

# ---------------------------------------------------------------------------
# CRP API
# ---------------------------------------------------------------------------

def _auth_headers(token: str) -> Dict[str, str]:
    return {**_HEADERS_JSON, "Authorization": f"Bearer {token}"}


def _fetch_username(token: str) -> str:
    r = requests.get(f"{CRP_BASE_URL}/api/user", headers=_auth_headers(token), timeout=30)
    r.raise_for_status()
    return r.json().get("Name", "")


def _list_topics(token: str, keyword: str, cfg: Dict[str, Any]) -> List[Dict]:
    username = _fetch_username(token)
    r = requests.post(
        f"{CRP_BASE_URL}/api/topics/search",
        headers=_auth_headers(token),
        json={
            "TopicType": cfg["topic_type"],
            "UserName":  username,
            "BranchID":  cfg["branch_id"],
        },
        timeout=30,
    )
    r.raise_for_status()
    return [
        {"id": t["ID"], "name": t["Name"]}
        for t in (r.json() or [])
        if re.search(keyword, t.get("Name", ""), re.IGNORECASE)
    ]


def _list_projects(token: str, name_filter: str, cfg: Dict[str, Any]) -> List[Dict]:
    r = requests.post(
        f"{CRP_BASE_URL}/api/project",
        headers=_auth_headers(token),
        json={
            "page": 0, "perPage": 0,
            "projectGroupID": 0, "newCommit": False, "archived": False,
            "branchID": cfg["branch_id"],
            "name": name_filter,
        },
        timeout=30,
    )
    r.raise_for_status()
    return [
        {"id": p["ID"], "name": p["Name"], "url": p.get("RepoUrl", "")}
        for p in r.json().get("Projects", [])
        if re.search(name_filter or ".", p.get("Name", ""), re.IGNORECASE)
    ]


def _fetch_commit_msg(token: str, repo_url: str, commit: str) -> str:
    try:
        r = requests.post(
            f"{CRP_BASE_URL}/api/projects/getGerritCommitMessage",
            headers=_auth_headers(token),
            json={"repo_url": repo_url, "commit_id": commit},
            timeout=30,
        )
        r.raise_for_status()
        return r.json().get("message", "")
    except Exception:
        return ""


def _list_branches(token: str, project_id: int, project_url: str, branch_filter: str) -> List[Dict]:
    r = requests.get(
        f"{CRP_BASE_URL}/api/projects/{project_id}/branches",
        headers=_auth_headers(token), timeout=30,
    )
    r.raise_for_status()
    result = []
    for b in r.json():
        name = b.get("Name", "")
        if branch_filter and not re.search(branch_filter, name, re.IGNORECASE):
            continue
        commit = b.get("Commit", "")
        msg = _fetch_commit_msg(token, project_url, commit) or b.get("Message", "")
        result.append({"name": name, "commit": commit, "changelog": msg})
    return result


def _list_instances(token: str, topic_id: int) -> List[Dict]:
    r = requests.get(
        f"{CRP_BASE_URL}/api/topics/{topic_id}/releases",
        headers=_auth_headers(token), timeout=30,
    )
    r.raise_for_status()
    result = []
    for i in r.json():
        build_id    = i.get("BuildID", 0)
        build_state = i.get("BuildState", {}).get("state", "UNKNOWN")
        build_url   = "" if build_state == "UPLOAD_OK" else (
            f"https://shuttle.uniontech.com/#/tasks/task?taskid={build_id}" if build_id else ""
        )
        result.append({
            "id":           i["ID"],
            "project_name": i["ProjectName"],
            "branch":       i["Branch"],
            "tag":          i["Tag"],
            "build_state":  build_state,
            "build_url":    build_url,
        })
    return result


def _list_crp_branches(token: str, keyword: str) -> List[Dict]:
    """模糊搜索 CRP 平台分支 (ID + Name)，关键词可匹配 Name 或 Description。"""
    r = requests.get(
        f"{CRP_BASE_URL}/api/branches",
        headers=_auth_headers(token), timeout=30,
    )
    r.raise_for_status()
    result = []
    for b in r.json():
        name = b.get("Name", "")
        desc = b.get("Description", "")
        if not keyword or re.search(keyword, name, re.IGNORECASE) or re.search(keyword, desc, re.IGNORECASE):
            result.append({"id": b["ID"], "name": name, "description": desc})
    return result


def _delete_instance(token: str, instance_id: int) -> None:
    r = requests.delete(
        f"{CRP_BASE_URL}/api/topic_releases/{instance_id}",
        headers=_auth_headers(token), timeout=30,
    )
    r.raise_for_status()


def _create_instance(token: str, topic_id: int, project: Dict, branch: Dict,
                     tag: Optional[str], cfg: Dict[str, Any]) -> None:
    payload = {
        "Arches":         cfg["archs"],
        "BaseTag":        None,
        "Branch":         branch["name"],
        "BuildID":        0,
        "BuildState":     None,
        "Changelog":      [branch["changelog"]],
        "Commit":         branch["commit"],
        "History":        None,
        "ID":             0,
        "ProjectID":      project["id"],
        "ProjectName":    project["name"],
        "ProjectRepoUrl": project["url"],
        "SlaveNode":      None,
        "Tag":            tag or "",
        "TagSuffix":      None,
        "TopicID":        topic_id,
        "TopicType":      cfg["topic_type"],
        "ChangeLogMode":  tag is None,
        "RepoType":       "deb",
        "Custom":         True,
        "BranchID":       str(cfg["branch_id"]),
    }
    r = requests.post(
        f"{CRP_BASE_URL}/api/topics/{topic_id}/new_release",
        headers=_auth_headers(token), json=payload, timeout=30,
    )
    r.raise_for_status()

# ---------------------------------------------------------------------------
# 子命令实现
# ---------------------------------------------------------------------------

def _out(data: Any) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_auth(args: argparse.Namespace) -> int:
    cred = _ensure_auth(force=args.force, loginid_hint=args.loginid)
    _out({"success": True, "message": "CRP 认证成功，凭证已缓存", "loginid": cred["loginid"]})
    return 0


def cmd_config(args: argparse.Namespace) -> int:
    current = _load_crp_cfg()
    if not args.force and _crp_cfg_file().exists():
        _out({"success": True, "message": "当前配置", "config": current})
        return 0

    def _prompt(key: str, label: str, cast: Any = str) -> Any:
        val = input(f"{label} [{current[key]}]: ").strip()
        return cast(val) if val else current[key]

    cfg: Dict[str, Any] = {
        "topic_type":     _prompt("topic_type", "TopicType (如 test)"),
        "branch_id":      _prompt("branch_id", "BranchID (整数)", int),
        "default_branch": _prompt("default_branch", "默认分支"),
        "archs":          _prompt("archs", "架构列表 (分号分隔)"),
    }
    _save_crp_cfg(cfg)
    _out({"success": True, "message": "配置已保存", "config": cfg})
    return 0


def cmd_test(args: argparse.Namespace) -> int:
    cred = _ensure_auth()
    cfg = _load_crp_cfg()
    if args.branch_id is not None:
        cfg["branch_id"] = args.branch_id
    if args.archs:
        cfg["archs"] = args.archs
    token = cred["token"]
    branch_filter = args.branch or cfg["default_branch"]

    topics   = _list_topics(token, args.topic, cfg)
    projects = _list_projects(token, args.project, cfg)
    if not topics:
        _out({"success": False, "message": f"未找到主题: {args.topic!r}"}); return 1
    if not projects:
        _out({"success": False, "message": f"未找到项目: {args.project!r}"}); return 1

    items = []
    for t in topics:
        for p in projects:
            for b in _list_branches(token, p["id"], p["url"], branch_filter):
                items.append({"topic": t["name"], "project": p["name"],
                               "branch": b["name"], "changelog": b["changelog"]})
    if items:
        _out({"success": True, "message": f"将打包 {len(items)} 个组合", "items": items})
        return 0
    _out({"success": False, "message": "未找到匹配的 topic/project/branch 组合"})
    return 1


def cmd_pack(args: argparse.Namespace) -> int:
    cred = _ensure_auth()
    cfg = _load_crp_cfg()
    if args.branch_id is not None:
        cfg["branch_id"] = args.branch_id
    if args.archs:
        cfg["archs"] = args.archs
    token = cred["token"]
    branch_filter = args.branch or cfg["default_branch"]
    tag = args.tag or None

    topics   = _list_topics(token, args.topic, cfg)
    projects = _list_projects(token, args.project, cfg)
    if not topics:
        _out({"success": False, "message": f"未找到主题: {args.topic!r}"}); return 1
    if not projects:
        _out({"success": False, "message": f"未找到项目: {args.project!r}"}); return 1

    created, errors = [], []
    for t in topics:
        for p in projects:
            branches = _list_branches(token, p["id"], p["url"], branch_filter)
            if not branches:
                errors.append(f"{p['name']}: 未找到分支 {branch_filter!r}")
                continue
            for b in branches:
                for inst in _list_instances(token, t["id"]):
                    if inst["project_name"] == p["name"] and inst["branch"] == b["name"]:
                        _delete_instance(token, inst["id"])
                _create_instance(token, t["id"], p, b, tag, cfg)
                created.append(f"{t['name']} / {p['name']} / {b['name']}")

    if created:
        _out({"success": True, "message": f"已提交打包: {', '.join(created)}"})
        return 0
    _out({"success": False, "message": "\n".join(errors) or "未匹配到任何组合"})
    return 1


def cmd_instances(args: argparse.Namespace) -> int:
    cred = _ensure_auth()
    cfg = _load_crp_cfg()
    if args.branch_id is not None:
        cfg["branch_id"] = args.branch_id
    topics = _list_topics(cred["token"], args.topic, cfg)
    if not topics:
        _out({"success": False, "message": f"未找到主题: {args.topic!r}"}); return 1
    all_inst = []
    for t in topics:
        for inst in _list_instances(cred["token"], t["id"]):
            inst["topic_name"] = t["name"]
            all_inst.append(inst)
    _out({"success": True, "instances": all_inst, "message": f"共 {len(all_inst)} 个 instance"})
    return 0


def cmd_topics(args: argparse.Namespace) -> int:
    cred = _ensure_auth()
    cfg = _load_crp_cfg()
    if args.branch_id is not None:
        cfg["branch_id"] = args.branch_id
    result = _list_topics(cred["token"], args.topic, cfg)
    _out({"success": True, "topics": result, "message": f"找到 {len(result)} 个主题"})
    return 0


def cmd_projects(args: argparse.Namespace) -> int:
    cred = _ensure_auth()
    cfg = _load_crp_cfg()
    result = _list_projects(cred["token"], args.project or "", cfg)
    _out({"success": True, "projects": result, "message": f"找到 {len(result)} 个项目"})
    return 0


def cmd_branches(args: argparse.Namespace) -> int:
    cred = _ensure_auth()
    result = _list_crp_branches(cred["token"], args.keyword)
    _out({"success": True, "branches": result, "message": f"找到 {len(result)} 个分支"})
    return 0

# ---------------------------------------------------------------------------
# CLI 入口
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="CRP 项目打包工具")
    sub = p.add_subparsers(dest="command", required=True)

    a = sub.add_parser("auth", help="认证并缓存 OA/LDAP 凭证")
    a.add_argument("--loginid", default="", help="预填 loginid")
    a.add_argument("--force", action="store_true", help="忽略缓存，重新输入")

    c = sub.add_parser("config", help="配置 CRP 打包参数（topic_type/branch_id 等）")
    c.add_argument("--force", action="store_true", help="强制重新配置（即使已有配置）")

    for name in ("test", "pack"):
        s = sub.add_parser(name, help="测试打包组合" if name == "test" else "提交打包")
        s.add_argument("--topic",   required=True, help="CRP 主题名")
        s.add_argument("--project", required=True, help="CRP 项目名")
        s.add_argument("--branch",  default="", help="分支（默认 upstream/master）")
        s.add_argument("--branch-id", type=int, default=None, help="临时指定 BranchID（不持久化）")
        s.add_argument("--archs", default="", help="临时指定架构（分号分隔，如 amd64;arm64，不持久化）")
        if name == "pack":
            s.add_argument("--tag", default="", help="指定 tag（不填则自动递增）")

    i = sub.add_parser("instances", help="查看主题下已有打包实例")
    i.add_argument("--topic", required=True)
    i.add_argument("--branch-id", type=int, default=None, help="临时指定 BranchID（不持久化）")

    t = sub.add_parser("topics", help="搜索主题")
    t.add_argument("--topic", required=True)
    t.add_argument("--branch-id", type=int, default=None, help="临时指定 BranchID（不持久化）")

    pr = sub.add_parser("projects", help="搜索项目")
    pr.add_argument("--project", default="")

    b = sub.add_parser("branches", help="模糊搜索 CRP 平台分支")
    b.add_argument("keyword", nargs="?", default="", help="分支名称或描述关键词（留空列出全部）")

    return p


def main() -> int:
    _clear_proxy()
    args = _build_parser().parse_args()
    try:
        return {
            "auth":      cmd_auth,
            "config":    cmd_config,
            "test":      cmd_test,
            "pack":      cmd_pack,
            "instances": cmd_instances,
            "topics":    cmd_topics,
            "projects":  cmd_projects,
            "branches":  cmd_branches,
        }[args.command](args)
    except KeyboardInterrupt:
        _out({"success": False, "message": "用户取消输入"})
        return 130
    except Exception as exc:
        _out({"success": False, "message": str(exc)})
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
