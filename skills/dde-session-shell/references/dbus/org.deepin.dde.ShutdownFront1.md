# org.deepin.dde.ShutdownFront1 接口参考

该接口提供关机界面显示和电源操作能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.ShutdownFront1` |
| Object path | `/org/deepin/dde/ShutdownFront1` |
| Interface | `org.deepin.dde.ShutdownFront1` |
| Bus | Session |

## 兼容接口

在早期 Qt5 版本（v20）中，该接口使用旧版服务名 `com.deepin.dde.shutdownFront`（对象路径 `/com/deepin/dde/shutdownFront`）。当前 Qt6 版本已切换至 `org.deepin.dde.ShutdownFront1`，旧版服务名不再注册，仅供历史应用参考。

## 方法

### Show

显示关机界面。

- **功能**: 激活并显示关机界面，展示关机、重启、注销、锁屏、切换用户、挂起、休眠操作选项。
- **触发条件**: 由系统快捷键、会话管理或 DBus 调用方在需要显示关机界面时调用。
- **使用场景**: 用户按下电源键或通过系统菜单选择关机时触发。

```bash
gdbus call --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1 \
  --method org.deepin.dde.ShutdownFront1.Show
```

### Shutdown

关闭系统。

- **功能**: 执行系统关机操作。
- **触发条件**: 用户在关机界面选择关机时调用。
- **使用场景**: 用户确认关机操作后，系统执行关机流程。

```bash
gdbus call --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1 \
  --method org.deepin.dde.ShutdownFront1.Shutdown
```

### Restart

重启系统。

- **功能**: 执行系统重启操作。
- **触发条件**: 用户在关机界面选择重启时调用。
- **使用场景**: 用户确认重启操作后，系统执行重启流程。

```bash
gdbus call --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1 \
  --method org.deepin.dde.ShutdownFront1.Restart
```

### Logout

注销当前会话。

- **功能**: 注销当前登录用户的会话，返回登录界面。
- **触发条件**: 用户在关机界面选择注销时调用。
- **使用场景**: 用户需要退出当前会话但不关机时使用。

```bash
gdbus call --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1 \
  --method org.deepin.dde.ShutdownFront1.Logout
```

### Suspend

挂起系统。

- **功能**: 执行系统挂起（待机）操作。
- **触发条件**: 用户在关机界面选择挂起时调用。
- **使用场景**: 用户需要将系统进入待机状态以节省功耗时使用。

```bash
gdbus call --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1 \
  --method org.deepin.dde.ShutdownFront1.Suspend
```

### Hibernate

休眠系统。

- **功能**: 执行系统休眠（写入磁盘）操作。
- **触发条件**: 用户在关机界面选择休眠时调用。
- **使用场景**: 用户需要将系统状态保存到磁盘后关机，下次开机恢复状态时使用。

```bash
gdbus call --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1 \
  --method org.deepin.dde.ShutdownFront1.Hibernate
```

### SwitchUser

切换用户。

- **功能**: 切换到另一个用户账户，不注销当前用户会话。
- **触发条件**: 用户在关机界面选择切换用户时调用。
- **使用场景**: 多用户环境下，用户需要切换到另一个账户而不退出当前会话时使用。

```bash
gdbus call --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1 \
  --method org.deepin.dde.ShutdownFront1.SwitchUser
```

### Lock

锁屏。

- **功能**: 锁定当前屏幕，显示锁屏界面。
- **触发条件**: 用户在关机界面选择锁屏时调用。
- **使用场景**: 用户需要临时锁定屏幕以保护隐私时使用。

```bash
gdbus call --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1 \
  --method org.deepin.dde.ShutdownFront1.Lock
```

### UpdateAndShutdown

更新并关机。

- **功能**: 先执行系统更新，更新完成后关机。
- **触发条件**: 有待安装的系统更新时，用户选择更新并关机时调用。
- **使用场景**: 系统有更新包待安装时，用户在关机前选择同时执行更新。

```bash
gdbus call --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1 \
  --method org.deepin.dde.ShutdownFront1.UpdateAndShutdown
```

### UpdateAndReboot

更新并重启。

- **功能**: 先执行系统更新，更新完成后重启。
- **触发条件**: 有待安装的系统更新时，用户选择更新并重启时调用。
- **使用场景**: 系统有更新包待安装时，用户在重启前选择同时执行更新。

```bash
gdbus call --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1 \
  --method org.deepin.dde.ShutdownFront1.UpdateAndReboot
```

## 属性

### Visible

关机界面是否可见。

- **功能**: 表示当前关机界面是否处于可见状态。
- **类型**: `b`
- **读写权限**: read
- **使用场景**: 外部程序需要判断当前关机界面是否处于显示状态时读取此属性。

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.ShutdownFront1 Visible
```

## 信号

### ChangKey

按键变化信号。

- **参数**: `key`（string, 类型 `s`）：按键名称
- **触发条件**: 关机界面接收到按键事件时发出。
- **使用场景**: 外部程序需要监听关机界面的按键操作时订阅此信号。

```bash
gdbus monitor --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1
```

### Visible

可见性变化信号。

- **参数**: `visible`（bool, 类型 `b`）：是否可见
- **触发条件**: 关机界面显示或隐藏时发出。
- **使用场景**: 外部程序需要感知关机界面显示/隐藏状态变化时订阅此信号。

```bash
gdbus monitor --session \
  --dest org.deepin.dde.ShutdownFront1 \
  --object-path /org/deepin/dde/ShutdownFront1
```
