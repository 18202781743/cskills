---
name: dde-appearance
description: 提供字体、主题、壁纸、光标、缩放、深色模式、窗口圆角、不透明度、窗口模糊效果的外观设置及工作区背景切换的 D-Bus 读写接口；另提供 dde-fakewm 虚拟窗口管理器作为 dde-appearance 自身的开发调试工具
Categories:
  - Settings
---

# dde-appearance

dde-appearance 是 DDE 外观管理组件。通过 Session 总线提供系统全局的外观设置（字体、主题、壁纸、光标、缩放、深色模式、窗口圆角、不透明度、窗口模糊效果）和窗口管理器工作区背景切换能力。此外，dde-appearance 项目还包含 dde-fakewm 虚拟窗口管理器，作为 dde-appearance 自身的开发调试工具。

## D-Bus 接口

### 外观设置

提供系统全局的字体、主题、壁纸、光标、缩放、深色模式、窗口圆角、不透明度和窗口模糊效果的读写接口。

详见 [org.deepin.dde.Appearance1.md](references/dbus/org.deepin.dde.Appearance1.md)

### 窗口管理器

提供系统全局的工作区背景切换、装饰主题设置、多任务状态控制和窗口显示操作。

详见 [com.deepin.wm.md](references/dbus/com.deepin.wm.md)

## CLI 命令

### dde-fakewm

dde-appearance 自身的开发调试工具，模拟最小化窗口管理器环境用于测试外观功能。非系统全局服务，仅在开发调试场景使用。

详见 [dde-fakewm.md](references/cli/dde-fakewm.md)
