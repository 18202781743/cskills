# org.deepin.dde.control-center.power

电源配置资源，管理控制中心电源设置中接入电源与使用电池时的关闭显示器、待机、锁屏延迟时间，以及休眠、关机、待机、定时关机的显示开关。

## 配置项

| Key | Name | Description | 类型 | Permissions |
|---|---|---|---|---|
| `linePowerScreenBlackDelay` | 接入电源关闭显示器延迟 | 配置接入电源时关闭显示器的延迟时间选项列表 | array | readwrite |
| `linePowerSleepDelay` | 接入电源待机延迟 | 配置接入电源时进入待机的延迟时间选项列表 | array | readwrite |
| `linePowerLockDelay` | 接入电源锁屏延迟 | 配置接入电源时锁屏的延迟时间选项列表 | array | readwrite |
| `batteryScreenBlackDelay` | 使用电池关闭显示器延迟 | 配置使用电池时关闭显示器的延迟时间选项列表 | array | readwrite |
| `batterySleepDelay` | 使用电池待机延迟 | 配置使用电池时进入待机的延迟时间选项列表 | array | readwrite |
| `batteryLockDelay` | 使用电池锁屏延迟 | 配置使用电池时锁屏的延迟时间选项列表 | array | readwrite |
| `showHibernate` | 休眠显示开关 | 控制是否在控制中心电源设置中显示休眠选项 | bool | readwrite |
| `showShutdown` | 关机显示开关 | 控制是否在控制中心电源设置中显示关机选项 | bool | readwrite |
| `showSuspend` | 待机显示开关 | 控制是否在控制中心电源设置中显示待机选项 | bool | readwrite |
| `enableScheduledShutdown` | 定时关机显示状态 | 控制控制中心电源管理关机设置中定时关机的显示状态，值为 Enabled 时正常显示，值为 Disabled 时显示禁用状态，值为 Hidden 时不显示 | string | readwrite |

## 读写示例

```bash
# 查询接入电源关闭显示器延迟
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.power -k linePowerScreenBlackDelay
# 设置接入电源关闭显示器延迟
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.power -k linePowerScreenBlackDelay -v "<value>"

# 查询使用电池待机延迟
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.power -k batterySleepDelay
# 设置使用电池待机延迟
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.power -k batterySleepDelay -v "<value>"

# 查询休眠显示开关
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.power -k showHibernate
# 设置休眠显示开关
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.power -k showHibernate -v "<value>"

# 查询定时关机显示状态
dde-dconfig get -a org.deepin.dde.control-center -r org.deepin.dde.control-center.power -k enableScheduledShutdown
# 设置定时关机显示状态
dde-dconfig set -a org.deepin.dde.control-center -r org.deepin.dde.control-center.power -k enableScheduledShutdown -v "<value>"
```
