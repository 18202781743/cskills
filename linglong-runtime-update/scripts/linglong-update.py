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
  python3 linglong-update.py status
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
import urllib.parse

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------

JENKINS_BASE = "https://jenkins.cicd.getdeepin.org"
JENKINS_REPO_UPDATE_JOB = "view/dtk/job/runtime-repo-update"
JENKINS_BUILD_JOB = "view/dtk/job/linglong-runtime-build"
JENKINS_PUSH_OLD_JOB = "view/dtk/job/linglong-runtime-push-to-old"
JENKINS_PUSH_TEST_JOB = "view/dtk/job/linglong-runtime-push-to-test"

N8N_FORM_URL = "https://n8n.cicd.getdeepin.org/form/097d0087-7f34-4614-8329-82d096af7ba5"
REPO_URL_HOST = "10.20.64.92:8080"
CRIMSON_BASE = f"http://{REPO_URL_HOST}/crimson_runtime"

RUNTIME_REPO_URL = "https://github.com/linglongdev/org.deepin.runtime.git"
WEBENGINE_REPO_URL = "https://github.com/linglongdev/org.deepin.runtime.webengine.git"

# Fork 推送目标 GitHub ID
FORK_OWNER = "18202781743"

# CRP 外部工具路径
_CRP_PACK_SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crp_pack.py")

CACHE_DIR = Path.home() / ".cache" / "linglong-update" / "repos"

DEFAULT_CONFIG: Dict[str, Any] = {
    "crp_topic": "玲珑runtime dtk版本更新",
    "crp_platform_branch": "crimson-testing",
    "crp_branch": "upstream/master",
    "crp_branch_id": 129,
    "archs": ["amd64", "arm64", "loong64"],
    "runtime_repo_path": str(CACHE_DIR / "org.deepin.runtime"),
    "webengine_repo_path": str(CACHE_DIR / "org.deepin.runtime.webengine"),
}

