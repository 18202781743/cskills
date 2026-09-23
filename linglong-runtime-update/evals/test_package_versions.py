#!/usr/bin/env python3
"""Debian 包版本降级检查回归测试。"""

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "check-package-versions.py"
)
SPEC = importlib.util.spec_from_file_location("check_package_versions", MODULE_PATH)
checker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = checker
SPEC.loader.exec_module(checker)


def yaml_with(package: str, version: str, arch: str = "amd64") -> str:
    return (
        "sources:\n"
        "  - kind: file\n"
        f"    url: https://repo.example/pool/{package}_{version}_{arch}.deb\n"
    )


class DebianVersionTests(unittest.TestCase):
    def test_debian_version_rules(self):
        self.assertTrue(checker.debian_version_is_at_least("1:1.0-1", "2.0-1"))
        self.assertTrue(checker.debian_version_is_at_least("1.0-2", "1.0-1"))
        self.assertTrue(checker.debian_version_is_at_least("1.0-1", "1.0-1"))
        self.assertFalse(checker.debian_version_is_at_least("1.0~rc1", "1.0"))

    def test_reports_every_downgraded_package(self):
        old = yaml_with("pkg-a", "2.0-1") + yaml_with("pkg-b", "1:1.0-1")
        new = yaml_with("pkg-a", "1.9-1") + yaml_with("pkg-b", "3.0-1")
        problems = checker.compare_package_versions(old, new, "linglong.yaml")
        self.assertEqual(
            [(p.package, p.old_version, p.new_version) for p in problems],
            [("pkg-a", "2.0-1", "1.9-1"), ("pkg-b", "1:1.0-1", "3.0-1")],
        )

    def test_equal_upgrade_and_new_package_pass(self):
        old = yaml_with("same", "1.0-1") + yaml_with("upgrade", "1.0~rc1")
        new = (
            yaml_with("same", "1.0-1")
            + yaml_with("upgrade", "1.0")
            + yaml_with("new-package", "0.1-1")
        )
        self.assertEqual(
            checker.compare_package_versions(old, new, "linglong.yaml"), []
        )

    def test_markdown_report_groups_same_problem_across_architectures(self):
        problems = [
            checker.VersionProblem("linglong.yaml", "libfoo", "2.0-1", "1.0-1"),
            checker.VersionProblem(
                "arm64/linglong.yaml", "libfoo", "2.0-1", "1.0-1"
            ),
        ]
        report = checker.render_markdown_report(problems, Path("/repo"), "HEAD")
        self.assertEqual(report.count("| `libfoo` |"), 1)
        self.assertIn("`arm64/linglong.yaml`<br>`linglong.yaml`", report)
        self.assertIn("降级记录：2", report)
        self.assertIn("问题包数：1", report)

    def test_writes_markdown_report(self):
        problem = checker.VersionProblem(
            "linglong.yaml", "libfoo", "2.0-1", "1.0-1"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            report_file = Path(temp_dir) / "reports" / "downgrades.md"
            checker.write_markdown_report(
                report_file, [problem], Path(temp_dir), "upstream/HEAD"
            )
            self.assertTrue(report_file.is_file())
            self.assertIn("libfoo", report_file.read_text())


class RepositoryCheckTests(unittest.TestCase):
    def test_checks_root_and_arch_yaml(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = Path(temp_dir)
            subprocess.run(["git", "init", "-b", "main", str(repo)], check=True,
                           capture_output=True)
            subprocess.run(["git", "-C", str(repo), "config", "user.name", "Test"],
                           check=True)
            subprocess.run(["git", "-C", str(repo), "config", "user.email",
                            "test@example.com"], check=True)
            (repo / "arm64").mkdir()
            (repo / "riscv64").mkdir()
            (repo / "linglong.yaml").write_text(yaml_with("root-pkg", "2.0-1"))
            (repo / "arm64" / "linglong.yaml").write_text(
                yaml_with("arch-pkg", "3.0-1", "arm64")
            )
            (repo / "riscv64" / "linglong.yaml").write_text(
                yaml_with("riscv-pkg", "4.0-1", "riscv64")
            )
            subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
            subprocess.run(["git", "-C", str(repo), "commit", "-m", "base"],
                           check=True, capture_output=True)

            (repo / "linglong.yaml").write_text(yaml_with("root-pkg", "1.0-1"))
            (repo / "arm64" / "linglong.yaml").write_text(
                yaml_with("arch-pkg", "2.0-1", "arm64")
            )
            (repo / "riscv64" / "linglong.yaml").write_text(
                yaml_with("riscv-pkg", "1.0-1", "riscv64")
            )
            problems = checker.check_repository(repo, "HEAD")
            self.assertEqual(
                [(p.yaml_path, p.package) for p in problems],
                [("arm64/linglong.yaml", "arch-pkg"),
                 ("linglong.yaml", "root-pkg")],
            )

            all_arch_problems = checker.check_repository(
                repo, "HEAD", ignored_arches=set()
            )
            self.assertIn(
                ("riscv64/linglong.yaml", "riscv-pkg"),
                [(p.yaml_path, p.package) for p in all_arch_problems],
            )

    def test_cli_defaults_to_ignoring_riscv64(self):
        parser = checker._build_parser()
        default_args = parser.parse_args(["--repo-path", "/repo"])
        self.assertFalse(default_args.check_riscv64)
        explicit_args = parser.parse_args([
            "--repo-path", "/repo", "--check-riscv64"
        ])
        self.assertTrue(explicit_args.check_riscv64)


if __name__ == "__main__":
    unittest.main()
