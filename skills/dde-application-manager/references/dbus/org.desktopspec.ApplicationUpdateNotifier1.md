# org.desktopspec.ApplicationUpdateNotifier1 接口参考

该接口提供应用更新完成通知能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.desktopspec.ApplicationUpdateNotifier1` |
| Object path | `/org/desktopspec/ApplicationUpdateNotifier1` |
| Interface | `org.desktopspec.ApplicationUpdateNotifier1` |
| Bus | Session |

> **核验状态**：已通过源码 D-Bus 内省 XML（`apps/app-update-notifier/api/dbus/org.desktopspec.ApplicationUpdateNotifier1.xml`）核验，接口名称、对象路径、信号定义均与源码一致。

### 应用更新信号

#### ApplicationUpdated

应用更新完成时发出。

- **参数**: 无
- **触发条件**: 应用信息需要更新时发出

```bash
gdbus monitor --session \
  --dest org.desktopspec.ApplicationUpdateNotifier1 \
  --object-path /org/desktopspec/ApplicationUpdateNotifier1
```
