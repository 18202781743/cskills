#!/usr/bin/env python3
"""检查 linglong.yaml 中的 Debian 包是否发生版本降级。

以 Git 基线中的 linglong.yaml 为旧版本，以当前工作区为新版本。已有包的新版本
必须大于或等于旧版本；新增、删除的包不参与版本大小比较。
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime
import re
import shutil
import subprocess
import sys
import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from typing import DefaultDict, Dict, Iterable, List, Optional, Sequence, Set, Tuple


DEB_URL_RE = re.compile(r"^\s*url:\s*['\"]?([^'\"\s#]+\.deb)(?:\?[^'\"\s#]*)?['\"]?\s*(?:#.*)?$")
DEB_FILENAME_RE = re.compile(
    r"^(?P<name>[^_]+)_(?P<version>[^_]+)_(?P<arch>[^_]+)\.deb$"
)
DEFAULT_IGNORED_ARCHES = {"riscv64"}


@dataclass(frozen=True)
class PackageVersion:
    name: str
    version: str
    arch: str


@dataclass(frozen=True)
class VersionProblem:
    yaml_path: str
    package: str
    old_version: str
    new_version: str


ProblemGroup = Tuple[str, str, str]


def extract_packages(content: str, source: str = "linglong.yaml") -> Dict[str, PackageVersion]:
    """从 linglong.yaml 的 deb URL 中提取包名、版本和架构。"""
    packages: Dict[str, PackageVersion] = {}
    for line_number, line in enumerate(content.splitlines(), 1):
        match = DEB_URL_RE.match(line)
        if not match:
            continue
        url = urllib.parse.unquote(match.group(1))
        filename = Path(urllib.parse.urlsplit(url).path).name
        filename_match = DEB_FILENAME_RE.match(filename)
        if not filename_match:
            raise ValueError(
                f"{source}:{line_number}: 无法解析 Debian 包文件名: {filename}"
            )
        package = PackageVersion(**filename_match.groupdict())
        previous = packages.get(package.name)
        if previous and previous != package:
            raise ValueError(
                f"{source}:{line_number}: 包 {package.name} 出现多个版本或架构: "
                f"{previous.version}/{previous.arch}, {package.version}/{package.arch}"
            )
        packages[package.name] = package
    return packages


def debian_version_is_at_least(new_version: str, old_version: str) -> bool:
    """按 Debian 版本规则判断 new_version >= old_version。"""
    if not shutil.which("dpkg"):
        raise RuntimeError("未找到 dpkg，无法按 Debian 版本规则比较包版本")
    result = subprocess.run(
        ["dpkg", "--compare-versions", new_version, "ge", old_version],
        check=False,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(
            f"dpkg 无法比较版本: {old_version!r} -> {new_version!r} "
            f"(退出码 {result.returncode})"
        )
    return result.returncode == 0


def compare_package_versions(
    old_content: str, new_content: str, yaml_path: str
) -> List[VersionProblem]:
    """返回同一个 YAML 中所有发生降级的已有包。"""
    old_packages = extract_packages(old_content, f"{yaml_path} (基线)")
    new_packages = extract_packages(new_content, f"{yaml_path} (当前)")
    problems: List[VersionProblem] = []
    for name in sorted(old_packages.keys() & new_packages.keys()):
        old = old_packages[name]
        new = new_packages[name]
        if not debian_version_is_at_least(new.version, old.version):
            problems.append(
                VersionProblem(yaml_path, name, old.version, new.version)
            )
    return problems


def _git(repo_path: Path, args: Sequence[str], check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo_path), *args],
        check=check,
        capture_output=True,
        text=True,
    )


def _baseline_yaml_paths(repo_path: Path, base_ref: str) -> Iterable[str]:
    result = _git(repo_path, ["ls-tree", "-r", "--name-only", base_ref])
    for path in result.stdout.splitlines():
        if path == "linglong.yaml" or path.endswith("/linglong.yaml"):
            yield path


def check_repository(
    repo_path: Path,
    base_ref: str,
    ignored_arches: Optional[Set[str]] = None,
) -> List[VersionProblem]:
    """比较 base_ref 与工作区，并返回非忽略架构的包版本降级问题。"""
    repo_path = repo_path.resolve()
    if ignored_arches is None:
        ignored_arches = set(DEFAULT_IGNORED_ARCHES)
    verify = _git(repo_path, ["rev-parse", "--verify", base_ref], check=False)
    if verify.returncode != 0:
        raise RuntimeError(f"Git 基线不存在: {base_ref}")

    problems: List[VersionProblem] = []
    checked_files = 0
    for yaml_path in sorted(_baseline_yaml_paths(repo_path, base_ref)):
        path_parts = Path(yaml_path).parts
        yaml_arch = path_parts[0] if len(path_parts) > 1 else ""
        if yaml_arch in ignored_arches:
            continue
        current_path = repo_path / yaml_path
        if not current_path.is_file():
            continue
        old = _git(repo_path, ["show", f"{base_ref}:{yaml_path}"]).stdout
        new = current_path.read_text(encoding="utf-8")
        problems.extend(compare_package_versions(old, new, yaml_path))
        checked_files += 1

    if checked_files == 0:
        raise RuntimeError(
            f"基线 {base_ref} 与工作区之间没有可比较的 linglong.yaml"
        )
    return problems


def group_problems(
    problems: Sequence[VersionProblem],
) -> Dict[ProblemGroup, List[str]]:
    """按包名和版本变化聚合，合并相同问题涉及的 YAML/架构。"""
    grouped: DefaultDict[ProblemGroup, List[str]] = defaultdict(list)
    for problem in problems:
        key = (problem.package, problem.old_version, problem.new_version)
        grouped[key].append(problem.yaml_path)
    return {
        key: sorted(set(paths))
        for key, paths in sorted(grouped.items())
    }


def render_markdown_report(
    problems: Sequence[VersionProblem], repo_path: Path, base_ref: str,
    ignored_arches: Optional[Set[str]] = None,
) -> str:
    """生成便于后续修复和跟踪的 Markdown 报告。"""
    if ignored_arches is None:
        ignored_arches = set(DEFAULT_IGNORED_ARCHES)
    grouped = group_problems(problems)
    lines = [
        "# Debian 包版本降级报告",
        "",
        f"- 生成时间：{datetime.now().astimezone().isoformat(timespec='seconds')}",
        f"- 仓库：`{repo_path.resolve()}`",
        f"- 比较基线：`{base_ref}`",
        f"- 忽略架构：{', '.join(sorted(ignored_arches)) or '无'}",
        f"- 降级记录：{len(problems)}",
        f"- 问题包数：{len({problem.package for problem in problems})}",
        "",
        "| 包名 | 原版本 | 新版本 | 影响的 YAML/架构 |",
        "|---|---|---|---|",
    ]
    for (package, old_version, new_version), paths in grouped.items():
        yaml_paths = "<br>".join(f"`{path}`" for path in paths)
        lines.append(
            f"| `{package}` | `{old_version}` | `{new_version}` | {yaml_paths} |"
        )
    lines.extend([
        "",
        "## 处理要求",
        "",
        "逐项确认新仓库中的包版本来源。将受检架构的降级包恢复到不低于原版本后，重新运行版本检查；全部通过后才能提交、推送和创建 PR。",
        "",
    ])
    return "\n".join(lines)


def write_markdown_report(
    report_file: Path,
    problems: Sequence[VersionProblem],
    repo_path: Path,
    base_ref: str,
    ignored_arches: Optional[Set[str]] = None,
) -> None:
    report_file.parent.mkdir(parents=True, exist_ok=True)
    report_file.write_text(
        render_markdown_report(
            problems, repo_path, base_ref, ignored_arches
        ), encoding="utf-8"
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="检查 linglong.yaml 中已有 Debian 包的新版本是否大于或等于基线版本"
    )
    parser.add_argument("--repo-path", required=True, type=Path, help="Git 仓库路径")
    parser.add_argument("--base-ref", default="upstream/HEAD", help="Git 基线引用")
    parser.add_argument(
        "--report-file", type=Path,
        help="检查失败时写入 Markdown 报告的路径",
    )
    parser.add_argument(
        "--check-riscv64", action="store_true",
        help="同时检查默认忽略的 riscv64 架构",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _build_parser().parse_args(argv)
    ignored_arches = set() if args.check_riscv64 else set(DEFAULT_IGNORED_ARCHES)
    try:
        problems = check_repository(args.repo_path, args.base_ref, ignored_arches)
    except (OSError, RuntimeError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"包版本检查失败: {exc}", file=sys.stderr)
        return 2

    if problems:
        grouped = group_problems(problems)
        package_count = len({problem.package for problem in problems})
        print(
            f"包版本检查失败：发现 {len(problems)} 条降级记录，"
            f"涉及 {package_count} 个包：",
            file=sys.stderr,
        )
        for (package, old_version, new_version), paths in grouped.items():
            print(
                f"  - {package}: {old_version} -> {new_version} "
                f"[{', '.join(paths)}]",
                file=sys.stderr,
            )
        if args.report_file:
            try:
                write_markdown_report(
                    args.report_file, problems, args.repo_path, args.base_ref,
                    ignored_arches,
                )
            except OSError as exc:
                print(f"无法写入包版本降级报告: {exc}", file=sys.stderr)
                return 2
            print(f"详细报告: {args.report_file.resolve()}", file=sys.stderr)
        return 1

    ignored_text = ", ".join(sorted(ignored_arches)) or "无"
    print(
        "包版本检查通过：所有受检架构的已有包版本均大于或等于基线版本。"
        f"（忽略架构: {ignored_text}）"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
