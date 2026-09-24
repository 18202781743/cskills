# org.deepin.dde.control-center.privacy

隐私配置资源，管理控制中心隐私设置中的权限黑名单。

## 配置项

| Key | Name | Description | 类型 | Permissions |
|---|---|---|---|---|
| `permissionBlacklist` | 权限黑名单 | 配置控制中心隐私设置中的权限黑名单 | string | readwrite |

## 读写示例

```bash
# 查询权限黑名单
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.privacy -k permissionBlacklist
# 设置权限黑名单
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.privacy -k permissionBlacklist -v "<value>"
```
