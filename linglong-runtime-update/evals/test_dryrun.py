#!/usr/bin/env python3
"""DTK 玲珑 Runtime 更新工具 - Eval 测试。

使用 DTK 版本 6.7.45（玲珑 runtime 6.7.0.45）进行 dry-run 测试，验证各命令参数传递和版本推断。

用法:
  python3 evals/test_dryrun.py [crp-pack|build-repo|update-repo|build-layer|push-layer|auto|all]
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import importlib.util
spec = importlib.util.spec_from_file_location('lu', os.path.join(os.path.dirname(__file__), '..', 'scripts', 'linglong-update.py'))
lu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lu)

TEST_DTK_VERSION = "6.7.45"
TEST_LINGLONG_VERSION = "6.7.0.45"  # 玲珑 runtime 版本格式 X.Y.0.Z (DTK 6.7.45 经 _to_linglong_version 映射)
TEST_DEB_REPO = "http://10.20.64.92:8080/crimson_runtime/stable_test/"
TEST_LAYER_URL = "https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/999/"


def _mock_auth():
    """Mock 所有认证函数和文件系统函数，避免交互式输入和权限问题"""
    lu._ensure_jenkins_auth = lambda force=False: {"user": "test", "password": "test"}
    lu._check_gh_auth = lambda: True
    lu._ensure_repos_ready = lambda cfg: True
    lu.load_config = lambda: dict(lu.DEFAULT_CONFIG)
    lu.save_config = lambda cfg: None
    lu.save_state = lambda state: None
    lu.clear_state = lambda: None
    lu._config_dir = lambda: lu.Path("/tmp/linglong-test-config")


def _test_version_infer():
    """测试版本推断：从 deb 仓库解析 dtkcore 版本并映射为玲珑版本"""
    print("=" * 60)
    print("[TEST] 版本推断与映射")
    print("=" * 60)
    orig_infer = lu._infer_version
    def mock_infer(deb_repo, cfg=None):
        return TEST_DTK_VERSION  # _infer_version 返回 DTK 版本
    lu._infer_version = mock_infer

    dtk_ver = lu._infer_version(TEST_DEB_REPO, {"archs": ["amd64"]})
    assert dtk_ver == TEST_DTK_VERSION, f"Expected DTK {TEST_DTK_VERSION}, got {dtk_ver}"
    print(f"  PASS: deb 仓库 → DTK 版本 {dtk_ver}")

    linglong_ver = lu._to_linglong_version(dtk_ver)
    assert linglong_ver == TEST_LINGLONG_VERSION, f"Expected 玲珑 {TEST_LINGLONG_VERSION}, got {linglong_ver}"
    print(f"  PASS: DTK {dtk_ver} → 玲珑 {linglong_ver}")

    # Test _to_linglong_version with edge cases
    assert lu._to_linglong_version("6.7.44") == "6.7.0.44", "6.7.44 → 6.7.0.44"
    assert lu._to_linglong_version("1.2.3") == "1.2.0.3", "1.2.3 → 1.2.0.3"
    assert lu._to_linglong_version("1.2") == "1.2", "non-X.Y.Z passed through"
    print(f"  PASS: _to_linglong_version 边界测试通过")

    lu._infer_version = orig_infer


def _test_crp_pack():
    """测试 CRP 打包 dry-run"""
    print("\n" + "=" * 60)
    print("[TEST] crp-pack --dry-run")
    print("=" * 60)
    _mock_auth()
    cfg = lu.load_config()
    ok = lu.crp_pack(cfg, version=TEST_DTK_VERSION, dry_run=True)
    assert ok, "crp-pack dry-run should return True"
    print("  PASS: crp-pack dry-run OK")


def _test_build_repo():
    """测试 build-repo dry-run"""
    print("\n" + "=" * 60)
    print("[TEST] build-repo --dry-run")
    print("=" * 60)
    _mock_auth()
    cfg = lu.load_config()
    url = lu.build_repo(cfg, repo_id="test20260722", dry_run=True)
    assert url is not None, "build-repo dry-run should return URL"
    assert "test20260722" in url, f"URL should contain repo_id: {url}"
    print(f"  PASS: build-repo dry-run OK, URL={url}")


def _test_update_repo():
    """测试 update-repo dry-run"""
    print("\n" + "=" * 60)
    print("[TEST] update-repo --dry-run")
    print("=" * 60)
    _mock_auth()
    cfg = lu.load_config()
    ok = lu.update_repo(cfg, version=TEST_LINGLONG_VERSION, deb_repo=TEST_DEB_REPO, dry_run=True)
    assert ok, "update-repo dry-run should return True"
    print("  PASS: update-repo dry-run OK")


def _test_build_layer():
    """测试 build-layer dry-run"""
    print("\n" + "=" * 60)
    print("[TEST] build-layer --dry-run")
    print("=" * 60)
    _mock_auth()
    cfg = lu.load_config()
    ok = lu.build_layer(cfg, repo_url="github.com/linglongdev/org.deepin.runtime",
                        repo_branch="main", repo="runtime", dry_run=True)
    assert ok, "build-layer dry-run should return True"
    print("  PASS: build-layer dry-run OK")


def _test_push_layer():
    """测试 push-layer dry-run"""
    print("\n" + "=" * 60)
    print("[TEST] push-layer --dry-run")
    print("=" * 60)
    _mock_auth()
    cfg = lu.load_config()
    ok = lu.push_layer(cfg, layer_url=TEST_LAYER_URL, repo="runtime", dry_run=True)
    assert ok, "push-layer dry-run should return True"
    print("  PASS: push-layer dry-run OK")


def _test_auto():
    """测试 auto dry-run"""
    print("\n" + "=" * 60)
    print("[TEST] auto --dry-run")
    print("=" * 60)
    _mock_auth()
    cfg = lu.load_config()

    orig_save = lu.save_state
    orig_clear = lu.clear_state
    orig_update_runtime = lu._update_runtime_repo
    orig_update_webengine = lu._update_webengine_repo
    def mock_save(state):
        pass
    def mock_clear():
        pass
    def mock_update(label, repo_path, version, deb_repo, fork_owner=None):
        return True
    def mock_update_web(label, repo_path, version, deb_repo, runtime_repo_path):
        return True
    lu.save_state = mock_save
    lu.clear_state = mock_clear
    lu._update_runtime_repo = mock_update
    lu._update_webengine_repo = mock_update_web

    # auto_mode 接收 DTK 版本号，内部调用 _to_linglong_version 映射为玲珑版本
    ok = lu.auto_mode(cfg, version=TEST_DTK_VERSION, repo_id="test",
                      deb_repo=TEST_DEB_REPO, layer_url=TEST_LAYER_URL,
                      dry_run=True, start_from=1)
    assert ok, "auto dry-run should return True"
    print(f"  PASS: auto dry-run OK (DTK {TEST_DTK_VERSION} → 玲珑 {TEST_LINGLONG_VERSION})")
    lu.save_state = orig_save
    lu.clear_state = orig_clear
    lu._update_runtime_repo = orig_update_runtime
    lu._update_webengine_repo = orig_update_webengine


def run_all():
    print("DTK 玲珑 Runtime 更新工具 - Eval 测试")
    print(f"测试 DTK 版本: {TEST_DTK_VERSION} (玲珑: {TEST_LINGLONG_VERSION})")

    _test_version_infer()
    _test_crp_pack()
    _test_build_repo()
    _test_update_repo()
    _test_build_layer()
    _test_push_layer()
    _test_auto()

    print("\n" + "=" * 60)
    print("所有测试通过!")
    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "crp-pack":
            _test_crp_pack()
        elif cmd == "build-repo":
            _test_build_repo()
        elif cmd == "update-repo":
            _test_update_repo()
        elif cmd == "build-layer":
            _test_build_layer()
        elif cmd == "push-layer":
            _test_push_layer()
        elif cmd == "auto":
            _test_auto()
        elif cmd == "version":
            _test_version_infer()
        elif cmd == "all":
            run_all()
        else:
            print(f"Unknown test: {cmd}")
            sys.exit(1)
    else:
        run_all()
