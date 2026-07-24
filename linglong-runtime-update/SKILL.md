---
name: linglong-runtime-update
description: DTK 玲珑 Runtime 更新自动化工具。当用户需要更新 org.deepin.runtime 和 org.deepin.runtime.webengine 的玲珑 runtime 时使用此 skill。覆盖 CRP 打包、Jenkins 仓库更新、yaml 文件修改与 PR 合并、玲珑 layer 构建、N8N 推送全流程。支持单步手动执行和全自动执行。
---

# DTK 玲珑 Runtime 更新

自动化更新 org.deepin.runtime 和 org.deepin.runtime.webengine 两个玲珑 runtime 仓库的完整工作流。

## 前置条件

- CRP OA/LDAP 账号（首次运行需认证，凭证加密缓存到 `~/.config/uniontech-oa/`）
- Jenkins 账号（首次运行交互输入，base64 混淆缓存到 `~/.config/linglong-runtime-update/jenkins_creds.json`；默认 yeshanshan）
- GitHub Token（通过 `gh auth status` 确认已登录，git 操作用当前用户身份）
- 本地无需预先 clone 仓库，脚本自动 clone 到 `~/.cache/linglong-runtime-update/repos/`

## 快速开始

```bash
# 交互式菜单（推荐，无参数启动）
python3 scripts/linglong-update.py

# 单步执行
python3 scripts/linglong-update.py crp-pack
python3 scripts/linglong-update.py crp-pack --topic "xxx" --branch "upstream/master" --version 6.7.46
python3 scripts/linglong-update.py build-repo
python3 scripts/linglong-update.py build-repo --repo-id 20260722
python3 scripts/linglong-update.py update-repo --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_xxx/
python3 scripts/linglong-update.py update-repo --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_xxx/ --repo webengine
python3 scripts/linglong-update.py build-layer                                      # runtime
python3 scripts/linglong-update.py build-layer --repo webengine                     # webengine
python3 scripts/linglong-update.py build-layer --repo-url github.com/linglongdev/org.deepin.runtime --repo-branch main
python3 scripts/linglong-update.py push-layer                                       # runtime
python3 scripts/linglong-update.py push-layer --repo webengine                      # webengine
python3 scripts/linglong-update.py push-layer --layer-url https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/205/

# 全自动执行
python3 scripts/linglong-update.py auto --version 6.7.46                            # DTK 版本号，自动映射为玲珑版本
python3 scripts/linglong-update.py auto --version 6.7.46 --repo-id 20260722 --start-from 3

# 状态查询
python3 scripts/linglong-update.py check-repo --build-url <Jenkins构建URL>
python3 scripts/linglong-update.py check-build --build-url <Jenkins构建URL>
python3 scripts/linglong-update.py config        # 配置参数和 Jenkins 凭证
python3 scripts/linglong-update.py status        # 查看各阶段状态（CRP/Jenkins/GitHub/本地）
```

## 版本号规则

从 deb 更新仓库解析 dtkcore 包的版本号，按映射规则计算玲珑 runtime 版本：

- 从 config 的 `archs` 第一个架构匹配 deb 包名（如 `libdtk6core_X.Y.Z-N_amd64.deb`）
- 提取 DTK 版本 `X.Y.Z`，映射为玲珑 runtime 版本 `X.Y.0.Z`
- 示例：dtkcore `6.7.44` → 玲珑 runtime `6.7.0.44`

不同阶段使用的版本格式不同：

| 命令 | --version 格式 | 说明 |
|------|---------------|------|
| `crp-pack` | DTK 版本 `X.Y.Z` | 如 `--version 6.7.44` |
| `update-repo` | 玲珑版本 `X.Y.0.Z` | 如 `--version 6.7.0.44`（未指定时从 deb 仓库自动推断并映射） |
| `auto` | DTK 版本 `X.Y.Z` | 如 `--version 6.7.44`，内部自动映射为玲珑版本用于 update-repo 阶段 |

## 工作流步骤

### Step 1: CRP 打包

在 CRP 平台上对 DTK 相关项目创建打包实例。调用外部 `crp_pack.py` 脚本（与 `linglong-update.py` 同目录），该脚本独立处理 CRP 认证和打包实例创建。

打包的项目列表与 github-workflow-autotag 保持一致（`dtkcommon-v25`, `dtklog-v25`, `dtkcore-v25`, `dtkgui-v25`, `dtkwidget-v25`, `dtkdeclarative-v25`, `qt5integration-v25`, `qt5platform-plugins-v25`）。

- **主题**: `玲珑runtime dtk版本更新`（可配置 `crp_topic`）
- **Git 分支过滤**: `upstream/master`（可配置 `crp_branch`，传给 CRP 的筛选分支名）
- **CRP BranchID**: `129`（可配置 `crp_branch_id`，对应 `crimson-testing` 平台分支）
- **架构**: `amd64, arm64, loong64`（可配置 `archs`，以分号 `;` 分隔传给 `crp_pack.py`）

支持通过 `--topic`、`--branch`、`--archs`（逗号分隔）、`--branch-id`、`--version` 命令行参数覆盖默认配置。

### Step 2: 制作更新仓库

触发 Jenkins job `runtime-repo-update` 制作更新仓库。`build-repo` 仅触发构建、不等待完成。

- Jenkins URL: https://jenkins.cicd.getdeepin.org/view/dtk/job/runtime-repo-update/
- Job 参数: `SUFFIX`（接收 `--repo-id` 传入的仓库标识，为空时使用当天日期 YYYYMMDD）
- 输出仓库地址格式: http://10.20.64.92:8080/crimson_runtime/stable_xxx/

