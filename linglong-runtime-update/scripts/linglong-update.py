#!/usr/bin/env python3
"""DTK 玲珑 Runtime 更新自动化工具。

覆盖 org.deepin.runtime 和 org.deepin.runtime.webengine 的完整更新流程。

用法:
  python3 linglong-update.py                      # 交互式菜单
  python3 linglong-update.py auto --version 1.1.1.1
  python3 linglong-update.py crp-pack
  python3 linglong-update.py build-repo [--param xxx]
  python3 linglong-update.py update-repo --version 1.1.1.1 --repo-url http://...
  python3 linglong-update.py build-layer
  python3 linglong-update.py push-layer
  python3 linglong-update.py config
"""

from __future__ import annotations

import argparse
import getpass
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------

JENKINS_BASE = "https://jenkins.cicd.getdeepin.org"
JENKINS_REPO_UPDATE_JOB = "view/dtk/job/runtime-repo-update"
JENKINS_BUILD_JOB = "view/dtk/job/linglong-runtime-build"
JENKINS_PUSH_OLD_JOB = "view/dtk/job/linglong-runtime-push-to-old"
JENKINS_PUSH_TEST_JOB = "view/dtk/job/linglong-runtime-push-to-test"

N8N_FORM_URL = "https://n8n.cicd.getdeepin.org/form/097d0087-7f34-4614-8329-82d096af7ba5"
REPO_URL_PREFIX = "http://10.20.64.92:8080/crimson_runtime/stable_"

RUNTIME_REPO_URL = "https://github.com/linuxdeepin/org.deepin.runtime.git"
WEBENGINE_REPO_URL = "https://github.com/linuxdeepin/org.deepin.runtime.webengine.git"

CACHE_DIR = Path.home() / ".cache" / "linglong-update" / "repos"

DEFAULT_CONFIG: Dict[str, Any] = {
    "crp_topic": "玲珑runtime dtk版本更新",
    "crp_branch": "crimson-testing",
    "archs": ["arm64", "loong64", "mips64", "riscv64", "sw64"],
    "crp_branch_id": 123,
    "runtime_repo_path": str(CACHE_DIR / "org.deepin.runtime"),
    "webengine_repo_path": str(CACHE_DIR / "org.deepin.runtime.webengine"),
}

# DTK 项目列表（与 github-workflow-autotag 保持一致）
DTK_PROJECTS = [
    "dtkcommon", "dtklog", "dtkcore", "dtkgui", "dtkwidget",
    "dtkdeclarative", "qt5integration", "qt5platform-plugins",
]

STATE_FILE = Path.home() / ".config" / "linglong-update" / "state.json"


# ---------------------------------------------------------------------------
# 配置管理
# ---------------------------------------------------------------------------

def _config_dir() -> Path:
    p = Path.home() / ".config" / "linglong-update"
    p.mkdir(parents=True, exist_ok=True)
    return p


def load_config() -> Dict[str, Any]:
    f = _config_dir() / "config.json"
    if f.exists():
        try:
            return {**DEFAULT_CONFIG, **json.loads(f.read_text())}
        except Exception:
            pass
    return dict(DEFAULT_CONFIG)


def save_config(cfg: Dict[str, Any]) -> None:
    (_config_dir() / "config.json").write_text(
        json.dumps(cfg, ensure_ascii=False, indent=2))


def load_state() -> Dict[str, Any]:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {}


def save_state(state: Dict[str, Any]) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2))


def clear_state() -> None:
    if STATE_FILE.exists():
        STATE_FILE.unlink()


# ---------------------------------------------------------------------------
# Jenkins 凭证
# ---------------------------------------------------------------------------

def _jenkins_cred_file() -> Path:
    return _config_dir() / "jenkins_creds.json"


def _load_jenkins_creds() -> Optional[Dict[str, str]]:
    cf = _jenkins_cred_file()
    if not cf.exists():
        return None
    try:
        import base64
        data = json.loads(cf.read_text())
        return {
            "user": base64.b64decode(data["u"].encode()).decode(),
            "password": base64.b64decode(data["p"].encode()).decode(),
        }
    except Exception:
        return None


def _save_jenkins_creds(user: str, password: str) -> None:
    import base64
    data = {
        "u": base64.b64encode(user.encode()).decode(),
        "p": base64.b64encode(password.encode()).decode(),
    }
    _jenkins_cred_file().write_text(json.dumps(data))
    _jenkins_cred_file().chmod(0o600)


def _ensure_jenkins_auth(force: bool = False) -> Dict[str, str]:
    if not force:
        creds = _load_jenkins_creds()
        if creds:
            return creds
    default_user = "yeshanshan"
    user = input(f"Jenkins 用户名 [{default_user}]: ").strip() or default_user
    password = getpass.getpass("Jenkins 密码: ")
    if not password:
        raise RuntimeError("Jenkins 密码不能为空")
    _save_jenkins_creds(user, password)
    return {"user": user, "password": password}


# ---------------------------------------------------------------------------
# CRP 打包（内置，不依赖外部 crp_pack.py）
# ---------------------------------------------------------------------------

CRP_BASE_URL = "https://crp.uniontech.com"
_CRP_RSA_PUBKEY = b"""-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCkA9WqirWQII3D8/M9UG8X8ybQ
Ou+cPSNTgR9b4HenJ7A5zSfkXZnetb5q6MmKTJLGCl9MSsHveQPHmLGDG+xw2MlB
w3Yefd/jJ1Cg8pP69wlHRX+wiyh5p8KY55ehFNsQLm3kDGXgVJdtrZn/MiBOlCtE
fe9YvvT0lqy2BtBpaQIDAQAB
-----END PUBLIC KEY-----"""


def _crp_cred_file() -> Path:
    return _config_dir() / "crp_creds.json"


