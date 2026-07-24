---
name: linglong-runtime-update
description: |
  DTK 玲珑 Runtime 更新自动化。当用户提到"玲珑 runtime 更新"、"linglong runtime"、"org.deepin.runtime 更新"、"玲珑 layer 构建"或需要执行玲珑相关的 CRP 打包、Jenkins 构建更新仓库、修改 linglong.yaml 并创建 PR、N8N 推送 layer 时使用此 skill。支持单步手动执行和 goal 自动执行。
---
# DTK 玲珑 Runtime 更新


自动化更新 org.deepin.runtime 和 org.deepin.runtime.webengine 两个玲珑 runtime 仓库的完整工作流。

## ⚠ 请求频率约束

CRP、Jenkins、N8N 均为内网服务，请求响应缓慢（单次 5-30 秒）。**严格遵守以下约束**：

- **轮询间隔至少 5 分钟**：`--check` 等所有主动查询，间隔不得低于 300 秒（5 分钟）
- **不要主动查询非当前步骤的状态**：除非用户明确要求，不要执行 `status` 或 `--check` 查看非当前步骤的状态
- **触发后等待足够时间再首次查询**：Jenkins 构建触发后至少等 2 分钟再首次 `--check`，CRP 打包触发后至少等 5 分钟
- **`auto` / goal 模式下可循环轮询**：agent 使用 goal 自动执行时，可以循环 `--check` 等待构建完成，但每次间隔至少 5 分钟
- **单次 `--check` 显示仍在进行中**：告知用户当前状态和预计等待时间，等待至少 5 分钟后再查询

## 前置条件

- CRP OA/LDAP 账号（首次运行需认证，凭证加密缓存到 `~/.config/uniontech-oa/`）
- Jenkins 账号（首次运行交互输入用户名和密码，base64 混淆缓存到 `~/.config/linglong-runtime-update/jenkins_creds.json`）
- GitHub Token（通过 `gh auth status` 确认已登录，git 操作用当前用户身份）
- `ll-builder` 已安装（`daily.bash` 内部调用 `ll-builder build` 生成包列表）
- 本地无需预先 clone 仓库，脚本自动 clone 到 `~/.cache/linglong-runtime-update/repos/`
- Python 3.8+ 及依赖：需在 venv 中运行，手动创建 `~/.cache/linglong-runtime-update/venv/` 并安装 `scripts/requirements.txt`
- Go 环境：系统已安装 `go`（`daily.bash` 内部 `go run update.go` 使用）
- 网络代理：需设置 `no_proxy=.uniontech.com,.getdeepin.org,10.20.64.92`，使内网直连、外网走系统代理

## 快速开始

```bash
# 交互式菜单（推荐，无参数启动）
python3 scripts/linglong-update.py

# 单步执行（详见各步骤说明）
python3 scripts/linglong-update.py <command> --help
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

## 工作流步骤

### Step 1: CRP 打包

在 CRP 平台上对 DTK 相关项目创建打包实例。调用外部 `crp_pack.py` 脚本（与 `linglong-update.py` 同目录），该脚本独立处理 CRP 认证和打包实例创建。

打包的项目列表与 github-workflow-autotag 保持一致（`dtkcommon-v25`, `dtklog-v25`, `dtkcore-v25`, `dtkgui-v25`, `dtkwidget-v25`, `dtkdeclarative-v25`, `qt5integration-v25`, `qt5platform-plugins-v25`）。

- **主题**: `玲珑runtime dtk版本更新`（可配置 `crp_topic`）
- **Git 分支过滤**: `upstream/master`（可配置 `crp_branch`，传给 CRP 的筛选分支名）
- **CRP BranchID**: `129`（可配置 `crp_branch_id`，对应 `crimson-testing` 平台分支）
- **架构**: `amd64, arm64, loong64`（可配置 `archs`，以分号 `;` 分隔传给 `crp_pack.py`）

支持通过 `--topic`、`--branch`、`--archs`（逗号分隔）、`--branch-id`、`--version` 命令行参数覆盖默认配置。

使用 `--check` 查询当前打包状态，显示每个项目的构建状态和版本信息，所有项目 `UPLOAD_OK` 才算成功：

```bash
python3 scripts/linglong-update.py crp-pack --check
```
> ⚠ CRP 打包耗时较长，触发后至少等 5 分钟再 `--check`，若仍在进行中等 5 分钟后再查。

### Step 2: 制作更新仓库

触发 Jenkins job `runtime-repo-update` 制作更新仓库。`build-repo` 仅触发构建、不等待完成。

- Jenkins URL: https://jenkins.cicd.getdeepin.org/view/dtk/job/runtime-repo-update/
- Job 参数: `SUFFIX`（接收 `--repo-id` 传入的仓库标识，为空时使用当天日期 YYYYMMDD）
- **输出**: deb 仓库地址（如 http://10.20.64.92:8080/crimson_runtime/stable_xxx/），作为 Step 3 的 `--deb-repo` 输入

触发后使用 `--check` 轮询构建状态并提取仓库地址：

```bash
# 触发构建
python3 scripts/linglong-update.py build-repo --repo-id 20260722

