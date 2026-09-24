# org.deepin.dde.dock.plugin.shutdown

任务栏关机按钮插件配置资源，管理关机按钮右键菜单内容。

## 配置项

| Key | Name | Description | 类型 | Permissions | Visibility |
|---|---|---|---|---|---|
| `contextMenu` | 关机按钮右键菜单 | 关机按钮的右键菜单内容，如需不显示某个选项，移除即可 | array | readwrite | private |

默认值为 `["Shutdown", "Reboot", "Suspend", "Hibernate", "Lock", "Logout", "SwitchUser", "PowerSettings"]`。

## 读写示例

```bash
# 查询关机按钮右键菜单
dde-dconfig get -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.shutdown -k contextMenu
```

输出示例：

```
"[
    "Shutdown",
    "Reboot",
    "Suspend",
    "Hibernate",
    "Lock",
    "Logout",
    "SwitchUser",
    "PowerSettings"
]
"
```

```bash
# 设置关机按钮右键菜单（移除 Hibernate 选项）
dde-dconfig set -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.shutdown -k contextMenu -v "[\"Shutdown\", \"Reboot\", \"Suspend\", \"Lock\", \"Logout\", \"SwitchUser\", \"PowerSettings\"]"
```
