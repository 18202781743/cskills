---
name: linglong-runtime-update
description: |
  DTK 玲珑 Runtime 更新自动化。当用户提到"玲珑 runtime 更新"、"linglong runtime"、"org.deepin.runtime 更新"、"玲珑 layer 构建"或需要执行玲珑相关的 CRP 打包、Jenkins 构建更新仓库、修改 linglong.yaml 并创建 PR、N8N 推送 layer 时使用此 skill。支持单步手动执行和 goal 自动执行。
---
# DTK 玲珑 Runtime 更新


自动化更新 org.deepin.runtime 和 org.deepin.runtime.webengine 三个玲珑 runtime 仓库（org.deepin.runtime、org.deepin.runtime.webengine、org.deepin.runtime.dtk5）的完整工作流。

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
- Python 3.8+ 及 `requests`、`cryptography`、`rsa` 模块
- Go 环境（`daily.bash` 内部 `go run update.go` 使用）
- `ll-builder`（`daily.bash` 内部调用 `ll-builder build`）
- `gh` CLI 已认证
- 网络代理需配置 `no_proxy=.uniontech.com,.getdeepin.org,10.20.64.92`（内网直连、外网走系统代理）

脚本启动时自动检查上述依赖，缺失会报错退出。

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

### 各阶段 `--check` 参数对照

各阶段的查询对象和 URL 参数不同，不能交叉使用：

| 阶段 | 查询命令 | 必需 URL/参数 | 查询结果 |
|------|----------|---------------|----------|
| CRP 打包 | `crp-pack --check` | `--topic`、`--branch-id`（默认从配置读取） | 各项目 CRP 实例状态，全部 `UPLOAD_OK` 才成功 |
| 更新仓库 | `build-repo --check --build-url <URL>` | `runtime-repo-update/<编号>/` 构建 URL | Jenkins 状态，成功后提取 deb 仓库 URL |
| 修改仓库/PR | 无 `update-repo --check` | `--version`、`--deb-repo`、可选 `--repo`/`--fork-owner` | 命令输出、git 推送结果和 GitHub PR |
| Layer 构建 | `build-layer --check --build-url <URL>` | `linglong-runtime-build/<编号>/` 构建 URL | Jenkins 状态；成功表示 layer artifacts 已生成 |
| Layer 推送 | `push-layer --check --layer-url <URL>` | `push-to-old/<编号>/` 或 `push-to-test/<编号>/` 构建 URL | 对应 push job 的 Jenkins 状态 |
| 最终验收 | `push-layer --check --repo <repo> --version <版本>` | repo 为 `runtime`/`webengine`/`dtk5`，版本为 `X.Y.0.Z` | pools 测试仓库中对应版本目录存在 |

`push-layer` 正常触发时的 `--layer-url` 与查询时不同：正常触发传入 **Layer 构建 URL**，由 N8N 表单枚举并推送全部 layer；`--check` 则传入某个具体 **push job 构建 URL**。

所有 Jenkins 构建首次查询前至少等待 2 分钟，后续查询间隔至少 5 分钟；CRP 打包首次查询前至少等待 5 分钟。

### Step 1: CRP 打包

在 CRP 平台上对 DTK 相关项目创建打包实例。调用外部 `crp_pack.py` 脚本（与 `linglong-update.py` 同目录），该脚本独立处理 CRP 认证和打包实例创建。

CRP 打包仍使用原有项目名（与 github-workflow-autotag 的 GitHub 仓库名不同）：`dtkcommon-v25`, `dtklog-v25`, `dtkcore-v25`, `dtkgui-v25`, `dtkwidget-v25`, `dtkdeclarative-v25`, `qt5integration-v25`, `qt5platform-plugins-v25`。

