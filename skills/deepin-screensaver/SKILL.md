---
name: deepin-screensaver
description: deepin-screensaver 是 DDE 的屏幕保护程序组件，负责在用户空闲时启动屏幕保护动画。提供全局的屏保启动停止、预览、配置管理和屏保列表查询的 D-Bus 接口与屏保启动及配置对话框的 CLI 命令，以及仅作用于 deepin-screensaver 自身的屏保轮播和屏保选择的 DConfig 配置
Categories:
  - Application
---

# deepin-screensaver

deepin-screensaver 是 DDE 的屏幕保护程序组件，负责在用户空闲一段时间后启动屏幕保护动画。该 skill 提供全局的屏保控制 D-Bus 接口与 CLI 命令，以及仅作用于 deepin-screensaver 自身的 DConfig 配置。

## CLI 命令

### deepin-screensaver

DDE 屏幕保护程序，负责在用户空闲一段时间后启动屏幕保护动画。支持通过 DBus 注册服务供系统调用、直接启动屏保、以及打开特定屏保应用的配置对话框。

详见 [deepin-screensaver.md](references/cli/deepin-screensaver.md)

## D-Bus 接口

### 屏保控制

提供全局的屏保启动、停止、预览、配置管理和屏保列表查询能力。

详见 [com.deepin.ScreenSaver.md](references/dbus/com.deepin.ScreenSaver.md)

### 兼容性说明

deepin-screensaver 仅注册一个 D-Bus 服务 `com.deepin.ScreenSaver`（对象路径 `/com/deepin/ScreenSaver`），无旧版别名或废弃接口。

系统中另存在 `org.freedesktop.ScreenSaver` 标准 FreeDesktop 屏保接口，由 `treeland-screensaver` 提供（对象路径 `/org/freedesktop/ScreenSaver`），提供 `Inhibit` 和 `UnInhibit` 标准屏保抑制功能。该接口属于 `treeland-screensaver` 组件，与 deepin-screensaver 的 `com.deepin.ScreenSaver` 是独立的不同实现，非兼容别名。

## DConfig 配置项

以下 DConfig 配置仅作用于 deepin-screensaver 自身应用（App ID: `org.deepin.screensaver`）。

### 自定义屏保配置

屏保轮播间隔、屏保播放模式、屏保图片路径配置。

详见 [org.deepin.customscreensaver](references/config/org.deepin.customscreensaver.md)

### 屏保选择配置

当前使用的屏保选择配置。

详见 [org.deepin.screensaver](references/config/org.deepin.screensaver.md)