def _load_crp_creds() -> Optional[Dict[str, str]]:
    cf = _crp_cred_file()
    if not cf.exists():
        return None
    try:
        import base64 as _b64
        data = json.loads(cf.read_text())
        return {
            "loginid": _b64.b64decode(data["u"].encode()).decode(),
            "password": _b64.b64decode(data["p"].encode()).decode(),
        }
    except Exception:
        return None


def _save_crp_creds(loginid: str, password: str) -> None:
    import base64 as _b64
    data = {"u": _b64.b64encode(loginid.encode()).decode(),
            "p": _b64.b64encode(password.encode()).decode()}
    _crp_cred_file().write_text(json.dumps(data))
    _crp_cred_file().chmod(0o600)


def _cached_crp_token() -> Optional[str]:
    cf = _config_dir() / "crp_token.json"
    if cf.exists():
        try:
            return json.loads(cf.read_text()).get("token")
        except Exception:
            pass
    return None


def _save_crp_token(token: str) -> None:
    (_config_dir() / "crp_token.json").write_text(json.dumps({"token": token}))


def _fetch_crp_token(loginid: str, password: str) -> str:
    try:
        import rsa as _rsa
        import base64 as _b64
        pub = _rsa.PublicKey.load_pkcs1_openssl_pem(_CRP_RSA_PUBKEY)
        enc = _b64.b64encode(_rsa.encrypt(password.encode(), pub)).decode()
    except ImportError:
        _log("rsa 模块未安装，明文发送密码", "WARN")
        enc = password
    resp = requests.post(
        f"{CRP_BASE_URL}/api/login",
        headers={"Content-Type": "application/json"},
        json={"userName": loginid, "password": enc}, timeout=30)
    resp.raise_for_status()
    token = resp.json().get("Token", "")
    if not token:
        raise RuntimeError("CRP 登录失败: 服务器未返回 Token")
    return token


class _CRPClient:
    def __init__(self, token: str):
        self.s = requests.Session()
        self.s.trust_env = False  # CRP 内网，不走代理
        self.s.headers.update({"Content-Type": "application/json",
                               "Authorization": f"Bearer {token}"})

    def _get(self, path):
        r = self.s.get(f"{CRP_BASE_URL}{path}", timeout=30)
        r.raise_for_status()
        return r.json()

    def _post(self, path, data):
        r = self.s.post(f"{CRP_BASE_URL}{path}", json=data, timeout=30)
        r.raise_for_status()
        return r.json()

    def search_topics(self, keyword, branch_id=123):
        user = self._get("/api/user").get("Name", "")
        data = self._post("/api/topics/search",
                          {"TopicType": "test", "UserName": user,
                           "BranchID": branch_id})
        return [{"id": t["ID"], "name": t["Name"]}
                for t in (data or [])
                if re.search(keyword, t.get("Name", ""), re.IGNORECASE)]

    def search_projects(self, keyword, branch_id=123):
        data = self._post("/api/project",
                          {"page": 0, "perPage": 0, "projectGroupID": 0,
                           "newCommit": False, "archived": False,
                           "branchID": branch_id, "name": keyword})
        return [{"id": p["ID"], "name": p["Name"],
                 "url": p.get("RepoUrl", "")}
                for p in data.get("Projects", [])]

    def list_branches(self, pid, purl, bfilter):
        data = self._get(f"/api/projects/{pid}/branches")
        result = []
        for b in data:
            name = b.get("Name", "")
            if bfilter and not re.search(bfilter, name, re.IGNORECASE):
                continue
            commit = b.get("Commit", "")
            msg = b.get("Message", "") or self._commit_msg(purl, commit)
            result.append({"name": name, "commit": commit, "changelog": msg})
        return result

    def _commit_msg(self, repo_url, commit):
        try:
            return self._post("/api/projects/getGerritCommitMessage",
                              {"repo_url": repo_url, "commit_id": commit}
                              ).get("message", "")
        except Exception:
            return ""

    def list_instances(self, topic_id):
        return [{"id": i["ID"], "project_name": i["ProjectName"],
                 "branch": i["Branch"], "tag": i["Tag"]}
                for i in self._get(f"/api/topics/{topic_id}/releases")]

    def delete_instance(self, iid):
        self.s.delete(f"{CRP_BASE_URL}/api/topic_releases/{iid}", timeout=30)

    def create_instance(self, topic_id, proj, branch, archs, branch_id, tag=""):
        data = {"Arches": archs, "BaseTag": None, "Branch": branch["name"],
                "BuildID": 0, "BuildState": None,
                "Changelog": [branch["changelog"]],
                "Commit": branch["commit"], "History": None, "ID": 0,
                "ProjectID": proj["id"], "ProjectName": proj["name"],
                "ProjectRepoUrl": proj["url"], "SlaveNode": None,
                "Tag": tag, "TagSuffix": None, "TopicID": topic_id,
                "TopicType": "test", "ChangeLogMode": True,
                "RepoType": "deb", "Custom": True,
                "BranchID": str(branch_id)}
        self._post(f"/api/topics/{topic_id}/new_release", data)


def _ensure_crp_auth():
    token = _cached_crp_token()
    if token:
        try:
            c = _CRPClient(token)
            c._get("/api/user")
            return c
        except Exception:
            pass
    creds = _load_crp_creds()
    if not creds:
        loginid = input("OA/LDAP loginid: ").strip()
        if not loginid:
            raise RuntimeError("loginid 不能为空")
        password = getpass.getpass("OA/LDAP 密码: ")
        if not password:
            raise RuntimeError("密码不能为空")
    else:
        loginid, password = creds["loginid"], creds["password"]
    token = _fetch_crp_token(loginid, password)
    _save_crp_creds(loginid, password)
    _save_crp_token(token)
    return _CRPClient(token)


