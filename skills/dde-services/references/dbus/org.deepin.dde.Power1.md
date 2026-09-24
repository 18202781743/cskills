# org.deepin.dde.Power1 接口参考

该接口提供电源管理能力，包括电源状态查询、延时配置和电源操作。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Power1` |
| Object path | `/org/deepin/dde/Power1` |
| Interface | `org.deepin.dde.Power1` |
| Bus | Session |

### 电源操作

#### Reset

重置电源配置为默认值。

- **功能**：将所有电源管理配置恢复为系统默认值
- **输入参数**：无
- **返回值**：无
- **使用场景**：用户在控制中心点击「恢复默认」电源设置时调用

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.deepin.dde.Power1.Reset
```

#### SetPrepareSuspend

设置挂起准备状态。

- **功能**：通知电源管理服务系统即将进入挂起状态，以便服务执行挂起前的准备工作
- **输入参数**：`state`（int32, 类型 `i`）：状态
- **返回值**：无
- **使用场景**：系统在执行挂起操作前由电源管理模块调用

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.deepin.dde.Power1.SetPrepareSuspend 1
```

### 电源状态属性

#### OnBattery（属性）

是否使用电池供电。

- **功能**：指示当前设备是否处于电池供电状态（未接入交流电源）
- **触发条件**：电源接入状态发生变化时更新
- **使用场景**：UI 根据供电状态显示不同的电源配置选项

| 属性 | 值 |
|------|------|
| 类型 | `b` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 OnBattery
```

#### UseWayland（属性）

是否使用 Wayland。

- **功能**：指示当前会话是否使用 Wayland 显示协议
- **触发条件**：会话启动时确定，运行期间保持不变
- **使用场景**：电源管理模块根据显示协议类型选择不同的电源行为

| 属性 | 值 |
|------|------|
| 类型 | `b` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 UseWayland
```

#### LidIsPresent（属性）

是否存在翻盖。

- **功能**：指示当前设备是否具备翻盖（笔记本电脑盖子）硬件
- **触发条件**：硬件探测完成时确定，设备未变更时保持不变
- **使用场景**：UI 根据设备类型决定是否显示翻盖关闭动作设置项

| 属性 | 值 |
|------|------|
| 类型 | `b` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 LidIsPresent
```

#### BatteryIsPresent（属性）

电池是否存在。

- **功能**：以映射形式返回各电池槽位的存在状态
- **触发条件**：电池热插拔时更新
- **使用场景**：UI 判断设备是否有电池以决定是否显示电池相关设置

| 属性 | 值 |
|------|------|
| 类型 | `map` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 BatteryIsPresent
```

#### BatteryPercentage（属性）

电池百分比。

- **功能**：以映射形式返回各电池的剩余电量百分比
- **触发条件**：电池电量变化时更新
- **使用场景**：UI 显示电池电量百分比

| 属性 | 值 |
|------|------|
| 类型 | `map` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 BatteryPercentage
```

#### BatteryState（属性）

电池状态。

- **功能**：以映射形式返回各电池的当前状态（充电、放电、已充满）
- **触发条件**：电池充放电状态变化时更新
- **使用场景**：UI 显示电池充电状态图标和提示信息

| 属性 | 值 |
|------|------|
| 类型 | `map` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 BatteryState
```

#### HasAmbientLightSensor（属性）

是否有环境光传感器。

- **功能**：指示当前设备是否具备环境光传感器硬件
- **触发条件**：硬件探测完成时确定，设备未变更时保持不变
- **使用场景**：UI 根据设备是否支持自动亮度来显示或隐藏相关设置项

| 属性 | 值 |
|------|------|
| 类型 | `b` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 HasAmbientLightSensor
```

#### WarnLevel（属性）

电量警告级别。

- **功能**：返回当前电池电量的警告级别，用于触发低电量通知或自动休眠
- **触发条件**：电池电量变化达到警告级别阈值时更新
- **使用场景**：系统根据警告级别执行低电量通知或自动休眠操作

| 属性 | 值 |
|------|------|
| 类型 | `u` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 WarnLevel
```

#### IsHighPerformanceSupported（属性）

是否支持高性能模式。

- **功能**：指示当前设备是否支持高性能电源模式
- **触发条件**：硬件探测完成时确定，设备未变更时保持不变
- **使用场景**：UI 根据设备是否支持高性能模式来显示或隐藏该模式选项

| 属性 | 值 |
|------|------|
| 类型 | `b` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 IsHighPerformanceSupported
```

### 交流电源延时配置

#### LinePowerScreensaverDelay（属性）

交流电源屏保延时。

- **功能**：设置交流电源下激活屏保的空闲等待时间（秒）
- **使用场景**：用户在控制中心设置交流电源下的屏保延时时间

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 LinePowerScreensaverDelay
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 LinePowerScreensaverDelay <int32 600>
```

#### LinePowerScreenBlackDelay（属性）

交流电源息屏延时。

- **功能**：设置交流电源下关闭屏幕的空闲等待时间（秒）
- **使用场景**：用户在控制中心设置交流电源下的息屏延时时间

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 LinePowerScreenBlackDelay
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 LinePowerScreenBlackDelay <int32 600>
```

#### LinePowerSleepDelay（属性）

交流电源休眠延时。

- **功能**：设置交流电源下进入休眠的空闲等待时间（秒）
- **使用场景**：用户在控制中心设置交流电源下的休眠延时时间

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 LinePowerSleepDelay
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 LinePowerSleepDelay <int32 900>
```

#### LinePowerLockDelay（属性）

交流电源锁屏延时。

- **功能**：设置交流电源下自动锁屏的空闲等待时间（秒）
- **使用场景**：用户在控制中心设置交流电源下的锁屏延时时间

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 LinePowerLockDelay
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 LinePowerLockDelay <int32 180>
```

