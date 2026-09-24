# org.desktopspec.JobManager1 接口参考

该接口提供应用启动任务跟踪能力。所有可能阻塞的方法会返回一个实现 `org.desktopspec.JobManager1.Job` 接口的对象路径，调用方可通过本接口的信号监听任务状态变化。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.desktopspec.JobManager1` |
| Object path | `/org/desktopspec/JobManager1` |
| Interface | `org.desktopspec.JobManager1` |
| Bus | Session |

> **核验状态**：已通过源码 D-Bus 内省 XML（`api/dbus/org.desktopspec.JobManager1.xml`）核验，接口名称、对象路径、信号定义均与源码一致。

### 任务信号

#### JobNew

新任务创建时发出。

- **参数**:
  - `job`（object path, 类型 `o`）：任务对象路径
  - `source`（object path, 类型 `o`）：产生该任务的 DBus 对象路径

监听示例：

```bash
gdbus monitor --session \
  --dest org.desktopspec.JobManager1 \
  --object-path /org/desktopspec/JobManager1
```

#### JobRemoved

任务完成移除时发出。

- **参数**:
  - `job`（object path, 类型 `o`）：任务对象路径
  - `status`（string, 类型 `s`）：任务最终状态，取值为 `started`、`running`、`finished`、`suspending`、`suspend`、`canceled`
  - `result`（数组, 类型 `av`）：任务结果，调用方需遍历列表判断值的有效性

监听示例：

```bash
gdbus monitor --session \
  --dest org.desktopspec.JobManager1 \
  --object-path /org/desktopspec/JobManager1
```
