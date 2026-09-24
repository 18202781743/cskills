---
name: dde-api
description: 提供图像处理、拼音查询、蓝牙设备管理、区域设置、声音主题播放的 D-Bus 接口，以及文件打开、GRUB 主题调整、图片模糊处理、声音主题播放守护进程的 CLI 命令
Categories:
  - Develop
---

# dde-api

dde-api 是 DDE 后端调用库组件，通过 Session 和 System 总线提供图像处理、拼音查询、蓝牙设备管理、区域设置和声音主题播放的 D-Bus 接口，同时提供文件打开、GRUB 主题调整、图片模糊处理和声音主题播放守护进程的 CLI 命令。

## D-Bus 接口

### 图像处理

提供图像裁剪、缩放、旋转、模糊、圆角处理能力。

详见 [org.deepin.dde.Graphic1.md](references/dbus/org.deepin.dde.Graphic1.md)

### 拼音查询

提供中文拼音搜索能力。

详见 [org.deepin.dde.Pinyin1.md](references/dbus/org.deepin.dde.Pinyin1.md)

### 蓝牙设备管理

提供蓝牙设备阻止状态查询和解锁能力。

详见 [org.deepin.dde.Device1.md](references/dbus/org.deepin.dde.Device1.md)

### 区域设置

提供系统区域设置生成和切换能力。

详见 [org.deepin.dde.LocaleHelper1.md](references/dbus/org.deepin.dde.LocaleHelper1.md)

### 声音主题播放

提供声音主题播放控制能力。对应的 CLI 守护进程为 `sound-theme-player`。

详见 [org.deepin.dde.SoundThemePlayer1.md](references/dbus/org.deepin.dde.SoundThemePlayer1.md)

### 兼容接口

以下接口为历史遗留或兼容性接口，当前可能未激活或已废弃，不建议在新代码中使用：

- **org.deepin.dde.LunarCalendar1**（Session 总线）：农历日历查询接口。其 `.service` 文件的 Exec 已被注释，当前可能未激活，保留用于兼容历史农历日历功能。
- **org.deepin.dde.Validator1**（Session 总线）：主机名和用户名校验接口。源码注释标注此程序当前未被使用和编译，可能已废弃，保留用于兼容旧版校验功能。
- **org.deepin.dde.InhibitHint1**（Session 总线）：抑制提示接口，以库形式由调用方注册，无独立 `.service` 文件。用于向调用方提供抑制提示信息，保留用于兼容旧版抑制提示机制。

## CLI 命令

### dde-open

DDE 文件/URL 打开工具，用于通过默认关联应用打开文件或 URL。

详见 [dde-open.md](references/cli/dde-open.md)

### adjust-grub-theme

GRUB 主题调整工具，用于根据屏幕分辨率和语言环境自动调整 GRUB 启动菜单的主题显示。

详见 [adjust-grub-theme.md](references/cli/adjust-grub-theme.md)

### image-blur

图片模糊处理工具，使用高斯模糊算法对图片进行模糊处理。与 `Graphic1` D-Bus 接口的 `BlurImage` 方法不同，该 CLI 工具支持通过 `-sigma` 参数控制模糊强度。

详见 [image-blur.md](references/cli/image-blur.md)

### sound-theme-player

声音主题播放守护进程，启动后提供 `org.deepin.dde.SoundThemePlayer1` D-Bus 接口供其他程序播放系统声音。

详见 [sound-theme-player.md](references/cli/sound-theme-player.md)
