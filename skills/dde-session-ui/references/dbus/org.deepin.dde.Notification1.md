# org.deepin.dde.Notification1 接口参考

该接口提供 DDE 通知扩展服务能力，包括通知发送、关闭、通知记录管理、应用通知设置管理、系统通知设置管理、通知中心显示控制。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Notification1` |
| Object path | `/org/deepin/dde/Notification1` |
| Interface | `org.deepin.dde.Notification1` |
| Bus | Session |

### Notify

发送一条通知，返回通知 ID。

- **功能**: 向通知服务发送一条新通知或替换已有通知，通知服务收到后弹出气泡并记录到通知中心
- **触发条件**: 由应用主动调用以发送通知
- **使用场景**: 应用需要向用户展示即时消息提示，如收到新邮件、下载完成、日程提醒
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

- **功能**: 关闭指定 ID 的通知气泡和通知中心记录
- **触发条件**: 由应用主动调用以关闭自己发送的通知
- **使用场景**: 应用在通知条件消除后关闭已发送的通知，如错误已修复、操作已取消
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

- **功能**: 返回通知中心当前存储的所有通知记录
- **触发条件**: 由调用方主动调用以查询通知历史
- **使用场景**: 通知中心界面加载时获取全部通知记录以展示通知列表
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

- **功能**: 返回指定 ID 的通知记录详情
- **触发条件**: 由调用方主动调用以查询单条通知记录
- **使用场景**: 点击通知中心中的某条通知时获取该通知的详细信息
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

- **功能**: 从指定记录 ID 开始返回指定数量的通知记录，用于分页加载
- **触发条件**: 由调用方主动调用以分页查询通知记录
- **使用场景**: 通知中心界面滚动加载更多通知时获取下一页记录
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

- **功能**: 从通知中心删除指定 ID 的通知记录
- **触发条件**: 由调用方主动调用以删除单条通知记录
- **使用场景**: 用户在通知中心中清除某条通知
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

- **功能**: 清空通知中心中存储的全部通知记录
- **触发条件**: 由调用方主动调用以清空通知历史
- **使用场景**: 用户点击通知中心的「清除全部」按钮
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

- **功能**: 返回所有已在通知服务中注册的应用名称列表
- **触发条件**: 由调用方主动调用以查询已注册的通知应用
- **使用场景**: 通知设置界面加载时获取所有可配置通知的应用列表
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

- **功能**: 返回指定应用的某项通知设置值
- **触发条件**: 由调用方主动调用以查询应用通知设置
- **使用场景**: 通知设置界面展示某个应用的通知开关、声音、横幅状态
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

- **功能**: 修改指定应用的某项通知设置值
- **触发条件**: 由调用方主动调用以修改应用通知设置
- **使用场景**: 用户在通知设置界面切换某个应用的通知开关或修改通知声音
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

- **功能**: 返回系统级通知设置的某项值
- **触发条件**: 由调用方主动调用以查询系统通知设置
- **使用场景**: 通知设置界面加载时读取系统级通知开关状态（如勿扰模式）
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

- **功能**: 修改系统级通知设置的某项值
- **触发条件**: 由调用方主动调用以修改系统通知设置
- **使用场景**: 用户在通知设置界面开启或关闭勿扰模式、修改系统通知行为
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

- **功能**: 返回指定应用的完整通知设置 JSON
- **触发条件**: 由调用方主动调用以查询应用的全部通知设置
- **使用场景**: 通知设置界面加载某个应用的完整通知配置以填充界面
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

- **功能**: 批量修改指定应用的通知设置
- **触发条件**: 由调用方主动调用以批量更新应用通知配置
- **使用场景**: 通知设置界面保存某个应用的完整通知设置变更
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

- **功能**: 返回通知服务支持的通知能力列表（如 body、actions、persistence）
- **触发条件**: 由调用方主动调用以查询通知服务能力
- **使用场景**: 应用在发送通知前查询服务支持哪些能力以决定通知格式
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

- **功能**: 返回通知服务的名称、厂商、版本和规范版本信息
- **触发条件**: 由调用方主动调用以查询通知服务信息
- **使用场景**: 应用在连接通知服务前验证服务身份和版本兼容性
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

- **功能**: 弹出通知中心面板，展示通知记录列表
- **触发条件**: 由调用方主动调用以打开通知中心
- **使用场景**: 用户点击任务栏通知图标或使用快捷键打开通知中心
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

- **功能**: 关闭通知中心面板
- **触发条件**: 由调用方主动调用以关闭通知中心
- **使用场景**: 用户点击通知中心外部区域或使用快捷键关闭通知中心
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

- **功能**: 在通知中心的显示和隐藏状态之间切换
- **触发条件**: 由调用方主动调用以切换通知中心可见性
- **使用场景**: 用户点击任务栏通知图标切换通知中心的显示状态
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

- **功能**: 返回通知中心当前存储的通知记录数量
- **触发条件**: 由调用方主动调用以查询通知记录数量
- **使用场景**: 任务栏通知图标上显示未读通知数量角标
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
| `allSetting` | `s` | readwrite | 全部通知设置（JSON 字符串），包含所有应用和系统的通知设置；读取时返回完整设置 JSON，写入时批量更新全部设置 |
| `systemSetting` | `s` | readwrite | 系统通知设置（JSON 字符串），仅包含系统级通知设置；读取时返回系统设置 JSON，写入时更新系统设置 |
| `recordCount` | `u` | read | 通知记录数量，当通知记录增减时自动更新 |

### 信号

| 信号名 | 参数 | 说明 |
|--------|------|------|
| `ShowBubble` | 通知气泡信息 | 当新通知被发送且气泡需要弹出时触发；用于通知中心界面同步气泡显示状态 |
| `NotificationClosed` | `u, u` | 当通知被关闭时触发，参数为通知 ID 和关闭原因；用于调用方感知通知已关闭 |
| `ActionInvoked` | `u, s` | 当用户点击通知上的行为按钮时触发，参数为通知 ID 和行为名称；用于应用响应用户在通知上的交互 |
| `RecordAdded` | `s` | 当新通知记录被添加到通知中心时触发，参数为通知记录 JSON；用于通知中心界面实时更新通知列表 |
| `AppInfoChanged` | `s, u, v` | 当应用通知设置发生变更时触发，参数为应用名称、信息类型和新值；用于通知设置界面同步更新 |
| `SystemInfoChanged` | `u, v` | 当系统通知设置发生变更时触发，参数为信息类型和新值；用于通知设置界面同步更新 |
| `AppAddedSignal` | `s` | 当新应用首次注册到通知服务时触发，参数为应用名称；用于通知设置界面动态添加新应用条目 |
| `AppRemovedSignal` | `s` | 当应用从通知服务中移除时触发，参数为应用名称；用于通知设置界面动态移除应用条目 |
| `recordCountChanged` | `u` | 当通知记录数量发生变化时触发，参数为新的记录数量；用于任务栏通知图标角标更新 |

## 兼容性接口说明

通知相关 D-Bus 服务存在多个服务名，各接口关系如下：

- **扩充关系（扩充）**：`org.deepin.dde.Notification1`（对象路径 `/org/deepin/dde/Notification1`）是 DDE 扩展通知接口，在标准 freedesktop 通知接口功能基础上扩充了通知记录管理、应用通知设置管理、系统通知设置管理、通知中心显示控制能力。新代码应推荐使用此接口。
- **兼容关系（兼容）**：`org.freedesktop.Notifications`（对象路径 `/org/freedesktop/Notifications`）是标准 freedesktop 通知接口，与 `org.deepin.dde.Notification1` 指向同一通知对象，用于兼容遵循 freedesktop.org Notification 规范的第三方应用，使其无需修改即可在 DDE 环境中正常发送通知。
- **废弃关系（废弃）**：旧版服务名 `com.deepin.dde.Notification` 和 `com.deepin.dde.osd` 已废弃，由 `dde-api-dbus-proxy-v1` 代理转发以兼容旧调用方，不应在新代码中使用。

上述服务名可能与 dde-shell 注册的服务名冲突，实际运行时仅一个进程持有这些服务名。
