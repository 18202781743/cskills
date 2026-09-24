# org.deepin.dde.dock.plugin.interaction

任务栏插件交互行为配置资源，控制托盘加载器是否允许调用插件的激活、上下文菜单、悬浮提示接口。

## 配置项

| Key | Name | Description | 类型 | Permissions | Visibility |
|---|---|---|---|---|---|
| `itemActivationEnabled` | 允许激活插件项 | 是否允许托盘加载器调用此插件各插件项的 itemCommand 和 itemPopupApplet 接口 | bool | readwrite | private |
| `itemContextMenuEnabled` | 允许插件项上下文菜单 | 是否允许托盘加载器调用此插件各插件项的 itemContextMenu 接口，并显示任务栏提供的驻留或移除驻留菜单 | bool | readwrite | private |
| `itemTooltipEnabled` | 允许插件项悬浮提示 | 是否允许托盘加载器调用此插件各插件项的 itemTipsWidget 接口并显示悬浮提示 | bool | readwrite | private |

## 读写示例

```bash
# 查询是否允许激活插件项
dde-dconfig get -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.interaction -k itemActivationEnabled
```

输出示例：

```
true
```

```bash
# 禁用插件项上下文菜单
dde-dconfig set -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.interaction -k itemContextMenuEnabled -v "false"
```