def _crp_pack_one(crp, topic, proj_name, bfilter, archs, branch_id, tag=""):
    topics = crp.search_topics(topic, branch_id)
    if not topics:
        raise RuntimeError(f"未找到 Topic: {topic}")
    projects = crp.search_projects(proj_name, branch_id)
    if not projects:
        raise RuntimeError(f"未找到项目: {proj_name}")
    t, p = topics[0], projects[0]
    branches = crp.list_branches(p["id"], p["url"], bfilter)
    if not branches:
        raise RuntimeError(f"未找到分支: {bfilter}")
    for b in branches:
        for inst in crp.list_instances(t["id"]):
            if inst["project_name"] == p["name"] and inst["branch"] == b["name"]:
                crp.delete_instance(inst["id"])
        crp.create_instance(t["id"], p, b, archs, branch_id, tag)


# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------


def _log(msg: str, level: str = "INFO") -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] [{level}] {msg}", file=sys.stderr)


def _run(cmd: List[str], cwd: Optional[str] = None, check: bool = True,
         capture: bool = False) -> subprocess.CompletedProcess:
    _log(f"执行: {' '.join(cmd)}")
    return subprocess.run(cmd, cwd=cwd, check=check,
                          capture_output=capture, text=True)


def _run_gh(args: List[str], cwd: Optional[str] = None) -> subprocess.CompletedProcess:
    _log(f"执行: gh {' '.join(args)}")
    return subprocess.run(["gh"] + args, cwd=cwd, check=True,
                          capture_output=True, text=True)


def _check_gh_auth() -> bool:
    try:
        result = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True, text=True,
)
        return result.returncode == 0
    except Exception:
        return False


def _input_confirm(msg: str, default: bool = True) -> bool:
    suffix = " [Y/n]: " if default else " [y/N]: "
    resp = input(msg + suffix).strip().lower()
    if not resp:
        return default
    return resp in ("y", "yes")


# ---------------------------------------------------------------------------
# 仓库管理
# ---------------------------------------------------------------------------

def _ensure_repo_cloned(repo_url: str, local_path: str, label: str) -> bool:
    p = Path(local_path)
    if p.is_dir() and (p / ".git").is_dir():
        _log(f"{label} 仓库已存在: {local_path}")
        return True
    _log(f"克隆 {label}: {repo_url}")
    parent = p.parent
    parent.mkdir(parents=True, exist_ok=True)
    try:
        _run(["git", "clone", repo_url, str(p)], cwd=str(parent))
        _log(f"{label} 克隆完成: {local_path}")
        return True
    except subprocess.CalledProcessError as e:
        _log(f"克隆失败 {label}: {e}", "ERROR")
        return False


def _ensure_repos_ready(cfg: Dict[str, Any]) -> bool:
    ok = True
    if not _ensure_repo_cloned(RUNTIME_REPO_URL, cfg["runtime_repo_path"],
                                "org.deepin.runtime"):
        ok = False
    if not _ensure_repo_cloned(WEBENGINE_REPO_URL, cfg["webengine_repo_path"],
                                "org.deepin.runtime.webengine"):
        ok = False
    return ok


# ---------------------------------------------------------------------------
# Jenkins 交互
# ---------------------------------------------------------------------------

class JenkinsClient:
    def __init__(self, user: str, password: str):
        self.user = user
        self.session = requests.Session()
        self.session.auth = (user, password)
        self.session.trust_env = False  # Jenkins 内网，不走代理
        self.session.headers.update({"User-Agent": "linglong-update/1.0"})

    def _api_url(self, job_path: str) -> str:
        return f"{JENKINS_BASE}/{job_path}/api/json"

    def _build_url(self, job_path: str) -> str:
        return f"{JENKINS_BASE}/{job_path}/build"

    def _build_params_url(self, job_path: str) -> str:
        return f"{JENKINS_BASE}/{job_path}/buildWithParameters"

    def trigger_build(self, job_path: str,
                      params: Optional[Dict[str, str]] = None) -> Optional[int]:
        if params:
            url = self._build_params_url(job_path)
            resp = self.session.post(url, data=params, timeout=60)
        else:
            url = self._build_url(job_path)
            resp = self.session.post(url, timeout=60)
        if resp.status_code in (200, 201, 302):
            _log(f"构建已触发, HTTP {resp.status_code}")
            time.sleep(3)
            return self._get_next_build_number(job_path)
        else:
            _log(f"触发失败: {resp.status_code} {resp.text[:200]}", "ERROR")
            return None

    def _get_next_build_number(self, job_path: str) -> Optional[int]:
        try:
            resp = self.session.get(self._api_url(job_path), timeout=30)
            last = resp.json().get("lastBuild", {})
            return last.get("number", 0) + 1
        except Exception:
            return None

    def get_build_status(self, job_path: str,
                         build_number: int) -> Dict[str, Any]:
        url = f"{JENKINS_BASE}/{job_path}/{build_number}/api/json"
        resp = self.session.get(url, timeout=30)
        data = resp.json()
        return {"result": data.get("result"),
                "building": data.get("building", False),
                "url": data.get("url", ""), "number": build_number}

    def get_last_build_status(self, job_path: str) -> Dict[str, Any]:
        url = f"{JENKINS_BASE}/{job_path}/lastBuild/api/json"
        resp = self.session.get(url, timeout=30)
        data = resp.json()
        return {"result": data.get("result"),
                "building": data.get("building", False),
                "url": data.get("url", ""), "number": data.get("number", 0)}

    def wait_for_build(self, job_path: str, build_number: int,
                       poll_interval: int = 30, timeout: int = 3600) -> bool:
        _log(f"等待构建 #{build_number} (超时 {timeout}s)...")
        start = time.time()
        while time.time() - start < timeout:
            try:
                status = self.get_build_status(job_path, build_number)
            except Exception as e:
                _log(f"轮询异常: {e}, 重试中...", "WARN")
                time.sleep(poll_interval)
                continue
            if not status["building"]:
                if status["result"] == "SUCCESS":
                    _log(f"构建 #{build_number} 成功!")
                    return True
                else:
                    _log(f"构建 #{build_number}: {status['result']}", "ERROR")
                    return False
            elapsed = int(time.time() - start)
            _log(f"构建 #{build_number} 进行中... ({elapsed}s)")
            time.sleep(poll_interval)
        _log(f"构建 #{build_number} 超时", "ERROR")
        return False

    def get_console_output(self, job_path: str, build_number: int) -> str:
        url = f"{JENKINS_BASE}/{job_path}/{build_number}/consoleText"
        resp = self.session.get(url, timeout=60)
        return resp.text

    def get_build_trend(self, job_path: str) -> List[Dict[str, Any]]:
        url = (f"{JENKINS_BASE}/{job_path}/api/json"
               "?tree=builds[number,result,building,url,timestamp]")
        resp = self.session.get(url, timeout=30)
        return resp.json().get("builds", [])

    def job_exists(self, job_path: str) -> bool:
        try:
            return self.session.get(
                self._api_url(job_path), timeout=30).status_code == 200
        except Exception:
            return False


