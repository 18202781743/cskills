## Jenkins 交互模块

Jenkins 是内网服务。需配置 `no_proxy` 包含 `.uniontech.com`、`.getdeepin.org`、`10.20.64.92`，
使内网请求直连、外网请求（GitHub 等）走系统代理。

### 涉及 Job

| Job | 命令 | 参数 | URL |
|-----|------|------|-----|
| runtime-repo-update | build-repo, build-repo --check | `SUFFIX` (可选，有意义的标识如 test) | `/view/dtk/job/runtime-repo-update/` |
| linglong-runtime-build | build-layer, build-layer --check | `REPO_URL`, `REPO_BRANCH` | `/view/dtk/job/linglong-runtime-build/` |
| linglong-runtime-push-to-old | N8N → push-layer | `LAYER_URL`（由 N8N 工作流传给 job） | `/view/dtk/job/linglong-runtime-push-to-old/` |
| linglong-runtime-push-to-test | N8N → push-layer | `LAYER_URL`（由 N8N 工作流传给 job） | `/view/dtk/job/linglong-runtime-push-to-test/` |

### JenkinsClient API

```python
jc = JenkinsClient(user, password)

# 触发构建（带参数）
build_num = jc.trigger_build(job_path, {"REPO_URL": "github.com/..."})

# 获取当前构建状态
status = jc.get_build_status(job_path, build_num)
# => {"result": "SUCCESS", "building": False, "url": "...", "number": 123}

# 获取最近构建状态
status = jc.get_last_build_status(job_path)

# 获取控制台输出
console = jc.get_console_output(job_path, build_num)

# 获取构建趋势
builds = jc.get_build_trend(job_path)
```
> ⚠ 所有阶段触发后均不等待，由 agent 通过 `--check` 手动轮询，间隔至少 5 分钟。

### Job 参数说明

**runtime-repo-update**:
- `SUFFIX`: 仓库标识，可为空；若设置一般为有意义的标识（如 `test`），而非时间——日期已由 Jenkins 在生成仓库 URL 时体现
- `build-repo` 仅触发构建、不等待完成，使用 `build-repo --check --build-url <URL>` 轮询并提取仓库 URL
- `--check` 轮询间隔至少 5 分钟；若仍在构建中，等 5 分钟后再查

**linglong-runtime-build**:
- `REPO_URL`: 目标仓库地址（默认 `github.com/linglongdev/org.deepin.runtime`）
- `REPO_BRANCH`: 构建分支（默认 `main`）
- 通过 `--repo-url` 和 `--repo-branch` 覆盖
- `build-layer` 仅触发构建、不等待完成，使用 `build-layer --check --build-url <URL>` 轮询构建状态
- `--check` 轮询间隔至少 5 分钟；若仍在构建中，等 5 分钟后再查

**linglong-runtime-push-to-old / push-to-test**:
- 网页显示字段标签为 `job_url`，实际 multipart 字段名为 `field-0`，值是 `build-layer` 的 Jenkins 构建 URL
- N8N 工作流枚举构建 artifacts，并为每个 layer 触发对应 push job
- `push-layer --check` 查询具体 push job 构建 URL，不查询原始 build-layer URL

### 分阶段查询示例

```bash
# CRP：查询配置中的 topic/BranchID 下所有项目
python3 scripts/linglong-update.py crp-pack --check

# 更新仓库：传 runtime-repo-update 的构建 URL，成功后提取 deb 仓库地址
python3 scripts/linglong-update.py build-repo --check \
  --build-url https://jenkins.cicd.getdeepin.org/view/dtk/job/runtime-repo-update/19/

# Layer 构建：传 linglong-runtime-build 的构建 URL
python3 scripts/linglong-update.py build-layer --check \
  --build-url https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-build/214/

# Layer 推送：传 N8N 已触发的具体 push-to-test/push-to-old 构建 URL
python3 scripts/linglong-update.py push-layer --check \
  --layer-url https://jenkins.cicd.getdeepin.org/view/dtk/job/linglong-runtime-push-to-test/420/

# 最终验收：按 repo/version 检查 pools 测试仓库
python3 scripts/linglong-update.py push-layer --check \
  --repo runtime --version 6.7.0.46
python3 scripts/linglong-update.py push-layer --check \
  --repo webengine --version 6.7.0.46
```

最终验收 URL 分别为：

- `https://pools.uniontech.com/linglong/repos/test/refs/heads/main/org.deepin.runtime.dtk/<版本>/`
- `https://pools.uniontech.com/linglong/repos/test/refs/heads/main/org.deepin.runtime.webengine/<版本>/`

### 认证

首次使用 Jenkins 时交互式输入账号密码，base64 混淆后缓存到
`~/.config/linglong-runtime-update/jenkins_creds.json`（600 权限）。
首次运行交互输入用户名，可通过 `python3 linglong-update.py config` 重新配置。

### 网络

需配置 `no_proxy`/`NO_PROXY` 包含内网域名（`.uniontech.com`、`.getdeepin.org`、`10.20.64.92`），
`requests` 和 `git`/`gh` 均使用系统代理，内网域名绕过代理直连。
