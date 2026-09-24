---
name: dde-control-center
description: 提供控制中心应用启动与模块查看的 CLI 命令、控制中心窗口显示控制与页面跳转及全局搜索的 D-Bus 接口、控制中心应用自身的窗口尺寸与模块显示配置的 DConfig 配置项
Categories:
  - Application
---

# dde-control-center

dde-control-center 是 DDE 控制中心，提供控制中心应用的启动与模块查看 CLI 命令，通过 Session 总线提供窗口显示控制、页面跳转、模块列表获取和全局搜索的 D-Bus 接口，以及控制中心应用自身的窗口尺寸与各模块显示配置的 DConfig 配置项。

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

### 兼容性接口

控制中心 D-Bus 服务保留了以下已废弃的兼容性方法，供旧版调用方继续使用，新代码应优先使用推荐替代方法：

- **ShowPage(QString module, QString page)**：旧版双参数页面跳转接口，通过模块名和页面名定位目标页面。已标记 `Q_DECL_DEPRECATED_X`，推荐使用单参数 `ShowPage(QString url)` 替代。
- **ShowModule(QString module)**：旧版模块显示接口，通过模块名显示指定模块。已标记 `Q_DECL_DEPRECATED_X`，推荐使用 `ShowPage(QString url)` 替代。

以上兼容性方法仅保留向后兼容，功能与当前 `ShowPage(QString url)` 相同，均为跳转到控制中心指定页面。详见 [org.deepin.dde.ControlCenter1.md](references/dbus/org.deepin.dde.ControlCenter1.md)

## DConfig 配置项

以下 DConfig 配置项均为控制中心应用自身的配置，用于控制控制中心窗口尺寸及各设置模块的显示行为，而非系统全局配置。

### 控制中心窗口配置

控制中心窗口宽度和高度配置。

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

隐藏图标主题配置。

详见 [org.deepin.dde.control-center.personalization](references/config/org.deepin.dde.control-center.personalization.md)

### 声音配置

设备管理显示开关配置。

详见 [org.deepin.dde.control-center.sound](references/config/org.deepin.dde.control-center.sound.md)