def _extract_repo_url(console: str) -> Optional[str]:
    pattern = r'http://10\.20\.64\.92:8080/crimson_runtime/stable_[^\s"]+/'
    m = re.search(pattern, console)
    return m.group(0) if m else None


# ---------------------------------------------------------------------------
# Step 1: CRP 打包
# ---------------------------------------------------------------------------

def crp_pack(cfg: Dict[str, Any], topic: Optional[str] = None,
               branch: Optional[str] = None, archs: Optional[str] = None,
               branch_id: Optional[int] = None, version: Optional[str] = None,
               dry_run: bool = False) -> bool:
    _log("=" * 60)
    _log("CRP 打包")
    _log("=" * 60)

    if topic is None:
        topic = cfg["crp_topic"]
    if branch is None:
        branch = cfg["crp_branch"]
    if archs is None:
        archs = ";".join(cfg["archs"])
    if branch_id is None:
        branch_id = cfg.get("crp_branch_id", 123)
    if version is None:
        version = ""

    print(f"\n  Topic   : {topic}")
    print(f"  分支    : {branch}")
    print(f"  架构    : {archs}")
    print(f"  版本/tag: {version or '(默认)'}")
    print(f"  项目    : {', '.join(DTK_PROJECTS)}\n")

    if dry_run:
        _log("DRY RUN — 不会实际提交", "WARN")
        return True

    if not _input_confirm(f"确认对 {len(DTK_PROJECTS)} 个项目执行 CRP 打包?"):
        _log("用户取消", "WARN")
        return False

    crp = _ensure_crp_auth()
    failed = []
    for proj in DTK_PROJECTS:
        _log(f"打包 {proj}...")
        try:
            _crp_pack_one(crp, topic, proj, branch, archs, branch_id, version)
            _log(f"✓ {proj}")
        except Exception as e:
            _log(f"✗ {proj}: {e}", "ERROR")
            failed.append(proj)

    if failed:
        _log(f"{len(failed)} 个项目失败: {failed}", "WARN")
    _log("CRP 打包完成")
    return len(failed) == 0


# ---------------------------------------------------------------------------
# Step 2: 制作更新仓库
# ---------------------------------------------------------------------------

def build_repo(cfg: Dict[str, Any], repo_id: Optional[str] = None,
               dry_run: bool = False) -> Optional[str]:
    _log("=" * 60)
    _log("制作更新仓库")
    _log("=" * 60)

    if repo_id is None:
        repo_id = input("仓库标识 (默认当天日期): ").strip()
        if not param:
            param = datetime.now().strftime("%Y%m%d")

    print(f"\n  标识: {repo_id}\n")

    creds = _ensure_jenkins_auth()
    jc = JenkinsClient(creds["user"], creds["password"])
    if not jc.job_exists(JENKINS_REPO_UPDATE_JOB):
        _log(f"Job 不存在: {JENKINS_REPO_UPDATE_JOB}", "ERROR")
        return None

    if dry_run:
        _log(f"DRY RUN — 将触发参数: repo_id={repo_id}", "WARN")
        return f"{REPO_URL_PREFIX}{repo_id}/"

    _log(f"触发: {JENKINS_REPO_UPDATE_JOB}")
    build_num = jc.trigger_build(JENKINS_REPO_UPDATE_JOB, {"param": repo_id})
    if not build_num:
        _log("未能获取构建编号", "ERROR")
        return None

    _log(f"构建 #{build_num}: {JENKINS_BASE}/{JENKINS_REPO_UPDATE_JOB}/{build_num}/")

    if not jc.wait_for_build(JENKINS_REPO_UPDATE_JOB, build_num):
        return None

    console = jc.get_console_output(JENKINS_REPO_UPDATE_JOB, build_num)
    repo_url = _extract_repo_url(console)
    if repo_url:
        print(f"\n  仓库地址: {repo_url}\n")
    else:
        repo_url = f"{REPO_URL_PREFIX}{repo_id}/"
        _log(f"推测仓库地址: {repo_url}")
    return repo_url


# ---------------------------------------------------------------------------
# Step 3: 仓库更新与 PR
# ---------------------------------------------------------------------------

def update_repo(cfg: Dict[str, Any], version: Optional[str] = None,
                deb_repo: Optional[str] = None, dry_run: bool = False) -> bool:
    _log("=" * 60)
    _log("修改 yaml 文件并创建 PR")
    _log("=" * 60)

    if deb_repo is None:
        deb_repo = input("deb 更新仓库地址 (如 http://10.20.64.92:8080/crimson_runtime/stable_xxx/): ").strip()

    if version is None:
        try:
            version = _infer_version(cfg)
        except Exception as e:
            _log(f"自动推断版本失败: {e}", "WARN")
            version = input("版本号 (如 6.7.0.45): ").strip()

    print(f"\n  版本号  : {version}")
    print(f"  deb 仓库: {deb_repo}\n")

    if not _check_gh_auth():
        _log("gh CLI 未认证，请先执行: gh auth login", "ERROR")
        return False

    if not _ensure_repos_ready(cfg):
        return False

    if dry_run:
        _log("DRY RUN — 不会实际提交", "WARN")
        return True

    if not _update_single_repo("org.deepin.runtime", cfg["runtime_repo_path"],
                                version, deb_repo):
        return False
    if not _update_single_repo("org.deepin.runtime.webengine",
                                cfg["webengine_repo_path"], version, deb_repo,
                                apply_patch=_find_webengine_patch()):
        return False

    _log("仓库更新完成")
    return True


