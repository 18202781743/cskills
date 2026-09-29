# org.deepin.dde.daemon.power DConfig 配置参考

该文件文档化电源管理的 DConfig 配置项，包括 CPU 调频、节能模式、定时关机、屏幕延时、电源按键动作配置。仅介绍 visibility 为 public 的配置项。

## 配置项总览

共 38 个 public 配置项。

## CPU 调频与性能模式

### supportCpuGovernors

- **类型**：`array<string>`
- **默认值**：["performance", "powersave", "userspace", "ondemand", "conservative", "schedutil"]
- **权限**：readwrite
- **功能**：CPU 支持的 Governor 模式列表，包括 performance、powersave、userspace、ondemand、conservative、schedutil

### specialCpuModeJson

- **类型**：`string`
- **默认值**：`{"PANGU":{"Balance":true,"Performace":true,"PowerSave":true}}`
- **权限**：readwrite
- **功能**：需要进行特殊处理的 CPU 配置，以 JSON 字符串形式存储，按机型名称映射各功耗模式是否可用

### mode

- **类型**：`string`
- **默认值**：`balance`
- **权限**：readwrite
- **功能**：当前性能模式，可选值：balance（平衡）、performance（高性能）、powersave（节能）

### powerMappingConfig

- **类型**：`string`
- **默认值**：`{"balance":{"DSPCConfig":"balance"},"lowBattery":{"DSPCConfig":"lowbat"},"performance":{"DSPCConfig":"performance"},"powersave":{"DSPCConfig":"saving"}}`
- **权限**：readwrite
- **功能**：四种功耗模式（平衡、低电量、高性能、节能）对应的 DSPC 配置映射，以 JSON 字符串形式存储

## 节能模式

### powerSavingModeAuto

- **类型**：`boolean`
- **默认值**：false
- **权限**：readwrite
- **功能**：使用电池时是否自动开启节能模式

### powerSavingModeEnabled

- **类型**：`boolean`
- **默认值**：false
- **权限**：readwrite
- **功能**：是否开启节能模式

### powerSavingModeAutoWhenBatteryLow

- **类型**：`boolean`
- **默认值**：true
- **权限**：readwrite
- **功能**：低电量时是否自动开启节能模式

### powerSavingModeAutoBatteryPercent

- **类型**：`int32`
- **默认值**：20
- **权限**：readwrite
- **功能**：自动开启节能模式的电池电量百分比阈值

### powerSavingModeBrightnessDropPercent

- **类型**：`int32`
- **默认值**：20
- **权限**：readwrite
- **功能**：节能模式下亮度降低的百分比

## 定时关机

### scheduledShutdownState

- **类型**：`boolean`
- **默认值**：false
- **权限**：readwrite
- **功能**：定时关机功能开关

### shutdownTime

- **类型**：`string`
- **默认值**：`19:00`
- **权限**：readwrite
- **功能**：定时关机的触发时间，格式为 HH:MM

### shutdownRepetition

- **类型**：`int32`
- **默认值**：0
- **权限**：readwrite
- **功能**：定时关机的重复类型：0=每天、1=工作日、2=周末、3=自定义

### customShutdownWeekDays

- **类型**：`array<string>`
- **默认值**：空数组
- **权限**：readwrite
- **功能**：自定义关机重复日期，数组形式存储星期几（1-7）

### shutdownCountdown

- **类型**：`int32`
- **默认值**：60
- **权限**：readwrite
- **功能**：关机倒计时时长，单位秒

### delayWakeupInterval

- **类型**：`int32`
- **默认值**：0
- **权限**：readwrite
- **功能**：延时关闭 DDE 黑屏程序的时间间隔，单位毫秒

### nextShutdownTime

- **类型**：`int32`
- **默认值**：0
- **权限**：readwrite
- **功能**：下一次关机时间，以 Unix 时间戳形式存储

## 屏幕延时配置

### linePowerScreensaverDelay

