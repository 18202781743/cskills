## 仓库更新与 PR 模块

修改 org.deepin.runtime 和 org.deepin.runtime.webengine 的 linglong.yaml 文件，
创建 PR 并等待合并。

### 前置条件

- `gh` CLI 已认证（`gh auth status` 通过）
- 仓库若不存在本地，脚本自动 clone 到 `~/.cache/linglong-runtime-update/repos/`：
  - `https://github.com/linglongdev/org.deepin.runtime.git`
  - `https://github.com/linglongdev/org.deepin.runtime.webengine.git`
- `gh` 和 `git clone/push/pull` 走系统代理，需确保 `https_proxy` 等环境变量已设置

### 版本号规则

从 config 的 `archs` 第一个架构匹配 dtkcore deb 包版本号，映射为玲珑 runtime 版本：

- DTK 版本 `X.Y.Z` → 玲珑 runtime 版本 `X.Y.0.Z`
- 示例：dtkcore `libdtk6core_6.7.44_amd64.deb` → 玲珑 runtime `6.7.0.44`
- 也可通过 `--version` 手动指定（如 `--version 6.7.0.44`）

### 更新流程

1. `git fetch origin` → checkout main/master → reset to origin/HEAD
2. 创建/复用分支 `update/linglong-runtime`（固定分支名）
3. **webengine**: `git apply assets/webengine.patch` 应用补丁（三路合并兜底）
4. 修改 `update.go` 中的 `deepinRepoURL` 为新的 deb 仓库地址
5. 传递玲珑版本号给 `daily.bash` 脚本
6. `git add -A` → commit → push
7. `gh pr create` 创建 PR 到 fork 仓库（fork owner 可通过 `--fork-owner` 指定，默认探测 `gh api user`，回退到 `18202781743`）
8. 自动等待 PR 合并（默认超时 600s）

> `linglong.yaml` 的版本号和仓库 URL 不直接修改，由 `update.go`（读取 `deepinRepoURL`）和 `daily.bash`（接收玲珑版本号参数）自动生成。

### webengine 仓库

webengine 仓库的更新流程与 runtime 不同：

1. 以 runtime 仓库本地副本为基准（通过 `runtime-base` remote 引用）
2. reset 到 runtime-base/HEAD
3. 应用 webengine 补丁（增加 QtWebEngine 支持）→ commit 1
4. 修改 `update.go` 中的 `deepinRepoURL`，传递玲珑版本号给 `daily.bash` → commit 2
5. 强推到 origin/main（**不创建 PR**）

#### webengine 补丁

webengine 仓库基础来自 org.deepin.runtime，额外需要应用一个补丁，增加
QtWebEngine 相关的环境变量和 package 依赖。

补丁已静态保存在 skill 的 `assets/webengine.patch` 中，脚本通过
`_find_webengine_patch()` 自动查找。原始仓库提交历史可能被改写，因此
以静态 patch 文件形式保存，不依赖远程 cherry-pick。

应用方式（仅对 webengine 仓库）：
- 先尝试 `git apply <patch>`
- 若失败则尝试 `git apply --3way <patch>`（三路合并）

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
- 支持通过 `--repo webengine` 仅更新 webengine 仓库
