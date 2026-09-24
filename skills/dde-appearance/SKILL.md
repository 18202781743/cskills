---
name: dde-appearance
description: dde-appearance 是 DDE 桌面环境的外观管理组件，负责管理系统全局的外观设置。本 skill 提供全局外观设置 D-Bus 读写接口（字体、主题、壁纸、光标、缩放、窗口圆角、不透明度）、全局工作区背景切换 D-Bus 接口（工作区背景设置、装饰主题设置、多任务状态控制、窗口显示操作），以及 dde-fakewm 虚拟窗口管理器（仅作用于 dde-appearance 自身的开发调试工具）
Categories:
  - Settings
---

# dde-appearance

dde-appearance 是 DDE 桌面环境的外观管理组件。通过 Session 总线提供系统全局的外观设置（字体、主题、壁纸、光标、缩放、窗口圆角、不透明度）和窗口管理器工作区背景切换能力。此外，dde-appearance 项目还包含 dde-fakewm 虚拟窗口管理器，作为 dde-appearance 自身的开发调试工具。

## D-Bus 接口

### 外观设置

提供全局的字体、主题、壁纸、光标、缩放、窗口圆角、不透明度的读写接口。

详见 [org.deepin.dde.Appearance1.md](references/dbus/org.deepin.dde.Appearance1.md)

### 窗口管理器

提供全局的工作区背景切换、装饰主题设置、多任务状态控制和窗口显示操作。

详见 [com.deepin.wm.md](references/dbus/com.deepin.wm.md)

### 接口兼容性说明

dde-appearance 当前提供以下两个 D-Bus 服务，均为当前正在使用的接口，无兼容性/旧版别名接口：

- `org.deepin.dde.Appearance1`（`/org/deepin/dde/Appearance1`）— 外观设置服务，提供字体、主题、壁纸、光标、缩放、窗口圆角、不透明度外观属性的读写。
- `com.deepin.wm`（`/com/deepin/wm`）— 窗口管理器接口，提供工作区背景切换、装饰主题设置、多任务状态控制、窗口显示操作。该接口由 dde-appearance 内置的 `dde-fakewm` 模块注册，在实际 DDE 环境中由真实窗口管理器（如 deepin-kwin）提供同名接口，接口名和对象路径保持一致，不存在旧版兼容别名。

此外，dde-appearance 还通过 `com.deepin.sync.Config` 接口在动态路径 `/org/deepin/dde/Appearance1/sync` 和 `/org/deepin/dde/Appearance1/Background` 上注册同步配置对象，用于外观设置的同步，同样为当前接口，非兼容接口。

## CLI 命令

### dde-fakewm

dde-appearance 自身的开发调试工具，模拟最小化窗口管理器环境用于测试外观功能。非系统全局服务，仅在开发调试场景使用。

详见 [dde-fakewm.md](references/cli/dde-fakewm.md)
