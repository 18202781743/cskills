# org.deepin.dde.LastoreSessionHelper1 接口参考

该接口提供应用商店会话辅助能力，包括磁盘空间检查、系统代理获取、通知发送、通知关闭和日志上报。该服务在系统总线上导出两个对象：`Lastore` 和 `Agent`。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.LastoreSessionHelper1` |
| Object path | `/org/deepin/dde/LastoreSessionHelper1` |
| Interface | `org.deepin.dde.LastoreSessionHelper1` |
| Bus | System |

### Lastore 对象方法

#### IsDiskSpaceSufficient

检查磁盘空间是否充足。

- **输入参数**: 无
- **返回值**: `result`（bool, 类型 `b`）：磁盘空间是否充足

```bash
gdbus call --system \
  --dest org.deepin.dde.LastoreSessionHelper1 \
  --object-path /org/deepin/dde/LastoreSessionHelper1 \
  --method org.deepin.dde.LastoreSessionHelper1.IsDiskSpaceSufficient
```

### Agent 对象方法

Agent 对象导出在相同的系统总线服务下，对象路径为 `/org/deepin/dde/Lastore1/Agent`，接口为 `org.deepin.dde.Lastore1.Agent`。

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.LastoreSessionHelper1` |
| Object path | `/org/deepin/dde/Lastore1/Agent` |
| Interface | `org.deepin.dde.Lastore1.Agent` |
| Bus | System |

#### GetManualProxy

获取手动配置的系统代理信息。

- **输入参数**: 无
- **返回值**: `outArg0`（`a{ss}`，map[string]string）：代理信息，键为代理类型（`http`、`https`、`ftp`、`socks`），值为代理地址

```bash
gdbus call --system \
  --dest org.deepin.dde.LastoreSessionHelper1 \
  --object-path /org/deepin/dde/Lastore1/Agent \
  --method org.deepin.dde.Lastore1.Agent.GetManualProxy
```

#### SendNotify

发送桌面通知。

- **输入参数**:
  - `appName`（string, 类型 `s`）：应用名称
  - `replacesId`（uint32, 类型 `u`）：替换的通知 ID，`0` 表示新通知
  - `appIcon`（string, 类型 `s`）：应用图标
  - `summary`（string, 类型 `s`）：通知摘要
  - `body`（string, 类型 `s`）：通知正文
  - `actions`（`as`，[]string）：通知动作列表
  - `hints`（`a{sv}`，map[string]dbus.Variant）：通知提示信息
  - `expireTimeout`（int32, 类型 `i`）：过期超时时间（毫秒），`-1` 表示默认，`0` 表示不自动隐藏
- **返回值**: `outArg0`（uint32, 类型 `u`）：通知 ID

```bash
gdbus call --system \
  --dest org.deepin.dde.LastoreSessionHelper1 \
  --object-path /org/deepin/dde/Lastore1/Agent \
  --method org.deepin.dde.Lastore1.Agent.SendNotify \
  "appName" 0 "icon" "summary" "body" "[]" "{}" -1
```

#### CloseNotification

关闭指定通知。

- **输入参数**: `id`（uint32, 类型 `u`）：通知 ID
- **返回值**: 无

```bash
gdbus call --system \
  --dest org.deepin.dde.LastoreSessionHelper1 \
  --object-path /org/deepin/dde/Lastore1/Agent \
  --method org.deepin.dde.Lastore1.Agent.CloseNotification 1
```

#### ReportLog

上报日志信息。

- **输入参数**: `msg`（string, 类型 `s`）：日志消息
- **返回值**: 无

```bash
gdbus call --system \
  --dest org.deepin.dde.LastoreSessionHelper1 \
  --object-path /org/deepin/dde/Lastore1/Agent \
  --method org.deepin.dde.Lastore1.Agent.ReportLog "log message"
```
