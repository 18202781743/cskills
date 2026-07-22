## Jenkins 交互模块

Jenkins 是内网服务，HTTP 请求不经过代理。脚本通过 `session.trust_env = False`
确保 Jenkins 和 CRP 请求直连内网，而 `gh`、`git clone/push` 仍走系统代理。

### 涉及 Job

| Job | 命令 | URL |
|-----|------|-----|
| runtime-repo-update | build-repo | `/view/dtk/job/runtime-repo-update/` |
| linglong-runtime-build | build-layer | `/view/dtk/job/linglong-runtime-build/` |
| linglong-runtime-push-to-old | push-layer | `/view/dtk/job/linglong-runtime-push-to-old/` |
| linglong-runtime-push-to-test | push-layer | `/view/dtk/job/linglong-runtime-push-to-test/` |

### JenkinsClient API

```python
jc = JenkinsClient(user, password)

# 触发构建（带参数）
build_num = jc.trigger_build(job_path, {"param": "20260721"})

# 获取构建状态
status = jc.get_build_status(job_path, build_num)
# => {"result": "SUCCESS", "building": False, "url": "...", "number": 123}

# 等待构建完成
ok = jc.wait_for_build(job_path, build_num, poll_interval=30, timeout=3600)

# 获取控制台输出
console = jc.get_console_output(job_path, build_num)

# 获取构建趋势
builds = jc.get_build_trend(job_path)
```

### Job 参数说明

**runtime-repo-update**:
- `param`: 仓库标识，为空时使用日期 (YYYYMMDD)
- 输出: 仓库 URL `http://10.20.64.92:8080/crimson_runtime/stable_YYYYMMDD/`

**linglong-runtime-build**:
- 无参数，自动从 main 分支取代码构建

**linglong-runtime-push-to-old / push-to-test**:
- 由 N8N 表单触发，不需要手动传参

### 认证

首次使用 Jenkins 时交互式输入账号密码，加密缓存到
`~/.config/linglong-update/jenkins_creds.json`（base64 混淆，600 权限）。
默认用户名 `yeshanshan`，可通过 `python3 linglong-update.py config` 修改。

### 网络

Jenkins 和 CRP 是内网服务，脚本设置 `trust_env=False` 直连。
GitHub 操作（`gh`、`git`）走系统代理（`https_proxy` 等环境变量）。
