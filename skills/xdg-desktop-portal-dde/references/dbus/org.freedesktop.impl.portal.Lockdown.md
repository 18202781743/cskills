# org.freedesktop.impl.portal.Lockdown 接口参考

该接口提供锁定模式设置能力。通过读写属性来控制各项锁定功能。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.impl.portal.desktop.dde` |
| Object path | `/org/freedesktop/portal/desktop` |
| Interface | `org.freedesktop.impl.portal.Lockdown` |
| Bus | Session |

### 属性

所有属性均为 `b`（bool）类型，可读可写。

| 属性名 | 类型 | 权限 | 说明 |
|--------|------|------|------|
| `disable_printing` | `b` | readwrite | 禁止打印 |
| `disable_save_to_disk` | `b` | readwrite | 禁止保存到磁盘 |
| `disable_application_handlers` | `b` | readwrite | 禁止应用处理器 |
| `disable_location` | `b` | readwrite | 禁止定位 |
| `disable_camera` | `b` | readwrite | 禁止摄像头 |
| `disable_microphone` | `b` | readwrite | 禁止麦克风 |
| `disable_sound_output` | `b` | readwrite | 禁止声音输出 |

### 使用示例

#### 读取所有锁定属性

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.DBus.Properties.GetAll "org.freedesktop.impl.portal.Lockdown"
```

#### 读取单个锁定属性

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.DBus.Properties.Get "org.freedesktop.impl.portal.Lockdown" "disable_printing"
```

#### 设置锁定属性

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.DBus.Properties.Set "org.freedesktop.impl.portal.Lockdown" "disable_printing" "<true>"
```
