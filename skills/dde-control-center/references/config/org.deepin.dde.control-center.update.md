# org.deepin.dde.control-center.update

更新配置资源，管理控制中心更新设置中安全更新、自动安装、第三方源、P2P 更新、更新历史记录、日志地址与版本号显示的配置。

## 配置项

| Key | Name | Description | 类型 | Permissions | Flags |
|---|---|---|---|---|---|
| `updateSafety` | 安全更新 | 配置控制中心更新设置中安全更新的显示状态 | string | readwrite | |
| `updateAutoInstall` | 自动安装 | 配置控制中心更新设置中自动安装的显示状态 | string | readwrite | |
| `updateThirdPartySource` | 第三方源 | 配置控制中心更新设置中第三方源的显示状态 | string | readwrite | global |
| `p2pUpdateEnabled` | P2P 更新 | 配置控制中心更新设置中 P2P 更新的显示状态 | string | readwrite | global |
| `updateHistoryEnabled` | 更新历史记录 | 配置控制中心更新设置中更新历史记录的显示状态 | string | readwrite | |
| `updateLogAddress` | 更新日志地址 | 配置控制中心更新设置的更新日志 API 地址 | string | readonly | global |
| `showVersion` | 版本号显示 | 配置控制中心更新设置中版本号的显示方式 | string | readwrite | global |

## 读写示例

```bash
# 查询安全更新显示状态
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.update -k updateSafety
# 设置安全更新显示状态
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.update -k updateSafety -v "<value>"

# 查询自动安装显示状态
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.update -k updateAutoInstall
# 设置自动安装显示状态
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.update -k updateAutoInstall -v "<value>"

# 查询更新日志地址
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.update -k updateLogAddress

# 查询版本号显示方式
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.update -k showVersion
# 设置版本号显示方式
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.update -k showVersion -v "<value>"
```
