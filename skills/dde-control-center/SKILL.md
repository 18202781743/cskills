---
name: dde-control-center
description: dde-control-center 是 DDE 控制中心，是 DDE 桌面环境中用于系统设置管理的核心图形应用。本 skill 提供控制中心应用启动与模块查看的 CLI 命令、控制中心窗口显示控制与页面跳转及全局搜索的 D-Bus 接口、控制中心应用自身的窗口尺寸、模块显隐、电源延迟、更新设置显示、个性化外观、账户头像、通用信息保护、显示亮度、日期时间 NTP 服务器、声音设备管理、隐私权限黑名单的 DConfig 配置项
Categories:
  - Application
---

# dde-control-center

dde-control-center 是 DDE 控制中心，提供控制中心应用的启动与模块查看 CLI 命令，通过 Session 总线提供窗口显示控制、页面跳转、模块列表获取和全局搜索的 D-Bus 接口，以及控制中心应用自身的窗口尺寸、模块显隐、电源延迟、更新设置显示、个性化外观、账户头像、通用信息保护、显示亮度、日期时间 NTP 服务器、声音设备管理、隐私权限黑名单的 DConfig 配置项。

## CLI 命令

### dde-control-center

DDE 控制中心主程序，是 DDE 桌面环境中用于系统设置管理的核心图形应用。

详见 [dde-control-center.md](references/cli/dde-control-center.md)


## D-Bus 接口

### 窗口显示与页面跳转

提供控制中心窗口的显示、隐藏、切换、退出，以及页面跳转和模块列表获取能力。

详见 [org.deepin.dde.ControlCenter1.md](references/dbus/org.deepin.dde.ControlCenter1.md)

### 全局搜索

提供控制中心内全局搜索能力，支持搜索、停止搜索和执行搜索动作。

详见 [org.deepin.dde.ControlCenter1.GrandSearch.md](references/dbus/org.deepin.dde.ControlCenter1.GrandSearch.md)

## DConfig 配置项

以下 DConfig 配置项均为控制中心应用自身的配置，用于控制控制中心窗口尺寸、各设置模块的显示行为、电源延迟、更新设置显示、个性化外观、账户头像、通用信息保护、显示亮度、日期时间 NTP 服务器、声音设备管理、隐私权限黑名单，而非系统全局配置。

### 控制中心窗口配置

控制中心窗口尺寸、侧边栏宽度与模块显隐配置。

详见 [org.deepin.dde.control-center](references/config/org.deepin.dde.control-center.md)

### 账户配置

用户头像路径配置。

详见 [org.deepin.dde.control-center.accounts](references/config/org.deepin.dde.control-center.accounts.md)

### 通用信息配置

只读保护显示开关配置。

详见 [org.deepin.dde.control-center.commoninfo](references/config/org.deepin.dde.control-center.commoninfo.md)

### 日期时间配置

自定义 NTP 服务器配置。

详见 [org.deepin.dde.control-center.datetime](references/config/org.deepin.dde.control-center.datetime.md)

### 显示配置

亮度最小值配置。

详见 [org.deepin.dde.control-center.display](references/config/org.deepin.dde.control-center.display.md)

### 个性化配置

图标主题隐藏、标题栏高度、紧凑模式与滚动条显示策略配置。

详见 [org.deepin.dde.control-center.personalization](references/config/org.deepin.dde.control-center.personalization.md)

### 电源配置

接入电源与使用电池时的关闭显示器、待机、锁屏延迟时间，以及休眠、关机、待机、定时关机的显示开关配置。

详见 [org.deepin.dde.control-center.power](references/config/org.deepin.dde.control-center.power.md)

### 更新配置

安全更新、自动安装、第三方源、P2P 更新、更新历史记录、更新日志地址与版本号显示配置。

详见 [org.deepin.dde.control-center.update](references/config/org.deepin.dde.control-center.update.md)

### 声音配置

设备管理显示开关配置。

详见 [org.deepin.dde.control-center.sound](references/config/org.deepin.dde.control-center.sound.md)

### 隐私配置

权限黑名单配置。

详见 [org.deepin.dde.control-center.privacy](references/config/org.deepin.dde.control-center.privacy.md)

### 安全密钥配置

安全密钥模块显隐配置。

详见 [org.deepin.dde.control-center.passkey](references/config/org.deepin.dde.control-center.passkey.md)
