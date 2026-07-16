#!/usr/bin/env python3
from __future__ import annotations

import argparse
import getpass
import hashlib
import html
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag
from cryptography.fernet import Fernet
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


DEFAULT_CONFIG = (
    Path.home()
    / ".config"
    / "uos-pms-bug-workflow-trigger"
    / "config.json"
)
DEFAULT_SESSION_CACHE = (
    Path.home()
    / ".cache"
    / "uos-pms-bug-workflow-trigger"
    / "session.json"
)
DEFAULT_BASE_URL = "https://pms.uniontech.com"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
SUPPORTED_ACTIONS = ("resolve", "activate", "close")
RESOLUTION_OPTIONS: list[tuple[str, str]] = [
    ("totask", "已集成"),
    ("checked", "已验证"),
    ("tempcheck", "临时方案已验证"),
    ("tempfix", "临时方案已解决"),
    ("fixed", "已解决"),
    ("custom_checkd", "定制方案已验证"),
    ("retested", "已转测"),
]
REPAIR_OPTIONS: list[tuple[str, str]] = [
    ("", "留空"),
    ("需求", "需求"),
    ("设计", "设计"),
    ("代码", "代码"),
    ("构建", "构建"),
    ("帮助文档", "帮助文档"),
    ("国际化语言", "国际化语言"),
    ("不涉及", "不涉及"),
]
EXTTYPE_OPTIONS: list[tuple[str, str]] = [
    ("", "留空"),
    ("分配初始化", "分配初始化"),
    ("检查", "检查"),
    ("算法/方法", "算法/方法"),
    ("功能/类/对象", "功能/类/对象"),
    ("定时/序列化错误", "定时/序列化错误"),
    ("接口错误", "接口错误"),
    ("依赖错误", "依赖错误"),
    ("不涉及", "不涉及"),
    ("需求和规格说明不完整", "需求和规格说明不完整"),
    ("需求变更", "需求变更"),
    ("实现细节分析不足", "实现细节分析不足"),
    ("技术可行性分析不足", "技术可行性分析不足"),
    ("不实际的客户期望", "不实际的客户期望"),
]
SYMBOL_OPTIONS: list[tuple[str, str]] = [
    ("", "留空"),
    ("丢失", "丢失"),
    ("错误", "错误"),
    ("外来", "无关"),
    ("不涉及", "不涉及"),
]
AGE_OPTIONS: list[tuple[str, str]] = [
    ("", "留空"),
    ("历史版本引入", "历史版本引入"),
    ("当前版本新增引入", "当前版本新增引入"),
    ("当前版本修复引入", "当前版本修复引入"),
    ("不涉及（终端产线禁用）", "不涉及（终端产线禁用）"),
]
ANALYSIS_OPTIONS: list[tuple[str, str]] = [
    ("", "留空"),
    ("当前版本需求新增引入", "当前版本需求新增引入"),
    ("当前版本上游已有bug", "当前版本上游已有bug"),
    ("当前版本适配新增bug", "当前版本适配新增bug"),
]
SOURCE_OPTIONS: list[tuple[str, str]] = [
    ("", "留空"),
    ("内部开发", "内部开发"),
    ("lib库调用", "lib库调用"),
    ("外包代码", "外包代码"),
    ("代码移植", "代码移植"),
    ("不涉及", "不涉及"),
]
RESOLVED_BUILD_OPTIONS: list[tuple[str, str]] = [
    ("trunk", "主干"),
    ("", "留空"),
]
CHANGELOG_CANDIDATE_PATHS = [
    "debian/changelog",
    "rpm/deepin-control-center.spec",
    "CHANGELOG.md",
    "CHANGELOG",
    "docs/CHANGELOG.md",
]
DEFAULT_RESOLVE_COMMENT_TEMPLATE = """【版本号】：见备注
【自测环境镜像版本】：见备注
【代码地址】：见备注
【根因分析（Bug）】：见备注
【影响范围】：见备注
【自测结果截图/视频】：见备注
【自测架构】：x86"""
BUILTIN_ACTION_DEFAULTS: dict[str, dict[str, Any]] = {
    "resolve": {
        "resolution": "fixed",
        "resolvedDate": "__NOW__",
        "status": "resolved",
    },
    "activate": {
        "status": "active",
    },
    "close": {},
}
DEFAULT_URL_TEMPLATES = {
    "view": "bug-view-{bug_id}.html",
    "resolve": "bug-resolve-{bug_id}.html",
    "activate": "bug-activate-{bug_id}.html",
    "close": "bug-close-{bug_id}.html",
}
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="自动触发 PMS bug 流程")
    target = parser.add_mutually_exclusive_group(required=False)
    target.add_argument("--url", help="bug 详情页 URL，例如 https://pms.uniontech.com/bug-view-353781.html")
    target.add_argument("--bug-id", help="bug 编号，例如 353781")

    parser.add_argument("--action", choices=SUPPORTED_ACTIONS, help="要触发的流程动作")
    parser.add_argument(
        "--config",
        default=str(DEFAULT_CONFIG),
        help="配置文件路径，默认 ~/.config/uos-pms-bug-workflow-trigger/config.json",
    )
    parser.add_argument(
        "--session-cache",
        default=str(DEFAULT_SESSION_CACHE),
        help="会话缓存文件路径，默认 ~/.cache/uos-pms-bug-workflow-trigger/session.json",
    )
    parser.add_argument("--timeout", type=int, default=0, help="覆盖配置中的超时时间，单位秒")
    parser.add_argument("--loginid", default="", help="指定 LDAP 用户名（loginid），用于首次认证或覆盖默认账号")
    parser.add_argument("--force-auth", action="store_true", help="忽略已缓存凭证并重新认证")
    parser.add_argument(
        "--field",
        action="append",
        default=[],
        help="字段覆盖，格式 key=value，可重复传入",
    )
    parser.add_argument(
        "--field-json",
        default="",
        help='JSON 对象形式的字段覆盖，例如 {"openedBuild[]":["trunk"]}',
    )
    parser.add_argument("--dry-run", action="store_true", help="只输出将提交的数据，不真正提交")
    parser.add_argument("--dump-form", action="store_true", help="输出页面表单字段与默认值")
    parser.epilog = (
        "配置命令：python3 trigger_pms_bug_flow.py config\n"
        "认证命令：python3 trigger_pms_bug_flow.py --force-auth"
    )
    return parser.parse_args()


def load_json_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f"配置文件不存在: {path}")
    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise RuntimeError(f"配置文件格式错误: {path}")
    return data


BUILTIN_RESOLVE_DEFAULTS: dict[str, Any] = {
    "resolution": "fixed",
    "resolvedBuild": "trunk",
    "resolvedDate": "__NOW__",
    "repair": "代码",
    "exttype": "功能/类/对象",
    "symbol": "错误",
    "age": "当前版本新增引入",
    "analysis": "当前版本需求新增引入",
    "source": "内部开发",
    "assignedTo": "ut000965",
    "status": "resolved",
    "comment": DEFAULT_RESOLVE_COMMENT_TEMPLATE,
}