- **主题**: `玲珑runtime dtk版本更新`（可配置 `crp_topic`）
- **Git 分支过滤**: `upstream/master`（可配置 `crp_branch`，传给 CRP 的筛选分支名）
- **CRP BranchID**: `129`（可配置 `crp_branch_id`，对应 `crimson-testing` 平台分支）
- **架构**: `amd64, arm64, loong64`（可配置 `archs`，以分号 `;` 分隔传给 `crp_pack.py`）

支持通过 `--topic`、`--branch`、`--archs`（逗号分隔）、`--branch-id`、`--version` 命令行参数覆盖默认配置。

使用 `--check` 查询当前打包状态，显示每个项目的构建状态和版本信息，所有项目 `UPLOAD_OK` 才算成功。可用 `--topic`、`--branch-id` 指定查询范围：

```bash
python3 scripts/linglong-update.py crp-pack --check
python3 scripts/linglong-update.py crp-pack --check \
  --topic "玲珑runtime dtk版本更新" --branch-id 129
```
> ⚠ CRP 打包耗时较长，触发后至少等 5 分钟再 `--check`，若仍在进行中等 5 分钟后再查。

### Step 2: 制作更新仓库

触发 Jenkins job `runtime-repo-update` 制作更新仓库。`build-repo` 仅触发构建、不等待完成。

- Jenkins URL: https://jenkins.cicd.getdeepin.org/view/dtk/job/runtime-repo-update/
- Job 参数: `SUFFIX`（接收 `--repo-id` 传入的仓库标识，可为空。不要添加 `test` 这类无意义后缀：无特殊含义时留空，或使用 `auto` 表示由 skill/自动流程创建——日期已由 Jenkins 在生成仓库 URL 时体现）
- **输出**: deb 仓库地址（如 http://10.20.64.92:8080/crimson_runtime/stable_xxx/），作为 Step 3 的 `--deb-repo` 输入

触发后使用该构建的 Jenkins URL 查询，不能把 `repo-id` 当作 `--check` 参数：

```bash
# 触发构建（repo-id 默认 auto，勿用 test 之类无意义后缀；也可 --repo-id "" 留空）
python3 scripts/linglong-update.py build-repo

# 等待至少 2 分钟后查询状态，间隔至少 5 分钟，构建成功后自动提取仓库地址
python3 scripts/linglong-update.py build-repo --check --build-url https://jenkins.cicd.getdeepin.org/view/dtk/job/runtime-repo-update/19/
```
> ⚠ 若仍在构建中，等 5 分钟后再查，不要短间隔反复查询。

### Step 3: 修改仓库并创建 PR

`update-repo` 没有 Jenkins 构建，因此不提供 `--check`。它接收 Step 2 的 deb 仓库地址，更新 GitHub 仓库并输出提交/PR 结果。版本号使用玲珑格式 `X.Y.0.Z`；省略 `--version` 时，脚本从 `--deb-repo` 自动推断 DTK 版本并转换。

runtime 默认使用 fork 工作流：从 `upstream` 最新代码重建 `update/linglong-runtime`，推送到 fork，再向 `linglongdev/org.deepin.runtime` 创建或复用 PR。

**⚠ 顺序约束（重要）**：webengine / dtk5 必须在 **runtime PR 合并后** 再执行 `update-repo --repo webengine` / `--repo dtk5`。脚本在更新 webengine/dtk5 前会校验 `linglongdev/org.deepin.runtime` 的 `main` 分支 `linglong.yaml` 是否已是目标版本；未合并时会直接报错中止，防止 runtime 更新未就绪时 webengine / dtk5 先行推送造成不一致。运行时若报“runtime PR 尚未合并”，请先合并 runtime PR 再重试。

```bash
# runtime：版本明确时直接执行
python3 scripts/linglong-update.py update-repo \
  --version 6.7.0.46 \
  --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_20260806/ \
  --fork-owner <GitHub用户名>

# webengine：从同一 deb 仓库更新 webengine 配置
python3 scripts/linglong-update.py update-repo \
  --version 6.7.0.46 \
  --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_20260806/ \
  --repo webengine \
  --fork-owner <GitHub用户名>
```

