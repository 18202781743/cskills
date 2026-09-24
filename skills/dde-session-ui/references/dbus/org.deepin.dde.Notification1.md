# org.deepin.dde.Notification1 接口参考

该接口提供 DDE 通知扩展服务能力，包括通知发送、关闭、通知记录管理、应用通知设置管理、系统通知设置管理、通知中心显示控制等。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Notification1` |
| Object path | `/org/deepin/dde/Notification1` |
| Interface | `org.deepin.dde.Notification1` |
| Bus | Session |

### Notify

发送一条通知，返回通知 ID。

- **输入参数**:
  - `appName`（string, 类型 `s`）：应用名称
  - `id`（uint, 类型 `u`）：通知 ID（0 表示新通知）
  - `appIcon`（string, 类型 `s`）：应用图标名称
  - `summary`（string, 类型 `s`）：通知概要
  - `body`（string, 类型 `s`）：通知正文
  - `actions`（string array, 类型 `as`）：行为列表
  - `hints`（dict, 类型 `a{sv}`）：附加提示信息
  - `timeout`（int, 类型 `i`）：超时时间（毫秒，-1 表示不超时）
- **返回值**: `u`（uint）：通知 ID

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.Notify \
  "TestApp" 0 "dialog-information" "测试通知" "通知正文" [] {} 5000
```

### CloseNotification

根据通知 ID 关闭指定通知。

- **输入参数**: `id`（uint, 类型 `u`）：通知 ID
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.CloseNotification 1
```

### GetAllRecords

获取所有通知记录（JSON 字符串）。

- **输入参数**: 无
- **返回值**: `s`（string）：所有通知记录的 JSON 字符串

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetAllRecords
```

### GetRecordById

根据 ID 获取单条通知记录。

- **输入参数**: `id`（string, 类型 `s`）：通知记录 ID
- **返回值**: `s`（string）：通知记录的 JSON 字符串

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetRecordById "1"
```

### GetRecordsFromId

从指定 ID 开始获取通知记录。

- **输入参数**:
  - `count`（int, 类型 `i`）：获取数量
  - `id`（string, 类型 `s`）：起始记录 ID
- **返回值**: `s`（string）：通知记录的 JSON 字符串

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetRecordsFromId 10 "0"
```

### RemoveRecord

根据 ID 删除指定通知记录。

- **输入参数**: `id`（string, 类型 `s`）：通知记录 ID
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.RemoveRecord "1"
```

### ClearRecords

清除所有通知记录。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.ClearRecords
```

### GetAppList

获取已注册的通知应用列表。

- **输入参数**: 无
- **返回值**: `as`（string array）：应用名称列表

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetAppList
```

### GetAppInfo

获取指定应用的通知设置信息。

- **输入参数**:
  - `appName`（string, 类型 `s`）：应用名称
  - `infoType`（uint, 类型 `u`）：信息类型
- **返回值**: `v`（variant）：应用信息

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetAppInfo "TestApp" 0
```

### SetAppInfo

设置指定应用的通知配置。

- **输入参数**:
  - `appName`（string, 类型 `s`）：应用名称
  - `infoType`（uint, 类型 `u`）：信息类型
  - `value`（variant, 类型 `v`）：配置值
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.SetAppInfo "TestApp" 0 "<'true'>"
```

### GetSystemInfo

获取系统通知设置信息。

- **输入参数**: `infoType`（uint, 类型 `u`）：信息类型
- **返回值**: `v`（variant）：系统信息

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetSystemInfo 0
```

### SetSystemInfo

设置系统通知配置。

- **输入参数**:
  - `infoType`（uint, 类型 `u`）：信息类型
  - `value`（variant, 类型 `v`）：配置值
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.SetSystemInfo 0 "<'true'>"
```

### getAppSetting

获取应用通知设置（JSON 字符串）。

- **输入参数**: `appName`（string, 类型 `s`）：应用名称
- **返回值**: `s`（string）：应用设置的 JSON 字符串

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.getAppSetting "TestApp"
```

### setAppSetting

设置应用通知设置（JSON 字符串）。

- **输入参数**: `settings`（string, 类型 `s`）：应用设置的 JSON 字符串
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.setAppSetting '{"appName":"TestApp","allowNotify":true}'
```

### GetCapbilities

获取通知服务支持的能力列表。

- **输入参数**: 无
- **返回值**: `as`（string array）：能力列表

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetCapbilities
```

### GetServerInformation

获取通知服务信息。

- **输入参数**: 无
- **返回值**: `s`（string）：服务名称（另有三个 out 参数：厂商、版本、规范版本）

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.GetServerInformation
```

### Show

显示通知中心。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.Show
```

### Hide

隐藏通知中心。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.Hide
```

### Toggle

切换通知中心显示/隐藏状态。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.Toggle
```

### recordCount

获取通知记录数量。

- **输入参数**: 无
- **返回值**: `u`（uint）：记录数量

```bash
gdbus call --session \
  --dest org.deepin.dde.Notification1 \
  --object-path /org/deepin/dde/Notification1 \
  --method org.deepin.dde.Notification1.recordCount
```

### 属性

| 属性名 | 类型 | 读写 | 说明 |
|--------|------|------|------|
| `allSetting` | `s` | readwrite | 全部通知设置（JSON 字符串） |
| `systemSetting` | `s` | readwrite | 系统通知设置（JSON 字符串） |
| `recordCount` | `u` | read | 通知记录数量 |

### 信号

| 信号名 | 参数 | 说明 |
|--------|------|------|
| `ShowBubble` | 通知气泡信息 | 显示通知气泡 |
| `NotificationClosed` | `u, u` | 通知关闭 |
| `ActionInvoked` | `u, s` | 通知行为触发 |
| `RecordAdded` | `s` | 通知记录添加 |
| `AppInfoChanged` | `s, u, v` | 应用信息变更 |
| `SystemInfoChanged` | `u, v` | 系统信息变更 |
| `AppAddedSignal` | `s` | 应用添加 |
| `AppRemovedSignal` | `s` | 应用移除 |
| `recordCountChanged` | `u` | 记录数量变更 |
