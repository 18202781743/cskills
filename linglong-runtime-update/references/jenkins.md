## Jenkins 交互模块

Jenkins 是内网服务，HTTP 请求不经过代理。脚本通过 `session.trust_env = False`
确保 Jenkins 和 CRP 请求直连内网，而 `gh`、`git clone/push` 仍走系统代理。

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

# 等待构建完成
ok = jc.wait_for_build(job_path, build_num, poll_interval=30, timeout=3600)

# 获取控制台输出
console = jc.get_console_output(job_path, build_num)

# 获取构建趋势
builds = jc.get_build_trend(job_path)
```

### Job 参数说明

**runtime-repo-update**:
- `SUFFIX`: 仓库标识，为空时使用日期 (YYYYMMDD)
- `build-repo` 仅触发构建、不等待完成，使用 `build-repo --check --build-url <URL>` 轮询并提取仓库 URL

**linglong-runtime-build**:
- `REPO_URL`: 目标仓库地址（默认 `github.com/linglongdev/org.deepin.runtime`）
- `REPO_BRANCH`: 构建分支（默认 `main`）
- 通过 `--repo-url` 和 `--repo-branch` 覆盖
- `build-layer` 仅触发构建、不等待完成，使用 `build-layer --check --build-url <URL>` 轮询构建状态

**linglong-runtime-push-to-old / push-to-test**:
- `LAYER_URL`: 构建产出的 layer 地址
- 由 N8N 表单流程触发，脚本在用户确认提交 N8N 后自动构建这两个 job

### 认证

首次使用 Jenkins 时交互式输入账号密码，base64 混淆后缓存到
`~/.config/linglong-runtime-update/jenkins_creds.json`（600 权限）。
首次运行交互输入用户名，可通过 `python3 linglong-update.py config` 重新配置。

### 网络

Jenkins 和 CRP 是内网服务，脚本设置 `trust_env=False` 直连。
GitHub 操作（`gh`、`git`）走系统代理（`https_proxy` 等环境变量）。
