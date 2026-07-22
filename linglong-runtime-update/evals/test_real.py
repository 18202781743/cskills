#!/usr/bin/env python3
"""DTK 玲珑 Runtime 更新工具 - 真实环境测试。

在真实环境（或 staging 环境）中分步骤执行，验证每个环节的实际行为。
⚠️ 注意：真实测试会触发实际的 CRP/Jenkins/GitHub 操作，
请确认环境安全后再执行。

用法:
  python3 evals/test_real.py [step1|step2|step3|step4|step5|auto|all]
"""

import sys
import os
import time
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import importlib.util
spec = importlib.util.spec_from_file_location('lu', os.path.join(os.path.dirname(__file__), '..', 'scripts', 'linglong-update.py'))
lu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lu)

# 测试参数
TEST_DTK_VERSION = "6.7.45"
TEST_LINGLONG_VERSION = "6.7.0.45"
TEST_REPO_ID = "test20260722"
TEST_DEB_REPO = f"http://10.20.64.92:8080/crimson_runtime/stable_{TEST_REPO_ID}/"
TEST_LAYER_URL = f"http://10.20.64.92:8080/crimson_runtime/stable_{TEST_REPO_ID}/"


def _confirm(msg: str) -> bool:
    """询问用户确认"""
    resp = input(f"{msg} [y/N]: ").strip().lower()
    return resp in ("y", "yes")


def _log_section(name: str):
    print("\n" + "=" * 70)
    print(f"[REAL TEST] {name}")
    print("=" * 70)


def test_step1_crp_pack():
    """Step 1: CRP 打包 - 在 CRP 平台创建 DTK 打包实例"""
    _log_section("Step 1: CRP 打包")
    
    print("\n检验要点:")
    print("  1. CRP 认证成功（OA/LDAP 账号密码或缓存 token）")
    print("  2. 能搜索到主题 '玲珑runtime dtk版本更新'")
    print("  3. 能搜索到 DTK 项目（dtkcore, dtkgui 等）")
    print("  4. 能列出 crimson-testing 分支的提交信息")
    print("  5. 创建打包实例成功（HTTP 200）")
    print("  6. 重复创建时能正确删除旧实例再创建新实例")
    print()
    
    if not _confirm("确认要在 CRP 上创建打包实例?"):
        print("用户取消 Step 1")
        return False
    
    cfg = lu.load_config()
    ok = lu.crp_pack(cfg, version=TEST_DTK_VERSION, dry_run=False)
    
    if ok:
        print("PASS Step 1: CRP 打包实例创建成功")
    else:
        print("FAIL Step 1: CRP 打包实例创建失败")
    return ok


def test_step2_build_repo():
    """Step 2: 制作更新仓库 - 触发 Jenkins runtime-repo-update"""
    _log_section("Step 2: 制作更新仓库")
    
    print("\n检验要点:")
    print("  1. Jenkins 认证成功（用户名密码或缓存）")
    print("  2. Job 触发成功（HTTP 200/201/302）")
    print("  3. 能正确获取构建编号")
    print("  4. 能轮询构建状态直到完成")
    print("  5. 构建成功后从控制台输出提取仓库 URL")
    print("  6. URL 格式正确且可访问")
    print()
    
    if not _confirm("确认要触发 Jenkins build-repo job?"):
        print("用户取消 Step 2")
        return False
    
    cfg = lu.load_config()
    url = lu.build_repo(cfg, repo_id=TEST_REPO_ID, dry_run=False)
    
    if url:
        print(f"PASS Step 2: 仓库 URL = {url}")
        # 验证 URL 可访问性
        try:
            import requests
            resp = requests.get(url, timeout=10)
            print(f"   URL 访问状态: HTTP {resp.status_code}")
        except Exception as e:
            print(f"   URL 访问异常: {e}")
    else:
        print("FAIL Step 2: 未能获取仓库 URL")
    return url is not None


def test_step3_update_repo():
    """Step 3: 修改 yaml + PR - 修改仓库并创建 PR"""
    _log_section("Step 3: 修改 yaml + PR")
    
    print("\n检验要点:")
    print("  1. gh auth status 通过")
    print("  2. 自动 clone 仓库到 ~/.cache/linglong-update/repos/")
    print("  3. 创建新分支")
    print("  4. webengine 正确应用 assets/webengine.patch")
    print("  5. linglong.yaml 版本号和仓库 URL 正确更新")
    print("  6. daily.bash 执行成功")
    print("  7. git commit 信息正确")
    print("  8. gh pr create 成功")
    print("  9. PR 标题和 body 格式正确")
    print()
    
    if not _confirm("确认要修改仓库并创建 PR?"):
        print("用户取消 Step 3")
        return False
    
    cfg = lu.load_config()
    ok = lu.update_repo(cfg, version=TEST_LINGLONG_VERSION, 
                        deb_repo=TEST_DEB_REPO, dry_run=False)
    
    if ok:
        print("PASS Step 3: PR 创建成功")
    else:
        print("FAIL Step 3: PR 创建失败")
    return ok