def _infer_version(cfg: Dict[str, Any]) -> str:
    """从 CRP 获取 dtkcore 打包 tag，计算玲珑 runtime 版本。

    优先从 CRP 平台读取 dtkcore 在对应 topic 下的打包实例 tag，
    若失败则回退到 GitHub dtkcore VERSION 文件。

    玲珑版本格式 X.Y.0.Z，与 DTK 版本 X.Y.Z 一一对应。
    例如 DTK 6.7.46 → 玲珑 6.7.0.46。
    """
    topic = cfg.get("crp_topic", "玲珑runtime dtk版本更新")
    branch_id = cfg.get("crp_branch_id", 123)

    try:
        crp = _ensure_crp_auth()
        topics = crp.search_topics(topic, branch_id)
        if topics:
            instances = crp.list_instances(topics[0]["id"])
            for inst in instances:
                if inst.get("project_name") == "dtkcore":
                    tag = inst.get("tag", "")
                    if tag:
                        _log(f"CRP dtkcore tag: {tag}")
                        parts = tag.split(".")
                        if len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
                            new_ver = f"{parts[0]}.{parts[1]}.0.{parts[2]}"
                            _log(f"玲珑推断版本: {new_ver}")
                            return new_ver
                        _log(f"CRP tag 格式异常: {tag}", "WARN")
                        break
        _log("CRP 未找到 dtkcore 实例或 tag 为空，回退到 GitHub", "WARN")
    except Exception as e:
        _log(f"CRP 查询失败: {e}，回退到 GitHub", "WARN")

    # 回退：从 GitHub 获取
    url = "https://raw.githubusercontent.com/linuxdeepin/dtkcore/master/VERSION"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        dtk_ver = resp.text.strip()
    except Exception as e:
        raise RuntimeError(f"无法获取 DTK VERSION: {e}")

    _log(f"DTK 当前版本: {dtk_ver}")
    parts = dtk_ver.split(".")
    if len(parts) < 2 or not parts[0].isdigit() or not parts[1].isdigit():
        raise RuntimeError(f"DTK 版本格式异常: {dtk_ver}")
    patch = int(parts[2]) if len(parts) >= 3 and parts[2].isdigit() else 0
    new_ver = f"{parts[0]}.{parts[1]}.0.{patch}"
    _log(f"玲珑推断版本: {new_ver}")
    return new_ver


def _find_webengine_patch() -> Optional[str]:
    candidates = [
        Path(__file__).resolve().parent.parent / "assets" / "webengine.patch",
        _config_dir() / "webengine.patch",
    ]
    for c in candidates:
        if c.exists() and c.stat().st_size > 100:
            return str(c)
    _log("webengine.patch 未找到或为空，请放置到 assets/ 或 ~/.config/linglong-update/", "WARN")
    return None


def _update_single_repo(label: str, repo_path: str, version: str,
                        deb_repo: str, apply_patch: Optional[str] = None) -> bool:
    _log(f"--- {label} ---")
    _run(["git", "-C", repo_path, "fetch", "origin"])
    try:
        _run(["git", "-C", repo_path, "checkout", "main"])
    except subprocess.CalledProcessError:
        _run(["git", "-C", repo_path, "checkout", "master"])
    try:
        _run(["git", "-C", repo_path, "pull", "origin"])
    except subprocess.CalledProcessError:
        _log("Pull 失败，继续...", "WARN")

    ts = datetime.now().strftime("%Y%m%d%H%M")
    branch = f"update/linglong-runtime-{version}-{ts}"
    _log(f"创建分支: {branch}")
    _run(["git", "-C", repo_path, "checkout", "-b", branch])

    if apply_patch:
        _log(f"应用补丁: {apply_patch}")
        try:
            _run(["git", "-C", repo_path, "apply", apply_patch])
            _log("补丁应用成功")
        except subprocess.CalledProcessError:
            _log("git apply 失败，尝试三路合并...", "WARN")
            try:
                _run(["git", "-C", repo_path, "apply", "--3way", apply_patch])
                _log("三路合并成功")
            except subprocess.CalledProcessError:
                _log("补丁应用彻底失败，检查冲突", "ERROR")
                return False

    _update_version_in_yaml(repo_path, version)
    _update_repo_url_in_yaml(repo_path, deb_repo)

    daily = os.path.join(repo_path, "daily.bash")
    if os.path.exists(daily):
        _log("执行 daily.bash...")
        _run(["bash", daily], cwd=repo_path)
    else:
        _log("daily.bash 不存在", "WARN")

    _run(["git", "-C", repo_path, "add", "-A"])
    msg = (f"chore: update linglong runtime to {version}\n\n"
           f"Update repo URL to {deb_repo}\nVersion: {version}\n\n"
           f"Log: 更新玲珑 runtime 到 {version}\n"
           f"Influence: 更新 DTK 玲珑 runtime 依赖仓库地址和版本")
    _run(["git", "-C", repo_path, "commit", "-m", msg])

    _log("推送分支...")
    _run(["git", "-C", repo_path, "push", "origin", branch])

    _log("创建 PR...")
    result = _run_gh(["pr", "create",
                      "--title", f"chore: update linglong runtime to {version}",
                      "--body", f"Update repo URL to {deb_repo}\nVersion: {version}",
                      "--base", "main", "--head", branch], cwd=repo_path)
    pr_url = result.stdout.strip()
    print(f"\n  PR: {pr_url}\n")

    if _input_confirm(f"等待 {label} PR 合并?"):
        _wait_for_pr_merge(label, repo_path, pr_url)
    return True


