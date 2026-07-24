## Jenkins 交互模块

Jenkins 是内网服务，HTTP 请求不经过代理。脚本通过 `session.trust_env = False`
确保 Jenkins 和 CRP 请求直连内网，而 `gh`、`git clone/push` 仍走系统代理。

### 请求频率约束

Jenkins/CRP/N8N 请求响应缓慢（5-30 秒/次），严格遵守：

- 触发构建后至少等 **2 分钟** 再 `--check`，CRP 打包至少等 **5 分钟**
- 除非用户明确要求，不主动查询非当前步骤的状态
- 轮询间隔至少 **5 分钟**（300 秒）：`--check` 等所有主动查询
- 一次 `--check` 显示仍在进行中 → 等 5 分钟后再查，不要短间隔反复查询
- `auto` / goal 模式下可循环轮询等待构建完成，但每次间隔至少 5 分钟

### 涉及 Job

| Job | 命令 | 参数 | URL |
|-----|------|------|-----|
| runtime-repo-update | build-repo, build-repo --check | `SUFFIX` (可选，默认日期) | `/view/dtk/job/runtime-repo-update/` |
| linglong-runtime-build | build-layer, build-layer --check | `REPO_URL`, `REPO_BRANCH` | `/view/dtk/job/linglong-runtime-build/` |
| linglong-runtime-push-to-old | push-layer | `LAYER_URL` | `/view/dtk/job/linglong-runtime-push-to-old/` |
| linglong-runtime-push-to-test | push-layer | `LAYER_URL` | `/view/dtk/job/linglong-runtime-push-to-test/` |

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
- `SUFFIX`: 仓库标识，为空时使用日期 (YYYYMMDD)
- `build-repo` 仅触发构建、不等待完成，使用 `build-repo --check --build-url <URL>` 轮询并提取仓库 URL
- `--check` 轮询间隔至少 5 分钟；若仍在构建中，等 5 分钟后再查

**linglong-runtime-build**:
- `REPO_URL`: 目标仓库地址（默认 `github.com/linglongdev/org.deepin.runtime`）
- `REPO_BRANCH`: 构建分支（默认 `main`）
- 通过 `--repo-url` 和 `--repo-branch` 覆盖
- `build-layer` 仅触发构建、不等待完成，使用 `build-layer --check --build-url <URL>` 轮询构建状态
- `--check` 轮询间隔至少 5 分钟；若仍在构建中，等 5 分钟后再查

**linglong-runtime-push-to-old / push-to-test**:
- `LAYER_URL`: 构建产出的 layer 地址
- 由 N8N 表单流程触发，脚本在用户确认提交 N8N 后触发这两个 job，不等待构建完成

### 认证

首次使用 Jenkins 时交互式输入账号密码，base64 混淆后缓存到
`~/.config/linglong-runtime-update/jenkins_creds.json`（600 权限）。
首次运行交互输入用户名，可通过 `python3 linglong-update.py config` 重新配置。

### 网络

Jenkins 和 CRP 是内网服务，脚本设置 `trust_env=False` 直连。
GitHub 操作（`gh`、`git`）走系统代理（`https_proxy` 等环境变量）。