# 等待至少 2 分钟后查询状态，间隔至少 5 分钟，构建成功后自动提取仓库地址
python3 scripts/linglong-update.py build-repo --check --build-url https://jenkins.cicd.getdeepin.org/view/dtk/job/runtime-repo-update/19/
```
> ⚠ 若仍在构建中，等 5 分钟后再查，不要短间隔反复查询。

### Step 3: 修改 yaml 文件并创建 PR

**输入**: Step 2 产出的 deb 仓库地址（`--deb-repo`）  **产物**: GitHub 仓库代码已更新（runtime 创建 PR 并合并，webengine 强推 origin/main）

修改 org.deepin.runtime 和 org.deepin.runtime.webengine 两个仓库的 `linglong.yaml`。两个仓库的更新流程不同：

**runtime 仓库**（默认）:
1. fetch origin → checkout main → reset to origin/HEAD
2. 创建/复用固定分支 `update/linglong-runtime`
3. 修改 `update.go` 中的 `deepinRepoURL` 为新的 deb 仓库地址
4. 将玲珑版本号传递给 `daily.bash`，由 `update.go` + `daily.bash` 自动更新 `linglong.yaml`
5. 分支已存在则 `git commit --amend`，否则新建 commit
6. 创建 fork（如不存在），强推到 fork 分支
7. 创建 PR 到 upstream（如 PR 已存在则复用）
8. PR 创建后返回，不等待合并（需手动合并或后续用 `--check` 查询）

> `linglong.yaml` 的版本号和仓库 URL 由 `update.go` 和 `daily.bash` 自动更新，脚本不直接修改 `linglong.yaml`。

**webengine 仓库**（`--repo webengine`）:
1. 以 runtime 仓库本地副本为基准（通过 `runtime-base` remote 引用）
2. reset 到 runtime-base/HEAD
3. 应用 `assets/webengine.patch` 补丁（增加 QtWebEngine 支持）→ commit 1
4. 修改 `update.go` 中的 `deepinRepoURL`，传递玲珑版本号给 `daily.bash` → commit 2
5. 强推到 origin/main（不创建 PR）

> webengine 的 commit 2 也由 `update.go` 和 `daily.bash` 自动生成，脚本不直接修改 `linglong.yaml`。

### Step 4: 构建玲珑 Layer

**隐含输入**: Step 3 已更新 GitHub 仓库代码（Jenkins 从该仓库拉取最新代码构建）  **输出**: layer 构建产物 URL

触发 Jenkins job `linglong-runtime-build` 制作玲珑 layer。与 Step 3 类似，runtime 和 webengine 各触发一次构建（通过 `--repo` 参数切换，默认 `runtime`）。`build-layer` 仅触发构建、不等待完成。

- Jenkins URL: https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/
- 参数: `REPO_URL`（默认 `github.com/linglongdev/org.deepin.runtime`）、`REPO_BRANCH`（默认 `main`）
- webengine 时 REPO_URL 为 `github.com/linglongdev/org.deepin.runtime.webengine`
- 可通过 `--repo-url` 和 `--repo-branch` 覆盖

触发后使用 `--check` 轮询构建状态：

```bash
# 触发 runtime 构建
python3 scripts/linglong-update.py build-layer

# 触发 webengine 构建
python3 scripts/linglong-update.py build-layer --repo webengine