# DTK 项目列表（与 github-workflow-autotag 保持一致）
DTK_PROJECTS = [
    "dtkcommon-v25", "dtklog-v25", "dtkcore-v25", "dtkgui-v25", "dtkwidget-v25",
    "dtkdeclarative-v25", "qt5integration-v25", "qt5platform-plugins-v25",
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
# CRP 打包（调用外部 crp_pack.py）
# ---------------------------------------------------------------------------

def _run_crp(args: List[str], check: bool = True) -> subprocess.CompletedProcess:
    """调用外部 crp_pack.py，自动清理代理环境变量。"""
    cmd = [sys.executable, _CRP_PACK_SCRIPT] + args
    _log(f"执行: {' '.join(cmd)}")
    env = {k: v for k, v in os.environ.items()
           if not k.lower().endswith("_proxy")}
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if check and result.returncode != 0:
        err = result.stderr.strip() or result.stdout.strip()
        if "EOF when reading a line" in err:
            _log("CRP 认证失败，请先执行: python3 " + _CRP_PACK_SCRIPT + " auth", "ERROR")
        else:
            _log(f"crp_pack.py 错误: {err[:500]}", "ERROR")
        raise RuntimeError(f"crp_pack.py 退出码 {result.returncode}")
    return result

def _get_crp_instances(topic: str, branch_id: Optional[int] = None) -> List[Dict[str, Any]]:
    """获取 CRP 指定 topic 下的所有打包实例（委托给外部 crp_pack.py，解析 JSON 输出）。"""
    try:
        args_list = ["instances", "--topic", topic]
        if branch_id:
            args_list.extend(["--branch-id", str(branch_id)])
        result = _run_crp(args_list, check=False)
        if result.returncode != 0:
            err = result.stderr.strip() or result.stdout.strip()
            _log(f"获取 CRP 实例失败: {err[:200]}", "WARN")
            return []
        data = json.loads(result.stdout)
        return data.get("instances", []) if data.get("success") else []
    except json.JSONDecodeError:
        _log("CRP instances 输出不是合法 JSON，请确认 crp_pack.py 版本", "WARN")
        return []
    except Exception as e:
        _log(f"获取 CRP 实例异常: {e}", "WARN")
        return []


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

def _get_repo_slug(repo_path: str) -> str:
    """从 git remote origin 提取 owner/repo。"""
    url = subprocess.run(
        ["git", "-C", repo_path, "remote", "get-url", "origin"],
        capture_output=True, text=True).stdout.strip()
    m = re.search(r'github\.com[:/]([^/]+/[^/]+?)(?:\.git)?$', url)
    if not m:
        raise RuntimeError(f"无法解析 GitHub repo: {url}")
    return m.group(1)


def _ensure_fork(repo_slug: str, fork_owner: Optional[str] = None) -> str:
    """确保 fork 存在，返回 fork 的 owner/repo。

    优先级: 外部参数 > gh api user 探测 > FORK_OWNER 默认值
    """
    if not fork_owner:
        # 探测当前 gh 登录用户
        try:
            fork_owner = subprocess.run(
                ["gh", "api", "user", "--jq", ".login"],
                capture_output=True, text=True).stdout.strip()
        except Exception:
            pass
    if not fork_owner:
        fork_owner = FORK_OWNER

    fork_slug = f"{fork_owner}/{repo_slug.split('/')[-1]}"
    # 检查 fork 是否已存在
    result = subprocess.run(
        ["gh", "repo", "view", fork_slug],
        capture_output=True, text=True)
    if result.returncode == 0:
        _log(f"fork 已存在: {fork_slug}")
        return fork_slug
    _log(f"创建 fork: {repo_slug} -> {fork_slug} ...")
    subprocess.run(["gh", "repo", "fork", repo_slug, "--clone=false"],
                   check=True)
    _log(f"fork 创建完成: {fork_slug}")
    return fork_slug


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
        self._fetch_csrf()

    def _fetch_csrf(self) -> None:
        try:
            resp = self.session.get(
                f"{JENKINS_BASE}/crumbIssuer/api/json", timeout=30
            )
            if resp.status_code == 200:
                data = resp.json()
                field = data.get("crumbRequestField", "Jenkins-Crumb")
                crumb = data.get("crumb", "")
                self.session.headers[field] = crumb
                self._crumb_field = field
                self._crumb = crumb
                _log(f"CSRF crumb 已获取")
            else:
                self._crumb_field = "Jenkins-Crumb"
                self._crumb = ""
                _log(f"crumbIssuer API 返回 {resp.status_code}，尝试从页面提取")
                self._fetch_csrf_from_html()
        except Exception:
            _log("无法通过 API 获取 CSRF crumb，尝试从页面提取", "WARN")
            self._fetch_csrf_from_html()

    def _fetch_csrf_from_html(self) -> None:
        try:
            resp = self.session.get(f"{JENKINS_BASE}/", timeout=30)
            m = re.search(r'data-crumb-value="([^"]+)"', resp.text)
            if m:
                self._crumb = m.group(1)
                m2 = re.search(r'data-crumb-header="([^"]+)"', resp.text)
                self._crumb_field = m2.group(1) if m2 else "Jenkins-Crumb"
                self.session.headers[self._crumb_field] = self._crumb
                _log(f"从页面提取 CSRF crumb 成功")
            else:
                self._crumb_field = "Jenkins-Crumb"
                self._crumb = ""
                _log("页面中未找到 crumb，POST 请求可能被拒", "WARN")
        except Exception:
            self._crumb_field = "Jenkins-Crumb"
            self._crumb = ""
            _log("无法从页面提取 crumb，POST 请求可能被拒", "WARN")

    def _api_url(self, job_path: str) -> str:
        return f"{JENKINS_BASE}/{job_path}/api/json"

    def _build_url(self, job_path: str) -> str:
        return f"{JENKINS_BASE}/{job_path}/build"

    def _build_params_url(self, job_path: str) -> str:
        return f"{JENKINS_BASE}/{job_path}/buildWithParameters"

    def trigger_build(self, job_path: str,
                      params: Optional[Dict[str, str]] = None) -> Optional[int]:
        """触发参数化构建，从 Location 或 queue item 获取真实 build 编号。

        Jenkins 参数化构建表单使用 name=PARAM&value=VAL 格式编码。
        当已有构建在跑时，新构建进入队列，Location 重定向到 job 页面，
        此时需要通过轮询 lastBuild 检测新构建编号。
        """
        url = f"{JENKINS_BASE}/{job_path}/build?delay=0sec"

        # 获取触发前的 lastBuild 编号，用于队列场景的增量检测
        prev_build = self._get_last_build_number(job_path)

        # 使用 Jenkins 标准表单格式: name=PARAM_NAME&value=PARAM_VALUE
        form_parts = []
        json_params = []
        if params:
            for k, v in params.items():
                form_parts.append(f"name={urllib.parse.quote(k, safe='')}&value={urllib.parse.quote(v, safe='')}")
                json_params.append({"name": k, "value": v})
        if self._crumb:
            form_parts.append(f"{self._crumb_field}={urllib.parse.quote(self._crumb, safe='')}")
        # 添加 statusCode/redirectTo 以触发正确的 HTTP 303 重定向
        form_parts.append("statusCode=303")
        form_parts.append("redirectTo=.")
        # 构建正确的 json 参数（包含实际参数和状态信息）
        json_obj = {"parameter": json_params, "statusCode": "303", "redirectTo": "."}
        form_parts.append("json=" + urllib.parse.quote(json.dumps(json_obj), safe=''))
        body = "&".join(form_parts)

        resp = self.session.post(
            url,
            data=body,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=60,
            allow_redirects=False,
        )
        if resp.status_code in (200, 201, 302, 303):
            _log(f"构建已触发, HTTP {resp.status_code}")
            loc = resp.headers.get("Location", "")
            m = re.search(r'/(\d+)/?$', loc)
            if m:
                return int(m.group(1))
            qm = re.search(r'/queue/item/(\d+)', loc)
            if qm:
                queue_id = qm.group(1)
                build_num = self._get_build_from_queue(queue_id)
                if build_num:
                    return build_num
            # 队列场景：轮询 lastBuild 直到编号变化或超时
            _log("构建已入队，等待分配 build 编号...")
            for _ in range(30):
                time.sleep(2)
                cur = self._get_last_build_number(job_path)
                if cur is not None and (prev_build is None or cur > prev_build):
                    return cur
            return None
        else:
            _log(f"触发失败: {resp.status_code} {resp.text[:200]}", "ERROR")
            return None
    def _get_last_build_number(self, job_path: str) -> Optional[int]:
        """获取最近一次构建的编号。"""
        try:
            resp = self.session.get(
                self._api_url(job_path),
                params={"tree": "lastBuild[number]"},
                timeout=30,
            )
            if resp.status_code != 200:
                return None
            data = resp.json()
            last = data.get("lastBuild", {})
            return last.get("number")
        except Exception:
            return None


    def _get_build_from_queue(self, queue_id: str) -> Optional[int]:
        """从 queue item API 获取对应的 build 编号。"""
        try:
            url = f"{JENKINS_BASE}/queue/item/{queue_id}/api/json"
            resp = self.session.get(url, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                executable = data.get("executable", {})
                if executable:
                    return executable.get("number")
            return None
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
    """从 Jenkins 控制台输出提取仓库地址。

    支持直接匹配实际地址，也支持 your-server 占位符替换。
    同时尝试匹配 aptly 输出中的 deb 行，以及 linglong-runtime-build
    下载路径中的相对路径。
    """
    # 直接匹配 10.20.64.92:8080 地址
    pattern = re.escape(CRIMSON_BASE) + r'/stable_[^\s"]+/'
    m = re.search(pattern, console)
    if m:
        return m.group(0)
    # 匹配 your-server 占位符地址，替换为实际服务器
    pattern2 = r'http://your-server/crimson_runtime/stable_[^\s"]+/'
    m2 = re.search(pattern2, console)
    if m2:
        return m2.group(0).replace('your-server', REPO_URL_HOST)
    # 匹配 deb 行中的地址（可能有缩进）
    pattern3 = r'deb\s+(http://your-server/crimson_runtime/stable_[^\s]+/)'
    m3 = re.search(pattern3, console)
    if m3:
        return m3.group(1).replace('your-server', REPO_URL_HOST)
    # 匹配 linglong-runtime-build 下载路径中的相对路径（无 http:// 前缀）
    pattern4 = r'/crimson_runtime/(stable_[\w]+/)'
    m4 = re.search(pattern4, console)
    if m4:
        return f"http://{REPO_URL_HOST}/crimson_runtime/{m4.group(1)}"
    return None


# ---------------------------------------------------------------------------
# Step 1: CRP 打包
# ---------------------------------------------------------------------------

def crp_pack(cfg: Dict[str, Any], topic: Optional[str] = None,
               branch: Optional[str] = None, archs: Optional[str] = None,
               branch_id: Optional[int] = None, version: Optional[str] = None,
               dry_run: bool = False) -> bool:
    """CRP 打包 — 调用外部 crp_pack.py。"""
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
        branch_id = cfg.get("crp_branch_id")

    print(f"\n  Topic   : {topic}")
    print(f"  分支    : {branch}")
    print(f"  架构    : {archs}")
    print(f"  版本/tag: {version or '(自动)'}")
    print(f"  项目    : {', '.join(DTK_PROJECTS)}\n")

    if dry_run:
        _log("DRY RUN — 不会实际提交打包", "WARN")
        _log(f"  topic: {topic}, 分支: {branch}, 架构: {archs}")
        _log(f"  将为 {len(DTK_PROJECTS)} 个项目创建打包实例: {', '.join(DTK_PROJECTS)}")
        return True

    failed = []
    for proj in DTK_PROJECTS:
        _log(f"打包 {proj}...")
        try:
            args = ["pack", "--topic", topic, "--project", proj,
                    "--branch", branch, "--archs", archs]
            if branch_id:
                args.extend(["--branch-id", str(branch_id)])
            if version:
                args.extend(["--tag", version])
            _run_crp(args)
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
        if not repo_id:
            repo_id = datetime.now().strftime("%Y%m%d")

    print(f"\n  标识: {repo_id}\n")

    if dry_run:
        _log("认证 Jenkins（dry-run 仍会验证凭证）...")
    creds = _ensure_jenkins_auth()
    _log("Jenkins 认证成功")

    if dry_run:
        _log(f"DRY RUN — 将触发参数: repo_id={repo_id}", "WARN")
        return f"{CRIMSON_BASE + "/stable_"}{datetime.now().strftime("%Y%m%d")}_{repo_id}/"

    jc = JenkinsClient(creds["user"], creds["password"])
    if not jc.job_exists(JENKINS_REPO_UPDATE_JOB):
        _log(f"Job 不存在: {JENKINS_REPO_UPDATE_JOB}", "ERROR")
        return None



    _log(f"触发: {JENKINS_REPO_UPDATE_JOB}")
    build_num = jc.trigger_build(JENKINS_REPO_UPDATE_JOB, {"SUFFIX": repo_id})
    if not build_num:
        _log("未能获取构建编号", "ERROR")
        return None

    _log(f"构建 #{build_num}: {JENKINS_BASE}/{JENKINS_REPO_UPDATE_JOB}/{build_num}/")

    _log("构建已触发，使用 check-repo 查询进度和仓库地址")
    return None




def check_repo(cfg, build_url, extract_repo: bool = True):
    """查询构建状态并提取仓库地址，不轮询等待。"""
    _log("=" * 60)
    _log("查询构建状态")
    _log("=" * 60)

    base = JENKINS_BASE.rstrip("/")
    if not build_url.startswith(base):
        _log(f"URL 必须以 {base} 开头", "ERROR")
        return None

    path = build_url[len(base):].strip("/")
    parts = [p for p in path.split("/") if p]
    if not parts:
        _log("无法解析 URL 中的 job 路径和构建编号", "ERROR")
        return None

    try:
        build_number = int(parts[-1])
    except ValueError:
        _log(f"构建编号无效: {parts[-1]}", "ERROR")
        return None

    job_path = "/".join(parts[:-1])

    print(f"\n  Job: {job_path}\n  构建: #{build_number}\n")
    _log(f"Jenkins URL: {JENKINS_BASE}/{job_path}/{build_number}/")

    creds = _ensure_jenkins_auth()
    _log("Jenkins 认证成功")

    jc = JenkinsClient(creds["user"], creds["password"])
    try:
        status = jc.get_build_status(job_path, build_number)
    except Exception as e:
        _log(f"获取构建状态失败: {e}", "ERROR")
        return None

    if status["building"]:
        _log(f"构建 #{build_number} 仍在进行中 (result={status.get('result', 'N/A')})")
        return None

    if status.get("result") == "SUCCESS":
        _log(f"构建 #{build_number} 成功!")
        if extract_repo:
            console = jc.get_console_output(job_path, build_number)
            repo_url = _extract_repo_url(console)
            if repo_url:
                print(f"\n  仓库地址: {repo_url}\n")
            else:
                today = datetime.now().strftime("%Y%m%d")
                _log("未能从控制台输出提取仓库地址", "WARN")
            return repo_url
        return True
    else:
        result = status.get("result", "UNKNOWN")
        _log(f"构建 #{build_number}: {result}", "ERROR")
        return None

# ---------------------------------------------------------------------------
# Step 3: 仓库更新与 PR
# ---------------------------------------------------------------------------

def update_repo(cfg: Dict[str, Any], version: Optional[str] = None,
                deb_repo: Optional[str] = None,
                fork_owner: Optional[str] = None,
                repo: str = "runtime",
                dry_run: bool = False) -> bool:
    _log("=" * 60)
    _log("修改 yaml 文件并创建 PR")
    _log("=" * 60)

    if deb_repo is None:
        deb_repo = input(f"deb 更新仓库地址 (如 {CRIMSON_BASE}/stable_xxx/): ").strip()

    if version is None:
        try:
            version = _infer_version(deb_repo)
        except Exception as e:
            _log(f"自动推断版本失败: {e}", "WARN")
            version = input("版本号 (如 6.7.0.45): ").strip()

    print(f"\n  版本号  : {version}")
    print(f"  deb 仓库: {deb_repo}\n")

    if dry_run:
        _log("检查 gh 认证（dry-run 仍会验证)...")
    _log("检查 gh 认证...")
    if not _check_gh_auth():
        _log("gh CLI 未认证，请先执行: gh auth login", "ERROR")
        return False
    _log("gh 认证通过")

    _log("检查仓库...")
    if not _ensure_repos_ready(cfg):
        return False
    _log("仓库就绪")

    if dry_run:
        _log("DRY RUN — 不会实际修改仓库", "WARN")
        _log(f"  将修改 linglong.yaml 版本为 {version}")
        _log(f"  将修改 linglong.yaml 仓库地址为 {deb_repo}")
        return True

    if repo == "webengine":
        if not _update_webengine_repo("org.deepin.runtime.webengine",
                                       cfg["webengine_repo_path"], version, deb_repo,
                                       cfg["runtime_repo_path"]):
            return False
    else:
        if not _update_runtime_repo("org.deepin.runtime", cfg["runtime_repo_path"],
                                     version, deb_repo, fork_owner):
            return False

    _log("仓库更新完成")
    return True


def _infer_version(deb_repo: str) -> str:
    """从 deb 仓库解析 dtkcore 版本计算玲珑 runtime 版本。

    以 amd64 架构为准，版本格式与 DTK 版本 X.Y.Z 一致。
    """
    pool_url = deb_repo.rstrip("/") + "/pool/main/d/dtkcore/"
    _log(f"从 deb 仓库获取 dtkcore 版本: {pool_url}")
    resp = requests.get(pool_url, timeout=30)
    if resp.status_code != 200:
        raise RuntimeError(f"无法访问 deb 仓库: {pool_url} ({resp.status_code})")
    # 匹配 libdtk6core_X.Y.Z-N_amd64.deb，提取版本号（以 amd64 为准）
    m = re.search(r'libdtk6core_(\d+\.\d+\.\d+)(?:-\d+)?_amd64\.deb', resp.text)
    if not m:
        raise RuntimeError(f"deb 仓库中未找到 dtkcore amd64 包: {pool_url}")
    new_ver = m.group(1)
    _log(f"从 deb 仓库推断版本: {new_ver} (dtkcore {m.group(1)})")
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

def _update_deepin_repo_url(repo_path: str, repo_url: str) -> None:
    """更新 update.go 中的 deepinRepoURL 变量。"""
    update_go = os.path.join(repo_path, "update.go")
    if not os.path.exists(update_go):
        _log("update.go 不存在", "WARN")
        return
    go_content = Path(update_go).read_text()
    # 匹配 Go 字符串字面量，处理双引号和反引号两种形式
    new_c = re.sub(
        r'(deepinRepoURL\s*=\s*)("[^"]*"|`[^`]*`)',
        f'\\g<1>"{repo_url.rstrip("/")}"',
        go_content,
        count=1,
    )
    if new_c != go_content:
        Path(update_go).write_text(new_c)
        _log(f"update.go 仓库地址已更新为 {repo_url}")

def _update_runtime_repo(label: str, repo_path: str, version: str,
                         deb_repo: str,
                         fork_owner: Optional[str] = None) -> bool:
    """更新 org.deepin.runtime 仓库：新分支 → 脚本 → amend → fork → PR。"""
    _log(f"--- {label} ---")
    # 1. 清理：fetch origin，reset 到最新
    _run(["git", "-C", repo_path, "fetch", "origin"])
    _run(["git", "-C", repo_path, "checkout", "--", "."], check=False)
    _run(["git", "-C", repo_path, "clean", "-fd"], check=False)
    # 删除旧的 update/linglong-runtime-* 分支
    result = subprocess.run(
        ["git", "-C", repo_path, "branch"], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        b = line.strip().lstrip("* ")
        if b.startswith("update/linglong-runtime-"):
            _run(["git", "-C", repo_path, "branch", "-D", b], check=False)
    # 切换到 main/master 并 reset
    try:
        _run(["git", "-C", repo_path, "checkout", "main"])
    except subprocess.CalledProcessError:
        _run(["git", "-C", repo_path, "checkout", "master"])
    _run(["git", "-C", repo_path, "reset", "--hard", "origin/HEAD"])

    # 2. 固定分支，存在则切过去，否则新建
    branch = "update/linglong-runtime"
    _log(f"使用固定分支: {branch}")
    result = subprocess.run(
        ["git", "-C", repo_path, "branch", "--list", branch],
        capture_output=True, text=True)
    branch_existed = bool(result.stdout.strip())
    if branch_existed:
        _run(["git", "-C", repo_path, "checkout", branch])
    else:
        _run(["git", "-C", repo_path, "checkout", "-b", branch])

    # 3. 修改 yaml + 执行 daily.bash
    _update_version_in_yaml(repo_path, version)
    _update_repo_url_in_yaml(repo_path, deb_repo)
    _update_deepin_repo_url(repo_path, deb_repo)

    daily = os.path.join(repo_path, "daily.bash")
    if os.path.exists(daily):
        _log("执行 daily.bash...")
        _run(["bash", daily, version], cwd=repo_path)
    else:
        _log("daily.bash 不存在", "WARN")

    # 4. 提交：分支已存在则 amend，否则新建
    _run(["git", "-C", repo_path, "add", "-A"])
    msg = (f"chore: update linglong runtime to {version}\n\n"
           f"Update repo URL to {deb_repo}\nVersion: {version}\n\n"
           f"Log: 更新玲珑 runtime 到 {version}\n"
           f"Influence: 更新 DTK 玲珑 runtime 依赖仓库地址和版本")
    if branch_existed:
        _run(["git", "-C", repo_path, "commit", "--amend", "-m", msg, "--allow-empty"], check=False)
        _log(f"合并到上一次提交")
    else:
        _run(["git", "-C", repo_path, "commit", "-m", msg])

    # 5. 通过 fork 推送
    repo_slug = _get_repo_slug(repo_path)
    fork_slug = _ensure_fork(repo_slug, fork_owner)
    fork_remote = f"https://github.com/{fork_slug}.git"
    _run(["git", "-C", repo_path, "remote", "remove", "fork"], check=False)
    _run(["git", "-C", repo_path, "remote", "add", "fork", fork_remote])
    _log(f"强推到 fork: {fork_slug}")
    _run(["git", "-C", repo_path, "push", "-f", "fork", branch])

    # 6. 创建或复用 PR
    existing_pr = subprocess.run(
        ["gh", "pr", "list", "--repo", repo_slug,
         "--state", "open", "--json", "headRefName,url",
         "--jq", f'.[] | select(.headRefName == "{branch}") | .url'],
        capture_output=True, text=True).stdout.strip()
    if existing_pr:
        _log(f"PR 已存在: {existing_pr}")
        pr_url = existing_pr
    else:
        _log("创建 PR...")
        result = _run_gh(["pr", "create",
                          "--repo", repo_slug,
                          "--title", f"chore: update linglong runtime to {version}",
                          "--body", f"Update repo URL to {deb_repo}\nVersion: {version}",
                          "--base", "main", "--head", f"{fork_slug.split('/')[0]}:{branch}"],
                          cwd=repo_path)
        pr_url = result.stdout.strip()
    print(f"\n  PR: {pr_url}\n")

    if _input_confirm(f"等待 {label} PR 合并?"):
        _wait_for_pr_merge(label, repo_path, pr_url)
    return True
def _update_webengine_repo(label: str, repo_path: str, version: str,
                           deb_repo: str,
                           runtime_repo_path: str) -> bool:
    """更新 org.deepin.runtime.webengine 仓库：以 runtime 为基准，补丁 + 脚本各一 commit，强推 main。"""
    _log(f"--- {label} ---")
    # 1. 以 runtime 最新代码为基准
    _run(["git", "-C", repo_path, "remote", "remove", "runtime-base"], check=False)
    _run(["git", "-C", repo_path, "remote", "add", "runtime-base", runtime_repo_path])
    _run(["git", "-C", repo_path, "fetch", "runtime-base"])
    _run(["git", "-C", repo_path, "checkout", "--", "."], check=False)
    _run(["git", "-C", repo_path, "clean", "-fd"], check=False)
    # 切到 main
    try:
        _run(["git", "-C", repo_path, "checkout", "main"])
    except subprocess.CalledProcessError:
        _run(["git", "-C", repo_path, "checkout", "master"])
    _run(["git", "-C", repo_path, "reset", "--hard", "runtime-base/HEAD"])

    # 2. 应用 webengine 补丁 → commit 1
    patch_path = _find_webengine_patch()
    if patch_path:
        # 检查是否已应用
        reverse_check = subprocess.run(
            ["git", "-C", repo_path, "apply", "--check", "--reverse", patch_path],
            capture_output=True)
        if reverse_check.returncode == 0:
            _log(f"补丁已应用，跳过: {patch_path}")
        else:
            _log(f"应用补丁: {patch_path}")
            try:
                _run(["git", "-C", repo_path, "apply", patch_path])
                _log("补丁应用成功")
            except subprocess.CalledProcessError:
                _log("git apply 失败，尝试三路合并...", "WARN")
                try:
                    _run(["git", "-C", repo_path, "apply", "--3way", patch_path])
                    _log("三路合并成功")
                except subprocess.CalledProcessError:
                    _log("补丁应用彻底失败，检查冲突", "ERROR")
                    return False
            _run(["git", "-C", repo_path, "add", "-A"])
            _run(["git", "-C", repo_path, "commit", "-m",
                  f"feat: apply webengine patch\n\n{os.path.basename(patch_path)}"])
    else:
        _log("未找到 webengine 补丁，跳过", "WARN")

    # 3. 修改 yaml + 执行 daily.bash → commit 2
    _update_version_in_yaml(repo_path, version)
    _update_repo_url_in_yaml(repo_path, deb_repo)
    _update_deepin_repo_url(repo_path, deb_repo)

    daily = os.path.join(repo_path, "daily.bash")
    if os.path.exists(daily):
        _log("执行 daily.bash...")
        _run(["bash", daily, version], cwd=repo_path)
    else:
        _log("daily.bash 不存在", "WARN")

    _run(["git", "-C", repo_path, "add", "-A"])
    msg = (f"chore: update linglong runtime to {version}\n\n"
           f"Update repo URL to {deb_repo}\nVersion: {version}\n\n"
           f"Log: 更新玲珑 runtime 到 {version}\n"
           f"Influence: 更新 DTK 玲珑 runtime 依赖仓库地址和版本")
    _run(["git", "-C", repo_path, "commit", "-m", msg])

    # 4. 强推到 origin/main
    _log(f"强制推送到 origin ({label})")
    _run(["git", "-C", repo_path, "push", "-f", "origin", "HEAD:main"])
    _log(f"{label} 已强推到 origin/main")
    return True


def _update_version_in_yaml(repo_path: str, version: str) -> None:
    yp = os.path.join(repo_path, "linglong.yaml")
    if not os.path.exists(yp):
        _log("linglong.yaml 不存在", "WARN")
        return
    yaml_content = Path(yp).read_text()
    new_c = re.sub(r'(version:\s*)\S*', f'\\g<1>{version}', yaml_content, count=1)
    if new_c != yaml_content:
        Path(yp).write_text(new_c)
        _log(f"版本号已更新为 {version}")
    else:
        _log(f"version 字段未找到或无需更新", "WARN")


def _update_repo_url_in_yaml(repo_path: str, repo_url: str) -> None:
    yp = os.path.join(repo_path, "linglong.yaml")
    if not os.path.exists(yp):
        _log("linglong.yaml 不存在", "WARN")
        return
    content = Path(yp).read_text()
    pat = re.escape(CRIMSON_BASE) + r'/stable_[^\s"\']+/'
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

    if repo_url is None:
        repo_url = "github.com/linglongdev/org.deepin.runtime"
    if repo_branch is None:
        repo_branch = "main"

    print(f"\n  REPO_URL    : {repo_url}")
    print(f"  REPO_BRANCH : {repo_branch}\n")

    if dry_run:
        _log("认证 Jenkins（dry-run 仍会验证凭证）...")
    _log("认证 Jenkins...")
    creds = _ensure_jenkins_auth()
    _log("Jenkins 认证成功")

    if dry_run:
        _log("DRY RUN — 不会实际触发构建", "WARN")
        _log(f"  将触发: {JENKINS_BUILD_JOB}")
        _log(f"  参数: REPO_URL={repo_url}, REPO_BRANCH={repo_branch}")
        return True

    jc = JenkinsClient(creds["user"], creds["password"])
    if not jc.job_exists(JENKINS_BUILD_JOB):
        _log(f"Job 不存在: {JENKINS_BUILD_JOB}", "ERROR")
        return False

    params = {"REPO_URL": repo_url, "REPO_BRANCH": repo_branch}
    _log(f"触发: {JENKINS_BUILD_JOB} params={params}")
    build_num = jc.trigger_build(JENKINS_BUILD_JOB, params)
    if not build_num:
        _log("未能获取构建编号", "ERROR")
        return False

    _log(f"构建 #{build_num}: {JENKINS_BASE}/{JENKINS_BUILD_JOB}/{build_num}/")
    _log("构建已触发，使用 check-build 查询进度")
    return True


# ---------------------------------------------------------------------------
# Step 5: N8N 推送
# ---------------------------------------------------------------------------


def _resolve_layer_url(url: str, jc: JenkinsClient) -> str:
    """如果 url 是 Jenkins 构建地址，从控制台输出提取真实 layer 地址。"""
    base = JENKINS_BASE.rstrip("/")
    if not url.startswith(base):
        return url

    path = url[len(base):].strip("/")
    parts = [p for p in path.split("/") if p]
    if not parts:
        _log(f"无法解析 Jenkins URL: {url}", "ERROR")
        return url

    try:
        build_number = int(parts[-1])
    except ValueError:
        return url

    job_path = "/".join(parts[:-1])
    _log(f"解析 Jenkins 构建: {job_path} #{build_number}")
    try:
        console = jc.get_console_output(job_path, build_number)
    except Exception as e:
        _log(f"获取控制台输出失败: {e}", "ERROR")
        return url

    repo_url = _extract_repo_url(console)
    if repo_url:
        _log(f"从构建输出提取地址: {repo_url}")
        return repo_url

    _log("控制台输出中未找到仓库地址，使用原始 URL", "WARN")
    return url

def push_layer(cfg: Dict[str, Any], layer_url: Optional[str] = None,
               dry_run: bool = False) -> bool:
    """N8N 推送 Layer 到玲珑仓库。

    layer_url: LAYER_URL 参数，对应 build-layer 产出的 layer 地址。
    先提交 N8N 表单，然后触发 Jenkins push-to-old 和 push-to-test。
    """
    _log("=" * 60)
    _log("N8N 推送 Layer")
    _log("=" * 60)

    if layer_url is None:
        if dry_run:
            layer_url = f"{CRIMSON_BASE}/stable_test/"
        else:
            layer_url = input(f"LAYER_URL (如 {CRIMSON_BASE}/stable_xxx/): ").strip()

    print(f"\n  LAYER_URL: {layer_url}")
    print(f"  N8N 表单 : {N8N_FORM_URL}\n")

    if dry_run:
        _log("认证 Jenkins（dry-run 仍会验证凭证）...")
    _log("认证 Jenkins...")
    creds = _ensure_jenkins_auth()
    _log("Jenkins 认证成功")

    jc = JenkinsClient(creds["user"], creds["password"])

    # 如果 layer_url 是 Jenkins 构建地址，解析出真实 layer 地址
    if layer_url and layer_url.startswith(JENKINS_BASE):
        resolved = _resolve_layer_url(layer_url, jc)
        if resolved != layer_url:
            layer_url = resolved
            print(f"\n  LAYER_URL: {layer_url}\n")

    if dry_run:
        _log("DRY RUN — 不会实际触发推送", "WARN")
        _log(f"  将触发: {JENKINS_PUSH_OLD_JOB} 和 {JENKINS_PUSH_TEST_JOB}")
        _log(f"  参数: LAYER_URL={layer_url}")
        return True

    if not layer_url:
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
    build_repo(cfg, repo_id, dry_run)
    return True


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
        "crp_branch": _p("crp_branch", "Git 分支过滤 (如 upstream/master)"),
        "crp_branch_id": _p("crp_branch_id", "CRP BranchID (整数)"),
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
# status 命令
# ---------------------------------------------------------------------------

def cmd_status(cfg: Dict[str, Any]) -> int:
    """查询各阶段状态，包括 CRP 实例、Jenkins 最近构建、GitHub PR 和本地 state。"""
    print("\n" + "=" * 60)
    print("状态查询")
    print("=" * 60)

    topic = cfg.get("crp_topic", "玲珑runtime dtk版本更新")

    # --- CRP 打包实例 ---
    print("\n--- CRP 打包实例 ---")
    try:
        instances = _get_crp_instances(topic, cfg.get("crp_branch_id"))
        if instances:
            for inst in instances:
                print(f"  {inst.get('project_name', '?'):30s} {inst.get('branch', '?'):25s} {inst.get('tag', '(无tag)')}")
        else:
            print("  (无打包实例或 CRP 未认证)")
    except Exception as e:
        print(f"  CRP 查询失败: {e}")

    # --- Jenkins 最近构建 ---
    print("\n--- Jenkins 最近构建 ---")
    try:
        creds = _load_jenkins_creds()
        if not creds:
            print("  Jenkins 未配置认证")
        else:
            jc = JenkinsClient(creds["user"], creds["password"])
            jobs = [
                (JENKINS_REPO_UPDATE_JOB, "runtime-repo-update"),
                (JENKINS_BUILD_JOB, "linglong-runtime-build"),
                (JENKINS_PUSH_OLD_JOB, "linglong-runtime-push-to-old"),
                (JENKINS_PUSH_TEST_JOB, "linglong-runtime-push-to-test"),
            ]
            for path, name in jobs:
                try:
                    b = jc.get_last_build_status(path)
                    result = b.get("result") or "BUILDING" if b.get("building") else "N/A"
                    num = b.get("number", "?")
                    print(f"  {name:35s} #{num:>5}  {result}")
                except Exception:
                    print(f"  {name:35s}  无法访问")
    except EOFError:
        print("  Jenkins 未配置认证")
    except Exception as e:
        print(f"  Jenkins 查询失败: {e}")

    # --- GitHub PR ---
    print("\n--- GitHub Open PR ---")
    try:
        for label, path in [("org.deepin.runtime", cfg["runtime_repo_path"]),
                            ("org.deepin.runtime.webengine", cfg["webengine_repo_path"])]:
            if not Path(path).is_dir():
                print(f"  {label}: 仓库未 clone")
                continue
            try:
                r = _run_gh(["pr", "list", "--state", "open", "--limit", "5",
                            "--json", "number,title,createdAt,url"], cwd=path)
                prs = json.loads(r.stdout)
                if prs:
                    for pr in prs:
                        print(f"  {label} #{pr['number']}: {pr['title']} ({pr['createdAt']})")
                        print(f"         {pr['url']}")
                else:
                    print(f"  {label}: 无 open PR")
            except Exception as e:
                print(f"  {label}: gh 查询失败 ({e})")
    except EOFError:
        print("  未配置 gh 认证")
    except Exception as e:
        print(f"  GitHub PR 查询失败: {e}")

    # --- 本地 state ---
    print("\n--- 本地状态 ---")
    state = load_state()
    if state:
        print(f"  版本: {state.get('version', 'N/A')}")
        print(f"  当前步骤: {state.get('current_step', 'N/A')}")
        print(f"  仓库地址: {state.get('repo_url', 'N/A')}")
        print(f"  开始时间: {state.get('started_at', 'N/A')}")
    else:
        print("  (无进行中的任务)")

    print()
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
│  s. 查看状态                                   │
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
                state["repo_url"] = input(f"仓库地址 (如 {CRIMSON_BASE}/stable_xxx/): ").strip()
            version = input("版本号 (如 1.1.1.1): ").strip()
            update_repo(cfg, version, state.get("repo_url"))
        elif choice == "4":
            build_layer(cfg)
        elif choice == "5":
            layer_url = input(f"LAYER_URL (可选，如 {CRIMSON_BASE}/stable_xxx/): ").strip() or None
            push_layer(cfg, layer_url)
        elif choice == "6":
            cmd_config()
        elif choice == "s":
            cmd_status(cfg)
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
            s.add_argument("--deb-repo", required=True, help=f"deb 更新仓库地址（如 {CRIMSON_BASE}/stable_xxx/）")
            s.add_argument("--fork-owner", default=None, help=f"Fork 目标 GitHub 用户/组织（默认 {FORK_OWNER}）")
            s.add_argument("--repo", default="runtime", choices=["runtime", "webengine"],
                           help="目标仓库: runtime (org.deepin.runtime, 默认), webengine (org.deepin.runtime.webengine)")
        elif name == "build-layer":
            s.add_argument("--repo-url", default=None, help="REPO_URL（默认 github.com/linglongdev/org.deepin.runtime）")
            s.add_argument("--repo-branch", default=None, help="REPO_BRANCH（默认 main）")
        elif name == "push-layer":
            s.add_argument("--layer-url", default=None, help="LAYER_URL（build-layer 产出地址）")

    # check-repo — 独立子命令，不在循环中处理
    s = sub.add_parser("check-repo", help="查询构建状态并提取仓库地址")
    s.add_argument("--build-url", required=True, help="Jenkins 构建 URL（如 https://jenkins.cicd.getdeepin.org/view/dtk/job/runtime-repo-update/19/）")

    bs = sub.add_parser("check-build", help="查询构建状态（不提取仓库地址）")
    bs.add_argument("--build-url", required=True, help="Jenkins 构建 URL（如 https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/202/）")

    sub.add_parser("config", help="配置参数（含 Jenkins 凭证）")
    sub.add_parser("status", help="查看各阶段状态（CRP/Jenkins/GitHub/本地）")
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
        elif args.command == "status":
            return cmd_status(cfg)
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
                                    args.fork_owner, args.repo, args.dry_run) else 1
        elif args.command == "build-layer":
            return 0 if build_layer(cfg, args.repo_url, args.repo_branch,
                                    args.dry_run) else 1
        elif args.command == "push-layer":
            return 0 if push_layer(cfg, args.layer_url, args.dry_run) else 1
        elif args.command == "check-repo":
            r = check_repo(cfg, args.build_url)
            return 0 if r else 1
        elif args.command == "check-build":
            r = check_repo(cfg, args.build_url, extract_repo=False)
            return 0 if r else 1
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
