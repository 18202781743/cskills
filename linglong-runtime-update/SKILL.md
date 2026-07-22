---
name: linglong-runtime-update
description: DTK 玲珑 Runtime 更新自动化工具。当用户需要更新 org.deepin.runtime 和 org.deepin.runtime.webengine 的玲珑 runtime 时使用此 skill。覆盖 CRP 打包、Jenkins 仓库更新、yaml 文件修改与 PR 合并、玲珑 layer 构建、N8N 推送全流程。支持单步手动执行和全自动执行。
---

# DTK 玲珑 Runtime 更新

自动化更新 org.deepin.runtime 和 org.deepin.runtime.webengine 两个玲珑 runtime 仓库的完整工作流。

## 前置条件

- CRP OA/LDAP 账号（首次运行需认证）
- Jenkins 账号（首次运行交互输入，加密缓存；默认 yeshanshan）
- GitHub Token（通过 `gh auth status` 确认已登录，git 操作用当前用户身份）
- 本地无需预先 clone 仓库，脚本自动 clone 到 `~/.cache/linglong-update/repos/`

## 快速开始

```bash
# 交互式菜单（推荐，无参数启动）
python3 scripts/linglong-update.py

# 命令行指定步骤
python3 scripts/linglong-update.py auto --version 1.1.1.1
python3 scripts/linglong-update.py crp-pack
python3 scripts/linglong-update.py crp-pack --topic "xxx" --branch "crimson-testing"
python3 scripts/linglong-update.py build-repo
python3 scripts/linglong-update.py build-repo --repo-id 20260722
python3 scripts/linglong-update.py update-repo --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_xxx/
python3 scripts/linglong-update.py build-layer
python3 scripts/linglong-update.py build-layer --repo-url github.com/linglongdev/org.deepin.runtime
python3 scripts/linglong-update.py push-layer --layer-url http://10.20.64.92:8080/crimson_runtime/stable_xxx/
```

## 版本号规则

玲珑 runtime 版本格式 `X.Y.0.Z`，与 DTK 版本 `X.Y.Z` 一一对应。

- 从 `https://github.com/linuxdeepin/dtkcore/blob/master/VERSION` 读取 DTK 版本
- 例如 DTK `6.7.46` → 玲珑 `6.7.0.46`
- 也可通过 `--version` 手动指定

## 工作流步骤

### Step 1: CRP 打包

在 CRP 平台上对 DTK 相关项目进行打包。调用 `uniontech-crp-pack` skill 的功能。

- 主题: 玲珑runtime dtk版本更新
- 平台分支: crimson-testing
- 架构: arm64, loong64, mips64, riscv64, sw64

### Step 2: 制作更新仓库

触发 Jenkins job `runtime-repo-update` 制作更新仓库。参数可为空（使用日期）或传入自定义标识。

- Jenkins URL: https://jenkins.cicd.getdeepin.org/view/dtk/job/runtime-repo-update/
- 输出仓库地址格式: http://10.20.64.92:8080/crimson_runtime/stable_xxx/
- 需要等待 job 构建成功才能进入下一步

### Step 3: 修改 yaml 文件并创建 PR

修改 org.deepin.runtime 和 org.deepin.runtime.webengine 仓库:

1. 更新仓库地址为 Step 2 生成的地址
2. 更新版本号
3. webengine 先 apply `assets/webengine.patch` 补丁（增加 QtWebEngine 支持）
4. 执行 `daily.bash` 脚本更新 yaml 文件
5. 创建 PR 并等待合并

### Step 4: 构建玲珑 Layer

触发 Jenkins job `linglong-runtime-build` 制作玲珑 layer。

- Jenkins URL: https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/
- 需要等待 job 构建成功

### Step 5: N8N 推送 Layer

通过 N8N 表单推送 layer 到玲珑仓库。同时关注 push-to-old 和 push-to-test 两个 Jenkins job 的状态。

- N8N 表单: https://n8n.cicd.getdeepin.org/form/097d0087-7f34-4614-8329-82d096af7ba5
- push-to-old: https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-push-to-old/
- push-to-test: https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-push-to-test/

## 配置

配置文件位于 `~/.config/linglong-update/config.json`，支持自定义:

```json
{
  "crp_topic": "玲珑runtime dtk版本更新",
  "crp_branch": "crimson-testing",
  "archs": ["arm64", "loong64", "mips64", "riscv64", "sw64"],
  "runtime_repo_path": "~/.cache/linglong-update/repos/org.deepin.runtime",
  "webengine_repo_path": "~/.cache/linglong-update/repos/org.deepin.runtime.webengine"
}
```

Jenkins 凭证独立存储于 `~/.config/linglong-update/jenkins_creds.json`（base64 混淆）。

webengine 补丁存放于 skill 的 `assets/webengine.patch`，脚本自动查找。

## 依赖

- Python 3.8+
- requests
- 需要 `gh` CLI 已认证
- CRP 认证（通过 uniontech-crp-pack）

## 详细参考

- [CRP 打包模块](references/crp-pack.md)
- [Jenkins 交互模块](references/jenkins.md)
- [仓库更新与 PR 模块](references/repo-update.md)