# 等待至少 2 分钟后查询状态（间隔至少 5 分钟）
python3 scripts/linglong-update.py build-layer --check --build-url https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/202/
```
> ⚠ 若仍在构建中，等 5 分钟后再查，不要短间隔反复查询。

### Step 5: N8N 推送 Layer

**输入**: Step 4 产出的 layer 构建 URL（`--layer-url`，脚本自动解析真实 layer 地址）

通过 N8N 表单推送 layer 到玲珑仓库。runtime 和 webengine 各执行一次推送（通过 `--repo` 参数切换，默认 `runtime`）。脚本提示用户手动提交 N8N 表单，确认后触发 `push-to-old` 和 `push-to-test` 两个 Jenkins job ，不等待构建完成。

- N8N 表单: https://n8n.cicd.getdeepin.org/form/097d0087-7f34-4614-8329-82d096af7ba5
- push-to-old: https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-push-to-old/
- push-to-test: https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-push-to-test/
- `--layer-url` 传入 **build-layer 产出的 Jenkins 构建 URL**（如 `https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/205/`），脚本自动从控制台输出解析真实 layer 地址后传入 push job
- `push-layer` 仅触发 push-to-old 和 push-to-test 两个 job，不等待构建完成

## 配置

配置文件位于 `~/.config/linglong-runtime-update/config.json`，支持自定义:

```json
{
  "crp_topic": "玲珑runtime dtk版本更新",
  "crp_branch": "upstream/master",
  "crp_branch_id": 129,
  "archs": ["amd64", "arm64", "loong64"],
  "runtime_repo_path": "~/.cache/linglong-runtime-update/repos/org.deepin.runtime",
  "webengine_repo_path": "~/.cache/linglong-runtime-update/repos/org.deepin.runtime.webengine",
  "fork_owner": null
}
```

- `crp_branch` 是 Git 分支过滤（传给 CRP 的筛选分支名），与 CRP 平台分支名（通过 BranchID `129` 映射到 `crimson-testing`）是不同概念
- Fork 推送目标可通过 `config` 配置 `fork_owner`，或通过 `--fork-owner` 指定；未配置时自动探测 `gh api user`
- Jenkins 凭证独立存储于 `~/.config/linglong-runtime-update/jenkins_creds.json`（base64 混淆，600 权限）
- webengine 补丁存放于 skill 的 `assets/webengine.patch`，脚本通过 `_find_webengine_patch()` 自动查找

## 缓存目录结构

```
~/.cache/linglong-runtime-update/
├── venv/                    # Python venv（需手动创建并安装依赖）
├── repos/
│   ├── org.deepin.runtime/          # runtime 仓库本地 clone
│   └── org.deepin.runtime.webengine/ # webengine 仓库本地 clone
```

Python venv 需手动创建并安装依赖，脚本不自动管理。Go 使用系统环境，脚本启动时检查 `go` 和 `ll-builder` 是否可用。

## 完整工作流

工作流严格串行，每步的输出是下一步的输入：

- **Step 2 输出** deb 仓库地址 → **Step 3 输入** `--deb-repo`
- **Step 3 产物** GitHub 仓库代码已更新（PR 合并后 main 分支为最新）→ **Step 4 隐含输入** Jenkins 从该仓库构建 layer
- **Step 4 输出** layer 构建产物 URL → **Step 5 输入** `--layer-url`

步骤 3-5 先对 runtime 仓库执行，再对 webengine 仓库执行：

```bash
# Step 1: CRP 打包
python3 scripts/linglong-update.py crp-pack --version 6.7.44
python3 scripts/linglong-update.py crp-pack --check

# Step 2: 制作更新仓库 → 输出 deb 仓库地址
python3 scripts/linglong-update.py build-repo
python3 scripts/linglong-update.py build-repo --check --build-url <Jenkins构建URL>
# 产出: http://10.20.64.92:8080/crimson_runtime/stable_xxx/

# Runtime 仓库 (Step 3-5)
# Step 3: 输入 deb 仓库地址 → 产物: GitHub 仓库代码已更新
python3 scripts/linglong-update.py update-repo --version 6.7.0.44 --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_xxx/
# Step 4: 隐含输入 Step 3 的代码 → 输出 layer 构建 URL
python3 scripts/linglong-update.py build-layer --repo runtime
python3 scripts/linglong-update.py build-layer --check --build-url <Jenkins构建URL>
# Step 5: 输入 Step 4 产出的 layer URL
python3 scripts/linglong-update.py push-layer --repo runtime --layer-url <build-layer产出的Jenkins URL>

# Webengine 仓库 (Step 3-5)
python3 scripts/linglong-update.py update-repo --version 6.7.0.44 --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_xxx/ --repo webengine
python3 scripts/linglong-update.py build-layer --repo webengine
python3 scripts/linglong-update.py build-layer --check --build-url <Jenkins构建URL>
python3 scripts/linglong-update.py push-layer --repo webengine --layer-url <build-layer产出的Jenkins URL>
```

> 版本号在不同阶段格式不同：CRP 打包用 DTK 版本 `6.7.44`，update-repo 阶段用玲珑版本 `6.7.0.44`。
>
> ⚠ 轮询间隔至少 5 分钟。若 `--check` 显示仍在进行中，等 5 分钟后再查，不要短间隔反复查询。

## 依赖

- Python 3.8+
- 需要 `gh` CLI 已认证
- CRP 认证通过外部 `crp_pack.py` 脚本（该脚本需要 `rsa` 和 `cryptography` 模块）
- `crp_pack.py` 使用 `Fernet` 加密缓存凭证到 `~/.config/uniontech-oa/`
- Python 依赖（`scripts/requirements.txt`）：`requests`、`cryptography`、`rsa`
- Go（系统已安装即可）
- `ll-builder`（`daily.bash` 内部调用）
- 网络代理需配置 `no_proxy` 包含 `.uniontech.com`、`.getdeepin.org`、`10.20.64.92`

## 详细参考

- [CRP 打包模块](references/crp-pack.md)
- [Jenkins 交互模块](references/jenkins.md)
- [仓库更新与 PR 模块](references/repo-update.md)
