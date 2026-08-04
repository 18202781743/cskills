#!/usr/bin/env python3
"""Trigger Auto Release workflow for GitHub repositories."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_USAGE = 2
EXIT_AUTH = 3

DEFAULT_WORKFLOW = "Auto Release"
DEFAULT_OWNER = "linuxdeepin"


@dataclass
class ValidationResult:
    valid: bool
    message: str = ""
    sanitized_value: Any = None


class InputValidator:
    @classmethod
    def validate_project_name(cls, value: str) -> ValidationResult:
        if not value:
            return ValidationResult(False, "项目名不能为空")
        if not re.match(r"^[A-Za-z0-9][A-Za-z0-9._-]*$", value):
            return ValidationResult(False, f"项目名格式无效: {value!r}")
        return ValidationResult(True, sanitized_value=value)

    @classmethod
    def validate_version(cls, value: str) -> ValidationResult:
        if not value:
            return ValidationResult(False, "版本号不能为空")
        if not re.match(r"^\d+(?:\.\d+)+(?:[-+~][^\s]+)?$", value):
            return ValidationResult(False, f"版本号格式无效: {value!r}")
        return ValidationResult(True, sanitized_value=value)

    @classmethod
    def validate_email(cls, value: str) -> ValidationResult:
        if not value:
            return ValidationResult(False, "邮箱不能为空")
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value):
            return ValidationResult(False, f"邮箱格式无效: {value!r}")
        return ValidationResult(True, sanitized_value=value)

    @classmethod
    def validate_username(cls, value: str) -> ValidationResult:
        if not value:
            return ValidationResult(False, "用户名不能为空")
        if any(ch in value for ch in ("\n", "\r", "\0")):
            return ValidationResult(False, "用户名包含非法字符")
        return ValidationResult(True, sanitized_value=value.strip())

def _ok(msg: str, **extra: Any) -> Dict[str, Any]:
    return {"success": True, "msg": msg, **extra}


def _err(msg: str, **extra: Any) -> Dict[str, Any]:
    return {"success": False, "msg": msg, **extra}


def error_response(error_type: str, message: str, suggestion: Optional[str] = None) -> str:
    payload = {"error": error_type, "message": message}
    if suggestion:
        payload["suggestion"] = suggestion
    return json.dumps(payload, ensure_ascii=False, indent=2)


def _run_command(args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, capture_output=True, text=True, check=check)


def _check_gh_cli() -> Optional[str]:
    if _run_command(["which", "gh"], check=False).returncode != 0:
        return "GitHub CLI (gh) 未安装，请运行: sudo apt install gh"
    if _run_command(["gh", "auth", "status"], check=False).returncode != 0:
        return "GitHub CLI (gh) 未登录，请运行: gh auth login"
    return None


def _git_config(key: str) -> str:
    result = _run_command(["git", "config", "--get", key], check=False)
    if result.returncode != 0:
        return ""
    return result.stdout.strip()


def _resolve_identity(username: Optional[str], email: Optional[str]) -> Dict[str, str]:
    resolved_username = username or _git_config("user.name")
    resolved_email = email or _git_config("user.email")

    if not resolved_username:
        raise RuntimeError("未提供用户名，且 git config user.name 为空")
    if not resolved_email:
        raise RuntimeError("未提供邮箱，且 git config user.email 为空")

    validations: list[tuple[str, str, Any]] = [
        ("username", resolved_username, InputValidator.validate_username),
        ("email", resolved_email, InputValidator.validate_email),
    ]
    for field, value, validator in validations:
        result: ValidationResult = validator(value)
        if not result.valid:
            raise RuntimeError(f"{field} 校验失败: {result.message}")

    return {"username": resolved_username.strip(), "email": resolved_email.strip()}


def _normalize_projects(projects: Optional[List[str]]) -> List[str]:
    if not projects:
        raise RuntimeError("必须至少提供一个 --project")

    normalized: List[str] = []
    seen = set()
    for item in projects:
        for raw_project in item.split(","):
            project = raw_project.strip()
            if not project:
                continue
            project_result = InputValidator.validate_project_name(project)
            if not project_result.valid:
                raise RuntimeError(project_result.message)
            name = project_result.sanitized_value
            if name not in seen:
                normalized.append(name)
                seen.add(name)

    if not normalized:
        raise RuntimeError("必须至少提供一个有效的 --project")
    return normalized


def _project_to_repo(project: str) -> str:
    project_result = InputValidator.validate_project_name(project)
    if not project_result.valid:
        raise RuntimeError(project_result.message)
    return f"{DEFAULT_OWNER}/{project_result.sanitized_value}"


def _get_current_gh_user() -> Optional[str]:
    result = _run_command(["gh", "api", "user", "--jq", ".login"], check=False)
    return result.stdout.strip() if result.returncode == 0 else None


def _get_top_contributor(repo: str) -> Optional[str]:
    collab_result = _run_command(
        ["gh", "api", f"repos/{repo}/collaborators", "--jq",
         '[.[] | select(.role_name == "maintain" or .role_name == "admin") | .login]'],
        check=False,
    )
    if collab_result.returncode != 0:
        return None
    try:
        maintainers = set(json.loads(collab_result.stdout.strip()))
    except json.JSONDecodeError:
        return None

    # Get recent commits (last 90 days) to find active maintainers
    since = (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - 90 * 86400)))
    recent_result = _run_command(
        ["gh", "api", f"repos/{repo}/commits", "--jq",
         "[.[].author.login]", "-f", f"since={since}", "-f", "per_page=100"],
        check=False,
    )
    recent_active: set[str] = set()
    if recent_result.returncode == 0:
        try:
            recent_active = set(json.loads(recent_result.stdout.strip())) & maintainers
        except json.JSONDecodeError:
            pass

    # Find maintainer with most total commits, preferring recently active ones
    contrib_result = _run_command(
        ["gh", "api", f"repos/{repo}/contributors", "--jq", "[.[].login]"],
        check=False,
    )
    if contrib_result.returncode != 0:
        return None
    try:
        logins = json.loads(contrib_result.stdout.strip())
        # First try recently active maintainers ranked by total commits
        for login in logins:
            if login in recent_active:
                return login
        # Fallback: any maintainer ranked by total commits
        for login in logins:
            if login in maintainers:
                return login
    except json.JSONDecodeError:
        pass
    return None




def _find_release_pr(repo: str, retries: int = 18, interval: int = 10) -> Optional[Dict[str, Any]]:
    """等待并查找最新的 release PR（重试直到找到或超时）。"""
    for _ in range(retries):
        result = _run_command(
            ["gh", "pr", "list", "--repo", repo, "--state", "open",
             "--json", "number,title,url,headRefName",
             "--jq", '[.[] | select(.headRefName | test("release|Release"))] | first'],
            check=False,
        )
        if result.returncode == 0 and result.stdout.strip() not in ("", "null"):
            try:
                return json.loads(result.stdout.strip())
            except json.JSONDecodeError:
                pass
        time.sleep(interval)
    return None


def _request_reviewers(repo: str, pr_number: int, reviewers: List[str]) -> bool:
    if not reviewers:
        return False
    body = json.dumps({"reviewers": reviewers})
    result = subprocess.run(
        ["gh", "api", f"repos/{repo}/pulls/{pr_number}/requested_reviewers",
         "--method", "POST", "--input", "-"],
        input=body, capture_output=True, text=True,
    )
    return result.returncode == 0


class GitHubReleaseClient:
    def __init__(self):
        self.workflow = DEFAULT_WORKFLOW

    def release(
        self,
        project: str,
        username: str,
        email: str,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        if version:
            version_result = InputValidator.validate_version(version)
            if not version_result.valid:
                return _err(version_result.message, project=project)

        repo = _project_to_repo(project)

        command = [
            "gh", "workflow", "run", self.workflow,
            "--repo", repo,
            "-F", f"name={username}",
            "-F", f"email={email}",
        ]
        if version:
            command.extend(["-F", f"version={version}"])

        try:
            _run_command(["gh", "repo", "set-default", repo], check=False)
            _run_command(command)
        except subprocess.CalledProcessError as exc:
            return _err(exc.stderr.strip() or str(exc), project=project, repo=repo)

        extra: Dict[str, Any] = {}

        top_contributor = _get_top_contributor(repo)
        current_user = _get_current_gh_user()
        reviewers: List[str] = list({
            *([ top_contributor] if top_contributor else []),
            *([current_user] if current_user else []),
        })
        pr = _find_release_pr(repo)
        if pr:
            extra["pr_number"] = pr["number"]
            extra["pr_url"] = pr["url"]
            extra["pr_title"] = pr["title"]
            if reviewers:
                ok = _request_reviewers(repo, pr["number"], reviewers)
                extra["reviewers_requested"] = reviewers if ok else []
        else:
            extra["pr_note"] = "未找到 release PR，请手动添加 reviewer"

        return _ok(
            "Auto Release workflow triggered",
            project=project,
            repo=repo,
            workflow=self.workflow,
            username=username,
            email=email,
            version=version or "",
            actions_url=f"https://github.com/{repo}/actions",
            **extra,
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Trigger Auto Release workflow for GitHub repositories")
    parser.add_argument("--project", action="append", help="项目名，可重复传入或逗号分隔")
    parser.add_argument("--username", help="workflow 用户名，不填则使用 git config user.name")
    parser.add_argument("--email", help="workflow 邮箱，不填则使用 git config user.email")
    parser.add_argument("--version", help="指定版本号，不填则由 workflow 自行生成")
    args = parser.parse_args()

    err = _check_gh_cli()
    if err:
        print(error_response("auth_error", err, "请先完成 gh auth login"), file=sys.stderr)
        return EXIT_AUTH

    try:
        projects = _normalize_projects(args.project)
        identity = _resolve_identity(args.username, args.email)
        client = GitHubReleaseClient()
        results = [
            client.release(
                project=project,
                username=identity["username"],
                email=identity["email"],
                version=args.version,
            )
            for project in projects
        ]
        success = all(item.get("success") for item in results)
        result = {
            "success": success,
            "msg": f"已处理 {len(results)} 个 DTK 项目",
            "projects": results,
        }
    except ValueError as exc:
        print(error_response("usage_error", str(exc)), file=sys.stderr)
        return EXIT_USAGE
    except RuntimeError as exc:
        print(error_response("error", str(exc)), file=sys.stderr)
        return EXIT_ERROR
    except Exception as exc:
        print(error_response("error", str(exc)), file=sys.stderr)
        return EXIT_ERROR

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return EXIT_SUCCESS if result.get("success") else EXIT_ERROR


if __name__ == "__main__":
    raise SystemExit(main())
