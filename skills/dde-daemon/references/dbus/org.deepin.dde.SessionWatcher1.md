# org.deepin.dde.SessionWatcher1 接口参考

该接口提供会话状态监控能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.SessionWatcher1` |
| Object path | `/org/deepin/dde/SessionWatcher1` |
| Interface | `org.deepin.dde.SessionWatcher1` |
| Bus | Session |
### 会话监控属性

#### Locked（属性）

会话是否锁定。

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
  org.deepin.dde.SessionWatcher1 Locked
```

### 会话监控信号

#### Unlock

会话解锁时发出。

- **参数**: 无
- **触发条件**: 会话解锁时发出

```bash
gdbus monitor --session \
  --dest org.deepin.dde.SessionWatcher1 \
  --object-path /org/deepin/dde/SessionWatcher1
```