- **类型**：`int32`
- **默认值**：0
- **权限**：readwrite
- **功能**：插电时显示屏保的超时时间，单位秒

### batteryScreensaverDelay

- **类型**：`int32`
- **默认值**：0
- **权限**：readwrite
- **功能**：使用电池时显示屏保的超时时间，单位秒

### linePowerScreenBlackDelay

- **类型**：`int32`
- **默认值**：900
- **权限**：readwrite
- **功能**：插电时屏幕黑屏延时，单位秒

### batteryScreenBlackDelay

- **类型**：`int32`
- **默认值**：300
- **权限**：readwrite
- **功能**：使用电池时屏幕黑屏延时，单位秒

### linePowerSleepDelay

- **类型**：`int32`
- **默认值**：1800
- **权限**：readwrite
- **功能**：插电时休眠延时，单位秒

### batterySleepDelay

- **类型**：`int32`
- **默认值**：900
- **权限**：readwrite
- **功能**：使用电池时休眠延时，单位秒

### linePowerLockDelay

- **类型**：`int32`
- **默认值**：900
- **权限**：readwrite
- **功能**：插电时锁屏延时，单位秒

### batteryLockDelay

- **类型**：`int32`
- **默认值**：300
- **权限**：readwrite
- **功能**：使用电池时锁屏延时，单位秒

### linePowerShortIdleDelay

- **类型**：`int32`
- **默认值**：300
- **权限**：readwrite
- **功能**：插电时短 idle 延时，单位秒

### batteryShortIdleDelay

- **类型**：`int32`
- **默认值**：300
- **权限**：readwrite
- **功能**：使用电池时短 idle 延时，单位秒

## 屏幕与亮度控制

### allowScreenSaver

- **类型**：`boolean`
- **默认值**：true
- **权限**：readwrite
- **功能**：是否允许屏幕保护程序运行

### adjustBrightnessEnabled

- **类型**：`boolean`
- **默认值**：false
- **权限**：readwrite
- **功能**：是否启用自动调节亮度功能

### ambientLightAdjustBrightness

- **类型**：`boolean`
- **默认值**：true
- **权限**：readwrite
- **功能**：是否通过环境光传感器自动调节屏幕背光亮度

### screenBlackLock

- **类型**：`boolean`
- **默认值**：true
- **权限**：readwrite
- **功能**：关闭屏幕前是否锁定会话

### sleepLock

- **类型**：`boolean`
- **默认值**：true
- **权限**：readwrite
- **功能**：系统休眠前是否锁定会话

### delayHandleIdleOffIntervalWhenScreenBlack

- **类型**：`int32`
- **默认值**：800
- **权限**：readwrite
- **功能**：屏幕黑屏后延时调用 HandleIdleOff 的时间间隔，单位毫秒

### fullscreenWorkaroundAppList

- **类型**：`array<string>`
- **默认值**：["libflash", "chrome", "firefox", "mplayer", "operaplugin", "soffice", "wpp", "evince", "vlc", "totem"]
- **权限**：readwrite
- **功能**：全屏工作模式应用列表，列表中的应用在全屏时抑制屏保

## 翻盖与电源键动作

### lidClosedSleep

- **类型**：`boolean`
- **默认值**：true
- **权限**：readwrite
- **功能**：插电时合上翻盖是否休眠

### batteryLidClosedSleep

- **类型**：`boolean`
- **默认值**：true
- **权限**：readwrite
- **功能**：使用电池时合上翻盖是否休眠

### powerButtonPressedExec

- **类型**：`string`
- **默认值**：`dde-shutdown`
- **权限**：readwrite
- **功能**：电源键按下时执行的命令

## 低电量策略

### usePercentageForPolicy

- **类型**：`boolean`
- **默认值**：true
- **权限**：readwrite
- **功能**：是否使用基于电池百分比的低电量策略，比剩余时间估算更可靠

## 其他

### powerModuleInitialized

- **类型**：`boolean`
- **默认值**：false
- **权限**：readwrite
- **功能**：电源模块是否已完成初始化
