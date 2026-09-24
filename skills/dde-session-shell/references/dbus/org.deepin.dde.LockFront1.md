# org.deepin.dde.LockFront1 接口参考

该接口提供锁屏界面显示、用户列表显示、认证状态控制和电源操作能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.LockFront1` |
| Object path | `/org/deepin/dde/LockFront1` |
| Interface | `org.deepin.dde.LockFront1` |
| Bus | Session |

## 兼容接口

在早期 Qt5 版本（v20）中，该接口使用旧版服务名 `com.deepin.dde.lockFront`（对象路径 `/com/deepin/dde/lockFront`）。当前 Qt6 版本已切换至 `org.deepin.dde.LockFront1`，旧版服务名不再注册，仅供历史应用参考。

## 方法

### Show

显示锁屏界面。

- **功能**: 激活并显示锁屏界面，覆盖当前桌面。
- **触发条件**: 由系统会话管理、快捷键或 DBus 调用方在需要锁定屏幕时调用。
- **使用场景**: 用户离开桌面、系统空闲超时或安全策略要求锁定时，由会话管理器自动调用。

```bash
gdbus call --session \
  --dest org.deepin.dde.LockFront1 \
  --object-path /org/deepin/dde/LockFront1 \
  --method org.deepin.dde.LockFront1.Show
```

### ShowUserList

显示用户列表。

- **功能**: 在锁屏界面上显示系统用户列表，供用户选择登录。
- **触发条件**: 由锁屏界面在需要展示用户切换选项时调用。
- **使用场景**: 多用户环境下，用户需要切换登录账户时。

```bash
gdbus call --session \
  --dest org.deepin.dde.LockFront1 \
  --object-path /org/deepin/dde/LockFront1 \
  --method org.deepin.dde.LockFront1.ShowUserList
```

### ShowAuth

显示认证界面。

- **功能**: 在锁屏界面上显示认证输入界面，接收用户密码或生物识别认证。
- **输入参数**: `active`（bool, 类型 `b`）：是否激活认证界面
- **触发条件**: 由锁屏界面在用户选择账户后需要输入密码时调用。
- **使用场景**: 用户在锁屏界面选择账户后，需要输入密码进行解锁认证时。

```bash
gdbus call --session \
  --dest org.deepin.dde.LockFront1 \
  --object-path /org/deepin/dde/LockFront1 \
  --method org.deepin.dde.LockFront1.ShowAuth true
```

### Suspend

挂起系统。

- **功能**: 触发系统挂起（待机），在挂起前确保锁屏界面已显示。
- **输入参数**: `enable`（bool, 类型 `b`）：是否启用挂起
- **触发条件**: 用户在锁屏界面选择挂起操作时调用。
- **使用场景**: 用户在锁屏界面点击「挂起」按钮时触发。

```bash
gdbus call --session \
  --dest org.deepin.dde.LockFront1 \
  --object-path /org/deepin/dde/LockFront1 \
  --method org.deepin.dde.LockFront1.Suspend true
```

### Hibernate

休眠系统。

- **功能**: 触发系统休眠（写入磁盘），在休眠前确保锁屏界面已显示。
- **输入参数**: `enable`（bool, 类型 `b`）：是否启用休眠
- **触发条件**: 用户在锁屏界面选择休眠操作时调用。
- **使用场景**: 用户在锁屏界面点击「休眠」按钮时触发。

```bash
gdbus call --session \
  --dest org.deepin.dde.LockFront1 \
  --object-path /org/deepin/dde/LockFront1 \
  --method org.deepin.dde.LockFront1.Hibernate true
```

## 属性

### Visible

锁屏界面是否可见。

- **功能**: 表示当前锁屏界面是否处于可见状态。
- **类型**: `b`
- **读写权限**: read
- **使用场景**: 外部程序需要判断当前是否处于锁屏状态时读取此属性。

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.LockFront1 \
  --object-path /org/deepin/dde/LockFront1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.LockFront1 Visible
```

## 信号

### ChangKey

按键变化信号。

- **参数**: `key`（string, 类型 `s`）：按键名称
- **触发条件**: 锁屏界面接收到按键事件时发出。
- **使用场景**: 外部程序需要监听锁屏界面的按键操作时订阅此信号。

```bash
gdbus monitor --session \
  --dest org.deepin.dde.LockFront1 \
  --object-path /org/deepin/dde/LockFront1
```

### Visible

可见性变化信号。

- **参数**: `visible`（bool, 类型 `b`）：是否可见
- **触发条件**: 锁屏界面显示或隐藏时发出。
- **使用场景**: 外部程序需要感知锁屏界面显示/隐藏状态变化时订阅此信号。

```bash
gdbus monitor --session \
  --dest org.deepin.dde.LockFront1 \
  --object-path /org/deepin/dde/LockFront1
```