def test_step4_build_layer():
    """Step 4: 构建玲珑 Layer - 触发 Jenkins linglong-runtime-build"""
    _log_section("Step 4: 构建玲珑 Layer")
    
    print("\n检验要点:")
    print("  1. Job 触发成功，传入正确的 REPO_URL 和 REPO_BRANCH")
    print("  2. 能正确获取构建编号")
    print("  3. 能轮询构建状态直到完成")
    print("  4. 构建成功（result == 'SUCCESS'）")
    print("  5. 控制台输出中可提取 layer URL")
    print()
    
    if not _confirm("确认要触发 Jenkins build-layer job?"):
        print("用户取消 Step 4")
        return False
    
    cfg = lu.load_config()
    ok = lu.build_layer(cfg, repo_url="github.com/linglongdev/org.deepin.runtime",
                        repo_branch="main", dry_run=False)
    
    if ok:
        print("PASS Step 4: Layer 构建成功")
    else:
        print("FAIL Step 4: Layer 构建失败")
    return ok


def test_step5_push_layer():
    """Step 5: N8N 推送 - 提交 N8N 表单并触发 push job"""
    _log_section("Step 5: N8N 推送 Layer")
    
    print("\n检验要点:")
    print("  1. N8N 表单 URL 可访问")
    print("  2. 正确提示用户手动提交 N8N 表单")
    print("  3. 触发 linglong-runtime-push-to-old 成功")
    print("  4. 触发 linglong-runtime-push-to-test 成功")
    print("  5. 两个 push job 都能正常完成")
    print()
    
    if not _confirm("确认要执行 N8N 推送?"):
        print("用户取消 Step 5")
        return False
    
    cfg = lu.load_config()
    ok = lu.push_layer(cfg, layer_url=TEST_LAYER_URL, dry_run=False)
    
    if ok:
        print("PASS Step 5: N8N 推送成功")
    else:
        print("FAIL Step 5: N8N 推送失败")
    return ok


def test_auto():
    """Auto 模式: 全自动执行全部步骤"""
    _log_section("Auto 模式: 全自动执行")
    
    print("\n检验要点:")
    print("  1. --start-from 参数能正确跳过前面的步骤")
    print("  2. 每个步骤完成后状态正确保存到 state.json")
    print("  3. 某步骤失败后，重新运行能从失败步骤恢复")
    print("  4. --dry-run 模式下不触发实际操作")
    print()
    
    if not _confirm("确认要执行全自动模式?"):
        print("用户取消 Auto 模式")
        return False
    
    cfg = lu.load_config()
    
    # Mock _infer_version to avoid actual inference
    orig_infer = lu._infer_version
    lu._infer_version = lambda cfg: TEST_LINGLONG_VERSION
    
    ok = lu.auto_mode(cfg, version=TEST_LINGLONG_VERSION, 
                      repo_id=TEST_REPO_ID, deb_repo=TEST_DEB_REPO,
                      layer_url=TEST_LAYER_URL, dry_run=False, start_from=1)
    
    lu._infer_version = orig_infer
    
    if ok:
        print("PASS Auto 模式: 全部步骤执行成功")
    else:
        print("FAIL Auto 模式")
    return ok


def run_all():
    """运行全部真实测试"""
    print("DTK 玲珑 Runtime 更新工具 - 真实环境测试")
    print(f"测试 DTK 版本: {TEST_DTK_VERSION}")
    print(f"测试玲珑版本: {TEST_LINGLONG_VERSION}")
    print("\n警告: 真实测试会触发实际的 CRP/Jenkins/GitHub 操作!")
    print("    请确认当前环境安全后再继续。\n")
    
    if not _confirm("确认要运行全部真实测试?"):
        print("用户取消")
        return 1
    
    results = {}
    
    results["step1"] = test_step1_crp_pack()
    results["step2"] = test_step2_build_repo()
    results["step3"] = test_step3_update_repo()
    results["step4"] = test_step4_build_layer()
    results["step5"] = test_step5_push_layer()
    
    print("\n" + "=" * 70)
    print("测试汇总")
    print("=" * 70)
    for name, ok in results.items():
        status = "PASS" if ok else "FAIL"
        print(f"  {name}: {status}")
    
    all_pass = all(results.values())
    if all_pass:
        print("\n所有真实测试通过!")
    else:
        print("\n部分测试失败，请查看上方日志")
    
    return 0 if all_pass else 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        ok = False
        if cmd == "step1":
            ok = test_step1_crp_pack()
        elif cmd == "step2":
            ok = test_step2_build_repo()
        elif cmd == "step3":
            ok = test_step3_update_repo()
        elif cmd == "step4":
            ok = test_step4_build_layer()
        elif cmd == "step5":
            ok = test_step5_push_layer()
        elif cmd == "auto":
            ok = test_auto()
        elif cmd == "all":
            sys.exit(run_all())
        else:
            print(f"Unknown test: {cmd}")
            print("Usage: python3 test_real.py [step1|step2|step3|step4|step5|auto|all]")
            sys.exit(1)
        sys.exit(0 if ok else 1)
    else:
        print("DTK 玲珑 Runtime 更新工具 - 真实环境测试")
        print(f"测试 DTK 版本: {TEST_DTK_VERSION}")
        print(f"测试玲珑版本: {TEST_LINGLONG_VERSION}")
        print()
        print("用法: python3 test_real.py [step1|step2|step3|step4|step5|auto|all]")
        print()
        print("步骤说明:")
        print("  step1 - CRP 打包")
        print("  step2 - 制作更新仓库 (Jenkins)")
        print("  step3 - 修改 yaml + PR (GitHub)")
        print("  step4 - 构建玲珑 Layer (Jenkins)")
        print("  step5 - N8N 推送 Layer")
        print("  auto  - 全自动模式")
        print("  all   - 运行全部步骤")
