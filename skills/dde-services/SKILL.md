---
name: dde-services
description: 提供快捷键操作执行、IP 地址监视的 CLI 命令，以及电源管理、X 设置、壁纸轮播、快捷键、手势、壁纸缓存、环境亮度的 Session D-Bus 接口
Categories:
  - Settings
---

# dde-services

dde-services 是 DDE 的后端服务组件，提供快捷键操作执行、IP 地址监视的 CLI 命令，以及通过 Session 总线提供电源管理、X 设置、壁纸轮播、快捷键、手势、壁纸缓存和环境亮度能力。

## CLI 命令

### dde-shortcut-tool

DDE 快捷键工具，通过子命令 + action 模式执行各类系统快捷操作。

详见 [dde-shortcut-tool.md](references/cli/dde-shortcut-tool.md)

### ipwatchd

IP 地址监视守护进程（upstream 开源项目），用于监视网络接口的 IP 地址变化。

详见 [ipwatchd.md](references/cli/ipwatchd.md)


## D-Bus 接口

### 电源管理

提供电源管理能力。

详见 [org.deepin.dde.Power1.md](references/dbus/org.deepin.dde.Power1.md)

### X 设置

提供X 设置能力。

详见 [org.deepin.dde.XSettings1.md](references/dbus/org.deepin.dde.XSettings1.md)

### 壁纸轮播

提供壁纸轮播能力。

详见 [org.deepin.dde.WallpaperSlideshow.md](references/dbus/org.deepin.dde.WallpaperSlideshow.md)

### 快捷键

提供快捷键能力。

详见 [org.deepin.dde.Keybinding1.md](references/dbus/org.deepin.dde.Keybinding1.md)

### 手势

提供手势能力。

详见 [org.deepin.dde.Gesture1.md](references/dbus/org.deepin.dde.Gesture1.md)

### 壁纸缓存

提供壁纸缓存能力。

详见 [org.deepin.dde.WallpaperCache.md](references/dbus/org.deepin.dde.WallpaperCache.md)

### 环境亮度

提供环境亮度能力。

详见 [org.deepin.dde.AmbientBrightness1.md](references/dbus/org.deepin.dde.AmbientBrightness1.md)

## 兼容性接口

dde-services 在 Treeland 会话下替代了 dde-daemon 的部分功能，为保持与旧版应用的兼容性，以下接口作为兼容接口提供，实际实现均挂载在 WallpaperCache 服务上：

- **org.deepin.dde.ImageEffect1**：兼容 dde-daemon 的 ImageEffect 服务，提供图像效果处理（Get/Delete）接口，实际委托给 WallpaperCache 服务处理，仅支持 "pixmix"/blur 效果。在 Treeland 会话下由 dde-services 提供，替代 dde-daemon 的同名服务。
- **org.deepin.dde.ImageBlur1**：兼容 dde-daemon 的 ImageBlur 服务，提供图像模糊处理（Get/Delete）及模糊完成信号（BlurDone），实际委托给 WallpaperCache 服务的模糊处理功能。在 Treeland 会话下由 dde-services 提供，替代 dde-daemon 的同名服务。

此外，org.deepin.dde.Power1、org.deepin.dde.Keybinding1 和 org.deepin.dde.Gesture1 与 dde-daemon 存在接口重名，属于 Treeland/X11 双轨分流设计：在 Treeland 会话下由 dde-services 提供，在 X11 会话下由 dde-daemon 提供，并非兼容性别名接口。
