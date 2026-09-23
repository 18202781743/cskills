#!/usr/bin/env python3
"""update-repo 仓库同步与补丁路径回归测试。"""

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "linglong-update.py"
SPEC = importlib.util.spec_from_file_location("linglong_update", MODULE_PATH)
lu = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lu)


class RepoUpdateTests(unittest.TestCase):
    def test_sync_runtime_base_updates_stale_cache_from_official_repo(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            official = root / "official"
            cache = root / "cache"

            subprocess.run(["git", "init", "-b", "main", str(official)],
                           check=True, capture_output=True)
            subprocess.run(["git", "-C", str(official), "config", "user.name",
                            "Test User"], check=True)
            subprocess.run(["git", "-C", str(official), "config", "user.email",
                            "test@example.com"], check=True)
            (official / "README.md").write_text("initial\n")
            subprocess.run(["git", "-C", str(official), "add", "README.md"],
                           check=True)
            subprocess.run(["git", "-C", str(official), "commit", "-m", "initial"],
                           check=True, capture_output=True)
            subprocess.run(["git", "clone", str(official), str(cache)],
                           check=True, capture_output=True)

            patch_dir = official / "patches" / "org.deepin.runtime.dtk5"
            patch_dir.mkdir(parents=True)
            (patch_dir / "0001-dtk5.patch").write_text("test patch\n")
            subprocess.run(["git", "-C", str(official), "add", "patches"],
                           check=True)
            subprocess.run(["git", "-C", str(official), "commit", "-m",
                            "add dtk5 patch"], check=True, capture_output=True)

            with mock.patch.object(lu, "RUNTIME_REPO_URL", str(official)):
                lu._sync_runtime_base_repo(str(cache))

            patches = lu._find_repo_patches(
                str(cache), "org.deepin.runtime.dtk5")
            self.assertEqual(
                patches,
                [str(cache / "patches" / "org.deepin.runtime.dtk5" /
                     "0001-dtk5.patch")],
            )
            official_head = subprocess.run(
                ["git", "-C", str(official), "rev-parse", "HEAD"],
                check=True, capture_output=True, text=True).stdout.strip()
            cache_head = subprocess.run(
                ["git", "-C", str(cache), "rev-parse", "HEAD"],
                check=True, capture_output=True, text=True).stdout.strip()
            self.assertEqual(cache_head, official_head)

    @mock.patch.object(lu, "_run")
    @mock.patch.object(lu.subprocess, "run")
    def test_sync_runtime_base_fetches_upstream_and_resets_default_branch(
            self, run_mock, command_mock):
        def result_for(cmd, **kwargs):
            if cmd[-3:] == ["remote", "get-url", "upstream"]:
                return subprocess.CompletedProcess(cmd, 1, "", "")
            if "symbolic-ref" in cmd:
                return subprocess.CompletedProcess(cmd, 0, "upstream/main\n", "")
            if "rev-parse" in cmd:
                return subprocess.CompletedProcess(cmd, 0, "deadbeef\n", "")
            return subprocess.CompletedProcess(cmd, 0, "", "")

        run_mock.side_effect = result_for
        lu._sync_runtime_base_repo("/cache/org.deepin.runtime")

        commands = [call.args[0] for call in command_mock.call_args_list]
        self.assertIn(
            ["git", "-C", "/cache/org.deepin.runtime", "remote", "add",
             "upstream", lu.RUNTIME_REPO_URL], commands)
        self.assertIn(
            ["git", "-C", "/cache/org.deepin.runtime", "fetch", "upstream",
             "--prune"], commands)
        self.assertIn(
            ["git", "-C", "/cache/org.deepin.runtime", "checkout", "-B",
             "main", "upstream/main"], commands)

    @mock.patch.object(lu, "_run")
    @mock.patch.object(lu, "_sync_runtime_base_repo")
    @mock.patch.object(lu, "_find_repo_patches", return_value=[])
    def test_fork_repo_reads_required_patches_from_runtime_repo(
            self, find_mock, sync_mock, command_mock):
        ok = lu._update_fork_repo(
            "org.deepin.runtime.dtk5",
            "/cache/org.deepin.runtime.dtk5",
            "6.7.0.48",
            "http://repo/stable_20260819",
            "/cache/org.deepin.runtime",
        )

        self.assertFalse(ok)
        sync_mock.assert_called_once_with("/cache/org.deepin.runtime")
        find_mock.assert_called_once_with(
            "/cache/org.deepin.runtime", "org.deepin.runtime.dtk5")
        # 补丁缺失时不能继续执行 daily.bash、commit 或 push。
        commands = [call.args[0] for call in command_mock.call_args_list]
        self.assertFalse(any("push" in cmd for cmd in commands))





class RuntimePrMergeGateTests(unittest.TestCase):
    """runtime PR 合并前置校验（webengine/dtk5 必须在 runtime PR 合并后推送）。"""

    @mock.patch.object(lu, "_log")
    def test_runtime_main_has_version_true_when_main_updated(self, log_mock):
        yaml = (
            'version: "1"\n'
            "  id: org.deepin.runtime.dtk\n"
            "  version: 6.7.0.49\n"
            "  description: Deepin Tool Kit Widget\n"
        )
        import base64
        payload = base64.b64encode(yaml.encode()).decode()
        cp = subprocess.CompletedProcess(["gh", "api"], 0, payload, "")
        with mock.patch.object(lu.subprocess, "run", return_value=cp) as run_mock:
            self.assertTrue(lu._runtime_main_has_version("6.7.0.49"))
            self.assertFalse(lu._runtime_main_has_version("6.7.0.48"))
        # 应查询 linglongdev/org.deepin.runtime main 的 linglong.yaml
        cmd = " ".join(run_mock.call_args.args[0])
        self.assertIn("linglongdev/org.deepin.runtime", cmd)
        self.assertIn("linglong.yaml", cmd)

    @mock.patch.object(lu, "_log")
    def test_runtime_main_has_version_false_on_failure(self, log_mock):
        cp = subprocess.CompletedProcess(["gh", "api"], 1, "", "boom")
        with mock.patch.object(lu.subprocess, "run", return_value=cp):
            self.assertFalse(lu._runtime_main_has_version("6.7.0.49"))

    @mock.patch.object(lu, "_update_fork_repo")
    @mock.patch.object(lu, "_runtime_main_has_version", return_value=False)
    @mock.patch.object(lu, "_ensure_repos_ready", return_value=True)
    @mock.patch.object(lu, "_check_gh_auth", return_value=True)
    def test_webengine_blocked_when_runtime_pr_not_merged(
            self, gh_mock, repos_mock, version_mock, fork_mock):
        cfg = {"webengine_repo_path": "/cache/org.deepin.runtime.webengine",
              "runtime_repo_path": "/cache/org.deepin.runtime"}
        ok = lu.update_repo(cfg, version="6.7.0.49",
                            deb_repo="http://repo/stable_x/",
                            repo="webengine", dry_run=False)
        self.assertFalse(ok)
        fork_mock.assert_not_called()

    @mock.patch.object(lu, "_update_fork_repo", return_value=True)
    @mock.patch.object(lu, "_runtime_main_has_version", return_value=True)
    @mock.patch.object(lu, "_ensure_repos_ready", return_value=True)
    @mock.patch.object(lu, "_check_gh_auth", return_value=True)
    def test_webengine_proceeds_when_runtime_pr_merged(
            self, gh_mock, repos_mock, version_mock, fork_mock):
        cfg = {"webengine_repo_path": "/cache/org.deepin.runtime.webengine",
              "runtime_repo_path": "/cache/org.deepin.runtime"}
        ok = lu.update_repo(cfg, version="6.7.0.49",
                            deb_repo="http://repo/stable_x/",
                            repo="webengine", dry_run=False)
        self.assertTrue(ok)
        fork_mock.assert_called_once()


class PackageVersionGateTests(unittest.TestCase):
    @mock.patch.object(lu, "_log")
    @mock.patch.object(lu.subprocess, "run")
    def test_checker_failure_blocks_following_operations(self, run_mock, log_mock):
        run_mock.return_value = subprocess.CompletedProcess(
            ["check-package-versions.py"], 1, "",
            "包版本检查失败：发现 1 个包发生版本降级：\n"
            "  - linglong.yaml: libfoo: 2.0-1 -> 1.0-1\n",
        )
        self.assertFalse(lu._check_package_versions("/repo", "upstream/HEAD"))
        command = run_mock.call_args.args[0]
        self.assertIn("--report-file", command)
        messages = [call.args for call in log_mock.call_args_list]
        self.assertTrue(any("libfoo" in args[0] for args in messages))
        self.assertTrue(any("包版本检查未通过" in args[0] for args in messages))

    @mock.patch.object(lu, "_run_gh")
    @mock.patch.object(lu, "_check_package_versions", return_value=False)
    @mock.patch.object(lu, "_ensure_fork", return_value="tester/org.deepin.runtime")
    @mock.patch.object(lu, "_run")
    @mock.patch.object(lu.subprocess, "run")
    def test_runtime_update_stops_before_commit_push_and_pr(
            self, run_mock, command_mock, fork_mock, check_mock, gh_mock):
        def result_for(cmd, **kwargs):
            if cmd[-3:] == ["remote", "get-url", "upstream"]:
                return subprocess.CompletedProcess(cmd, 1, "", "")
            if cmd[-1:] == ["branch"]:
                return subprocess.CompletedProcess(cmd, 0, "", "")
            return subprocess.CompletedProcess(cmd, 0, "", "")

        run_mock.side_effect = result_for
        with tempfile.TemporaryDirectory() as repo_path:
            ok = lu._update_runtime_repo(
                "org.deepin.runtime", repo_path, "6.7.0.50",
                "http://repo/stable_x", "tester", {},
            )

        self.assertFalse(ok)
        check_mock.assert_called_once_with(repo_path, "upstream/HEAD")
        commands = [call.args[0] for call in command_mock.call_args_list]
        self.assertFalse(any("commit" in cmd for cmd in commands))
        self.assertFalse(any("push" in cmd for cmd in commands))
        gh_mock.assert_not_called()

    @mock.patch.object(lu, "_run_gh")
    @mock.patch.object(lu, "_check_package_versions", return_value=False)
    @mock.patch.object(lu, "_ensure_fork", return_value="tester/org.deepin.runtime")
    @mock.patch.object(lu, "_run")
    @mock.patch.object(lu.subprocess, "run")
    def test_explicit_ignore_continues_to_commit_push_and_pr(
            self, run_mock, command_mock, fork_mock, check_mock, gh_mock):
        def result_for(cmd, **kwargs):
            if cmd[-3:] == ["remote", "get-url", "upstream"]:
                return subprocess.CompletedProcess(cmd, 1, "", "")
            if cmd[-1:] == ["branch"]:
                return subprocess.CompletedProcess(cmd, 0, "", "")
            if cmd[:3] == ["gh", "pr", "list"]:
                return subprocess.CompletedProcess(
                    cmd, 0, "https://github.com/linglongdev/org.deepin.runtime/pull/1\n", ""
                )
            return subprocess.CompletedProcess(cmd, 0, "", "")

        run_mock.side_effect = result_for
        with tempfile.TemporaryDirectory() as repo_path:
            ok = lu._update_runtime_repo(
                "org.deepin.runtime", repo_path, "6.7.0.50",
                "http://repo/stable_x", "tester", {},
                ignore_package_version_gate=True,
            )

        self.assertTrue(ok)
        commands = [call.args[0] for call in command_mock.call_args_list]
        self.assertTrue(any("commit" in cmd for cmd in commands))
        self.assertTrue(any("push" in cmd for cmd in commands))
        gh_mock.assert_not_called()

    def test_ignore_gate_cli_flag_defaults_false_and_can_be_explicit(self):
        common = [
            "update-repo", "--version", "6.7.0.50",
            "--deb-repo", "http://repo/stable_x",
        ]
        self.assertFalse(
            lu._build_parser().parse_args(common).ignore_package_version_gate
        )
        self.assertTrue(
            lu._build_parser().parse_args(
                common + ["--ignore-package-version-gate"]
            ).ignore_package_version_gate
        )

if __name__ == "__main__":
    unittest.main()
