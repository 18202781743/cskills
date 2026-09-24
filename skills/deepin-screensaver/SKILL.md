---
name: deepin-screensaver
description: 提供屏保启动停止、预览、配置管理和屏保列表查询接口
Categories:
  - Settings
---

# deepin-screensaver

deepin-screensaver 是 DDE 的屏幕保护程序组件，通过 Session 总线提供屏保的启动、停止、预览、配置管理和屏保列表查询能力。

## CLI 命令

### deepin-screensaver

DDE 屏幕保护程序，负责在用户空闲一段时间后启动屏幕保护动画。

详见 [deepin-screensaver.md](references/cli/deepin-screensaver.md)


## D-Bus 接口

### 屏保控制

提供屏保的启动、停止、预览、配置管理和屏保列表查询能力。

详见 [com.deepin.ScreenSaver.md](references/dbus/com.deepin.ScreenSaver.md)

### 兼容性说明

deepin-screensaver 仅注册一个 D-Bus 服务 `com.deepin.ScreenSaver`（对象路径 `/com/deepin/ScreenSaver`），无旧版别名或废弃接口。

系统中另存在 `org.freedesktop.ScreenSaver` 标准 FreeDesktop 屏保接口，由 dde-daemon 的 `org.deepin.dde.ScreenSaver1` 服务提供（对象路径 `/org/freedesktop/ScreenSaver`），提供 Inhibit/UnInhibit、SetTimeout、SimulateUserActivity 等标准屏保抑制功能。该接口属于 dde-daemon 组件，与 deepin-screensaver 的 `com.deepin.ScreenSaver` 是独立的不同实现，非兼容别名。

## DConfig 配置项

deepin-screensaver 通过 DConfig 暴露屏保轮播和当前屏保选择的配置资源。

### 自定义屏保配置

屏保轮播间隔、屏保播放模式、屏保图片路径配置。

详见 [org.deepin.customscreensaver](references/config/org.deepin.customscreensaver.md)

### 屏保选择配置

当前使用的屏保选择配置。

详见 [org.deepin.screensaver](references/config/org.deepin.screensaver.md)
