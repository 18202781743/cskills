# org.deepin.dde.control-center.passkey

安全密钥配置资源，管理控制中心中安全密钥模块的显示与隐藏。

## 配置项

| Key | Name | Description | 类型 | Permissions | Flags |
|---|---|---|---|---|---|
| `dccPasskeyPluginHideStatus` | 安全密钥模块显隐 | 控制控制中心中是否显示安全密钥模块，值为 true 时不显示，值为 false 时显示 | bool | readwrite | global |

## 读写示例

```bash
# 查询安全密钥模块显隐状态
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.passkey -k dccPasskeyPluginHideStatus
# 设置安全密钥模块显隐状态
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.passkey -k dccPasskeyPluginHideStatus -v "<value>"
```