验证该阶段请检查：命令返回成功、目标分支已推送、runtime 输出 PR URL；webengine 则检查 fork 分支和提交。PR 合并状态不由 `update-repo --check` 查询，应在 GitHub 页面或使用 `gh pr view` 检查。

#### 实现细节

**输入**: Step 2 产出的 deb 仓库地址（`--deb-repo`）  **产物**: GitHub 仓库代码已更新（runtime 创建 PR 并合并，webengine 强推 origin/main）

修改 org.deepin.runtime、org.deepin.runtime.webengine 和 org.deepin.runtime.dtk5 三个仓库的 `linglong.yaml`。两类仓库的更新流程不同：

**runtime 仓库**（默认）:
1. 配置 `origin=<用户 fork>`、`upstream=linglongdev`，fetch 官方 upstream 最新代码
2. 从 `upstream/HEAD` 强制重建固定分支 `update/linglong-runtime`
3. 修改 `update.go` 中的 `deepinRepoURL` 为新的 deb 仓库地址
4. 将玲珑版本号传递给 `daily.bash`，由 `update.go` + `daily.bash` 自动更新 `linglong.yaml`
5. 创建单个更新 commit，强推到 fork 的固定分支
6. 创建 PR 到 upstream（如 PR 已存在则复用）
7. PR 创建后返回，不等待合并；该阶段没有 `update-repo --check`，使用 GitHub 页面或 `gh pr view` 查询

> `linglong.yaml` 的版本号和仓库 URL 由 `update.go` 和 `daily.bash` 自动更新，脚本不直接修改 `linglong.yaml`。

**Fork 仓库**（`--repo webengine` / `--repo dtk5`）:
1. 先从官方 `upstream` 同步 runtime 本地缓存到最新默认分支
2. 以同步后的 runtime 仓库为基准（通过 `runtime-base` remote 引用），reset 到 `runtime-base/HEAD`
3. 从 runtime 仓库读取 `patches/<仓库名>/`（如 `patches/org.deepin.runtime.webengine/` 或 `patches/org.deepin.runtime.dtk5/`），用 `git am` 应用补丁（保留原始 commit 信息）→ commit 1；补丁缺失则停止
4. 修改 `update.go` 中的 `deepinRepoURL`，传递玲珑版本号给 `daily.bash` → commit 2
5. 强推到 origin/main（不创建 PR）

> fork 仓库的 commit 2 也由 `update.go` 和 `daily.bash` 自动生成，脚本不直接修改 `linglong.yaml`。

### Step 4: 构建玲珑 Layer

**隐含输入**: Step 3 已更新 GitHub 仓库代码（Jenkins 从该仓库拉取最新代码构建）  **输出**: layer 构建产物 URL

触发 Jenkins job `linglong-runtime-build` 制作玲珑 layer。与 Step 3 类似，runtime、webengine 和 dtk5 各触发一次构建（通过 `--repo` 参数切换，默认 `runtime`）。`build-layer` 仅触发构建、不等待完成。

- Jenkins URL: https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/
- 参数: `REPO_URL`（默认 `github.com/linglongdev/org.deepin.runtime`）、`REPO_BRANCH`（默认 `main`）
- webengine 时 REPO_URL 为 `github.com/linglongdev/org.deepin.runtime.webengine`
- dtk5 时 REPO_URL 为 `github.com/linglongdev/org.deepin.runtime.dtk5`
- 可通过 `--repo-url` 和 `--repo-branch` 覆盖

触发后使用 **Layer 构建 job** 的 URL 查询（不是 push job URL）：

```bash
# 触发 runtime 构建
python3 scripts/linglong-update.py build-layer

# 触发 webengine 构建

# 触发 dtk5 构建
python3 scripts/linglong-update.py build-layer --repo dtk5
python3 scripts/linglong-update.py build-layer --repo webengine

# 等待至少 2 分钟后查询状态（间隔至少 5 分钟）
python3 scripts/linglong-update.py build-layer --check --build-url https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/202/
```
> ⚠ 若仍在构建中，等 5 分钟后再查，不要短间隔反复查询。