#### LinePowerShortIdleDelay（属性）

交流电源短空闲延时。

- **功能**：设置交流电源下进入短空闲状态的空闲等待时间（秒），用于触发低功耗降频
- **使用场景**：系统电源管理模块根据此值在短空闲时执行降频操作

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 LinePowerShortIdleDelay
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 LinePowerShortIdleDelay <int32 300>
```

### 电池延时配置

#### BatteryScreensaverDelay（属性）

电池屏保延时。

- **功能**：设置电池供电下激活屏保的空闲等待时间（秒）
- **使用场景**：用户在控制中心设置电池供电下的屏保延时时间

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 BatteryScreensaverDelay
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 BatteryScreensaverDelay <int32 120>
```

#### BatteryScreenBlackDelay（属性）

电池息屏延时。

- **功能**：设置电池供电下关闭屏幕的空闲等待时间（秒）
- **使用场景**：用户在控制中心设置电池供电下的息屏延时时间

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 BatteryScreenBlackDelay
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 BatteryScreenBlackDelay <int32 120>
```

#### BatterySleepDelay（属性）

电池休眠延时。

- **功能**：设置电池供电下进入休眠的空闲等待时间（秒）
- **使用场景**：用户在控制中心设置电池供电下的休眠延时时间

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 BatterySleepDelay
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 BatterySleepDelay <int32 300>
```

#### BatteryLockDelay（属性）

电池锁屏延时。

- **功能**：设置电池供电下自动锁屏的空闲等待时间（秒）
- **使用场景**：用户在控制中心设置电池供电下的锁屏延时时间

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 BatteryLockDelay
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 BatteryLockDelay <int32 60>
```

#### BatteryShortIdleDelay（属性）

电池短空闲延时。

- **功能**：设置电池供电下进入短空闲状态的空闲等待时间（秒），用于触发低功耗降频
- **使用场景**：系统电源管理模块根据此值在短空闲时执行降频操作

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 BatteryShortIdleDelay
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 BatteryShortIdleDelay <int32 60>
```

### 锁屏与动作配置

#### ScreenBlackLock（属性）

息屏时是否锁定。

- **功能**：设置息屏时是否同时锁定屏幕
- **使用场景**：用户在控制中心设置息屏时是否自动锁屏

| 属性 | 值 |
|------|------|
| 类型 | `b` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 ScreenBlackLock
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 ScreenBlackLock <true>
```

#### SleepLock（属性）

休眠时是否锁定。

- **功能**：设置系统从休眠唤醒时是否需要锁定屏幕
- **使用场景**：用户在控制中心设置休眠唤醒后是否自动锁屏

| 属性 | 值 |
|------|------|
| 类型 | `b` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 SleepLock
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 SleepLock <true>
```

#### LinePowerLidClosedAction（属性）

交流电源翻盖关闭动作。

- **功能**：设置交流电源下合上翻盖时执行的动作（如无操作、息屏、休眠）
- **使用场景**：用户在控制中心设置交流电源下合上翻盖时的系统行为

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 LinePowerLidClosedAction
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 LinePowerLidClosedAction <int32 0>
```

#### BatteryLidClosedAction（属性）

电池翻盖关闭动作。

- **功能**：设置电池供电下合上翻盖时执行的动作（如无操作、息屏、休眠）
- **使用场景**：用户在控制中心设置电池供电下合上翻盖时的系统行为

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 BatteryLidClosedAction
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 BatteryLidClosedAction <int32 0>
```

#### LinePowerPressPowerBtnAction（属性）

交流电源按下电源键动作。

- **功能**：设置交流电源下按下电源键时执行的动作（如无操作、息屏、休眠、关机）
- **使用场景**：用户在控制中心设置交流电源下按下电源键时的系统行为

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 LinePowerPressPowerBtnAction
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 LinePowerPressPowerBtnAction <int32 0>
```

#### BatteryPressPowerBtnAction（属性）

电池按下电源键动作。

- **功能**：设置电池供电下按下电源键时执行的动作（如无操作、息屏、休眠、关机）
- **使用场景**：用户在控制中心设置电池供电下按下电源键时的系统行为

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 BatteryPressPowerBtnAction
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 BatteryPressPowerBtnAction <int32 0>
```

### 低电量配置

#### LowPowerNotifyEnable（属性）

低电量通知是否启用。

- **功能**：设置是否在电池电量低于阈值时发送低电量通知
- **使用场景**：用户在控制中心开启或关闭低电量通知功能

| 属性 | 值 |
|------|------|
| 类型 | `b` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 LowPowerNotifyEnable
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 LowPowerNotifyEnable <true>
```

#### LowPowerNotifyThreshold（属性）

低电量通知阈值。

- **功能**：设置触发低电量通知的电池电量百分比阈值
- **使用场景**：用户在控制中心设置低电量通知触发的电量百分比

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 LowPowerNotifyThreshold
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 LowPowerNotifyThreshold <int32 20>
```

#### LowPowerAutoSleepThreshold（属性）

低电量自动休眠阈值。

- **功能**：设置触发自动休眠的电池电量百分比阈值
- **使用场景**：用户在控制中心设置自动休眠触发的电量百分比

| 属性 | 值 |
|------|------|
| 类型 | `i` |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Power1 LowPowerAutoSleepThreshold
```
设置示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Power1 \
  --object-path /org/deepin/dde/Power1 \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.dde.Power1 LowPowerAutoSleepThreshold <int32 5>
```

---
