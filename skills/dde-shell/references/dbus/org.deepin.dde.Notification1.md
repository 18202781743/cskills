# org.deepin.dde.Notification1 接口参考

该接口完整提供桌面通知能力，并扩展应用通知配置、系统通知配置和通知记录状态查询。可用于查询通知能力、发送和关闭通知、查询通知服务器信息、管理应用与系统通知配置、读取通知记录数量，以及监听通知与配置变化。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Notification1` |
| Object path | `/org/deepin/dde/Notification1` |
| Interface | `org.deepin.dde.Notification1` |
| Bus | Session |

## 兼容性接口

dde-shell 的通知服务注册了以下 D-Bus 服务接口，以兼容 freedesktop 标准通知规范并提供 DDE 扩展功能：

- `org.freedesktop.Notifications`（`/org/freedesktop/Notifications`）— freedesktop 标准通知接口，是 `org.deepin.dde.Notification1` 的子集，仅提供通知发送（`Notify`）、关闭（`CloseNotification`）、能力查询（`GetCapabilities`）和服务器信息查询（`GetServerInformation`）功能。保留此接口是为了兼容遵循 freedesktop 通知规范的应用。

`org.deepin.dde.Notification1`（`/org/deepin/dde/Notification1`）是 `org.freedesktop.Notifications` 的超集，在标准通知功能基础上增加了应用通知管理、系统通知配置和通知记录管理功能。两个接口共用同一通知服务实现。

> 注意：`org.deepin.dde.shell.notification.center` 是独立的通知中心面板接口，不属于本接口的兼容范围，详见 [org.deepin.dde.shell.notification.center](org.deepin.dde.shell.notification.center.md)。

## 方法、属性与信号

### 桌面通知操作

#### GetCapabilities

获取通知服务器支持的能力列表。

- **输入参数**: 无
- **返回值**: `as`（string 数组）：能力名称列表

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetCapabilities
```

#### Notify

发送桌面通知，或使用已有通知 ID 替换通知。

- **输入参数**:
  - `appName`（string, 类型 `s`）：应用名称
  - `replacesId`（uint, 类型 `u`）：要替换的通知 ID，`0` 表示创建通知
  - `appIcon`（string, 类型 `s`）：应用图标路径或图标名称
  - `summary`（string, 类型 `s`）：通知标题
  - `body`（string, 类型 `s`）：通知正文
  - `actions`（string 数组, 类型 `as`）：动作键与动作标题组成的列表
  - `hints`（字典, 类型 `a{sv}`）：通知提示信息
  - `expireTimeout`（int32, 类型 `i`）：超时时间，单位为毫秒；`-1` 使用服务器默认值
- **返回值**: `u`（uint）：通知 ID

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.Notify \
  "my-app" 0 "dialog-information" "通知标题" "通知正文" \
  "['open', '打开']" "{}" 5000
```

#### CloseNotification

关闭指定通知。

- **输入参数**:
  - `id`（uint, 类型 `u`）：通知 ID
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.CloseNotification 1
```

#### GetServerInformation

获取通知服务器的名称、厂商、版本和所实现的通知规范版本。

- **输入参数**: 无
- **返回值**: `(ssss)`：服务器名称、厂商、版本、通知规范版本

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetServerInformation
```

### 应用通知配置

#### GetAppList

获取已注册通知的应用列表。

- **输入参数**: 无
- **返回值**: `as`（string 数组）：应用 ID 列表

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetAppList
```

#### GetAppInfo

获取指定应用的通知配置项。

- **输入参数**:
  - `appId`（string, 类型 `s`）：应用 ID
  - `configItem`（uint, 类型 `u`）：配置项编号
- **返回值**: `v`（variant）：配置值

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetAppInfo "my-app" 0
```

#### SetAppInfo

设置指定应用的通知配置项。

- **输入参数**:
  - `appId`（string, 类型 `s`）：应用 ID
  - `configItem`（uint, 类型 `u`）：配置项编号
  - `value`（variant, 类型 `v`）：新值
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.SetAppInfo \
  "my-app" 0 "<true>"
```

#### GetAppSetting

获取指定应用的通知设置 JSON。

- **输入参数**:
  - `appName`（string, 类型 `s`）：应用名称