### Step 5: N8N 推送 Layer

**输入**: Step 4 产出的 layer 构建 URL（`--layer-url`）

脚本按网页相同格式提交 N8N 表单（字段 `field-0`），由 N8N 枚举构建产物并批量触发 `push-to-old` 和 `push-to-test`。`--repo` 仅用于标识 runtime/webengine/dtk5，N8N 根据传入的 Layer 构建 URL 处理。

- N8N 表单: https://n8n.cicd.getdeepin.org/form/097d0087-7f34-4614-8329-82d096af7ba5
- push-to-old: https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-push-to-old/
- push-to-test: https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-push-to-test/
- `--layer-url` 传入 **build-layer 产出的 Jenkins 构建 URL**（如 `https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/205/`），不要手动改成 artifact URL
- `push-layer` 仅提交 N8N 表单，不等待全部 push job 完成
- 查询时传入 N8N 触发的具体 push 构建 URL，例如：

```bash
python3 scripts/linglong-update.py push-layer --check \
  --layer-url https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-push-to-test/420/
python3 scripts/linglong-update.py push-layer --check \
  --build-url https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-push-to-old/419/
```

全部 push job 完成后，以 pools 测试仓库中的版本目录作为整个流程的最终验收结果：

```bash
# runtime 最终结果
python3 scripts/linglong-update.py push-layer --check \
  --repo runtime --version 6.7.0.46
# 对应 https://pools.uniontech.com/linglong/repos/test/refs/heads/main/org.deepin.runtime.dtk/6.7.0.46/

# webengine 最终结果

# dtk5 最终结果
python3 scripts/linglong-update.py push-layer --check \
  --repo dtk5 --version 6.7.0.46
# 对应 https://pools.uniontech.com/linglong/repos/test/refs/heads/main/org.deepin.runtime.dtk5/6.7.0.46/
python3 scripts/linglong-update.py push-layer --check \
  --repo webengine --version 6.7.0.46
# 对应 https://pools.uniontech.com/linglong/repos/test/refs/heads/main/org.deepin.runtime.webengine/6.7.0.46/
```

三个 URL 均可访问时，runtime、webengine 与 dtk5 的构建、N8N 推送和测试仓库发布流程才算全部完成。

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
  "dtk5_repo_path": "~/.cache/linglong-runtime-update/repos/org.deepin.runtime.dtk5",
  "fork_owner": null
}
```

- `crp_branch` 是 Git 分支过滤（传给 CRP 的筛选分支名），与 CRP 平台分支名（通过 BranchID `129` 映射到 `crimson-testing`）是不同概念
- Fork 推送目标可通过 `config` 配置 `fork_owner`，或通过 `--fork-owner` 指定；未配置时自动探测 `gh api user`
- Jenkins 凭证独立存储于 `~/.config/linglong-runtime-update/jenkins_creds.json`（base64 混淆，600 权限）
- fork 仓库补丁存放于 runtime 仓库的 `patches/<仓库名>/` 目录（如 `patches/org.deepin.runtime.webengine/`、`patches/org.deepin.runtime.dtk5/`）；脚本会先同步 runtime 官方 `upstream`，再从 runtime 缓存中查找，缺失时停止更新

## 缓存目录结构

```
~/.cache/linglong-runtime-update/
├── repos/
│   ├── org.deepin.runtime/          # runtime 仓库本地 clone
│   └── org.deepin.runtime.webengine/ # webengine 仓库本地 clone
│   ├── org.deepin.runtime.dtk5/     # dtk5 仓库本地 clone
```

脚本启动时自动检查 `go`、`ll-builder`、`gh` 及 Python 模块依赖，缺失会报错退出。

## 完整工作流

工作流严格串行，每步的输出是下一步的输入：

- **Step 2 输出** deb 仓库地址 → **Step 3 输入** `--deb-repo`
- **Step 3 产物** GitHub 仓库代码已更新（PR 合并后 main 分支为最新）→ **Step 4 隐含输入** Jenkins 从该仓库构建 layer
- **Step 4 输出** layer 构建产物 URL → **Step 5 输入** `--layer-url`

步骤 3-5 先对 runtime 仓库执行，再依次对 webengine 和 dtk5 仓库执行。**注意**：runtime 的 PR 合并后（`gh pr view <编号> --repo linglongdev/org.deepin.runtime` 状态为 MERGED）才能继续更新 webengine / dtk5，脚本会自动校验并在未合并时中止：

```bash
# Step 1: CRP 打包
python3 scripts/linglong-update.py crp-pack --version 6.7.44
python3 scripts/linglong-update.py crp-pack --check

