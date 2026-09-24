# org.freedesktop.impl.portal.Notification 接口参考

该接口提供桌面通知发送和移除能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.impl.portal.desktop.dde` |
| Object path | `/org/freedesktop/portal/desktop` |
| Interface | `org.freedesktop.impl.portal.Notification` |
| Bus | Session |

### 通知方法

#### AddNotification

发送桌面通知。

- **输入参数**: `app_id`（string, 类型 `s`）：应用 ID；`id`（string, 类型 `s`）：通知 ID；`notification`（字典, 类型 `a{sv}`）：通知内容（包含 title、body、icon 等）
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Notification.AddNotification "app" "notif1" "{}"
```

#### RemoveNotification

移除桌面通知。

- **输入参数**: `app_id`（string, 类型 `s`）：应用 ID；`id`（string, 类型 `s`）：通知 ID
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Notification.RemoveNotification "app" "notif1"
```
