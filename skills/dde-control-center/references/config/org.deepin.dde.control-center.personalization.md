# org.deepin.dde.control-center.personalization

个性化配置资源，管理控制中心个性化设置中的图标主题隐藏、标题栏高度、紧凑模式与滚动条策略配置。

## 配置项

| Key | Name | Description | 类型 | Permissions | Flags |
|---|---|---|---|---|---|
| `hideIconThemes` | 隐藏图标主题 | 配置需要在个性化设置中隐藏的图标主题列表 | array | readonly | global |
| `titleBarHeightStatus` | 标题栏高度状态 | 配置控制中心个性化设置中标题栏高度的显示状态 | string | readwrite | |
| `titleBarHeightSupportCompactDisplay` | 标题栏高度紧凑模式联动 | 配置标题栏高度是否与紧凑模式联动 | bool | readwrite | |
| `scrollbarPolicyStatus` | 滚动条显示策略状态 | 配置控制中心个性化设置中滚动条显示策略的状态 | string | readwrite | |
| `compactDisplayStatus` | 紧凑模式状态 | 配置控制中心个性化设置中紧凑模式的状态 | string | readwrite | |

## 读写示例

```bash
# 查询隐藏图标主题
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.personalization -k hideIconThemes

# 查询标题栏高度状态
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.personalization -k titleBarHeightStatus
# 设置标题栏高度状态
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.personalization -k titleBarHeightStatus -v "<value>"

# 查询标题栏高度紧凑模式联动
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.personalization -k titleBarHeightSupportCompactDisplay
# 设置标题栏高度紧凑模式联动
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.personalization -k titleBarHeightSupportCompactDisplay -v "<value>"

# 查询滚动条显示策略状态
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.personalization -k scrollbarPolicyStatus
# 设置滚动条显示策略状态
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.personalization -k scrollbarPolicyStatus -v "<value>"

# 查询紧凑模式状态
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.personalization -k compactDisplayStatus
# 设置紧凑模式状态
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.personalization -k compactDisplayStatus -v "<value>"
```
