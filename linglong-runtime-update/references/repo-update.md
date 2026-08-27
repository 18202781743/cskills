## 仓库更新与 PR 模块

修改 org.deepin.runtime、org.deepin.runtime.webengine 和 org.deepin.runtime.dtk5 的 `update.go`/`linglong.yaml`，
推送更新分支并创建 PR。`update-repo` 是本地 Git/GitHub 操作，没有 Jenkins 构建，
因此不支持 `update-repo --check`。

### 前置条件

- `gh` CLI 已认证（`gh auth status` 通过）
- 仓库若不存在本地，脚本自动 clone 到 `~/.cache/linglong-runtime-update/repos/`：
  - `https://github.com/linglongdev/org.deepin.runtime.git`
  - `https://github.com/linglongdev/org.deepin.runtime.webengine.git`
  - `https://github.com/linglongdev/org.deepin.runtime.dtk5.git`
- `gh` 和 `git clone/push/pull` 走系统代理，需确保 `https_proxy` 等环境变量已设置

### 版本号规则

从 config 的 `archs` 第一个架构匹配 dtkcore deb 包版本号，映射为玲珑 runtime 版本：

- DTK 版本 `X.Y.Z` → 玲珑 runtime 版本 `X.Y.0.Z`
- 示例：dtkcore `libdtk6core_6.7.44_amd64.deb` → 玲珑 runtime `6.7.0.44`
- 也可通过 `--version` 手动指定（如 `--version 6.7.0.44`）

### 更新流程

1. runtime 配置 `upstream=linglongdev`、`origin=<fork>`，从 `upstream/HEAD` 获取最新基线
2. 每次重建分支 `update/linglong-runtime`（固定分支名）
3. **webengine/dtk5**: `git am patches/<仓库名>/*.patch` 应用补丁（三路合并兜底，保留原始 commit 信息）
4. 修改 `update.go` 中的 `deepinRepoURL` 为新的 deb 仓库地址
5. 传递玲珑版本号给 `daily.bash` 脚本
6. `git add -A` → commit → 强推到 fork 的 `origin/update/linglong-runtime`
7. `gh pr create` 向 upstream 创建 PR（head 为 `<fork-owner>:update/linglong-runtime`）
8. 命令返回后手动检查 GitHub PR；没有 `--check` 子命令

### 命令示例

```bash
# runtime：版本号可显式传入
python3 scripts/linglong-update.py update-repo \
  --version 6.7.0.46 \
  --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_20260806/ \
  --fork-owner <GitHub用户名>

# webengine：使用 --repo 切换目标仓库
python3 scripts/linglong-update.py update-repo \
  --version 6.7.0.46 \
  --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_20260806/ \
  --repo webengine \
  --fork-owner <GitHub用户名>

# dtk5：使用 --repo 切换目标仓库
python3 scripts/linglong-update.py update-repo \
  --version 6.7.0.46 \
  --deb-repo http://10.20.64.92:8080/crimson_runtime/stable_20260806/ \
  --repo dtk5 \
  --fork-owner <GitHub用户名>
```

验证方式：检查命令返回码、git push 输出、fork 分支内容和 GitHub PR；PR 合并状态使用 GitHub 页面或 `gh pr view <编号> --repo linglongdev/org.deepin.runtime` 查询。

> `linglong.yaml` 的版本号和仓库 URL 不直接修改，由 `update.go`（读取 `deepinRepoURL`）和 `daily.bash`（接收玲珑版本号参数）自动生成。

### Fork 仓库（webengine / dtk5）

webengine 和 dtk5 仓库的更新流程与 runtime 不同：

1. 以 runtime 仓库本地副本为基准（通过 `runtime-base` remote 引用）
2. reset 到 runtime-base/HEAD
3. 应用 webengine 补丁（增加 QtWebEngine 支持）→ commit 1
4. 修改 `update.go` 中的 `deepinRepoURL`，传递玲珑版本号给 `daily.bash` → commit 2
5. 强推到 origin/main（**不创建 PR**）

#### Fork 仓库补丁

webengine/dtk5 仓库基础来自 org.deepin.runtime，额外需要应用补丁，增加
QtWebEngine 相关的环境变量和 package 依赖（dtk5 则是 Qt6 -> Qt5 切换）。

补丁存放在 runtime 仓库的 `patches/<仓库名>/` 目录下（如 `patches/org.deepin.runtime.webengine/`、`patches/org.deepin.runtime.dtk5/`），
脚本通过 `_find_repo_patches()` 自动查找该目录下的所有 `.patch` 文件。
补丁随 runtime 仓库一起维护，不再依赖 skill 内静态文件。

应用方式（对 webengine 和 dtk5 仓库）：
- 对目录下每个 `.patch` 文件，先 `git apply --check --reverse` 检查是否已应用
- 未应用则用 `git am <patch>` 应用（补丁包含 commit 信息，`git am` 自动创建 commit）
- 若失败则 `git am --abort` 后用 `git am --3way <patch>` 三路合并

### update.go 修改规则

**仓库地址**: 修改 `update.go` 中的 `deepinRepoURL` 变量。

脚本通过正则 `deepinRepoURL\s*=\s*("[^"]*"|`[^`]*`)` 匹配并替换。

**linglong.yaml**: 由 `update.go`（读取 `deepinRepoURL`）和 `daily.bash`（接收玲珑版本号参数）自动更新，脚本不直接修改 `linglong.yaml`。

### daily.bash 脚本

`daily.bash` 是仓库自带的脚本，根据 `linglong.yaml` 中的仓库地址
自动更新各 layer 的 yaml 配置。

### PR 创建

PR 标题: `chore: update linglong runtime to {version}`
PR body: 包含更新的 repo URL 和版本号
目标分支: `main`

### 注意事项

- `gh` 和 `git` 操作走系统代理（`https_proxy`），Jenkins/CRP 内网服务不走代理
- 如果 daily.bash 修改了额外文件，这些变更也会包含在 commit 中
- PR 合并等待默认超时 600 秒，可手动跳过等待
- git 提交使用当前用户身份（gh 配置的用户信息）
- 支持通过 `--repo webengine` 或 `--repo dtk5` 更新对应 fork 仓库