# Step 2: 制作更新仓库 → 输出 deb 仓库地址
python3 scripts/linglong-update.py build-repo
python3 scripts/linglong-update.py build-repo --check --build-url <Jenkins构建URL>
# 产出: http://10.20.64.92:8080/crimson_runtime/stable_xxx/

# Runtime 仓库 (Step 3-5)
# Step 3: 输入 deb 仓库地址 → 产物: GitHub 仓库代码已更新（生成 runtime PR，需先合并再继续）
python3 scripts/linglong-update.py update-repo --version 6.7.0.44 --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_xxx/
# 等待 runtime PR 合并: gh pr view <编号> --repo linglongdev/org.deepin.runtime --json state (MERGED 后再继续 webengine/dtk5)
# Step 4: 隐含输入 Step 3 的代码 → 输出 layer 构建 URL
python3 scripts/linglong-update.py build-layer --repo runtime
python3 scripts/linglong-update.py build-layer --check --build-url <Jenkins构建URL>
# Step 5: 输入 Step 4 产出的 layer URL
python3 scripts/linglong-update.py push-layer --repo runtime --layer-url <build-layer产出的Jenkins URL>

# Webengine 仓库 (Step 3-5) —— 需 runtime PR 已合并，脚本会自动校验
python3 scripts/linglong-update.py update-repo --version 6.7.0.44 --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_xxx/ --repo webengine
python3 scripts/linglong-update.py build-layer --repo webengine
python3 scripts/linglong-update.py build-layer --check --build-url <Jenkins构建URL>
python3 scripts/linglong-update.py push-layer --repo webengine --layer-url <build-layer产出的Jenkins URL>

# DTK5 仓库 (Step 3-5) —— 需 runtime PR 已合并，脚本会自动校验
python3 scripts/linglong-update.py update-repo --version 6.7.0.44 --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_xxx/ --repo dtk5
python3 scripts/linglong-update.py build-layer --repo dtk5
python3 scripts/linglong-update.py build-layer --check --build-url <Jenkins构建URL>
python3 scripts/linglong-update.py push-layer --repo dtk5 --layer-url <build-layer产出的Jenkins URL>
```

> 版本号在不同阶段格式不同：CRP 打包用 DTK 版本 `6.7.44`，update-repo 阶段用玲珑版本 `6.7.0.44`。
>
> ⚠ 轮询间隔至少 5 分钟。若 `--check` 显示仍在进行中，等 5 分钟后再查，不要短间隔反复查询。

## 依赖

- Python 3.8+ 及 `requests`、`cryptography`、`rsa` 模块
- Go（系统已安装）
- `ll-builder`、`gh` CLI
- CRP 认证通过外部 `crp_pack.py` 脚本（`Fernet` 加密缓存凭证到 `~/.config/uniontech-oa/`）
- 网络代理需配置 `no_proxy` 包含 `.uniontech.com`、`.getdeepin.org`、`10.20.64.92`

## 详细参考

- [CRP 打包模块](references/crp-pack.md)
- [Jenkins 交互模块](references/jenkins.md)
- [仓库更新与 PR 模块](references/repo-update.md)