def _update_version_in_yaml(repo_path: str, version: str) -> None:
    yp = os.path.join(repo_path, "linglong.yaml")
    if not os.path.exists(yp):
        _log("linglong.yaml 不存在", "WARN")
        return
    content = Path(yp).read_text()
    new_c = re.sub(r'(version:\s*)\S+', f'\\g<1>{version}', content)
    if new_c != content:
        Path(yp).write_text(new_c)
        _log(f"版本号已更新为 {version}")


def _update_repo_url_in_yaml(repo_path: str, repo_url: str) -> None:
    yp = os.path.join(repo_path, "linglong.yaml")
    if not os.path.exists(yp):
        _log("linglong.yaml 不存在", "WARN")
        return
    content = Path(yp).read_text()
    pat = r'http://10\.20\.64\.92:8080/crimson_runtime/stable_[^\s"\']+/'
    new_c = re.sub(pat, repo_url, content)
    if new_c != content:
        Path(yp).write_text(new_c)
        _log(f"仓库地址已更新为 {repo_url}")


def _wait_for_pr_merge(label: str, repo_path: str, pr_url: str,
                       timeout: int = 600) -> bool:
    _log(f"等待 {label} PR 合并...")
    start = time.time()
    pr_num = pr_url.rstrip("/").split("/")[-1]
    while time.time() - start < timeout:
        try:
            r = _run_gh(["pr", "view", pr_num, "--json", "state,mergedAt"],
                        cwd=repo_path)
            d = json.loads(r.stdout)
            if d.get("mergedAt"):
                _log(f"{label} PR #{pr_num} 已合并!")
                _run(["git", "-C", repo_path, "checkout", "main"])
                _run(["git", "-C", repo_path, "pull", "origin", "main"])
                return True
            if d.get("state") == "CLOSED":
                _log(f"{label} PR #{pr_num} 已关闭 (未合并)", "WARN")
                return False
        except Exception:
            pass
        _log(f"{label} PR #{pr_num} 仍在开放，等待...")
        time.sleep(30)
    _log(f"等待 {label} PR 合并超时", "WARN")
    return False


# ---------------------------------------------------------------------------
# Step 4: 构建玲珑 Layer
# ---------------------------------------------------------------------------

def build_layer(cfg: Dict[str, Any], repo_url: Optional[str] = None,
               repo_branch: Optional[str] = None, dry_run: bool = False) -> bool:
    """触发 Jenkins 构建玲珑 Layer。

    repo_url: REPO_URL 参数，默认 github.com/linglongdev/org.deepin.runtime
    repo_branch: REPO_BRANCH 参数，默认 main
    """
    _log("=" * 60)
    _log("构建玲珑 Layer")
    _log("=" * 60)

    creds = _ensure_jenkins_auth()
    jc = JenkinsClient(creds["user"], creds["password"])
    if not jc.job_exists(JENKINS_BUILD_JOB):
        _log(f"Job 不存在: {JENKINS_BUILD_JOB}", "ERROR")
        return False

    if repo_url is None:
        repo_url = input("REPO_URL [github.com/linglongdev/org.deepin.runtime]: ").strip()
        if not repo_url:
            repo_url = "github.com/linglongdev/org.deepin.runtime"
    if repo_branch is None:
        repo_branch = input("REPO_BRANCH [main]: ").strip() or "main"

    print(f"\n  REPO_URL    : {repo_url}")
    print(f"  REPO_BRANCH : {repo_branch}\n")

    if dry_run:
        _log("DRY RUN", "WARN")
        return True

    params = {"REPO_URL": repo_url, "REPO_BRANCH": repo_branch}
    _log(f"触发: {JENKINS_BUILD_JOB} params={params}")
    build_num = jc.trigger_build(JENKINS_BUILD_JOB, params)
    if not build_num:
        _log("未能获取构建编号", "ERROR")
        return False

    _log(f"构建 #{build_num}: {JENKINS_BASE}/{JENKINS_BUILD_JOB}/{build_num}/")
    ok = jc.wait_for_build(JENKINS_BUILD_JOB, build_num)
    if ok:
        _log("Layer 构建完成")
    return ok


# ---------------------------------------------------------------------------
# Step 5: N8N 推送
# ---------------------------------------------------------------------------

def push_layer(cfg: Dict[str, Any], layer_url: Optional[str] = None,
               dry_run: bool = False) -> bool:
    """N8N 推送 Layer 到玲珑仓库。

    layer_url: LAYER_URL 参数，对应 build-layer 产出的 layer 地址。
    先提交 N8N 表单，然后触发 Jenkins push-to-old 和 push-to-test。
    """
    _log("=" * 60)
    _log("N8N 推送 Layer")
    _log("=" * 60)

    creds = _ensure_jenkins_auth()
    jc = JenkinsClient(creds["user"], creds["password"])

    if layer_url is None:
        layer_url = input("LAYER_URL (如 http://10.20.64.92:8080/crimson_runtime/stable_xxx/): ").strip()

    print(f"\n  LAYER_URL: {layer_url}")
    print(f"  N8N 表单 : {N8N_FORM_URL}\n")

    if dry_run:
        _log("DRY RUN", "WARN")
        return True

    print("请手动提交 N8N 表单后，脚本将自动触发 Jenkins push job。")
    if not _input_confirm("已提交 N8N 表单?"):
        _log("用户取消", "WARN")
        return False

    params = {"LAYER_URL": layer_url}
    for label, job in [("push-to-old", JENKINS_PUSH_OLD_JOB),
                       ("push-to-test", JENKINS_PUSH_TEST_JOB)]:
        _log(f"--- 触发 {label} ---")
        if not jc.job_exists(job):
            _log(f"Job 不可访问: {label}", "WARN")
            continue
        build_num = jc.trigger_build(job, params)
        if build_num:
            _log(f"构建 #{build_num}: {JENKINS_BASE}/{job}/{build_num}/")
            jc.wait_for_build(job, build_num)
        else:
            _log(f"触发 {label} 失败", "ERROR")

    _log("推送完成")
    return True


