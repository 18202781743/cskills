# org.freedesktop.Notifications 接口参考

该接口实现 freedesktop.org 桌面通知规范，提供桌面通知的发送、关闭和能力查询功能。dde-shell 的 NotificationManager 在 Session 总线上注册此标准接口，与 `org.deepin.dde.Notification1` 共用同一对象实例。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.Notifications` |
| Object path | `/org/freedesktop/Notifications` |
| Interface | `org.freedesktop.Notifications` |
| Bus | Session |
## 通知接口兼容性

dde-shell 的通知服务由同一个通知对象注册了以下多个 D-Bus 服务接口，以兼容标准接口并提供 DDE 扩展功能：

- `org.freedesktop.Notifications`（`/org/freedesktop/Notifications`）— freedesktop 标准通知接口，提供通知发送、关闭和能力查询功能，供使用 freedesktop 通知规范的应用调用。
- `org.deepin.dde.Notification1`（`/org/deepin/dde/Notification1`）— DDE 扩展通知接口，是 `org.freedesktop.Notifications` 的超集，在标准通知功能基础上增加了应用通知管理、系统通知配置和通知记录管理功能。
- `org.deepin.dde.shell.notification.center` — 通知中心接口，提供通知中心的管理功能。
- `org.deepin.dde.Widgets1`（`/org/deepin/dde/Widgets1`）— 通知中心窗口控制接口，提供通知中心窗口的 Toggle/Show/Hide 控制。

`org.deepin.dde.Notification1` 与 `org.freedesktop.Notifications` 共用同一通知服务实现，前者是后者的超集。保留 `org.freedesktop.Notifications` 是为了兼容遵循 freedesktop 通知规范的应用，`org.deepin.dde.Notification1` 则在标准接口基础上提供 DDE 扩展的通知管理功能。

## 方法

### GetCapabilities

获取通知服务器支持的能力列表。

- **输入参数**: 无
- **返回值**: `as`（string 数组）：能力名称列表

```bash
gdbus call --session \
  --dest org.freedesktop.Notifications \
  --object-path /org/freedesktop/Notifications \
  --method org.freedesktop.Notifications.GetCapabilities
```

### Notify

发送桌面通知，或使用已有通知 ID 替换通知。

- **输入参数**:
  - `appName`（string, 类型 `s`）：应用名称
  - `replacesId`（uint, 类型 `u`）：要替换的通知 ID，`0` 表示创建新通知
  - `appIcon`（string, 类型 `s`）：应用图标路径或图标名称
  - `summary`（string, 类型 `s`）：通知标题
  - `body`（string, 类型 `s`）：通知正文
  - `actions`（string 数组, 类型 `as`）：动作键与动作标题组成的列表
  - `hints`（字典, 类型 `a{sv}`）：通知提示信息
  - `expireTimeout`（int32, 类型 `i`）：超时时间，单位为毫秒；`-1` 使用服务器默认值
- **返回值**: `u`（uint）：通知 ID

```bash
gdbus call --session \
  --dest org.freedesktop.Notifications \
  --object-path /org/freedesktop/Notifications \
  --method org.freedesktop.Notifications.Notify \
  "my-app" 0 "dialog-information" "通知标题" "通知正文" \
  "[]" "{}" 5000
```

### CloseNotification

关闭指定通知。

- **输入参数**:
  - `id`（uint, 类型 `u`）：通知 ID
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.freedesktop.Notifications \
  --object-path /org/freedesktop/Notifications \
  --method org.freedesktop.Notifications.CloseNotification 1
```

### GetServerInformation

获取通知服务器的名称、厂商、版本和所实现的通知规范版本。

- **输入参数**: 无
- **返回值**: `(ssss)`：服务器名称、厂商、版本、通知规范版本

```bash
gdbus call --session \
  --dest org.freedesktop.Notifications \
  --object-path /org/freedesktop/Notifications \
  --method org.freedesktop.Notifications.GetServerInformation
```

## 信号

### ActionInvoked

用户触发通知动作时发出。

- **参数**:
  - `id`（uint, 类型 `u`）：通知 ID
  - `actionKey`（string, 类型 `s`）：动作键

```bash
gdbus monitor --session \
  --dest org.freedesktop.Notifications \
  --object-path /org/freedesktop/Notifications
```

### NotificationClosed

通知关闭时发出。

- **参数**:
  - `id`（uint, 类型 `u`）：通知 ID
  - `reason`（uint, 类型 `u`）：关闭原因；`1` 表示过期，`2` 表示用户关闭，`3` 表示调用方关闭，`4` 表示原因未定义

```bash
gdbus monitor --session \
  --dest org.freedesktop.Notifications \
  --object-path /org/freedesktop/Notifications
```

---
