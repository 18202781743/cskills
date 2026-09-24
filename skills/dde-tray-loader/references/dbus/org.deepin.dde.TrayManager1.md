# org.deepin.dde.TrayManager1 接口参考

该接口提供托盘图标管理和通知控制能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.TrayManager1` |
| Object path | `/org/deepin/dde/TrayManager1` |
| Interface | `org.deepin.dde.TrayManager1` |
| Bus | Session |
### 托盘操作

#### EnableNotification

启用或禁用指定窗口的通知。

- **功能**: 控制指定托盘窗口是否允许发送桌面通知
- **输入参数**: `win`（uint32, 类型 `u`）：窗口 ID；`enabled`（bool, 类型 `b`）：是否启用
- **返回值**: 无
- **触发条件**: 当用户或应用程序需要控制特定托盘应用的通知行为时调用
- **使用场景**: 当用户希望屏蔽某个托盘应用的通知弹窗时使用

```bash
gdbus call --session \
  --dest org.deepin.dde.TrayManager1 \
  --object-path /org/deepin/dde/TrayManager1 \
  --method org.deepin.dde.TrayManager1.EnableNotification 12345 true
```

#### GetName

获取指定窗口的名称。

- **功能**: 查询托盘中指定窗口 ID 对应的应用名称
- **输入参数**: `win`（uint32, 类型 `u`）：窗口 ID
- **返回值**: `s`（string）：窗口名称
- **触发条件**: 当需要获取某个托盘图标的显示名称时调用
- **使用场景**: 当需要在 UI 中显示托盘图标对应的应用名称时使用

```bash
gdbus call --session \
  --dest org.deepin.dde.TrayManager1 \
  --object-path /org/deepin/dde/TrayManager1 \
  --method org.deepin.dde.TrayManager1.GetName 12345
```

#### Manage

打开托盘管理界面。

- **功能**: 打开托盘图标管理界面，允许用户查看和管理当前托盘中的应用
- **输入参数**: 无
- **返回值**: `b`（bool）：是否成功
- **触发条件**: 当用户需要进入托盘管理界面时调用
- **使用场景**: 当用户需要查看托盘中的应用列表或调整托盘设置时使用

```bash
gdbus call --session \
  --dest org.deepin.dde.TrayManager1 \
  --object-path /org/deepin/dde/TrayManager1 \
  --method org.deepin.dde.TrayManager1.Manage
```
### 托盘属性

#### TrayIcons（属性）

当前托盘图标列表。

| 属性 | 值 |
|------|------|
| 类型 | `au` |
| 读写权限 | read |

- **功能**: 返回当前所有已注册的托盘图标窗口 ID 列表
- **触发条件**: 读取该属性时返回当前快照
- **使用场景**: 当需要获取当前托盘中所有图标的窗口 ID 列表时使用

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.TrayManager1 \
  --object-path /org/deepin/dde/TrayManager1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.TrayManager1 TrayIcons
```

### 托盘信号

#### Inited

托盘初始化完成时发出。

- **功能**: 通知托盘管理器已完成初始化，可以接受托盘图标注册
- **参数**: 无
- **触发条件**: 托盘管理器初始化完成时发出
- **使用场景**: 当需要在托盘初始化完成后执行后续操作（如注册新的托盘图标）时监听此信号

```bash
gdbus monitor --session \
  --dest org.deepin.dde.TrayManager1 \
  --object-path /org/deepin/dde/TrayManager1
```

#### Added

托盘图标添加时发出。

- **功能**: 通知有新的托盘图标被添加到托盘中
- **参数**: `id`（uint32, 类型 `u`）：窗口 ID
- **触发条件**: 有新窗口添加到托盘时发出
- **使用场景**: 当需要监听新托盘图标出现并做出响应（如更新 UI 显示）时使用

```bash
gdbus monitor --session \
  --dest org.deepin.dde.TrayManager1 \
  --object-path /org/deepin/dde/TrayManager1
```

#### Removed

托盘图标移除时发出。

- **功能**: 通知有托盘图标从托盘中被移除
- **参数**: `id`（uint32, 类型 `u`）：窗口 ID
- **触发条件**: 托盘图标被移除时发出
- **使用场景**: 当需要监听托盘图标消失并做出响应（如更新 UI 显示）时使用

```bash
gdbus monitor --session \
  --dest org.deepin.dde.TrayManager1 \
  --object-path /org/deepin/dde/TrayManager1
```

#### Changed

托盘图标变化时发出。

- **功能**: 通知某个托盘图标的属性或状态发生变化
- **参数**: `id`（uint32, 类型 `u`）：窗口 ID
- **触发条件**: 托盘图标属性变化时发出（如图标更新、窗口状态改变）
- **使用场景**: 当需要监听托盘图标变化并刷新对应图标的显示时使用

```bash
gdbus monitor --session \
  --dest org.deepin.dde.TrayManager1 \
  --object-path /org/deepin/dde/TrayManager1
```

---