# ---------------------------------------------------------------------------
# 全自动模式
# ---------------------------------------------------------------------------

def auto_mode(cfg: Dict[str, Any], version: Optional[str] = None,
              repo_id: Optional[str] = None,
              deb_repo: Optional[str] = None,
              layer_url: Optional[str] = None,
              dry_run: bool = False, start_from: int = 1) -> bool:
    _log("=" * 60)

    if version is None:
        try:
            version = _infer_version(cfg)
        except Exception as e:
            _log(f"自动推断版本失败: {e}", "ERROR")
            return False
    _log(f"DTK 玲珑 Runtime 更新 - 自动模式 (v{version})")
    _log("=" * 60)

    if start_from <= 3 and not dry_run:
        if not _check_gh_auth():
            _log("gh CLI 未认证，请先执行: gh auth login", "ERROR")
            return False
        if not _ensure_repos_ready(cfg):
            return False

    clear_state()
    state: Dict[str, Any] = {"version": version,
                              "started_at": datetime.now().isoformat()}

    steps = [
        (1, "CRP 打包", lambda: crp_pack(cfg, version=version, dry_run=dry_run)),
        (2, "制作更新仓库", lambda: _auto_step2(cfg, state, repo_id, dry_run)),
        (3, "修改 yaml + PR", lambda: _auto_step3(cfg, state, version, deb_repo, dry_run)),
        (4, "构建玲珑 Layer", lambda: build_layer(cfg, dry_run=dry_run)),
        (5, "N8N 推送 Layer", lambda: _auto_step5(cfg, state, layer_url, dry_run)),
    ]

    for snum, sname, sfn in steps:
        if snum < start_from:
            _log(f"跳过步骤 {snum} ({sname}) — start_from={start_from}")
            continue

        _log(f"\n>>> 步骤 {snum}: {sname}")
        state["current_step"] = snum
        save_state(state)

        try:
            result = sfn()
            if result is False:
                _log(f"步骤 {snum} 失败，状态已保存", "ERROR")
                return False
            state[f"step_{snum}_complete"] = True
            save_state(state)
        except Exception as e:
            _log(f"步骤 {snum} 异常: {e}", "ERROR")
            import traceback
            traceback.print_exc()
            save_state(state)
            return False

    _log("=" * 60)
    _log("全部步骤完成!")
    _log("=" * 60)
    clear_state()
    return True


def _auto_step2(cfg, state, repo_id, dry_run):
    url = build_repo(cfg, repo_id, dry_run)
    if url:
        state["repo_url"] = url
        save_state(state)
    return url


def _auto_step3(cfg, state, version, deb_repo, dry_run):
    if not deb_repo:
        deb_repo = state.get("repo_url")
    if not deb_repo and not dry_run:
        _log("state 中没有 deb_repo，请先执行 build-repo", "ERROR")
        return False
    return update_repo(cfg, version, deb_repo or "DRY_RUN_URL", dry_run)


def _auto_step5(cfg, state, layer_url, dry_run):
    """auto 模式下 push-layer：优先用传入的 layer_url，否则用 state 中的 repo_url。"""
    if not layer_url:
        layer_url = state.get("repo_url") or state.get("layer_url")
    if not layer_url and not dry_run:
        layer_url = input("LAYER_URL: ").strip()
    return push_layer(cfg, layer_url, dry_run)


# ---------------------------------------------------------------------------
# 配置命令
# ---------------------------------------------------------------------------

def cmd_config() -> int:
    current = load_config()
    print("当前配置:")
    print(json.dumps(current, ensure_ascii=False, indent=2))
    print()

    def _p(key, label):
        v = input(f"{label} [{current.get(key)}]: ").strip()
        return v if v else current.get(key)

    cfg = {
        "crp_topic": _p("crp_topic", "CRP topic"),
        "crp_branch": _p("crp_branch", "CRP branch"),
        "runtime_repo_path": _p("runtime_repo_path", "runtime repo path"),
        "webengine_repo_path": _p("webengine_repo_path", "webengine repo path"),
    }

    archs_str = ",".join(current.get("archs", []))
    inp = input(f"架构 (逗号分隔) [{archs_str}]: ").strip()
    cfg["archs"] = [a.strip() for a in inp.split(",")] if inp else current.get("archs", [])

    save_config(cfg)
    print(f"配置已保存到 {_config_dir() / 'config.json'}")

    print()
    if _input_confirm("更新 Jenkins 凭证?"):
        user = input(f"Jenkins 用户名 [yeshanshan]: ").strip() or "yeshanshan"
        password = getpass.getpass("Jenkins 密码: ")
        if password:
            _save_jenkins_creds(user, password)
            print("Jenkins 凭证已更新")

    return 0


# ---------------------------------------------------------------------------
# 交互式菜单
# ---------------------------------------------------------------------------

_MENU = """
┌──────────────────────────────────────────────┐
│         DTK 玲珑 Runtime 更新工具             │
├──────────────────────────────────────────────┤
│  1. CRP 打包                                  │
│  2. 制作更新仓库                               │
│  3. 修改 yaml + 创建 PR                        │
│  4. 构建玲珑 Layer                             │
│  5. N8N 推送 Layer                             │
│  6. 配置参数                                   │
│  a. 自动执行全部 (auto)                        │
│  0. 退出                                       │
└──────────────────────────────────────────────┘"""


