# org.deepin.dde.SessionWatcher1 接口参考

该接口提供会话状态监控能力，包括获取会话列表和检查 X11 会话是否活跃。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.SessionWatcher1` |
| Object path | `/org/deepin/dde/SessionWatcher1` |
| Interface | `org.deepin.dde.SessionWatcher1` |
| Bus | Session |

### 会话监控属性

#### IsActive（属性）

会话是否活跃。

| 属性 | 值 |
|------|------|
| 类型 | `b` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.SessionWatcher1 \
  --object-path /org/deepin/dde/SessionWatcher1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.SessionWatcher1 IsActive
```

### 会话监控方法

#### GetSessions

获取当前所有会话的对象路径列表。

- **输入参数**: 无
- **返回值**: `sessions`（`ao`，[]object_path）：会话对象路径列表

```bash
gdbus call --session \
  --dest org.deepin.dde.SessionWatcher1 \
  --object-path /org/deepin/dde/SessionWatcher1 \
  --method org.deepin.dde.SessionWatcher1.GetSessions
```

#### IsX11SessionActive

检查当前 X11 会话是否活跃。

- **输入参数**: 无
- **返回值**: `active`（bool, 类型 `b`）：X11 会话是否活跃

```bash
gdbus call --session \
  --dest org.deepin.dde.SessionWatcher1 \
  --object-path /org/deepin/dde/SessionWatcher1 \
  --method org.deepin.dde.SessionWatcher1.IsX11SessionActive
```
