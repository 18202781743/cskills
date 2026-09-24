# org.kde.StatusNotifierWatcher 接口参考

该接口提供系统托盘状态通知管理能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.kde.StatusNotifierWatcher` |
| Object path | `/org/kde/StatusNotifierWatcher` |
| Interface | `org.kde.StatusNotifierWatcher` |
| Bus | Session |
### 托盘监控属性

#### RegisteredStatusNotifierItems（属性）

已注册的状态通知项列表。

- **功能**：已注册的状态通知项列表。
- **触发条件**：属性，当有新的通知项注册或注销时通过 PropertiesChanged 信号通知。
- **使用场景**：系统托盘初始化时获取已有通知项列表。

| 属性 | 值 |
|------|------|
| 类型 | `as` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.kde.StatusNotifierWatcher \
  --object-path /org/kde/StatusNotifierWatcher \
  --method org.freedesktop.DBus.Properties.Get \
  org.kde.StatusNotifierWatcher RegisteredStatusNotifierItems
```
#### IsStatusNotifierHostRegistered（属性）

是否有状态通知宿主注册。

- **功能**：是否有状态通知宿主已注册。
- **触发条件**：属性，当宿主注册或注销时通过 PropertiesChanged 信号通知。
- **使用场景**：通知项应用检查是否有可用的系统托盘宿主。

| 属性 | 值 |
|------|------|
| 类型 | `b` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.kde.StatusNotifierWatcher \
  --object-path /org/kde/StatusNotifierWatcher \
  --method org.freedesktop.DBus.Properties.Get \
  org.kde.StatusNotifierWatcher IsStatusNotifierHostRegistered
```

### 托盘监控信号

#### StatusNotifierItemRegistered

状态通知项注册时发出。

- **功能**：状态通知项注册时发出。
- **触发条件**：当新的 StatusNotifierItem 应用注册到系统托盘时发出。
- **使用场景**：系统托盘监听此信号以更新托盘图标列表。

- **参数**: `itemId`（string, 类型 `s`）：项 ID

```bash
gdbus monitor --session \
  --dest org.kde.StatusNotifierWatcher \
  --object-path /org/kde/StatusNotifierWatcher
```

#### StatusNotifierItemUnregistered

状态通知项注销时发出。

- **功能**：状态通知项注销时发出。
- **触发条件**：当已注册的 StatusNotifierItem 应用从系统托盘注销时发出。
- **使用场景**：系统托盘监听此信号以移除对应的托盘图标。

- **参数**: `itemId`（string, 类型 `s`）：项 ID

```bash
gdbus monitor --session \
  --dest org.kde.StatusNotifierWatcher \
  --object-path /org/kde/StatusNotifierWatcher
```


## 兼容性接口

`org.kde.StatusNotifierWatcher` 是 KDE 标准系统托盘状态通知接口，由 `trayicon1/` 模块在 `org.deepin.dde.TrayManager1` 服务上注册，兼容遵循 KDE StatusNotifierItem 协议的应用程序。
