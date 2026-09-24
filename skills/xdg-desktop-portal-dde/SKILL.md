---
name: xdg-desktop-portal-dde
description: 提供截图、设置、壁纸、锁定、请求、inhibit、密钥、通知、文件选择、应用选择、访问、全局快捷键、账户和后台管理的 Session Portal D-Bus 接口，以及 xdg-desktop-portal-dde 自身的后台服务命令行工具
Categories:
  - Settings
---

# xdg-desktop-portal-dde

xdg-desktop-portal-dde 是 xdg-desktop-portal 的 DDE 后端实现。通过 Session 总线为沙箱应用提供截图、设置、壁纸、锁定、请求、inhibit、密钥、通知、文件选择、应用选择、访问、全局快捷键、账户和后台管理的 Portal D-Bus 接口；同时提供 xdg-desktop-portal-dde 自身的后台服务命令行工具，由 DBus 在沙箱应用请求系统服务时自动激活。

## CLI 命令

### xdg-desktop-portal-dde

xdg-desktop-portal-dde 自身的后台服务进程，为沙箱应用（如 Flatpak）提供访问系统资源（文件选择、屏幕截图、屏幕共享）的 DBus 接口。由 DBus 在沙箱应用请求系统服务时自动激活，一般不需要用户直接运行。

详见 [xdg-desktop-portal-dde.md](references/cli/xdg-desktop-portal-dde.md)


## D-Bus 接口

### 截图

提供屏幕截图能力。

详见 [org.freedesktop.impl.portal.Screenshot.md](references/dbus/org.freedesktop.impl.portal.Screenshot.md)

### 设置

提供桌面环境设置读写能力。

详见 [org.freedesktop.impl.portal.Settings.md](references/dbus/org.freedesktop.impl.portal.Settings.md)

### 壁纸

提供壁纸设置能力。

详见 [org.freedesktop.impl.portal.Wallpaper.md](references/dbus/org.freedesktop.impl.portal.Wallpaper.md)

### 通知

提供桌面通知发送和移除能力。

详见 [org.freedesktop.impl.portal.Notification.md](references/dbus/org.freedesktop.impl.portal.Notification.md)

### 文件选择

提供文件打开和保存对话框能力。

详见 [org.freedesktop.impl.portal.FileChooser.md](references/dbus/org.freedesktop.impl.portal.FileChooser.md)

### 账户

提供用户信息查询能力。

详见 [org.freedesktop.impl.portal.Account.md](references/dbus/org.freedesktop.impl.portal.Account.md)

### 访问

提供访问对话框能力。

详见 [org.freedesktop.impl.portal.Access.md](references/dbus/org.freedesktop.impl.portal.Access.md)

### 应用选择

提供应用选择对话框能力。

详见 [org.freedesktop.impl.portal.AppChooser.md](references/dbus/org.freedesktop.impl.portal.AppChooser.md)

### 后台管理

提供后台运行请求和通知能力。

详见 [org.freedesktop.impl.portal.Background.md](references/dbus/org.freedesktop.impl.portal.Background.md)

### 全局快捷键

提供全局快捷键会话创建和绑定能力。

详见 [org.freedesktop.impl.portal.GlobalShortcuts.md](references/dbus/org.freedesktop.impl.portal.GlobalShortcuts.md)

### Inhibit

提供会话抑制能力。

详见 [org.freedesktop.impl.portal.Inhibit.md](references/dbus/org.freedesktop.impl.portal.Inhibit.md)

### 密钥

提供密钥检索能力。

详见 [org.freedesktop.impl.portal.Secret.md](references/dbus/org.freedesktop.impl.portal.Secret.md)

### 锁定

提供锁定模式设置能力。

详见 [org.freedesktop.impl.portal.Lockdown.md](references/dbus/org.freedesktop.impl.portal.Lockdown.md)

### 请求

提供标准 portal 请求关闭能力。

详见 [org.freedesktop.impl.portal.Request.md](references/dbus/org.freedesktop.impl.portal.Request.md)

## 兼容性说明

xdg-desktop-portal-dde 的所有 D-Bus 接口均遵循 xdg-desktop-portal 标准规范，使用唯一的服务名 `org.freedesktop.impl.portal.desktop.dde` 和对象路径 `/org/freedesktop/portal/desktop`，不存在兼容旧版接口的别名或废弃接口。所有接口均为当前正在使用的标准 portal 实现接口。
