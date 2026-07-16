#!/usr/bin/env python3
"""远程开发同步编译工具"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# ── 路径 ─────────────────────────────────────────────

CONFIG_DIR = Path.home() / ".config" / "remote-dev"
GLOBAL_CONFIG = CONFIG_DIR / "config.json"
PROJECTS_DIR = CONFIG_DIR / "projects"

ACTIONS = {"sync", "build", "install", "all", "watch"}
COMMANDS = {"setup", "list", "ls"} | ACTIONS

# ── 工具链命令模板 ─────────────────────────────────────

TOOL_COMMANDS = {
    "cmake": {
        "configure": "cmake .. {extra}",                         # cmake 配置
        "build": "cmake --build {build_dir} -j{jobs}",           # cmake 编译
        "install": "sudo cmake --install {build_dir}",           # cmake 安装
    },
    "make": {
        "configure": "",                                          # make 无需配置
        "build": "make -j{jobs}",                                 # make 编译
        "install": "sudo make install",                           # make 安装
    },
    "ninja": {
        "configure": "cmake -G Ninja .. {extra}",                 # ninja 配置
        "build": "ninja -C {build_dir} -j{jobs}",                # ninja 编译
        "install": "sudo ninja -C {build_dir} install",          # ninja 安装
    },
    "qmake": {
        "configure": "qmake6 .. {extra}",                         # qmake 配置
        "build": "make -j{jobs}",                                 # qmake 使用 make 编译
        "install": "sudo make install",                           # qmake 使用 make 安装
    },
}

SUPPORTED_TOOLS = list(TOOL_COMMANDS.keys())


def generate_tool_commands(tool, build_dir, extra_args, jobs):
    """根据工具链类型生成配置/编译/安装命令"""
    templates = TOOL_COMMANDS.get(tool, TOOL_COMMANDS["cmake"])
    fmt = {"build_dir": build_dir, "extra": extra_args, "jobs": jobs}
    return {
        "configure": templates["configure"].format(**fmt).strip(),
        "build": templates["build"].format(**fmt),
        "install": templates["install"].format(**fmt),
    }

# ── 颜色 ─────────────────────────────────────────────

GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
RED = "\033[0;31m"
CYAN = "\033[0;36m"
BOLD = "\033[1m"
RESET = "\033[0m"


def log_info(msg):
    print(f"{GREEN}[INFO]{RESET} {timestamp()} {msg}")


def log_warn(msg):
    print(f"{YELLOW}[WARN]{RESET} {timestamp()} {msg}")


def log_error(msg):
    print(f"{RED}[ERROR]{RESET} {timestamp()} {msg}")


def log_watch(msg):
    print(f"{CYAN}[WATCH]{RESET} {timestamp()} {msg}")


def log_cmd(cmd):
    """输出即将执行的命令，供排查使用"""
    if isinstance(cmd, list):
        display = " ".join(str(c) for c in cmd)
    else:
        display = str(cmd)
    print(f"{YELLOW}[CMD]{RESET}  {display}")


def timestamp():
    return datetime.now().strftime("%H:%M:%S")


def run_quiet_command(cmd, label, display_cmd=None, timeout=None, input_text=None):
    """成功时静默，失败时输出命令与错误信息。"""
    r = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        input=input_text,
    )
    if r.returncode != 0:
        log_error(f"{label}失败，详细信息如下")
        if display_cmd is not None:
            log_cmd(display_cmd)
        output = ((r.stdout or "") + (r.stderr or "")).strip()
        if output:
            print(output)
    return r


# ── 同步历史记录 ──────────────────────────────────────

RSYNC_CHANGE_TYPES = {
    "f": "file",
    "d": "directory",
    "L": "symlink",
    "D": "device",
}


def parse_rsync_itemize(output):
    """解析 rsync --itemize-changes 输出，提取变更文件列表"""
    changes = []
    for line in output.splitlines():
        line = line.strip()
        if not line:
            continue
        # itemize 格式: YXcstpoguax  path
        # Y 是 > (发送) 或 < (接收) 或 * (删除等)
        # *deleting 是特殊格式: "*deleting   path"（只有 10 字符前缀 + 空格）
        if line.startswith("*deleting"):
            path = line[12:] if len(line) > 12 else ""
            if path:
                changes.append({"path": path, "action": "deleted"})
            continue
        if len(line) < 13:
            continue
        if line[0] not in (">", "<"):
            continue
        flags = line[:11]
        path = line[12:]

        item_type = RSYNC_CHANGE_TYPES.get(flags[1], "file")

        if "+" in flags:
            action = "created"
        elif "d" in flags:
            action = "deleted"
        elif any(c in flags for c in "cstpog"):
            action = "modified"
        else:
            action = "transferred"

        changes.append({"path": path, "action": action, "type": item_type})
    return changes


def save_sync_history(remote_host, remote_project, project_name, changes, direction="push"):
    """保存最近一次同步历史到远端"""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "project": project_name,
        "direction": direction,
        "count": len(changes),
        "changes": changes,
    }
    remote_path = "~/.remote-dev/history"
    json_str = json.dumps(entry, ensure_ascii=False)
    # 在远端创建目录并写入历史文件（只保留最近一次）
    cmd = [
        "ssh", remote_host,
        f"mkdir -p {remote_path} && cat > {remote_path}/{project_name}.json"
    ]
    r = subprocess.run(cmd, input=json_str, text=True, capture_output=True)
    if r.returncode == 0:
        return f"{remote_host}:{remote_path}/{project_name}.json"
    return None


# ── 配置加载 ─────────────────────────────────────────


def ensure_config_dirs():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)


def load_json(path):
    with open(path) as f:
        return json.load(f)


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_global_config():
    if not GLOBAL_CONFIG.exists():
        return {}
    return load_json(GLOBAL_CONFIG)


def load_project_config(name):
    path = PROJECTS_DIR / f"{name}.json"
    if not path.exists():
        return {}
    return load_json(path)


def _expand_path(path_value):
    return Path(os.path.expanduser(path_value)).resolve()


def _path_is_relative_to(path, other):
    try:
        path.relative_to(other)
        return True
    except ValueError:
        return False


def _nearest_existing_path(path):
    current = _expand_path(path)
    while not current.exists() and current != current.parent:
        current = current.parent
    return current


def get_git_repo_info(path):
    """返回目录所属 Git 仓库信息；worktree 使用 common_dir 关联同一仓库。"""
    base = _nearest_existing_path(path)
    try:
        top = subprocess.run(
            ["git", "-C", str(base), "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
        )
        if top.returncode != 0:
            return None

        common = subprocess.run(
            ["git", "-C", str(base), "rev-parse", "--path-format=absolute", "--git-common-dir"],
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return None

    top_level = _expand_path(top.stdout.strip())
    if common.returncode == 0 and common.stdout.strip():
        common_dir = _expand_path(common.stdout.strip())
    else:
        git_dir = subprocess.run(
            ["git", "-C", str(base), "rev-parse", "--absolute-git-dir"],
            capture_output=True,
            text=True,
        )
        if git_dir.returncode != 0 or not git_dir.stdout.strip():
            return None
        common_dir = _expand_path(git_dir.stdout.strip())

    return {
        "top_level": top_level,
        "common_dir": common_dir,
    }


def normalize_local_project(path_value):
    """将目录归一为绝对路径；若在 Git 仓库中则提升到仓库/worktree 根目录。"""
    resolved = _expand_path(path_value)
    git_info = get_git_repo_info(resolved)
    if git_info:
        return git_info["top_level"], git_info
    return resolved, None


def iter_project_configs():
    ensure_config_dirs()
    for path in sorted(PROJECTS_DIR.glob("*.json")):
        yield path.stem, load_json(path)


def find_project_by_local_dir(local_dir):
    """按本地目录反查项目配置，支持普通目录和 Git worktree。"""
    normalized_local, git_info = normalize_local_project(local_dir)
    candidates = []

    for project_name, project_cfg in iter_project_configs():
        configured_local, configured_git = normalize_local_project(project_cfg["local_project"])
        score = None
        reason = ""

        if normalized_local == configured_local:
            score = 0
            reason = "目录完全匹配"
        elif _path_is_relative_to(normalized_local, configured_local):
            score = 1
            reason = "位于已配置项目目录下"
        elif _path_is_relative_to(configured_local, normalized_local):
            score = 2
            reason = "显式目录包含已配置项目目录"
        elif git_info and configured_git and git_info["common_dir"] == configured_git["common_dir"]:
            score = 3
            reason = "Git worktree 匹配"

        if score is not None:
            candidates.append((score, project_name, project_cfg, reason))

    if not candidates:
        return None, None, None

    candidates.sort(key=lambda item: (item[0], item[1]))
    _, project_name, project_cfg, reason = candidates[0]
    return project_name, project_cfg, reason


def merge_config(global_cfg, project_cfg, adhoc_overrides=None):
    """合并全局配置、项目配置和临时 CLI 参数，优先级: adhoc > project > global"""
    if adhoc_overrides is None:
        adhoc_overrides = {}

    remote_host = adhoc_overrides.get("remote_host") or project_cfg.get("remote_host") or global_cfg.get("remote_host")
    if not remote_host:
        log_error("未配置远程主机")
        log_error("请运行: python remote_dev.py setup --global")
        log_error("或通过 --remote-host 参数指定")
        sys.exit(1)

    local_project = adhoc_overrides.get("local_project") or project_cfg.get("local_project")
    if not local_project:
        log_error("未配置本地项目路径")
        log_error("请运行: python remote_dev.py setup")
        log_error("或通过 --project-dir 参数指定")
        sys.exit(1)

    remote_project = adhoc_overrides.get("remote_project") or project_cfg.get("remote_project")
    if not remote_project:
        log_error("未配置远程项目路径")
        log_error("请运行: python remote_dev.py setup")
        log_error("或通过 --remote-project 参数指定")
        sys.exit(1)

    project_name = project_cfg.get("name") or adhoc_overrides.get("project_name") or Path(local_project).name

    sudo_password = project_cfg.get("sudo_password") or global_cfg.get("sudo_password", "")
    retry_global = global_cfg.get("retry", {})
    retry_project = project_cfg.get("retry", {})
    cmake = project_cfg.get("cmake", {})
    sync = project_cfg.get("sync", {})
    build_cfg = project_cfg.get("build", {})
    deps = project_cfg.get("deps", {})
    restart = project_cfg.get("restart", {})

    build_tool = adhoc_overrides.get("build_tool") or cmake.get("tool", "cmake")
    build_dir = adhoc_overrides.get("build_dir") or cmake.get("build_dir", "build")
    extra_args = adhoc_overrides.get("extra_args") or cmake.get("extra_args", "")
    jobs = adhoc_overrides.get("jobs") or build_cfg.get("parallel_jobs", os.cpu_count() or 4)

    tool_cmds = generate_tool_commands(build_tool, build_dir, extra_args, jobs)

    return {
        "project_name": project_name,
        "remote_host": remote_host,
        "local_project": str(_expand_path(local_project)),
        "configured_local_project": str(_expand_path(local_project)),
        "remote_project": remote_project,
        "sudo_password": sudo_password,
        "build_tool": build_tool,
        "build_dir": build_dir,
        "cmake_extra": extra_args,
        "tool_cmds": tool_cmds,
        "jobs": jobs,
        "install_enabled": adhoc_overrides.get("install_enabled",
            build_cfg.get("install_enabled", True)),
        "exclude": sync.get(
            "exclude", [".git/", "build/", "*.o", "*.pyc", "__pycache__/", ".vscode/", ".idea/"]
        ),
        "delete_extra": sync.get("delete_extra", True),
        "max_retries": retry_project.get("max_attempts", retry_global.get("max_attempts", 5)),
        "wait_seconds": retry_project.get("wait_seconds", retry_global.get("wait_seconds", 30)),
        "deps_enabled": adhoc_overrides.get("deps_enabled",
            deps.get("enabled", False)),
        "deps_command": deps.get("command", ""),
        "restart_enabled": adhoc_overrides.get("restart_enabled",
            restart.get("enabled", False)),
        "restart_command": restart.get("command", ""),
        "auto_sync": adhoc_overrides.get("auto_sync",
            sync.get("auto_sync", False)),
    }


# ── 交互式配置 ────────────────────────────────────────


def prompt(label, default=""):
    """交互式输入，支持默认值"""
    if default:
        raw = input(f"  {label} [{default}]: ").strip()
        return raw if raw else default
    else:
        while True:
            raw = input(f"  {label}: ").strip()
            if raw:
                return raw
            print(f"  {RED}此项必填{RESET}")


def prompt_yn(label, default=True):
    """是/否确认"""
    hint = "Y/n" if default else "y/N"
    raw = input(f"  {label} [{hint}]: ").strip().lower()
    if not raw:
        return default
    return raw in ("y", "yes", "是")


def setup_global():
    """交互式配置全局远程机器信息"""
    ensure_config_dirs()

    print()
    print(f"{BOLD}配置远程机器信息{RESET}")
    print(f"配置将保存到: {GLOBAL_CONFIG}")
    print()

    existing = {}
    if GLOBAL_CONFIG.exists():
        existing = load_global_config()
        print(f"  检测到已有配置，直接回车保留原值")
        print()

    remote_host = prompt("远程主机 (user@host)", existing.get("remote_host", ""))

    sudo_password = existing.get("sudo_password", "")
    if prompt_yn("配置 sudo 密码（明文存储）?", default=False):
        sudo_password = prompt("sudo 密码", sudo_password)

    print()
    retry_attempts = int(prompt("最大重试次数", str(existing.get("retry", {}).get("max_attempts", 5))))
    retry_wait = int(prompt("重试等待秒数", str(existing.get("retry", {}).get("wait_seconds", 30))))

    config = {
        "remote_host": remote_host,
        "sudo_password": sudo_password,
        "retry": {
            "max_attempts": retry_attempts,
            "wait_seconds": retry_wait,
        },
    }

    save_json(GLOBAL_CONFIG, config)
    print()
    log_info(f"全局配置已保存: {GLOBAL_CONFIG}")


def setup_project(args=None):
    """交互式配置项目"""
    ensure_config_dirs()

    # 当前目录推断默认值
    cwd, _ = normalize_local_project(Path.cwd())
    cwd_name = cwd.name

    print()
    print(f"{BOLD}配置项目{RESET}")
    print(f"项目配置将保存到: {PROJECTS_DIR}/<项目名>.json")
    print()

    # 列出已有项目
    existing_projects = list_projects()
    if existing_projects:
        print(f"  已有项目: {', '.join(existing_projects)}")
        print()

    default_name = getattr(args, "project", None) or cwd_name
    name = prompt("项目名称（用于命令行调用）", default_name)

    # 如果项目已存在，加载旧值
    existing = {}
    old_path = PROJECTS_DIR / f"{name}.json"
    if old_path.exists():
        existing = load_json(old_path)
        print(f"  检测到已有配置，直接回车保留原值")
        print()

    default_local = getattr(args, "project_dir", None) or str(cwd)
    local_project = prompt("本地项目路径", existing.get("local_project", default_local))
    local_project, local_git = normalize_local_project(local_project)
    local_project = str(local_project)
    if local_git:
        print(f"  {CYAN}已识别 Git/worktree 根目录: {local_project}{RESET}")

    # 远程路径默认为家目录下同名目录
    default_remote = existing.get("remote_project", f"~/{name}")
    remote_project = prompt("远程项目路径", default_remote)

    # 远程机器覆盖（可选）
    print()
    global_cfg = {}
    if GLOBAL_CONFIG.exists():
        global_cfg = load_global_config()
    global_host = global_cfg.get("remote_host", "(未配置)")
    print(f"  {BOLD}远程机器（全局默认: {global_host}）{RESET}")
    project_host = ""
    project_sudo = ""
    if prompt_yn("使用不同的远程机器?", bool(existing.get("remote_host"))):
        project_host = prompt("远程主机 (user@host)", existing.get("remote_host", ""))
        project_sudo = prompt("sudo 密码（可选，留空用全局配置）", existing.get("sudo_password", ""))

    print()
    print(f"  {BOLD}构建工具{RESET}")
    tool_hint = ", ".join(SUPPORTED_TOOLS)
    build_tool = prompt(f"工具链 ({tool_hint})", existing.get("cmake", {}).get("tool", "cmake"))
    if build_tool not in SUPPORTED_TOOLS:
        print(f"  {YELLOW}不支持 {build_tool}，使用 cmake{RESET}")
        build_tool = "cmake"
    build_dir = prompt("构建目录名", existing.get("cmake", {}).get("build_dir", "build"))
    if build_tool in ("cmake", "ninja"):
        cmake_extra = prompt(
            "cmake 额外参数",
            existing.get("cmake", {}).get("extra_args", "-DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Debug"),
        )
    elif build_tool == "qmake":
        cmake_extra = prompt(
            "qmake 额外参数",
            existing.get("cmake", {}).get("extra_args", "CONFIG+=debug"),
        )
    else:
        cmake_extra = ""

    print()
    print(f"  {BOLD}编译配置{RESET}")
    parallel_jobs = int(prompt("并行线程数", str(existing.get("build", {}).get("parallel_jobs", os.cpu_count() or 4))))

    # 显示自动生成的命令
    cmds = generate_tool_commands(build_tool, build_dir, cmake_extra, parallel_jobs)
    print()
    print(f"  {BOLD}自动生成的命令:{RESET}")
    if cmds["configure"]:
        print(f"    配置: {cmds['configure']}")
    print(f"    编译: {cmds['build']}")
    print(f"    安装: {cmds['install']}")
    install_enabled = prompt_yn("编译后执行安装?", True)

    print()
    print(f"  {BOLD}同步配置{RESET}")
    default_exclude = existing.get("sync", {}).get("exclude", ".git/, build/, *.o, *.pyc, __pycache__/, .vscode/, .idea/,obj-x86_64-linux-gnu/")
    if isinstance(default_exclude, list):
        default_exclude = ", ".join(default_exclude)
    exclude_str = prompt("排除文件/目录（逗号分隔）", default_exclude)
    exclude_list = [e.strip() for e in exclude_str.split(",") if e.strip()]

    delete_extra = prompt_yn("删除远程多出的文件?", existing.get("sync", {}).get("delete_extra", True))

    auto_sync = prompt_yn("watch 模式自动同步编译?", existing.get("sync", {}).get("auto_sync", False))
    if not auto_sync:
        print(f"  {CYAN}提示: 文件变化后需按回车确认才会同步编译{RESET}")

    print()
    print(f"  {BOLD}构建依赖{RESET}")
    deps_enabled = prompt_yn("首次编译前自动安装依赖?", existing.get("deps", {}).get("enabled", True))
    deps_cmd = ""
    if deps_enabled:
        deps_cmd = prompt(
            "依赖安装命令",
            existing.get("deps", {}).get(
                "command",
                f"cd {remote_project} && sudo apt build-dep .",
            ),
        )

    print()
    print(f"  {BOLD}编译后重启{RESET}")
    restart_enabled = prompt_yn("编译安装后执行重启?", existing.get("restart", {}).get("enabled", True))
    restart_cmd = ""
    if restart_enabled:
        restart_cmd = prompt("重启命令", existing.get("restart", {}).get("command", ""))

    config = {
        "name": name,
        "local_project": local_project,
        "remote_project": remote_project,
    }

    # 项目级远程机器覆盖
    if project_host:
        config["remote_host"] = project_host
    sudo_pass = existing.get("sudo_password", "")
    if project_host and existing.get("_project_sudo"):
        sudo_pass = prompt("sudo 密码", sudo_pass)
    if sudo_pass:
        config["sudo_password"] = sudo_pass

    config.update({
        "cmake": {
            "tool": build_tool,
            "build_dir": build_dir,
            "extra_args": cmake_extra,
        },
        "build": {
            "parallel_jobs": parallel_jobs,
            "install_enabled": install_enabled,
        },
        "sync": {
            "exclude": exclude_list,
            "delete_extra": delete_extra,
            "auto_sync": auto_sync,
        },
        "deps": {
            "enabled": deps_enabled,
            "command": deps_cmd,
        },
        "restart": {
            "enabled": restart_enabled,
            "command": restart_cmd,
        },
    })

    # 项目级远程机器覆盖（可选，不填则用全局配置）
    if project_host:
        config["remote_host"] = project_host
    if project_sudo:
        config["sudo_password"] = project_sudo

    path = PROJECTS_DIR / f"{name}.json"
    save_json(path, config)
    print()
    log_info(f"项目配置已保存: {path}")
    log_info(f"使用: python remote_dev.py {name} watch")


def list_projects():
    """列出所有已配置的项目"""
    ensure_config_dirs()
    projects = []
    for f in sorted(PROJECTS_DIR.glob("*.json")):
        projects.append(f.stem)
    return projects


def cmd_list():
    """列出所有项目"""
    projects = list_projects()
    if not projects:
        log_info("暂无已配置项目")
        log_info("运行 'python remote_dev.py setup' 添加项目")
        return

    print()
    print(f"{BOLD}已配置项目:{RESET}")
    for name in projects:
        cfg = load_json(PROJECTS_DIR / f"{name}.json")
        local = cfg.get("local_project", "?")
        remote = cfg.get("remote_project", "?")
        print(f"  {GREEN}{name}{RESET}")
        print(f"    本地: {local}")
        print(f"    远程: {remote}")
    print()


# ── 带重试的执行 ──────────────────────────────────────


def retry(func, cfg, label="操作"):
    for attempt in range(1, cfg["max_retries"] + 1):
        result = func()
        if result is True or result == 0:
            return True
        if attempt < cfg["max_retries"]:
            log_warn(f"{label}失败，{cfg['wait_seconds']}秒后重试 ({attempt}/{cfg['max_retries']})")
            time.sleep(cfg["wait_seconds"])
    log_error(f"{label}失败，已达最大重试次数 ({cfg['max_retries']})")
    return False


# ── 核心操作 ─────────────────────────────────────────


def check_connection(cfg):
    log_info(f"检查远程连接: {cfg['remote_host']}")

    def _check():
        cmd = ["ssh", "-o", "ConnectTimeout=5", "-o", "BatchMode=yes",
               cfg["remote_host"], "echo ok"]
        r = run_quiet_command(cmd, "连接", display_cmd=cmd, timeout=10)
        return r.returncode == 0

    if retry(_check, cfg, "连接"):
        log_info("远程连接正常")
        return True
    return False


def sync_code(cfg):
    local = Path(cfg["local_project"])
    if not local.exists():
        log_error(f"本地项目目录不存在: {local}")
        return False

    log_info("同步代码到远程...")

    cmd = ["rsync", "-azPi"]
    if cfg["delete_extra"]:
        cmd.append("--delete")
    for ex in cfg["exclude"]:
        cmd.append(f"--exclude={ex}")
    cmd.append(f"{cfg['local_project']}/")
    cmd.append(f"{cfg['remote_host']}:{cfg['remote_project']}/")

    last_output = ""

    def _sync():
        nonlocal last_output
        r = run_quiet_command(cmd, "同步", display_cmd=cmd)
        last_output = r.stdout + r.stderr
        return r.returncode == 0

    if retry(_sync, cfg, "同步"):
        log_info("代码同步完成")
        # 解析并保存同步历史到远端
        changes = parse_rsync_itemize(last_output)
        if changes:
            project_name = cfg.get("project_name", "unknown")
            history_file = save_sync_history(
                cfg["remote_host"], cfg["remote_project"],
                project_name, changes
            )
            if history_file:
                log_info(f"同步记录已保存: {len(changes)} 个文件变更 → {history_file}")
        return True
    return False


def remote_build(cfg):
    log_info("开始远程编译...")

    remote_project = cfg["remote_project"]
    build_dir = cfg["build_dir"]
    build_path = f"{remote_project}/{build_dir}"
    cmds = cfg["tool_cmds"]
    build_tool = cfg.get("build_tool", "cmake")

    # 组装远程命令
    # configure 需要进入 build 子目录执行
    # qmake/make 的 build 也需要在 build 目录执行（Makefile 在那里）
    parts = [f"mkdir -p {build_dir}"]
    if build_tool in ("qmake", "make"):
        # configure 和 build 都在 build 目录执行，合并避免重复 cd
        if cmds["configure"]:
            parts.append(f"cd {build_dir} && {cmds['configure']} && {cmds['build']}")
        else:
            parts.append(f"cd {build_dir} && {cmds['build']}")
    else:
        if cmds["configure"]:
            parts.append(f"cd {build_dir} && {cmds['configure']}")
        parts.append(f"cd {remote_project} && {cmds['build']}")
    remote_cmd = f"cd {remote_project} && " + " && ".join(parts)

    ssh_cmd = ["ssh", "-o", "ServerAliveInterval=15", "-o", "ServerAliveCountMax=3",
                cfg["remote_host"], remote_cmd]

    def _build():
        r = run_quiet_command(ssh_cmd, "编译", display_cmd=ssh_cmd)
        return r.returncode == 0

    if retry(_build, cfg, "编译"):
        log_info("编译成功")
        return True
    return False


def remote_install(cfg):
    if not cfg.get("install_enabled", True):
        log_info("安装已禁用，跳过")
        return True

    log_info("执行远程安装...")
    remote_project = cfg["remote_project"]
    build_dir = cfg["build_dir"]
    build_tool = cfg.get("build_tool", "cmake")
    install_cmd = cfg["tool_cmds"]["install"]

    # qmake/make 的 Makefile 在 build 目录，需要 cd 进去执行
    if build_tool in ("qmake", "make"):
        dir_prefix = f"cd {remote_project}/{build_dir}"
    else:
        dir_prefix = f"cd {remote_project}"

    if cfg["sudo_password"]:
        # install_cmd 已包含 sudo，需去掉避免双重 sudo
        install_cmd_nosudo = install_cmd.removeprefix("sudo ")
        log_cmd_display = dir_prefix + " && echo '***' | sudo -S " + install_cmd_nosudo
        real_cmd = dir_prefix + " && echo '" + cfg["sudo_password"] + "' | sudo -S " + install_cmd_nosudo
    else:
        wrapped_cmd = dir_prefix + " && " + install_cmd
        log_cmd_display = wrapped_cmd
        real_cmd = wrapped_cmd

    ssh_cmd_display = ["ssh", cfg["remote_host"], log_cmd_display]
    ssh_cmd = ["ssh", cfg["remote_host"], real_cmd]

    def _install():
        r = run_quiet_command(ssh_cmd, "安装", display_cmd=ssh_cmd_display)
        return r.returncode == 0

    if retry(_install, cfg, "安装"):
        log_info("安装成功")
        return True
    return False


def remote_install_deps(cfg):
    """首次编译前安装构建依赖（基于 debian/control）"""
    if not cfg["deps_enabled"]:
        return True

    project_name = cfg["project_name"]
    remote_host = cfg["remote_host"]
    remote_project = cfg["remote_project"]

    # 远程标记文件，记录依赖已安装
    marker = "~/.remote-dev/deps/" + project_name + ".installed"

    # 检查是否已安装过
    check_cmd = "test -f " + marker + " && echo installed || echo missing"
    check_ssh = ["ssh", remote_host, check_cmd]
    r = subprocess.run(check_ssh, capture_output=True, text=True)
    if "installed" in r.stdout:
        log_info("构建依赖已安装，跳过")
        return True

    log_info("首次安装构建依赖...")

    deps_cmd = cfg["deps_command"]
    if deps_cmd:
        # 用户自定义命令：拆分出 sudo 调用部分，避免将 cd 等 shell 内建命令包在 sudo -S 里
        # 例如 "cd ~/proj && sudo apt build-dep ." → cd 部分 + sudo apt build-dep 部分
        parts = [p.strip() for p in deps_cmd.split("&&")]
        cd_parts = []
        sudo_parts = []
        for p in parts:
            if p.startswith("cd "):
                cd_parts.append(p)
            elif p.startswith("sudo "):
                sudo_parts.append(p.removeprefix("sudo "))
            else:
                sudo_parts.append(p)
        if cfg["sudo_password"] and sudo_parts:
            sudo_cmd = " && ".join(sudo_parts)
            sudo_real = "echo '" + cfg["sudo_password"] + "' | sudo -S " + sudo_cmd
            sudo_log = "echo '***' | sudo -S " + sudo_cmd
        else:
            sudo_real = " && ".join(sudo_parts)
            sudo_log = sudo_real
        all_parts = cd_parts + [sudo_real]
        real_deps_cmd = " && ".join(all_parts)
        log_parts = cd_parts + [sudo_log]
        log_deps_cmd = " && ".join(log_parts)
    else:
        # 默认：先 cd 到项目目录（~ 由远程 shell 展开），再 sudo 运行 build-dep
        if cfg["sudo_password"]:
            log_deps_cmd = "cd " + remote_project + " && echo '***' | sudo -S apt build-dep ."
            real_deps_cmd = "cd " + remote_project + " && echo '" + cfg["sudo_password"] + "' | sudo -S apt build-dep ."
        else:
            log_deps_cmd = "cd " + remote_project + " && sudo apt build-dep ."
            real_deps_cmd = log_deps_cmd

    ssh_deps_display = ["ssh", "-o", "ServerAliveInterval=15", remote_host, log_deps_cmd]
    ssh_deps = ["ssh", "-o", "ServerAliveInterval=15", remote_host, real_deps_cmd]

    def _install_deps():
        r = run_quiet_command(ssh_deps, "依赖安装", display_cmd=ssh_deps_display)
        return r.returncode == 0

    if retry(_install_deps, cfg, "依赖安装"):
        # 写标记文件
        marker_cmd = ["ssh", remote_host, "mkdir -p ~/.remote-dev/deps && touch " + marker]
        run_quiet_command(marker_cmd, "依赖标记")
        log_info("构建依赖安装完成")
        return True
    return False


def remote_restart(cfg):
    """编译安装后重启服务"""
    if not cfg["restart_enabled"] or not cfg["restart_command"]:
        return True

    log_info("执行重启命令...")
    remote_cmd = cfg["restart_command"]

    if cfg["sudo_password"] and "sudo" in remote_cmd:
        log_cmd_display = remote_cmd.replace("sudo ", "echo '***' | sudo -S ", 1)
        real_cmd = remote_cmd.replace("sudo ", f"echo '{cfg['sudo_password']}' | sudo -S ", 1)
    else:
        log_cmd_display = remote_cmd
        real_cmd = remote_cmd

    ssh_cmd_display = ["ssh", cfg["remote_host"], log_cmd_display]
    ssh_cmd = ["ssh", cfg["remote_host"], real_cmd]

    def _restart():
        r = run_quiet_command(ssh_cmd, "重启", display_cmd=ssh_cmd_display)
        return r.returncode == 0

    if retry(_restart, cfg, "重启"):
        log_info("重启成功")
        return True
    return False


def run_all(cfg):
    return (
        check_connection(cfg)
        and sync_code(cfg)
        and remote_install_deps(cfg)
        and remote_build(cfg)
        and remote_install(cfg)
        and remote_restart(cfg)
    )


# ── Watch 模式 ────────────────────────────────────────


def watch_mode(cfg, debounce=2, no_build=False, auto_sync=None):
    local = Path(cfg["local_project"])
    if not local.exists():
        log_error(f"本地项目目录不存在: {local}")
        sys.exit(1)

    # auto_sync: True=检测到变化自动同步, False=等待用户确认
    # 优先使用命令行参数，否则读配置
    if auto_sync is None:
        auto_sync = cfg.get("auto_sync", True)

    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        log_error("watch 模式需要 watchdog 库")
        log_error("安装: pip install watchdog")
        sys.exit(1)

    last_trigger = 0.0
    building = False
    pending_changes = False

    class Handler(FileSystemEventHandler):
        def on_any_event(self, event):
            nonlocal last_trigger, pending_changes
            if event.is_directory:
                return
            rel = os.path.relpath(
                getattr(event, "dest_path", event.src_path) or event.src_path,
                cfg["local_project"],
            )
            for ex in cfg["exclude"]:
                ex_clean = ex.rstrip("/")
                if rel.startswith(ex_clean) or rel.startswith(ex_clean + os.sep):
                    return
            last_trigger = time.time()
            pending_changes = True

    observer = Observer()
    handler = Handler()
    observer.schedule(handler, cfg["local_project"], recursive=True)
    observer.start()

    mode_label = "自动同步" if auto_sync else "确认后同步"
    log_info(f"项目: {cfg['project_name']}")
    log_info(f"监控目录: {cfg['local_project']}")
    log_info(f"远程目标: {cfg['remote_host']}:{cfg['remote_project']}")
    log_info(f"防抖延迟: {debounce}s")
    log_info(f"同步模式: {mode_label}")
    print()

    # 首次：同步 + 安装依赖
    if not (sync_code(cfg) and remote_install_deps(cfg)):
        log_error("初始化失败，停止监控")
        sys.exit(1)
    print()
    if auto_sync:
        log_watch("等待文件变化... (Ctrl+C 停止)")
    else:
        log_watch("等待文件变化... 检测到变化后按回车确认同步 (Ctrl+C 停止)")
    print()

    def do_build():
        """执行同步编译流程"""
        print()
        log_info("=== 开始同步编译 ===")
        succeeded = sync_code(cfg)
        if succeeded and not no_build:
            succeeded = (
                remote_build(cfg)
                and remote_install(cfg)
                and remote_restart(cfg)
            )
        if succeeded:
            log_info("=== 完成，继续监控 ===")
        else:
            log_error("=== 本次同步编译失败，已终止后续步骤 ===")
        print()
        if auto_sync:
            log_watch("等待文件变化...")
        else:
            log_watch("等待文件变化... 检测到变化后按回车确认同步")

    try:
        while True:
            time.sleep(0.5)
            if not pending_changes:
                continue
            if time.time() - last_trigger < debounce:
                continue
            if building:
                continue

            pending_changes = False
            building = True
            try:
                if auto_sync:
                    # 自动模式：直接同步
                    do_build()
                else:
                    # 确认模式：阻塞等待用户输入
                    log_info("检测到文件变化")
                    log_info("按回车同步编译，输入 s 跳过，输入 q 退出：")
                    try:
                        user_input = input(f"  {BOLD}>{RESET} ").strip().lower()
                    except EOFError:
                        user_input = "q"

                    if user_input == "q":
                        log_info("用户请求退出")
                        break
                    elif user_input == "s":
                        log_info("跳过此次同步")
                        log_watch("等待文件变化... 检测到变化后按回车确认同步")
                    else:
                        do_build()
            finally:
                building = False

    except KeyboardInterrupt:
        print()
        log_info("停止监控")
    finally:
        observer.stop()
        observer.join()


# ── CLI ──────────────────────────────────────────────


def _resolve_project(args):
    """解析项目名并加载配置，支持 ad-hoc CLI 参数（无需预配置）"""
    requested_project = getattr(args, "project", None)
    requested_dir = getattr(args, "project_dir", None)
    global_cfg = load_global_config()

    project_cfg = {}

    if requested_project:
        project_cfg = load_project_config(requested_project)
        if project_cfg:
            project_name = requested_project
        else:
            log_warn(f"项目 {requested_project} 未预配置，使用 ad-hoc 模式")
            project_name = requested_project
    else:
        lookup_dir, _ = normalize_local_project(requested_dir or Path.cwd())
        project_name, found_cfg, match_reason = find_project_by_local_dir(lookup_dir)
        if found_cfg is not None:
            project_cfg = found_cfg
        else:
            project_name = lookup_dir.name
            log_warn(f"当前目录 {lookup_dir} 未找到已配置项目，使用 ad-hoc 模式")

    adhoc = _extract_adhoc_overrides(args)

    if not project_cfg:
        if not requested_dir:
            requested_dir = str(Path.cwd())
        project_cfg = {
            "name": project_name,
            "local_project": requested_dir,
        }

    cfg = merge_config(global_cfg, project_cfg, adhoc)

    if requested_dir:
        normalized_dir, _ = normalize_local_project(requested_dir)
        cfg["local_project"] = str(normalized_dir)
    elif not project_cfg:
        lookup_dir, _ = normalize_local_project(Path.cwd())
        cfg["local_project"] = str(lookup_dir)

    return cfg


def _extract_adhoc_overrides(args):
    """从 CLI args 提取 ad-hoc 配置覆盖"""
    overrides = {}
    for key in ("remote_host", "remote_project", "build_tool", "extra_args",
                "jobs", "build_dir"):
        val = getattr(args, key, None)
        if val is not None:
            overrides[key] = val
    if getattr(args, "no_install", False):
        overrides["install_enabled"] = False
    if getattr(args, "no_restart", False):
        overrides["restart_enabled"] = False
    if getattr(args, "no_deps", False):
        overrides["deps_enabled"] = False
    return overrides


def _print_banner(cfg):
    log_info(f"项目: {cfg['project_name']}")
    log_info(f"远程: {cfg['remote_host']}")
    log_info(f"本地: {cfg['local_project']}")
    if cfg.get("configured_local_project") != cfg["local_project"]:
        log_info(f"配置本地路径: {cfg['configured_local_project']}")
    if cfg.get("project_match_reason"):
        log_info(f"项目解析: {cfg['project_match_reason']}")
    log_info(f"远程: {cfg['remote_project']}")
    print()


def cmd_sync(args):
    cfg = _resolve_project(args)
    _print_banner(cfg)
    if not (check_connection(cfg) and sync_code(cfg)):
        sys.exit(1)
    log_info("操作完成")


def cmd_build(args):
    cfg = _resolve_project(args)
    _print_banner(cfg)
    if not (check_connection(cfg) and sync_code(cfg) and remote_build(cfg)):
        sys.exit(1)
    log_info("操作完成")


def cmd_install(args):
    cfg = _resolve_project(args)
    _print_banner(cfg)
    if not run_all(cfg):
        sys.exit(1)
    log_info("操作完成")


def cmd_all(args):
    cfg = _resolve_project(args)
    _print_banner(cfg)
    if not run_all(cfg):
        sys.exit(1)
    log_info("操作完成")


def cmd_watch(args):
    cfg = _resolve_project(args)
    _print_banner(cfg)
    auto_sync = args.auto if args.auto else (False if args.confirm else None)
    watch_mode(cfg, args.debounce, args.no_build, auto_sync)


def _add_adhoc_args(parser):
    """为子命令添加 ad-hoc 参数（无需预配置）"""
    parser.add_argument("-H", "--remote-host", default=None,
                        help="远程主机 (user@host)，ad-hoc 模式下必需")
    parser.add_argument("-r", "--remote-project", default=None,
                        help="远程项目路径，ad-hoc 模式下必需")
    parser.add_argument("-t", "--build-tool", default=None,
                        choices=SUPPORTED_TOOLS,
                        help=f"构建工具链 ({', '.join(SUPPORTED_TOOLS)})")
    parser.add_argument("--extra-args", default=None,
                        help="cmake/qmake 额外参数")
    parser.add_argument("-j", "--jobs", type=int, default=None,
                        help="并行编译线程数")
    parser.add_argument("--build-dir", default=None,
                        help="构建目录名（默认 build）")
    parser.add_argument("--no-install", action="store_true",
                        help="跳过编译后安装步骤")
    parser.add_argument("--no-restart", action="store_true",
                        help="跳过编译后重启步骤")
    parser.add_argument("--no-deps", action="store_true",
                        help="跳过构建依赖安装步骤")


def main():
    default_project = normalize_local_project(Path.cwd())[0].name

    # 兼容 "remote_dev.py <项目名> <action>" 格式
    # 自动转换为 "remote_dev.py <action> -p <项目名>"
    argv = sys.argv[1:]
    if (
        len(argv) >= 2
        and argv[0] not in COMMANDS
        and not argv[0].startswith("-")
        and argv[1] in ACTIONS
    ):
        sys.argv = [sys.argv[0], argv[1], "-p", argv[0]] + argv[2:]

    parser = argparse.ArgumentParser(
        prog="remote_dev.py",
        description="远程开发同步编译工具 — 在本机写代码，远程编译测试",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""\
示例:
  %(prog)s setup                       配置项目（交互式）
  %(prog)s setup --global              配置远程机器信息
  %(prog)s list                        列出所有已配置项目

  # 使用预配置的项目
  %(prog)s watch                       监控当前目录对应项目
  %(prog)s build -p dde-shell          同步+编译指定项目
  %(prog)s all -p dde-shell            同步+依赖+编译+安装+重启

  # ad-hoc 模式（无需预配置）
  %(prog)s build -H user@192.168.1.50 -r ~/work/myproj
  %(prog)s build -H user@ip -r ~/work/proj -t qmake --extra-args "CONFIG+=debug" -j 4
  %(prog)s all -H user@ip -r ~/work/proj --no-install --no-restart
  %(prog)s watch -H user@ip -r ~/work/proj --auto --no-restart

  # 混合使用（CLI 参数覆盖预配置值）
  %(prog)s build -p dde-shell -j 4     用预配置但覆盖线程数

当前目录: {Path.cwd()}  默认项目名: {default_project}
""",
    )
    subparsers = parser.add_subparsers(dest="command")

    # setup
    p_setup = subparsers.add_parser("setup", help="交互式配置项目或远程机器信息")
    p_setup.add_argument("--global", dest="is_global", action="store_true",
                         help="配置远程机器信息（而非项目）")
    p_setup.add_argument("-p", "--project", default=None,
                         help=f"项目名默认值（默认从当前目录推断: {default_project}）")
    p_setup.add_argument("-d", "--project-dir", default=None,
                         help="本地项目目录默认值；若在 Git/worktree 中会自动归一到仓库根目录")
    p_setup.set_defaults(func=lambda args: setup_global() if args.is_global else setup_project(args))

    # list
    p_list = subparsers.add_parser("list", aliases=["ls"], help="列出所有已配置项目")
    p_list.set_defaults(func=lambda args: cmd_list())

    # sync
    p_sync = subparsers.add_parser("sync", help="同步代码到远程")
    p_sync.add_argument("-p", "--project", default=None,
                        help=f"项目名（默认从当前目录推断: {default_project}）")
    p_sync.add_argument("-d", "--project-dir", default=None,
                        help="本地项目目录；支持传入 worktree 目录或其子目录")
    _add_adhoc_args(p_sync)
    p_sync.set_defaults(func=cmd_sync)

    # build
    p_build = subparsers.add_parser("build", help="同步代码 + 远程编译")
    p_build.add_argument("-p", "--project", default=None,
                         help=f"项目名（默认从当前目录推断: {default_project}）")
    p_build.add_argument("-d", "--project-dir", default=None,
                         help="本地项目目录；支持传入 worktree 目录或其子目录")
    _add_adhoc_args(p_build)
    p_build.set_defaults(func=cmd_build)

    # install
    p_install = subparsers.add_parser("install", help="同步 + 编译 + 安装")
    p_install.add_argument("-p", "--project", default=None,
                           help=f"项目名（默认从当前目录推断: {default_project}）")
    p_install.add_argument("-d", "--project-dir", default=None,
                           help="本地项目目录；支持传入 worktree 目录或其子目录")
    _add_adhoc_args(p_install)
    p_install.set_defaults(func=cmd_install)

    # all
    p_all = subparsers.add_parser("all", help="同步 + 依赖安装 + 编译 + 安装 + 重启")
    p_all.add_argument("-p", "--project", default=None,
                       help=f"项目名（默认从当前目录推断: {default_project}）")
    p_all.add_argument("-d", "--project-dir", default=None,
                       help="本地项目目录；支持传入 worktree 目录或其子目录")
    _add_adhoc_args(p_all)
    p_all.set_defaults(func=cmd_all)

    # watch
    p_watch = subparsers.add_parser("watch", help="监控文件变化，自动或确认后同步编译")
    p_watch.add_argument("-p", "--project", default=None,
                         help=f"项目名（默认从当前目录推断: {default_project}）")
    p_watch.add_argument("--project-dir", default=None,
                         help="本地项目目录；支持传入 worktree 目录或其子目录")
    p_watch.add_argument("--debounce", type=float, default=2,
                         help="防抖等待秒数（默认 2）")
    p_watch.add_argument("--no-build", action="store_true",
                         help="只同步不编译")
    p_watch_mode = p_watch.add_mutually_exclusive_group()
    p_watch_mode.add_argument("--auto", action="store_true",
                              help="检测到变化自动同步编译")
    p_watch_mode.add_argument("--confirm", action="store_true",
                              help="检测到变化后等待确认再同步（默认）")
    _add_adhoc_args(p_watch)
    p_watch.set_defaults(func=cmd_watch)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    args.func(args)


if __name__ == "__main__":
    main()
