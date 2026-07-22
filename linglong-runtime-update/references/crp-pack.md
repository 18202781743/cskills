## CRP 打包模块

在 CRP 平台创建打包实例，CRP 是内网服务（不经过代理）。

### 使用的 CRP 参数

- **主题名称**: `玲珑runtime dtk版本更新`
- **平台分支**: `crimson-testing` (BranchID 通过配置指定，默认 123)
- **架构**: arm64, loong64, mips64, riscv64, sw64

### DTK 打包项目列表

```
dtkcommon, dtklog, dtkcore, dtkgui, dtkwidget,
dtkdeclarative, qt5integration, qt5platform-plugins
```

与 github-workflow-autotag 的 DTK 项目列表保持一致。

### 认证

首次运行需要 OA/LDAP 账号密码，加密缓存到
`~/.config/linglong-update/crp_creds.json`。

### 打包原理

脚本内置 CRP API 客户端（`_CRPClient`），直接调用 CRP REST API，
不依赖外部 `crp_pack.py`。Session 设置 `trust_env=False` 确保直连内网。

流程：搜索 topic → 搜索 project → 列出分支 → 删除已有实例 → 创建新打包实例。

### 注意事项

- 如果同一 topic 下已存在相同 project+branch 的 instance，先删除再创建
- 打包是异步的，脚本只负责提交，不等待 CRP 构建完成
- 需要 `rsa` 模块（`pip install rsa`），如不可用则降级为明文发送密码