- **返回值**: `s`（string）：通知设置 JSON 字符串

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetAppSetting "my-app"
```

#### SetAppSetting

设置应用通知设置。

- **输入参数**:
  - `settings`（string, 类型 `s`）：通知设置 JSON 字符串
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.SetAppSetting '"{\"app\":\"my-app\",\"enabled\":true}"'
```

### 系统通知配置

#### SetSystemInfo

设置系统级通知配置项。

- **输入参数**:
  - `configItem`（uint, 类型 `u`）：配置项编号
  - `value`（variant, 类型 `v`）：新值
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.SetSystemInfo 0 "<true>"
```

#### GetSystemInfo

获取系统级通知配置项。

- **输入参数**:
  - `configItem`（uint, 类型 `u`）：配置项编号
- **返回值**: `v`（variant）：配置值

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetSystemInfo 0
```

### 通知记录状态

#### recordCount（属性）

当前通知记录数量。

| 属性 | 值 |
|------|------|
| 类型 | `u`（uint） |
| 读写权限 | read |

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.freedesktop.DBus.Properties.Get \
  "org.deepin.dde.Notification1" "recordCount"
```

### 通知事件信号

#### ActionInvoked

用户触发通知动作时发出。

- **触发条件**: 用户点击通知上的动作按钮时触发
- **参数**:
  - `id`（uint, 类型 `u`）：通知 ID
  - `actionKey`（string, 类型 `s`）：动作键

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1
```

#### NotificationClosed

通知关闭时发出。

- **触发条件**: 通知过期、用户手动关闭、调用 CloseNotification 时触发
- **参数**:
  - `id`（uint, 类型 `u`）：通知 ID
  - `reason`（uint, 类型 `u`）：关闭原因；`1` 表示过期，`2` 表示用户关闭，`3` 表示调用方关闭，`4` 表示原因未定义

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1
```

#### ActivationToken

通知激活并产生激活令牌时发出。

- **触发条件**: 通知被点击激活且系统提供 xdg-activation token 时触发
- **参数**:
  - `id`（uint, 类型 `u`）：通知 ID
  - `token`（string, 类型 `s`）：激活令牌

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1
```

### 配置与状态变化信号

#### AppAdded

新应用注册通知时发出。

- **参数**:
  - `appId`（string, 类型 `s`）：应用 ID
- **触发条件**: 有新应用首次发送通知时发出

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1
```

#### AppRemoved

应用被移除时发出。

- **参数**:
  - `appId`（string, 类型 `s`）：应用 ID
- **触发条件**: 应用被从通知列表中移除时发出

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1
```

#### AppInfoChanged

应用通知配置变化时发出。

- **参数**:
  - `appId`（string, 类型 `s`）：应用 ID
  - `configItem`（uint, 类型 `u`）：配置项编号
  - `value`（variant, 类型 `v`）：新值
- **触发条件**: 调用 `SetAppInfo` 后发出

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1
```

#### AppSettingChanged

> ⚠️ **当前未实现**：已声明但从未 emit，当前不会触发。

应用通知设置变化时发出。

- **参数**:
  - `settings`（string, 类型 `s`）：设置 JSON 字符串

#### SystemSettingChanged

> ⚠️ **当前未实现**：已声明但从未 emit，当前不会触发。

系统通知设置变化时发出。

- **参数**:
  - `settings`（string, 类型 `s`）：设置 JSON 字符串

#### SystemInfoChanged

系统级通知配置变化时发出。

- **参数**:
  - `configItem`（uint, 类型 `u`）：配置项编号
  - `value`（variant, 类型 `v`）：新值
- **触发条件**: 调用 `SetSystemInfo` 后发出

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1
```

#### NotificationStateChanged

通知处理状态变化时发出。

- **参数**:
  - `id`（int64, 类型 `x`）：通知 ID
  - `processedType`（int32, 类型 `i`）：处理类型
- **触发条件**: 通知被处理（显示、关闭）时发出

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1
```

#### RecordCountChanged

通知记录数量变化时发出。

- **参数**:
  - `count`（uint, 类型 `u`）：新的记录数量
- **触发条件**: 通知记录增加或减少时发出

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1
```

---