def _interactive_menu(cfg: Dict[str, Any]) -> int:
    """交互式菜单模式。"""
    state: Dict[str, Any] = {}
    while True:
        print(_MENU)
        choice = input("选择 [0-6/a]: ").strip().lower()

        if choice in ("0", "q", "quit", "exit"):
            print("退出")
            return 0
        elif choice == "1":
            crp_pack(cfg)
        elif choice == "2":
            repo_url = build_repo(cfg)
            if repo_url:
                state["repo_url"] = repo_url
        elif choice == "3":
            if not state.get("repo_url"):
                state["repo_url"] = input("仓库地址 (如 http://10.20.64.92:8080/crimson_runtime/stable_xxx/): ").strip()
            version = input("版本号 (如 1.1.1.1): ").strip()
            update_repo(cfg, version, state.get("repo_url"))
        elif choice == "4":
            build_layer(cfg)
        elif choice == "5":
            layer_url = input("LAYER_URL (可选，如 http://10.20.64.92:8080/crimson_runtime/stable_xxx/): ").strip() or None
            push_layer(cfg, layer_url)
        elif choice == "6":
            cmd_config()
        elif choice == "a":
            try:
                version = _infer_version(cfg)
                if not _input_confirm(f"自动推断版本: {version}，确认?"):
                    version = input("版本号: ").strip()
            except Exception:
                version = input("版本号: ").strip()
            repo_id = input("仓库标识 (可选，默认当天日期): ").strip() or None
            start = input("起始步骤 [1]: ").strip()
            start_from = int(start) if start else 1
            auto_mode(cfg, version, repo_id, start_from=start_from)
        else:
            print("无效选择")


# ---------------------------------------------------------------------------
# CLI 入口
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="DTK 玲珑 Runtime 更新工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s                                  交互式菜单
  %(prog)s auto --version 1.1.1.1          全自动执行
  %(prog)s auto --version 1.1.1.1 --repo-id 20260722 --deb-repo http://... --layer-url http://...
  %(prog)s crp-pack                         CRP 打包
  %(prog)s crp-pack --topic "xxx" --branch "crimson-testing"  指定主题和分支
  %(prog)s build-repo                       制作更新仓库
  %(prog)s build-repo --repo-id 20260722    指定仓库标识
  %(prog)s update-repo --version 1.1.1.1 --repo-url http://...
  %(prog)s build-layer                      构建玲珑 Layer
  %(prog)s push-layer                       N8N 推送
  %(prog)s config                           配置参数
        """)
    sub = p.add_subparsers(dest="command")

    a = sub.add_parser("auto", help="全自动执行全部 5 个步骤")
    a.add_argument("--version", default=None, help="版本号（默认自动从 linglong.yaml 推断）")
    a.add_argument("--repo-id", default=None, help="仓库标识（默认当天日期）")
    a.add_argument("--start-from", type=int, default=1, choices=[1, 2, 3, 4, 5],
                   help="从指定步骤开始 (默认 1)")
    a.add_argument("--dry-run", action="store_true", help="只打印不执行")

    for name, help_text in [
        ("crp-pack", "CRP 打包"),
        ("build-repo", "制作更新仓库"),
        ("update-repo", "修改 yaml + 创建 PR"),
        ("build-layer", "构建玲珑 Layer"),
        ("push-layer", "N8N 推送"),
    ]:
        s = sub.add_parser(name, help=help_text)
        s.add_argument("--dry-run", action="store_true", help="只打印不执行")
        if name == "crp-pack":
            s.add_argument("--topic", default=None, help="CRP 主题名称")
            s.add_argument("--branch", default=None, help="CRP 平台分支")
            s.add_argument("--archs", default=None, help="架构列表（逗号分隔，如 arm64,loong64,mips64,riscv64,sw64）")
            s.add_argument("--branch-id", type=int, default=None, help="CRP BranchID")
            s.add_argument("--version", default=None, help="CRP 打包 tag/版本（如 6.7.46）")
        elif name == "build-repo":
            s.add_argument("--repo-id", default=None, help="仓库标识（如日期 20260722）")
        elif name == "update-repo":
            s.add_argument("--version", default=None, help="版本号（默认自动推断）")
            s.add_argument("--deb-repo", required=True, help="deb 更新仓库地址（如 http://10.20.64.92:8080/crimson_runtime/stable_xxx/）")
        elif name == "build-layer":
            s.add_argument("--repo-url", default=None, help="REPO_URL（默认 github.com/linglongdev/org.deepin.runtime）")
            s.add_argument("--repo-branch", default=None, help="REPO_BRANCH（默认 main）")
        elif name == "push-layer":
            s.add_argument("--layer-url", default=None, help="LAYER_URL（build-layer 产出地址）")

    sub.add_parser("config", help="配置参数（含 Jenkins 凭证）")
    return p


def main() -> int:
    args = _build_parser().parse_args()

    # 无命令 → 交互式菜单
    if not args.command:
        return _interactive_menu(load_config())

    cfg = load_config()

    try:
        if args.command == "config":
            return cmd_config()
        elif args.command == "auto":
            return 0 if auto_mode(cfg, args.version, args.repo_id,
                                  args.deb_repo, args.layer_url,
                                  args.dry_run, args.start_from) else 1
        elif args.command == "crp-pack":
            archs_arg = args.archs
            if archs_arg:
                archs_arg = ";".join([a.strip() for a in archs_arg.split(",")])
            return 0 if crp_pack(cfg, args.topic, args.branch, archs_arg,
                                    args.branch_id, args.version, args.dry_run) else 1
        elif args.command == "build-repo":
            r = build_repo(cfg, args.repo_id, args.dry_run)
            return 0 if r else 1
        elif args.command == "update-repo":
            return 0 if update_repo(cfg, args.version, args.deb_repo,
                                    args.dry_run) else 1
        elif args.command == "build-layer":
            return 0 if build_layer(cfg, args.repo_url, args.repo_branch,
                                    args.dry_run) else 1
        elif args.command == "push-layer":
            return 0 if push_layer(cfg, args.layer_url, args.dry_run) else 1
        return 1
    except KeyboardInterrupt:
        _log("用户中断", "WARN")
        return 130
    except Exception as e:
        _log(f"未预期错误: {e}", "ERROR")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
