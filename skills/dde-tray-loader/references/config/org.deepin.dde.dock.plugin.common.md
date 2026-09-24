# org.deepin.dde.dock.plugin.common

任务栏插件公共配置资源，管理默认驻留在任务栏上的插件列表和插件排序。

## 配置项

| Key | Name | Description | 类型 | Permissions | Visibility |
|---|---|---|---|---|---|
| `defaultDockedPlugins` | 默认驻留任务栏插件 | 配置默认驻留在任务栏上的插件列表，仅控制初始默认状态，重启后生效 | array | readonly | public |
| `pluginsOrder` | 任务栏插件顺序 | 任务栏运行时的插件排列顺序，2-普通插件区域，3-固定区域（最左侧），7-工具插件区域（最右边） | string | readwrite | private |

## 读写示例

```bash
# 查询默认驻留插件列表
dde-dconfig get -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.common -k defaultDockedPlugins
```

输出示例：

```
"[
    "multitasking",
    "show-desktop",
    "battery",
    "shutdown",
    "datetime"
]
"
```

```bash
# 查询任务栏插件顺序
dde-dconfig get -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.common -k pluginsOrder
```

输出示例：

```
"{"2": ["dde-tray", "network-item-key", "dde-quick-panel", "AiAssistant", "notifications", "power", "shutdown"], "3": [ "show-desktop", "multitasking" ], "7": [ "datetime", "trash" ] }"
```
