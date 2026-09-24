# org.deepin.dde.dock.plugin.notification

任务栏通知插件配置资源，管理通知未读状态。

## 配置项

| Key | Name | Description | 类型 | Permissions | Visibility |
|---|---|---|---|---|---|
| `hasUnreadNotification` | 是否有未读通知 | 控制任务栏通知图标是否显示未读通知状态 | bool | readwrite | private |

## 读写示例

```bash
# 查询是否有未读通知
dde-dconfig get -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.notification -k hasUnreadNotification
```

输出示例：

```
false
```

```bash
# 设置未读通知状态
dde-dconfig set -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.notification -k hasUnreadNotification -v "true"
```
