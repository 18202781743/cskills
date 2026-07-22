## 仓库更新与 PR 模块

修改 org.deepin.runtime 和 org.deepin.runtime.webengine 的 linglong.yaml 文件，
创建 PR 并等待合并。

### 前置条件

- `gh` CLI 已认证（`gh auth status` 通过）
- 仓库若不存在本地，脚本自动 clone 到 `~/.cache/linglong-update/repos/`：
  - `https://github.com/linuxdeepin/org.deepin.runtime.git`
  - `https://github.com/linuxdeepin/org.deepin.runtime.webengine.git`
- `gh` 和 `git clone/push/pull` 走系统代理，需确保 `https_proxy` 等环境变量已设置

### 版本号规则

版本号跟随 DTK 版本，格式为 `X.Y.0.Z`：

- 前两位 `X.Y` 对应 DTK 主版本和次版本
- 第三位固定为 `0`
- 第四位 `Z` 对应 DTK 补丁版本号

例如 DTK `6.7.46` → 玲珑 runtime `6.7.0.46`。

也可通过 `--version` 手动指定。

### 更新流程

1. `git fetch origin` → checkout main/master → pull
2. 创建分支 `update/linglong-runtime-{version}-{timestamp}`
3. **webengine**: `git apply assets/webengine.patch` 应用补丁
4. 修改 `linglong.yaml` 中的 `version:` 和仓库 URL
5. 执行 `daily.bash` 脚本更新 layer 对应的仓库地址
6. `git add -A` → commit → push
7. `gh pr create` 创建 PR
8. 轮询等待 PR 合并（可选）

### webengine 补丁

webengine 仓库基础来自 org.deepin.runtime，额外需要应用一个补丁，增加
QtWebEngine 相关的环境变量和 package 依赖。

补丁已静态保存在 skill 的 `assets/webengine.patch` 中，脚本通过
`_find_webengine_patch()` 自动查找。原始仓库提交历史可能被改写，因此
以静态 patch 文件形式保存，不依赖远程 cherry-pick。

应用方式（仅对 webengine 仓库）：
- 先尝试 `git apply <patch>`
- 若失败则尝试 `git apply --3way <patch>`（三路合并）

### linglong.yaml 修改规则

**版本号**: 正则匹配 `version:\s*\S+`，替换为指定版本。

**仓库 URL**: 正则匹配 `http://10.20.64.92:8080/crimson_runtime/stable_[^\s"']+/`，
替换为 build-repo 生成的新 URL。

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