def build_default_config() -> dict[str, Any]:
    return {
        "base_url": DEFAULT_BASE_URL,
        "request": {
            "timeout": 15,
            "verify_tls": True,
        },
        "url_templates": DEFAULT_URL_TEMPLATES.copy(),
        "actions": {
            "resolve": {
                "defaults": dict(BUILTIN_RESOLVE_DEFAULTS),
            },
            "activate": {
                "defaults": {
                    "status": "active",
                }
            },
            "close": {
                "defaults": {
                    "comment": "脚本自动触发关闭流程",
                }
            },
        },
    }


def write_config(path: Path, config: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def load_config(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f"配置文件不存在: {path}；可先执行 --init-config 生成默认配置")
    data = load_json_file(path)
    if not str(data.get("base_url", "")).strip():
        raise RuntimeError("配置文件缺少字段: base_url")

    config: dict[str, Any] = {
        "base_url": str(data["base_url"]).strip().rstrip("/"),
        "request": data.get("request", {}) if isinstance(data.get("request", {}), dict) else {},
        "actions": data.get("actions", {}) if isinstance(data.get("actions", {}), dict) else {},
        "url_templates": DEFAULT_URL_TEMPLATES.copy(),
    }
    custom_templates = data.get("url_templates", {})
    if isinstance(custom_templates, dict):
        for key, value in custom_templates.items():
            if key in config["url_templates"] and str(value).strip():
                config["url_templates"][key] = str(value).strip()
    return apply_config_defaults(config)


def apply_config_defaults(config: dict[str, Any]) -> dict[str, Any]:
    actions = config.setdefault("actions", {})
    if not isinstance(actions, dict):
        config["actions"] = {}
        actions = config["actions"]
    resolve = actions.setdefault("resolve", {})
    if not isinstance(resolve, dict):
        actions["resolve"] = {}
        resolve = actions["resolve"]
    defaults = resolve.setdefault("defaults", {})
    if not isinstance(defaults, dict):
        resolve["defaults"] = {}
        defaults = resolve["defaults"]
    for key, builtin_value in BUILTIN_RESOLVE_DEFAULTS.items():
        if not str(defaults.get(key, "")).strip():
            defaults[key] = builtin_value
    return config


def parse_bug_id(url: str) -> str:
    match = re.search(r"bug-view-(\d+)", url)
    if not match:
        raise RuntimeError(f"无法从 URL 解析 PMS ID: {url}")
    return match.group(1)


def get_bug_id(args: argparse.Namespace) -> str:
    if args.url:
        return parse_bug_id(args.url)
    bug_id = str(args.bug_id).strip()
    if not re.fullmatch(r"\d+", bug_id):
        raise RuntimeError(f"bug ID 非法: {bug_id}")
    return bug_id


def build_headers(referer: str) -> dict[str, str]:
    return {
        "User-Agent": USER_AGENT,
        "Referer": referer,
    }


def now_string() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def expand_special_value(value: Any) -> Any:
    if isinstance(value, list):
        return [expand_special_value(item) for item in value]
    if isinstance(value, dict):
        return {str(key): expand_special_value(item) for key, item in value.items()}
    if value == "__NOW__":
        return now_string()
    return value


def create_session_with_retry(verify_tls: bool, trust_env: bool = True) -> requests.Session:
    session = requests.Session()
    session.verify = verify_tls
    session.trust_env = trust_env
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=frozenset(["GET", "POST"]),
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def _cred_dir() -> Path:
    env = os.getenv("UNIONTECH_OA_CONFIG_DIR")
    path = Path(env) if env else Path.home() / ".config" / "uniontech-oa"
    path.mkdir(parents=True, exist_ok=True)
    return path


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
    data = {
        "loginid": loginid,
        "password_encrypted": _fernet().encrypt(password.encode()).decode(),
        "saved_at": datetime.now().isoformat(),
        "metadata": {},
    }
    cred_file = _cred_dir() / "default.json"
    cred_file.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    cred_file.chmod(0o600)


def _load_creds() -> Optional[dict[str, str]]:
    cred_file = _cred_dir() / "default.json"
    if not cred_file.exists():
        return None
    try:
        data = json.loads(cred_file.read_text(encoding="utf-8"))
        password = _fernet().decrypt(data["password_encrypted"].encode()).decode()
        loginid = str(data["loginid"]).strip()
        if not loginid or not password:
            return None
        return {"loginid": loginid, "password": password}
    except Exception:
        return None


def load_session_cache(path: Path) -> str:
    if not path.exists():
        return ""
    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    return str(data.get("zentaosid", "")).strip()


def save_session_cache(path: Path, zentaosid: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "zentaosid": zentaosid,
        "saved_at": datetime.now().isoformat(),
    }
    with path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
    try:
        path.chmod(0o600)
    except OSError:
        pass


def is_login_page(response: requests.Response) -> bool:
    final_url = str(response.url)
    if "user-login" in final_url:
        return True

    body = response.text.lower()
    return (
        'name="account"' in body
        or "name='account'" in body
        or "self.location='/user-login-" in body
        or 'self.location="/user-login-' in body
    )


def extract_login_error(response: requests.Response) -> str:
    text = response.text
    parsed = try_parse_json(text)
    if isinstance(parsed, dict):
        if parsed.get("result") == "success":
            return ""
        if parsed.get("result") == "fail":
            return str(parsed.get("message", "")).strip() or "登录失败"
    match = re.search(r"alert\('([^']+)'\)", text)
    if match:
        return match.group(1).strip()
    match = re.search(r'alert\("([^"]+)"\)', text)
    if match:
        return match.group(1).strip()
    if is_login_page(response):
        return "登录后仍停留在登录页"
    return ""


def md5_hex(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def encrypt_login_password(password: str, verify_rand: str) -> str:
    if not verify_rand:
        return password
    return md5_hex(md5_hex(password) + verify_rand)


def compute_password_strength(password: str) -> int:
    if not password:
        return 0
    score = 0
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    if len(password) >= 12:
        score += 1
    return min(score, 5)


def fetch_login_form(session: requests.Session, login_url: str, timeout: int) -> dict[str, str]:
    response = session.get(
        login_url,
        headers=build_headers(login_url),
        timeout=timeout,
        allow_redirects=True,
    )
    response.raise_for_status()
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    verify_rand = ""
    referer = "/"
    verify_node = soup.select_one("input#verifyRand, input[name='verifyRand']")
    if verify_node:
        verify_rand = str(verify_node.get("value", "")).strip()
    referer_node = soup.select_one("input#referer, input[name='referer']")
    if referer_node:
        referer = str(referer_node.get("value", "/")).strip() or "/"
    return {"verifyRand": verify_rand, "referer": referer}


def login(
    session: requests.Session,
    base_url: str,
    loginid: str,
    password: str,
    timeout: int,
    verify_url: str = "",
) -> str:
    login_url = f"{base_url}/user-login.html"
    login_form = fetch_login_form(session, login_url, timeout)
    verify_rand = login_form.get("verifyRand", "")
    referer = login_form.get("referer", "/")
    ajax_headers = build_headers(login_url)
    ajax_headers.update(
        {
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "application/json, text/javascript, */*; q=0.01",
        }
    )
    response = session.post(
        login_url,
        data={
            "account": loginid,
            "password": encrypt_login_password(password, verify_rand),
            "passwordStrength": str(compute_password_strength(password)),
            "referer": referer,
            "verifyRand": verify_rand,
            "keepLogin": "1",
        },
        headers=ajax_headers,
        timeout=timeout,
        allow_redirects=True,
    )
    response.raise_for_status()
    zentaosid = session.cookies.get_dict().get("zentaosid", "")
    if not zentaosid:
        raise RuntimeError("未检测到 zentaosid，登录可能失败，请检查账号密码或登录方式。")
    login_error = extract_login_error(response)
    if login_error:
        raise RuntimeError(f"登录失败：{login_error}")
    verify_target = verify_url or f"{base_url}/my/"
    verify_response = session.get(
        verify_target,
        headers=build_headers(verify_target),
        timeout=timeout,
        allow_redirects=True,
    )
    verify_response.raise_for_status()
    verify_response.encoding = "utf-8"
    login_error = extract_login_error(verify_response)
    if login_error:
        raise RuntimeError(f"登录失败：{login_error}")
    return zentaosid


def prompt_for_creds(default_loginid: str = "") -> dict[str, str]:
    prompt = f"OA/LDAP loginid [{default_loginid}]: " if default_loginid else "OA/LDAP loginid: "
    loginid = input(prompt).strip() or default_loginid
    if not loginid:
        raise RuntimeError("未输入 loginid")

    password = getpass.getpass("OA/LDAP password: ")
    if not password:
        raise RuntimeError("未输入密码")
    return {"loginid": loginid, "password": password}


def prompt_text(message: str, default: str) -> str:
    prompt = f"{message} [{default}]: " if default else f"{message}: "
    value = input(prompt).strip()
    return value or default


def prompt_int(message: str, default: int) -> int:
    while True:
        raw = input(f"{message} [{default}]: ").strip()
        if not raw:
            return default
        try:
            value = int(raw)
        except ValueError:
            print("请输入整数。")
            continue
        if value <= 0:
            print("请输入大于 0 的整数。")
            continue
        return value


def prompt_bool(message: str, default: bool) -> bool:
    hint = "Y/n" if default else "y/N"
    while True:
        raw = input(f"{message} [{hint}]: ").strip().lower()
        if not raw:
            return default
        if raw in {"y", "yes", "1", "true"}:
            return True
        if raw in {"n", "no", "0", "false"}:
            return False
        print("请输入 y 或 n。")


def prompt_choice(message: str, options: list[tuple[str, str]], default: str) -> str:
    valid_values = {value for value, _ in options}
    resolved_default = default if default in valid_values else options[0][0]
    default_index = next(
        index for index, (value, _) in enumerate(options, start=1) if value == resolved_default
    )

    print(message)
    for index, (value, label) in enumerate(options, start=1):
        marker = " (默认)" if value == resolved_default else ""
        print(f"  {index}. {label} [{value}]{marker}")

    while True:
        raw = input(f"请选择 [默认 {default_index}]: ").strip()
        if not raw:
            return resolved_default
        if raw.isdigit():
            index = int(raw)
            if 1 <= index <= len(options):
                return options[index - 1][0]
        for value, _ in options:
            if raw == value:
                return value
        print("请输入编号或合法值。")


def configure_interactively(config_path: Path) -> dict[str, Any]:
    config = load_config(config_path) if config_path.exists() else build_default_config()

    print(f"配置文件路径: {config_path}")
    if config_path.exists():
        print("检测到已有配置，将进入交互式修改。")
    else:
        print("未检测到配置文件，将创建默认配置后进入交互式设置。")

    request_config = config.setdefault("request", {})
    actions_config = config.setdefault("actions", {})
    config.pop("url_templates", None)

    config["base_url"] = prompt_text("PMS base_url", str(config.get("base_url", DEFAULT_BASE_URL)).strip() or DEFAULT_BASE_URL).rstrip("/")
    request_config["timeout"] = prompt_int("请求超时（秒）", int(request_config.get("timeout", 15)))
    request_config["verify_tls"] = prompt_bool("是否校验证书 verify_tls", bool(request_config.get("verify_tls", True)))

    resolve_defaults = actions_config.setdefault("resolve", {}).setdefault("defaults", {})
    activate_defaults = actions_config.setdefault("activate", {}).setdefault("defaults", {})
    close_defaults = actions_config.setdefault("close", {}).setdefault("defaults", {})

    resolve_defaults.setdefault("duplicateBug", "")
    resolve_defaults.setdefault("buildProject", "")
    resolve_defaults.setdefault("resolvedBuild", "trunk")
    resolve_defaults.setdefault("buildName", "")
    resolve_defaults.setdefault("resolvedDate", "__NOW__")
    resolve_defaults.setdefault("repair", "")
    resolve_defaults.setdefault("exttype", "")
    resolve_defaults.setdefault("symbol", "")
    resolve_defaults.setdefault("age", "")
    resolve_defaults.setdefault("analysis", "")
    resolve_defaults.setdefault("source", "")
    resolve_defaults.setdefault("assignedTo", "ut000965")
    resolve_defaults.setdefault("status", "resolved")
    resolve_defaults.setdefault("labels[]", "")
    resolve_defaults.setdefault("comment", DEFAULT_RESOLVE_COMMENT_TEMPLATE)

    resolve_defaults["resolution"] = prompt_choice(
        "resolve 默认 resolution 选项：",
        RESOLUTION_OPTIONS,
        str(resolve_defaults.get("resolution", "fixed")).strip() or "fixed",
    )
    resolve_defaults["repair"] = prompt_choice(
        "resolve 默认 repair（修复点）选项：",
        REPAIR_OPTIONS,
        str(resolve_defaults.get("repair", "")).strip(),
    )
    resolve_defaults["exttype"] = prompt_choice(
        "resolve 默认 exttype（类型）选项：",
        EXTTYPE_OPTIONS,
        str(resolve_defaults.get("exttype", "")).strip(),
    )
    resolve_defaults["symbol"] = prompt_choice(
        "resolve 默认 symbol（限定符）选项：",
        SYMBOL_OPTIONS,
        str(resolve_defaults.get("symbol", "")).strip(),
    )
    resolve_defaults["age"] = prompt_choice(
        "resolve 默认 age（引入阶段）选项：",
        AGE_OPTIONS,
        str(resolve_defaults.get("age", "")).strip(),
    )
    resolve_defaults["analysis"] = prompt_choice(
        "resolve 默认 analysis（引入分析）选项：",
        ANALYSIS_OPTIONS,
        str(resolve_defaults.get("analysis", "")).strip(),
    )
    resolve_defaults["source"] = prompt_choice(
        "resolve 默认 source（来源）选项：",
        SOURCE_OPTIONS,
        str(resolve_defaults.get("source", "")).strip(),
    )
    resolve_defaults["duplicateBug"] = prompt_text("resolve 默认 duplicateBug（重复ID，可留空）", str(resolve_defaults.get("duplicateBug", "")).strip())
    resolve_defaults["buildProject"] = prompt_text("resolve 默认 buildProject（所属项目ID，可留空）", str(resolve_defaults.get("buildProject", "")).strip())
    resolve_defaults["resolvedBuild"] = prompt_choice(
        "resolve 默认 resolvedBuild（解决版本）选项：",
        RESOLVED_BUILD_OPTIONS,
        str(resolve_defaults.get("resolvedBuild", "trunk")).strip() or "trunk",
    )
    resolve_defaults["buildName"] = prompt_text("resolve 默认 buildName（新建版本名，可留空）", str(resolve_defaults.get("buildName", "")).strip())
    resolve_defaults["assignedTo"] = prompt_text(
        "resolve 默认 assignedTo（指派账号，可留空）",
        str(resolve_defaults.get("assignedTo", "")).strip() or "ut000965",
    )
    resolve_defaults["labels[]"] = prompt_text("resolve 默认 labels[]（标签，可留空）", str(resolve_defaults.get("labels[]", "")).strip())
    resolve_defaults["comment"] = str(resolve_defaults.get("comment", DEFAULT_RESOLVE_COMMENT_TEMPLATE))
    print("resolve 默认 comment 已保存在配置文件中，当前使用多行模板；如需调整，建议直接编辑 config.json。")
    activate_defaults["status"] = prompt_text("activate 默认 status", str(activate_defaults.get("status", "active")).strip() or "active")
    close_defaults["comment"] = prompt_text("close 默认 comment", str(close_defaults.get("comment", "脚本自动触发关闭流程")).strip() or "脚本自动触发关闭流程")

    write_config(config_path, config)
    print(f"已保存配置: {config_path}")
    return config


def parse_config_command(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="交互式配置 PMS bug 流程触发器")
    parser.add_argument(
        "--config",
        default=str(DEFAULT_CONFIG),
        help="配置文件路径，默认 ~/.config/uos-pms-bug-workflow-trigger/config.json",
    )
    return parser.parse_args(argv)


def resolve_loginid_hint(config: dict[str, Any], args: argparse.Namespace) -> str:
    return str(args.loginid or (_load_creds() or {}).get("loginid", "")).strip()


def authenticate_and_cache(
    session: requests.Session,
    config: dict[str, Any],
    timeout: int,
    session_cache_path: Path,
    verify_url: str,
    loginid_hint: str = "",
    force_auth: bool = False,
) -> dict[str, str]:
    candidates: list[dict[str, str]] = []
    if not force_auth:
        cached_creds = _load_creds()
        if cached_creds:
            candidates.append(cached_creds)

    for creds in candidates:
        try:
            zentaosid = login(
                session=session,
                base_url=config["base_url"],
                loginid=creds["loginid"],
                password=creds["password"],
                timeout=timeout,
                verify_url=verify_url,
            )
            save_session_cache(session_cache_path, zentaosid)
            return {"loginid": creds["loginid"], "zentaosid": zentaosid, "source": "cache"}
        except Exception:
            session.cookies.clear()

    prompted = prompt_for_creds(loginid_hint)
    zentaosid = login(
        session=session,
        base_url=config["base_url"],
        loginid=prompted["loginid"],
        password=prompted["password"],
        timeout=timeout,
        verify_url=verify_url,
    )
    _save_creds(prompted["loginid"], prompted["password"])
    save_session_cache(session_cache_path, zentaosid)
    return {"loginid": prompted["loginid"], "zentaosid": zentaosid, "source": "prompt"}


def ensure_session(
    session: requests.Session,
    config: dict[str, Any],
    target_url: str,
    timeout: int,
    session_cache_path: Path,
    loginid_hint: str = "",
    force_auth: bool = False,
) -> None:
    cached_sid = load_session_cache(session_cache_path)
    if cached_sid:
        session.cookies.set("zentaosid", cached_sid)
        response = session.get(
            target_url,
            headers=build_headers(target_url),
            timeout=timeout,
            allow_redirects=True,
        )
        response.encoding = "utf-8"
        if response.status_code == 200 and not is_login_page(response):
            return

    authenticate_and_cache(
        session=session,
        config=config,
        timeout=timeout,
        session_cache_path=session_cache_path,
        verify_url=target_url,
        loginid_hint=loginid_hint,
        force_auth=force_auth,
    )


def build_url(base_url: str, template: str, bug_id: str) -> str:
    return urljoin(f"{base_url}/", template.format(bug_id=bug_id))


def fetch_page(session: requests.Session, url: str, timeout: int) -> requests.Response:
    response = session.get(url, headers=build_headers(url), timeout=timeout, allow_redirects=True)
    response.raise_for_status()
    response.encoding = "utf-8"
    if is_login_page(response):
        raise RuntimeError(f"访问页面时仍然跳到了登录页: {url}")
    return response


def choose_form(soup: BeautifulSoup) -> Tag:
    forms = soup.find_all("form")
    if not forms:
        raise RuntimeError("未在动作页面中找到 form，无法分析提交字段。")

    scored_forms: list[tuple[int, Tag]] = []
    for form in forms:
        score = 0
        if str(form.get("method", "")).lower() == "post":
            score += 10
        named_fields = form.select("[name]")
        score += len(named_fields)
        if form.get("id") == "ajaxForm":
            score += 20
        scored_forms.append((score, form))

    scored_forms.sort(key=lambda item: item[0], reverse=True)
    return scored_forms[0][1]


def collect_field_value(field: Tag) -> Any:
    tag = field.name.lower()
    if tag == "textarea":
        return field.get_text()

    if tag == "select":
        options = field.find_all("option")
        selected = [option for option in options if option.has_attr("selected")]
        if not selected and options:
            selected = [options[0]]
        values = [option.get("value", option.get_text(strip=True)) for option in selected]
        return values if field.has_attr("multiple") else (values[0] if values else "")

    input_type = str(field.get("type", "text")).lower()
    if input_type in {"checkbox", "radio"}:
        if not field.has_attr("checked"):
            return None
        return field.get("value", "on")
    if input_type in {"file", "submit", "button", "reset", "image"}:
        return None
    return field.get("value", "")


def is_required(field: Tag) -> bool:
    if field.has_attr("required"):
        return True
    classes = field.get("class", [])
    return "required" in classes if isinstance(classes, list) else False


def collect_form_definition(form: Tag) -> tuple[dict[str, Any], dict[str, Any]]:
    defaults: dict[str, Any] = {}
    metadata: dict[str, Any] = {}

    for field in form.find_all(["input", "textarea", "select"]):
        name = str(field.get("name", "")).strip()
        if not name or field.has_attr("disabled"):
            continue

        value = collect_field_value(field)
        if value is None:
            continue

        defaults[name] = value
        item: dict[str, Any] = {
            "tag": field.name.lower(),
            "required": is_required(field),
            "default": value,
        }

        if field.name.lower() == "input":
            item["type"] = str(field.get("type", "text")).lower()
        elif field.name.lower() == "select":
            item["multiple"] = field.has_attr("multiple")
            item["options"] = [
                {
                    "value": option.get("value", option.get_text(strip=True)),
                    "text": option.get_text(" ", strip=True),
                    "selected": option.has_attr("selected"),
                }
                for option in field.find_all("option")
            ]
        metadata[name] = item

    return defaults, metadata


def parse_field_pairs(items: list[str]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for item in items:
        if "=" not in item:
            raise RuntimeError(f"--field 参数格式错误，必须是 key=value：{item}")
        key, value = item.split("=", 1)
        key = key.strip()
        if not key:
            raise RuntimeError(f"--field 参数格式错误，key 不能为空：{item}")
        result[key] = value
    return result


def parse_field_json(raw: str) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"--field-json 不是合法 JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise RuntimeError("--field-json 必须是 JSON 对象")
    return data


def merge_fields(*sources: dict[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = {}
    for source in sources:
        for key, value in source.items():
            merged[str(key)] = expand_special_value(value)
    return merged


def normalize_scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "1" if value else "0"
    return str(value)


def payload_to_tuples(payload: dict[str, Any]) -> list[tuple[str, str]]:
    tuples: list[tuple[str, str]] = []
    for key, value in payload.items():
        if isinstance(value, list):
            tuples.extend((key, normalize_scalar(item)) for item in value)
        else:
            tuples.append((key, normalize_scalar(value)))
    return tuples


def comment_to_html(comment: str) -> str:
    normalized = comment.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not normalized:
        return ""
    if re.search(r"<(?:p|br|div|ul|ol|li)\b", normalized, flags=re.I):
        return normalized
    blocks = normalized.split("\n")
    html_lines: list[str] = []
    for line in blocks:
        escaped = html.escape(line.strip())
        if escaped:
            html_lines.append(f"<p>{escaped}</p>")
        else:
            html_lines.append("<p><br /></p>")
    return "".join(html_lines)


def build_submission_payload(payload: dict[str, Any]) -> dict[str, Any]:
    submission_payload = dict(payload)
    comment = submission_payload.get("comment")
    if isinstance(comment, str) and comment.strip():
        submission_payload["comment"] = comment_to_html(comment)
    return submission_payload


def try_parse_json(text: str) -> Any | None:
    text = text.strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    match = re.search(r'(\{"result".*\})', text, flags=re.S)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            return None
    return None


def summarize_response(response: requests.Response) -> dict[str, Any]:
    parsed = try_parse_json(response.text)
    if isinstance(parsed, dict):
        return parsed
    snippet = response.text.strip().replace("\n", " ")
    return {
        "status_code": response.status_code,
        "url": response.url,
        "snippet": snippet[:500],
    }


def extract_bug_status(soup: BeautifulSoup) -> str:
    selectors = [
        "span.status-bug",
        ".cell-status",
        ".status",
    ]
    for selector in selectors:
        node = soup.select_one(selector)
        if node:
            return node.get_text(" ", strip=True)
    return ""


def extract_bug_title(soup: BeautifulSoup) -> str:
    title_node = soup.title
    if title_node:
        return title_node.get_text(" ", strip=True)
    heading = soup.select_one("h1, .panel-title, .title")
    if heading:
        return heading.get_text(" ", strip=True)
    return ""


def action_defaults_from_config(config: dict[str, Any], action: str) -> dict[str, Any]:
    actions = config.get("actions", {})
    if not isinstance(actions, dict):
        return {}
    action_config = actions.get(action, {})
    if not isinstance(action_config, dict):
        return {}
    defaults = action_config.get("defaults", {})
    if not isinstance(defaults, dict):
        return {}
    return defaults


def extract_text_urls(text: str) -> list[str]:
    urls: list[str] = []
    for match in re.finditer(r"https?://[^\s<>'\"]+", text):
        candidate = match.group(0).rstrip(".,);]>")
        if candidate not in urls:
            urls.append(candidate)
    return urls


def extract_history_urls(soup: BeautifulSoup) -> list[str]:
    container = soup.select_one("#actionbox") or soup.select_one(".histories") or soup
    urls: list[str] = []
    for link in container.select("a[href]"):
        href = str(link.get("href") or "").strip()
        if href.startswith("http://") or href.startswith("https://"):
            if href not in urls:
                urls.append(href)
    for node in container.select(".comment-content, .article-content.comment, .history-changes, li"):
        for url in extract_text_urls(node.get_text("\n", strip=True)):
            if url not in urls:
                urls.append(url)
    return urls


def code_link_score(url: str) -> tuple[int, int]:
    if re.search(r"github\.com/[^/]+/[^/]+/pull/\d+", url):
        return (100, len(url))
    if "gerrit" in url.lower() or "/changes/" in url.lower():
        return (90, len(url))
    if re.search(r"github\.com/[^/]+/[^/]+/commit/[0-9a-fA-F]+", url):
        return (80, len(url))
    if "github.com" in url.lower():
        return (70, len(url))
    return (0, len(url))


def collect_code_links(urls: list[str]) -> list[str]:
    ranked = sorted((url for url in urls if code_link_score(url)[0] > 0), key=code_link_score, reverse=True)
    result: list[str] = []
    for url in ranked:
        if url not in result:
            result.append(url)
    return result


def pick_code_link(urls: list[str]) -> str:
    links = collect_code_links(urls)
    return links[0] if links else ""


def parse_github_pull_url(url: str) -> tuple[str, str, int] | None:
    match = re.match(r"https?://github\.com/([^/]+)/([^/]+)/pull/(\d+)", url)
    if not match:
        return None
    owner, repo, number = match.groups()
    return owner, repo, int(number)


def split_pr_body_sections(body: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current = "summary"
    sections[current] = []
    for raw_line in body.splitlines():
        line = raw_line.strip()
        lower = line.lower()
        if lower in {"influence:", "影响范围：", "影响范围:", "测试点：", "测试点:"}:
            current = "influence"
            sections.setdefault(current, [])
            continue
        if lower in {"log:", "根因分析：", "根因分析:", "fix:", "summary:"} or re.match(
            r"^(feat|fix|perf|refactor|docs|test|chore)(\([^)]+\))?[:：]",
            lower,
        ):
            current = "summary"
            sections.setdefault(current, [])
            continue
        if lower.startswith("pms:") or lower.startswith("## summary by"):
            current = "meta"
            sections.setdefault(current, [])
            continue
        sections.setdefault(current, []).append(raw_line)
    return sections


def compact_lines(lines: list[str]) -> list[str]:
    result: list[str] = []
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if line.startswith("- "):
            line = line[2:].strip()
        result.append(line)
    return result


def strip_change_prefix(text: str) -> str:
    return re.sub(r"^(feat|fix|perf|refactor|docs|test|chore)(\([^)]+\))?[:：]\s*", "", text.strip(), flags=re.I)


def pick_root_cause(body: str, title: str) -> str:
    lines = [raw_line.strip() for raw_line in body.splitlines()]
    for index, line in enumerate(lines):
        if not line:
            continue
        if re.match(r"^(fix|log|influence|pms|summary)[:：]", line, flags=re.I):
            continue
        if re.search(r"[\u4e00-\u9fff]", line):
            merged = [line]
            for next_line in lines[index + 1 : index + 4]:
                if not next_line:
                    break
                if re.match(r"^(fix|log|influence|pms|summary)[:：]|^##\s", next_line, flags=re.I):
                    break
                merged.append(next_line)
                if re.search(r"[。！？]$", next_line):
                    break
            return strip_change_prefix("".join(merged))
    for line in lines:
        if not line:
            continue
        if re.match(r"^(fix|log|influence|pms|summary)[:：]", line, flags=re.I):
            continue
        return strip_change_prefix(line)
    return strip_change_prefix(title)


def pick_test_points(body: str) -> str:
    lines: list[str] = []
    in_influence = False
    for raw_line in body.splitlines():
        line = raw_line.strip()
        lower = line.lower()
        if lower in {"influence:", "测试点：", "测试点:"}:
            in_influence = True
            continue
        if in_influence and (
            lower.startswith("fix:")
            or lower.startswith("log:")
            or lower.startswith("pms:")
            or lower.startswith("## summary by")
            or lower == "影响范围："
            or lower == "影响范围:"
        ):
            if lines:
                break
            in_influence = False
            continue
        if not in_influence:
            continue
        if re.match(r"^(\d+\.)", line):
            lines.append(line)
    if lines:
        return "\n".join(lines[:8])
    return ""


def pick_chinese_influence_items(body: str) -> list[str]:
    items: list[str] = []
    sections = split_pr_body_sections(body)
    for raw_line in sections.get("influence", []):
        line = raw_line.strip()
        if not line or not re.match(r"^\d+\.", line):
            continue
        if not re.search(r"[\u4e00-\u9fff]", line):
            continue
        items.append(re.sub(r"^\d+\.\s*", "", line))
    return items


def normalize_influence_item(item: str) -> str:
    text = item.strip()
    text = re.sub(r"\s*[–—-]\s*验证.*$", "", text)
    text = re.sub(r"\s*[–—-]\s*确保.*$", "", text)
    text = re.sub(r"\s*[：:]\s*验证.*$", "", text)
    text = re.sub(r"\s*[：:]\s*确保.*$", "", text)
    text = re.sub(r"[，,]\s*(验证|确保).*$", "", text)
    text = re.sub(r"^测试", "", text)
    text = re.sub(r"^验证", "", text)
    text = re.sub(r"^(功能|模块|场景)[：:]\s*", "", text)
    if "：" in text:
        head, tail = text.split("：", 1)
        if head and len(head) <= 20:
            text = head
        else:
            text = f"{head} {tail}".strip()
    elif ":" in text:
        head, tail = text.split(":", 1)
        if head and len(head) <= 24:
            text = head
        else:
            text = f"{head} {tail}".strip()
    text = text.strip("：:；;，,。 ")
    return text


def infer_impact_from_influence(body: str) -> str:
    raw_items = pick_chinese_influence_items(body)
    if not raw_items:
        return ""
    normalized: list[str] = []
    for item in raw_items:
        text = normalize_influence_item(item)
        if not text:
            continue
        if text not in normalized:
            normalized.append(text)
    if not normalized:
        return ""
    return "、".join(normalized[:5])


def infer_impact_from_files(repo: str, files: list[dict[str, Any]]) -> str:
    keywords: list[str] = []
    # 文件路径关键词 -> 简短通俗的影响描述
    _file_patterns = [
        ("popup", "弹窗提示"),
        ("dialog", "对话框"),
        ("menu", "右键菜单"),
        ("notification", "通知提示"),
        ("blur", "模糊效果"),
        ("window", "窗口操作"),
        ("qml", "应用界面"),
        ("icon", "图标显示"),
        ("theme", "主题样式"),
        ("style", "主题样式"),
        ("i18n", "多语言显示"),
        ("locale", "多语言显示"),
        ("translation", "多语言显示"),
        ("dock", "任务栏"),
        ("launcher", "启动器"),
        ("desktop", "桌面"),
        ("titlebar", "标题栏"),
        ("sidebar", "侧边栏"),
    ]
    for item in files:
        filename = str(item.get("filename", "")).strip()
        if not filename:
            continue
        lowered = filename.lower()
        for pattern, label in _file_patterns:
            if pattern in lowered and label not in keywords:
                keywords.append(label)
    repo_lower = repo.lower()
    if "dtk" in repo_lower and "应用界面" not in keywords:
        keywords.insert(0, "应用界面")
    if "control-center" in repo_lower and "控制中心" not in keywords:
        keywords.insert(0, "控制中心")
    if not keywords:
        return ""
    return "可能影响：" + "、".join(keywords[:5])


def fetch_github_text_file(
    session: requests.Session,
    owner: str,
    repo: str,
    path: str,
    ref: str,
    timeout: int,
) -> str:
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{path}"
    response = session.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
    if response.status_code == 404:
        return ""
    response.raise_for_status()
    response.encoding = "utf-8"
    return response.text


def extract_version_from_text(text: str) -> str:
    patterns = [
        r"^[^(]+\(([^)]+)\)\s+\w+;",
        r"(?im)^version\s*[:=]\s*([0-9][A-Za-z0-9.+:~\-]*)\s*$",
        r"(?im)^##?\s*v?([0-9]+\.[0-9]+\.[0-9][A-Za-z0-9.+:~\-]*)\b",
        r"(?im)\bv?([0-9]+\.[0-9]+\.[0-9][A-Za-z0-9.+:~\-]*)\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
    return ""


def extract_source_name_from_text(text: str) -> str:
    match = re.search(r"(?im)^source:\s*(\S+)\s*$", text)
    if match:
        return match.group(1).strip()
    match = re.search(r"^([^(]+)\([^)]+\)\s+\w+;", text)
    if match:
        return match.group(1).strip()
    return ""


def extract_package_names_from_control(text: str) -> list[str]:
    packages: list[str] = []
    for match in re.finditer(r"(?im)^package:\s*(\S+)\s*$", text):
        package = match.group(1).strip()
        if package and package not in packages:
            packages.append(package)
    return packages


def choose_preferred_package_name(source_name: str, repo_name: str, packages: list[str]) -> str:
    if not packages:
        return ""

    source_norm = re.sub(r"[^a-z0-9]+", "", source_name.lower())
    repo_norm = re.sub(r"[^a-z0-9]+", "", repo_name.lower())

    def score(package: str) -> tuple[int, int]:
        pkg = package.lower()
        pkg_norm = re.sub(r"[^a-z0-9]+", "", pkg)
        pkg_no_digits = re.sub(r"\d+", "", pkg_norm)
        value = 0
        if source_norm and (source_norm in pkg_norm or source_norm in pkg_no_digits):
            value += 70
        if repo_norm and (repo_norm in pkg_norm or repo_norm in pkg_no_digits):
            value += 50
        if pkg.startswith("lib"):
            value += 20
        if pkg == source_name.lower() or pkg == repo_name.lower():
            value += 15
        if any(token in pkg for token in ("-dev", "-dbg", "-doc", "qml-module", "module-", "exhibition")):
            value -= 25
        return value, -len(package)

    ranked = sorted(packages, key=score, reverse=True)
    return ranked[0]


def format_version_requirement(package_name: str, version: str) -> str:
    if package_name and version:
        return f"{package_name} >= {version}"
    return version


def bump_patch_version(version: str) -> str:
    epoch = ""
    remainder = version.strip()
    if ":" in remainder:
        epoch_part, remainder = remainder.split(":", 1)
        epoch = f"{epoch_part}:"

    revision = ""
    if "-" in remainder:
        upstream, _revision = remainder.split("-", 1)
        remainder = upstream
        revision = ""

    match = re.match(r"^(\d+)\.(\d+)\.(\d+)$", remainder)
    if not match:
        return ""
    major, minor, patch = (int(item) for item in match.groups())
    return f"{epoch}{major}.{minor}.{patch + 1}{revision}"


def infer_version_from_github_repo(
    session: requests.Session,
    owner: str,
    repo: str,
    ref: str,
    timeout: int,
    merge_commit_sha: str = "",
) -> str:
    # 取 merge commit 的第一个 parent（合入前的 base 分支状态），
    # 确保版本号基于 PR 合入时的 changelog，而非当前最新的 base 分支。
    actual_ref = ref
    if merge_commit_sha:
        try:
            commit_url = f"https://api.github.com/repos/{owner}/{repo}/commits/{merge_commit_sha}"
            headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"}
            resp = session.get(commit_url, headers=headers, timeout=timeout)
            if resp.ok:
                parents = resp.json().get("parents", [])
                if parents:
                    actual_ref = parents[0]["sha"]
        except requests.RequestException:
            pass

    # 从 changelog 取第一个版本号（最新的 tag），然后 patch 递增
    # 例如 changelog 第一行是 6.6.6，则推断为 6.6.7
    source_name = ""
    for path in CHANGELOG_CANDIDATE_PATHS:
        try:
            text = fetch_github_text_file(session, owner, repo, path, actual_ref, timeout)
        except requests.RequestException:
            continue
        if not text:
            continue
        if not source_name:
            source_name = extract_source_name_from_text(text)
        version = extract_version_from_text(text)
        if version:
            bumped = bump_patch_version(version)
            if bumped:
                package_name = ""
                try:
                    control_text = fetch_github_text_file(session, owner, repo, "debian/control", actual_ref, timeout)
                except requests.RequestException:
                    control_text = ""
                if control_text:
                    package_name = choose_preferred_package_name(
                        source_name or repo,
                        repo,
                        extract_package_names_from_control(control_text),
                    )
                return format_version_requirement(package_name or source_name, bumped)
    return ""


def fetch_github_pr_context(session: requests.Session, url: str, timeout: int) -> dict[str, str]:
    parsed = parse_github_pull_url(url)
    if not parsed:
        return {}
    owner, repo, number = parsed
    api_base = f"https://api.github.com/repos/{owner}/{repo}/pulls/{number}"
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
    }
    pr_resp = session.get(api_base, headers=headers, timeout=timeout)
    pr_resp.raise_for_status()
    pr_data = pr_resp.json()

    files_resp = session.get(f"{api_base}/files?per_page=100", headers=headers, timeout=timeout)
    files_resp.raise_for_status()
    files_data = files_resp.json()
    if not isinstance(files_data, list):
        files_data = []

    body = str(pr_data.get("body") or "").strip()
    title = str(pr_data.get("title") or "").strip()
    merged_at = str(pr_data.get("merged_at") or "").strip()
    merge_commit_sha = str(pr_data.get("merge_commit_sha") or "").strip()
    base_data = pr_data.get("base", {}) if isinstance(pr_data.get("base"), dict) else {}
    base_ref = str(base_data.get("ref") or "master").strip() or "master"
    base_repo_data = base_data.get("repo", {}) if isinstance(base_data.get("repo"), dict) else {}
    base_full_name = str(base_repo_data.get("full_name") or f"{owner}/{repo}").strip()
    base_owner, base_repo = (base_full_name.split("/", 1) + [repo])[:2] if "/" in base_full_name else (owner, repo)
    test_points = pick_test_points(body)
    impact = infer_impact_from_influence(body) or infer_impact_from_files(f"{base_owner}/{base_repo}", files_data)
    try:
        predicted_version = infer_version_from_github_repo(
            session, base_owner, base_repo, base_ref, timeout,
            merge_commit_sha=merge_commit_sha,
        )
    except requests.RequestException:
        predicted_version = ""

    return {
        "repo": f"{base_owner}/{base_repo}",
        "pr_url": url,
        "pr_title": title,
        "root_cause": pick_root_cause(body, title),
        "impact_scope": impact,
        "test_points": test_points,
        "merged_at": merged_at,
        "predicted_version": predicted_version,
    }


def merge_distinct_texts(items: list[str], separator: str = "；") -> str:
    result: list[str] = []
    for item in items:
        text = str(item).strip()
        if not text or text in result:
            continue
        result.append(text)
    return separator.join(result)


def aggregate_code_context(pr_contexts: list[dict[str, str]], fallback_link: str = "") -> dict[str, str]:
    if not pr_contexts:
        return {"代码地址": fallback_link} if fallback_link else {}
    versions = merge_distinct_texts([item.get("predicted_version", "") for item in pr_contexts])
    links = merge_distinct_texts([item.get("pr_url", "") for item in pr_contexts])
    root_causes = merge_distinct_texts([item.get("root_cause", "") for item in pr_contexts])
    impacts = merge_distinct_texts([item.get("impact_scope", "") for item in pr_contexts])
    return {
        key: value
        for key, value in {
            "版本号": versions,
            "代码地址": links or fallback_link,
            "根因分析（Bug）": root_causes,
            "影响范围": impacts,
        }.items()
        if value
    }


def extract_bug_basic_info(soup: BeautifulSoup) -> dict[str, str]:
    info: dict[str, str] = {}
    for row in soup.select("table.table-data tr"):
        th = row.find("th")
        td = row.find("td")
        if not th or not td:
            continue
        key = th.get_text(" ", strip=True)
        value = td.get_text(" ", strip=True)
        if key and value:
            info[key] = value
    return info


def build_resolve_comment_context(
    github_session: requests.Session,
    bug_soup: BeautifulSoup,
    timeout: int,
) -> dict[str, str]:
    urls = extract_history_urls(bug_soup)
    code_links = collect_code_links(urls)
    code_link = code_links[0] if code_links else ""
    bug_info = extract_bug_basic_info(bug_soup)
    context: dict[str, str] = {
        "代码地址": code_link,
        "自测环境镜像版本": bug_info.get("发现基线", ""),
        "自测架构": bug_info.get("平台", ""),
    }
    pr_contexts: list[dict[str, str]] = []
    for link in code_links:
        if not ("github.com" in link and "/pull/" in link):
            continue
        try:
            pr_context = fetch_github_pr_context(github_session, link, timeout)
        except Exception:
            pr_context = {}
        if pr_context:
            pr_contexts.append(pr_context)
    if pr_contexts:
        context.update(aggregate_code_context(pr_contexts, fallback_link=context.get("代码地址", "")))
    return {key: value for key, value in context.items() if value}


def is_template_comment(comment: str) -> bool:
    return "【代码地址】" in comment and "【根因分析（Bug）】" in comment


def is_legacy_auto_comment(comment: str) -> bool:
    normalized = comment.strip()
    if normalized in {"", "脚本自动触发解决流程"}:
        return True
    legacy_markers = [
        "【引入责任人】",
        "【引入提交链接】",
        "【维护线是否回合主线】",
        "【测试点】",
        "【前置条件】",
        "【步骤】",
        "【预期】",
        "【自测结果】",
    ]
    return any(marker in normalized for marker in legacy_markers)


PLACEHOLDER_COMMENT = "见备注"

COMMENT_FIELD_LABELS = [
    "版本号",
    "自测环境镜像版本",
    "代码地址",
    "根因分析（Bug）",
    "影响范围",
    "自测结果截图/视频",
]


def fill_comment_template(comment: str, context: dict[str, str]) -> str:
    result = comment
    for label in COMMENT_FIELD_LABELS:
        pattern = rf"(^【{re.escape(label)}】[：:])\s*$"
        result = re.sub(pattern, rf"\1{PLACEHOLDER_COMMENT}", result, flags=re.M)
    for label, value in context.items():
        if not value:
            continue
        pattern = rf"(^【{re.escape(label)}】[：:])(.*)$"
        result, count = re.subn(
            pattern,
            lambda match, replacement=value: f"{match.group(1)}{replacement}",
            result,
            count=1,
            flags=re.M,
        )
    result = re.sub(
        r"(【版本号】[：:].*)\n{2,}(【自测环境镜像版本】[：:])",
        r"\1\n\2",
        result,
        flags=re.M,
    )
    return result


def build_result(
    success: bool,
    action: str,
    bug_id: str,
    form_url: str,
    payload: dict[str, Any],
    server_response: dict[str, Any],
    bug_title: str = "",
    bug_status: str = "",
) -> dict[str, Any]:
    return {
        "success": success,
        "action": action,
        "bug_id": bug_id,
        "form_url": form_url,
        "submitted_fields": payload,
        "server_response": server_response,
        "bug_title": bug_title,
        "bug_status": bug_status,
    }


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "config":
        args = parse_config_command(sys.argv[2:])
        config_path = Path(args.config).expanduser()
        config = configure_interactively(config_path)
        print(
            json.dumps(
                {
                    "success": True,
                    "mode": "config",
                    "config_path": str(config_path),
                    "config": config,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    args = parse_args()
    config_path = Path(args.config).expanduser()
    cached_creds = _load_creds() or {}

    if config_path.exists():
        config = load_config(config_path)
    else:
        config = build_default_config()

    request_config = config.get("request", {})
    verify_tls = bool(request_config.get("verify_tls", True))
    timeout = args.timeout or int(request_config.get("timeout", 15))
    session_cache_path = Path(args.session_cache).expanduser()
    loginid_hint = resolve_loginid_hint(config, args)

    if args.force_auth and not args.action and not args.url and not args.bug_id:
        session = create_session_with_retry(verify_tls=verify_tls, trust_env=False)
        auth_info = authenticate_and_cache(
            session=session,
            config=config,
            timeout=timeout,
            session_cache_path=session_cache_path,
            verify_url=f"{config['base_url']}/my/",
            loginid_hint=loginid_hint,
            force_auth=True,
        )
        print(
            json.dumps(
                {
                    "success": True,
                    "mode": "auth-only",
                    "loginid": auth_info["loginid"],
                    "source": auth_info["source"],
                    "config_path": str(config_path),
                    "session_cache": str(session_cache_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    if not args.action:
        raise RuntimeError("缺少 --action。配置请使用 `config` 子命令，仅认证请使用 --force-auth。")
    if not args.url and not args.bug_id:
        raise RuntimeError("缺少目标 bug，请提供 --url 或 --bug-id。")

    bug_id = get_bug_id(args)
    view_url = (
        args.url
        if args.url
        else build_url(config["base_url"], config["url_templates"]["view"], bug_id)
    )
    form_url = build_url(config["base_url"], config["url_templates"][args.action], bug_id)

    session = create_session_with_retry(verify_tls=verify_tls, trust_env=False)
    ensure_session(
        session=session,
        config=config,
        target_url=form_url,
        timeout=timeout,
        session_cache_path=session_cache_path,
        loginid_hint=loginid_hint,
        force_auth=args.force_auth,
    )

    bug_page = fetch_page(session, view_url, timeout)
    bug_soup = BeautifulSoup(bug_page.text, "html.parser")
    github_session = create_session_with_retry(verify_tls=True, trust_env=True)
    auto_comment_context = (
        build_resolve_comment_context(github_session, bug_soup, timeout)
        if args.action == "resolve"
        else {}
    )

    form_page = fetch_page(session, form_url, timeout)
    soup = BeautifulSoup(form_page.text, "html.parser")
    form = choose_form(soup)
    form_defaults, form_metadata = collect_form_definition(form)

    cli_fields = merge_fields(
        parse_field_pairs(args.field),
        parse_field_json(args.field_json),
    )
    payload = merge_fields(
        form_defaults,
        BUILTIN_ACTION_DEFAULTS.get(args.action, {}),
        action_defaults_from_config(config, args.action),
        cli_fields,
    )
    if args.action == "resolve" and isinstance(payload.get("comment"), str):
        current_comment = str(payload.get("comment", ""))
        if is_legacy_auto_comment(current_comment):
            current_comment = DEFAULT_RESOLVE_COMMENT_TEMPLATE
        if is_template_comment(current_comment):
            payload["comment"] = fill_comment_template(current_comment, auto_comment_context)
    submission_payload = build_submission_payload(payload)

    if args.dump_form:
        print(
            json.dumps(
                {
                    "success": True,
                    "action": args.action,
                    "bug_id": bug_id,
                    "form_url": form_url,
                    "fields": form_metadata,
                    "effective_defaults": payload,
                    "submission_fields": submission_payload,
                    "auto_comment_context": auto_comment_context,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    if args.dry_run:
        print(
            json.dumps(
                build_result(
                    success=True,
                    action=args.action,
                    bug_id=bug_id,
                    form_url=form_url,
                    payload=submission_payload,
                    server_response={"mode": "dry-run"},
                    bug_title=extract_bug_title(bug_soup),
                    bug_status=extract_bug_status(bug_soup),
                ),
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    response = session.post(
        form_url,
        data=payload_to_tuples(submission_payload),
        headers=build_headers(form_url),
        timeout=timeout,
        allow_redirects=True,
    )
    response.raise_for_status()
    response.encoding = "utf-8"

    server_response = summarize_response(response)
    if isinstance(server_response, dict) and server_response.get("result") == "fail":
        print(
            json.dumps(
                build_result(
                    success=False,
                    action=args.action,
                    bug_id=bug_id,
                    form_url=form_url,
                    payload=submission_payload,
                    server_response=server_response,
                ),
                ensure_ascii=False,
                indent=2,
            ),
            file=sys.stderr,
        )
        return 1

    bug_page = fetch_page(session, view_url, timeout)
    bug_soup = BeautifulSoup(bug_page.text, "html.parser")
    bug_status = extract_bug_status(bug_soup)
    bug_title = extract_bug_title(bug_soup)

    print(
        json.dumps(
            build_result(
                success=True,
                action=args.action,
                bug_id=bug_id,
                form_url=form_url,
                payload=submission_payload,
                server_response=server_response,
                bug_title=bug_title,
                bug_status=bug_status,
            ),
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(
            json.dumps(
                {
                    "success": False,
                    "error": str(exc),
                },
                ensure_ascii=False,
                indent=2,
            ),
            file=sys.stderr,
        )
        raise SystemExit(1)