触发后使用 `check-repo` 轮询构建状态并提取仓库地址：

```bash
# 触发构建
python3 scripts/linglong-update.py build-repo --repo-id 20260722

# 轮询状态，构建成功后自动提取仓库地址
python3 scripts/linglong-update.py check-repo --build-url https://jenkins.cicd.getdeepin.org/view/dtk/job/runtime-repo-update/19/
```

### Step 3: 修改 yaml 文件并创建 PR

修改 org.deepin.runtime 和 org.deepin.runtime.webengine 两个仓库的 `linglong.yaml`。两个仓库的更新流程不同：

**runtime 仓库**（默认）:
1. fetch origin → checkout main → reset to origin/HEAD
2. 创建/复用固定分支 `update/linglong-runtime`
3. 修改 `linglong.yaml` 版本号和仓库 URL，修改 `update.go` 中的 `deepinRepoURL`
4. 执行 `daily.bash` 脚本生成更新的 yaml 文件
5. 分支已存在则 `git commit --amend`，否则新建 commit
6. 创建 fork（如不存在），强推到 fork 分支
7. 创建 PR 到 upstream（如 PR 已存在则复用）
8. 可选等待 PR 合并

**webengine 仓库**（`--repo webengine`）:
1. 以 runtime 仓库本地副本为基准（通过 `runtime-base` remote 引用）
2. reset 到 runtime-base/HEAD
3. 应用 `assets/webengine.patch` 补丁（增加 QtWebEngine 支持）→ commit 1
4. 修改 `linglong.yaml` 版本号和仓库 URL → commit 2
5. 强推到 origin/main（不创建 PR）

### Step 4: 构建玲珑 Layer

触发 Jenkins job `linglong-runtime-build` 制作玲珑 layer。与 Step 3 类似，runtime 和 webengine 各触发一次构建（通过 `--repo` 参数切换，默认 `runtime`）。`build-layer` 仅触发构建、不等待完成。

- Jenkins URL: https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/
- 参数: `REPO_URL`（默认 `github.com/linglongdev/org.deepin.runtime`）、`REPO_BRANCH`（默认 `main`）
- webengine 时 REPO_URL 为 `github.com/linglongdev/org.deepin.runtime.webengine`
- 可通过 `--repo-url` 和 `--repo-branch` 覆盖

触发后使用 `check-build` 轮询构建状态：

```bash
# 触发 runtime 构建
python3 scripts/linglong-update.py build-layer

# 触发 webengine 构建
python3 scripts/linglong-update.py build-layer --repo webengine

# 轮询状态
python3 scripts/linglong-update.py check-build --build-url https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/202/
```

### Step 5: N8N 推送 Layer

通过 N8N 表单推送 layer 到玲珑仓库。runtime 和 webengine 各执行一次推送（通过 `--repo` 参数切换，默认 `runtime`）。脚本提示用户手动提交 N8N 表单，确认后自动触发 `push-to-old` 和 `push-to-test` 两个 Jenkins job 并等待完成。

- N8N 表单: https://n8n.cicd.getdeepin.org/form/097d0087-7f34-4614-8329-82d096af7ba5
- push-to-old: https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-push-to-old/
- push-to-test: https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-push-to-test/
- `--layer-url` 传入 **build-layer 产出的 Jenkins 构建 URL**（如 `https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/205/`），脚本自动从控制台输出解析真实 layer 地址后传入 push job
- `push-layer` 会等待两个 push job 构建完成才返回

## 配置

配置文件位于 `~/.config/linglong-runtime-update/config.json`，支持自定义:

```json
{
  "crp_topic": "玲珑runtime dtk版本更新",
  "crp_branch": "upstream/master",
  "crp_branch_id": 129,
  "archs": ["amd64", "arm64", "loong64"],
  "runtime_repo_path": "~/.cache/linglong-runtime-update/repos/org.deepin.runtime",
  "webengine_repo_path": "~/.cache/linglong-runtime-update/repos/org.deepin.runtime.webengine"
}
```

- `crp_branch` 是 Git 分支过滤（传给 CRP 的筛选分支名），与 CRP 平台分支名（通过 BranchID `129` 映射到 `crimson-testing`）是不同概念
- Fork 推送目标由脚本自动探测（`gh api user`），回退到常量 `FORK_OWNER`（`18202781743`），不可配置
- Jenkins 凭证独立存储于 `~/.config/linglong-runtime-update/jenkins_creds.json`（base64 混淆，600 权限）
- webengine 补丁存放于 skill 的 `assets/webengine.patch`，脚本通过 `_find_webengine_patch()` 自动查找

## auto 模式说明

全自动模式按顺序执行 Step 1-5，支持断点续传：

- `--start-from N` 从指定步骤开始（跳过前面步骤）
- 每步完成后状态保存到 `~/.config/linglong-runtime-update/state.json`
- 某步失败后重新运行，自动从失败步骤恢复
- `--dry-run` 模式下不触发实际操作，仅打印参数
- `--version` 接收 DTK 版本号（如 `6.7.44`），内部自动映射为玲珑版本用于 update-repo 阶段

## 依赖

- Python 3.8+
- requests
- 需要 `gh` CLI 已认证
- CRP 认证通过外部 `crp_pack.py` 脚本（该脚本需要 `rsa` 和 `cryptography` 模块）
- `crp_pack.py` 使用 `Fernet` 加密缓存凭证到 `~/.config/uniontech-oa/`

## 详细参考

- [CRP 打包模块](references/crp-pack.md)
- [Jenkins 交互模块](references/jenkins.md)
- [仓库更新与 PR 模块](references/repo-update.md)
