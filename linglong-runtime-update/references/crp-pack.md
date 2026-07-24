## CRP 打包模块

在 CRP 平台创建打包实例，CRP 是内网服务（不经过代理）。

### 使用的 CRP 参数

- **主题名称**: `玲珑runtime dtk版本更新`
- **平台分支**: `crimson-testing` → 对应 CRP BranchID `129`（可通过 `--branch-id` 覆盖）
- **Git 分支过滤**: `upstream/master`（CRP 根据此分支筛选可选提交）
- **架构**: `amd64;arm64;loong64`（分号分隔，由 `crp_pack.py` 使用）

### DTK 打包项目列表

```
dtkcommon-v25, dtklog-v25, dtkcore-v25, dtkgui-v25, dtkwidget-v25,
dtkdeclarative-v25, qt5integration-v25, qt5platform-plugins-v25
```

与 github-workflow-autotag 的 DTK 项目列表保持一致。

### 认证

首次运行需要 OA/LDAP 账号密码，通过 RSA 公钥加密传输后用 Fernet 加密缓存到
`~/.config/uniontech-oa/default.json`。每次运行 `crp_pack.py` 时自动获取 Token。

### 打包原理

CRP 打包由外部 `crp_pack.py` 脚本独立完成。`linglong-update.py` 通过 `_run_crp()` 函数
调用该脚本（`subprocess.run`），自动清除代理环境变量确保直连内网。

`crp_pack.py` 内置完整的 CRP API 客户端，不依赖第三方 CRP SDK。

流程：搜索 topic → 搜索 project → 列出分支 → 删除已有实例 → 创建新打包实例。

### 注意事项

- 如果同一 topic 下已存在相同 project+branch 的 instance，先删除再创建
- 打包是异步的，脚本只负责提交，不等待 CRP 构建完成
- 需要 `rsa` 和 `cryptography` 模块（`pip install rsa cryptography`），如 RSA 不可用则降级为明文发送密码
- 代理环境变量（`https_proxy` 等）在调用 `crp_pack.py` 时自动清除，确保直连内网
