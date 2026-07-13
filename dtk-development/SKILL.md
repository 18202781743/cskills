--- 
name: dtk-development
description: |
  DTK (Deepin Tool Kit) 开发指南，覆盖 dtkcore/dtkgui/dtkwidget/dtkdeclarative/dtklog。
  触发场景：
  - 开发 DDE 应用需要选择 DTK 控件
  - 实现主题感知 UI（图标、配色、窗口装饰）
  - 使用 DConfig 管理配置
  - 需要遵循 DDE 日志规范
  - 图标/主题/窗口装饰相关问题
  - 多个 DDE 应用出现相同问题时，可能是 DTK 的问题，需要排查 DTK 源码或提供 DTK 层面的解决方案
---

# DTK 开发指南

DTK 是深度桌面环境的核心开发框架。按场景快速定位：

## 快速路由

| 场景 | 参考文档 |
|------|----------|
| 了解 DTK 整体架构与依赖关系 | [references/architecture.md](references/architecture.md) |
| 修改/编译/调试 DTK 自身源码 | [references/dtksrc-compile-debug.md](references/dtksrc-compile-debug.md) |
| 创建新应用项目 | [references/app-dev-with-dtk.md](references/app-dev-with-dtk.md) |
| 窗口装饰（圆角/阴影/模糊/CSD） | [references/platform-abstraction.md](references/platform-abstraction.md) |
| 控件用法示例（QWidget + QML） | [references/examples.md](references/examples.md) |
| 选择/显示图标 | [references/theme/index.md](references/theme/index.md) |
| 主题切换/配色 | [references/theme/index.md](references/theme/index.md) |
| 选择 QWidget 控件 | [references/widgets/index.md](references/widgets/index.md) |
| 选择 QML 控件 | [references/declarative/index.md](references/declarative/index.md) |
| 应用配置持久化 | [references/config/index.md](references/config/index.md) |
| 日志/DBus/通知/单实例 | [references/utilities/index.md](references/utilities/index.md) |
| 主题系统/字体/平台判断 | [references/utilities/index.md](references/utilities/index.md) |
| DApplication 应用入口 | [references/widgets/application.md](references/widgets/application.md) |
| 窗口模糊效果 | [references/widgets/blur-effect.md](references/widgets/blur-effect.md) |
| QML DTK 全局对象 | [references/declarative/dtk-global.md](references/declarative/dtk-global.md) |
| QML 窗口附加属性 | [references/declarative/dwindow.md](references/declarative/dwindow.md) |

## 高频跨域场景

- **了解 DTK 架构和仓库依赖** → [architecture.md](references/architecture.md)
- **查看控件用法示例** → [examples.md](references/examples.md)（QWidget 16 个分类、QML 控件画廊）
- **窗口圆角/阴影/模糊/无标题栏** → [platform-abstraction.md](references/platform-abstraction.md)
- **修改 DTK 源码并编译调试** → [dtksrc-compile-debug.md](references/dtksrc-compile-debug.md)
- **创建新的 DTK 项目** → [app-dev-with-dtk.md](references/app-dev-with-dtk.md)
- **自定义控件使用主题图标** → [theme/index.md](references/theme/index.md) + [theme/palette.md](references/theme/palette.md)
- **设置控件颜色样式（避免 QSS）** → [theme/palette.md](references/theme/palette.md)
- **QML 中显示 dci 图标** → [declarative/dci-icon.md](references/declarative/dci-icon.md)
- **控件内嵌入消息提示** → [widgets/message.md](references/widgets/message.md)
- **DApplication 应用入口/单实例/翻译** → [widgets/application.md](references/widgets/application.md)
- **DGuiApplicationHelper 主题/调色板/平台** → [utilities/gui-helper.md](references/utilities/gui-helper.md)
- **DFontSizeManager 字体管理** → [utilities/font-manager.md](references/utilities/font-manager.md)
- **DSysInfo 系统版本判断** → [utilities/sysinfo.md](references/utilities/sysinfo.md)
- **DDBusSender DBus 通信** → [utilities/dbus.md](references/utilities/dbus.md)
- **DWindowManagerHelper 窗口管理** → [utilities/window-manager.md](references/utilities/window-manager.md)
- **DDesktopServices 桌面服务** → [utilities/desktop-services.md](references/utilities/desktop-services.md)
- **QML D.DTK 全局对象/字体/主题** → [declarative/dtk-global.md](references/declarative/dtk-global.md)
- **QML D.DWindow 窗口效果** → [declarative/dwindow.md](references/declarative/dwindow.md)
- **DBlurEffectWidget 模糊效果** → [widgets/blur-effect.md](references/widgets/blur-effect.md)
- **DLabel 标签控件（前景色/文本省略）** → [widgets/label.md](references/widgets/label.md)
- **DPaletteHelper 控件调色板** → [widgets/palette-helper.md](references/widgets/palette-helper.md)
- **DToolTip 工具提示** → [widgets/tooltip.md](references/widgets/tooltip.md)
- **DSlider 滑动条** → [widgets/slider.md](references/widgets/slider.md)
- **DStyledItemDelegate 列表项委托** → [widgets/item-delegate.md](references/widgets/item-delegate.md)

## 核心模块速览

| 模块 | 基础层（dtkcore/dtkgui） | QWidget 层（dtkwidget/qt5integration） | QML 层（dtkdeclarative） | 入口文档 |
|------|--------------------------|----------------------------------------|--------------------------|----------|
| 架构与依赖 | 全部 8 个项目 | — | — | [architecture.md](references/architecture.md) |
| 工具类/核心类 | DGuiApplicationHelper/DFontSizeManager/DSysInfo/DDBusSender/DWindowManagerHelper/DDesktopServices/DLogManager/DDBusInterface | DApplication | D.DTK/D.DWindow/ApplicationHelper | [utilities/index.md](references/utilities/index.md) |
| 图标 | DDciIcon/DIconTheme (dtkgui), DDciFile (dtkcore) | DStyle::standardIcon, DIcon | DciIcon, IconLabel | [theme/index.md](references/theme/index.md) |
| 主题/调色板 | DPalette/DGuiApplicationHelper (dtkgui), QDeepinTheme (qt5integration) | DStyle/DStyleHelper | Palette, ColorSelector | [theme/index.md](references/theme/index.md) |
| 字体 | DFontManager/DPlatformTheme (dtkgui) | DFontSizeManager | D.DTK.fontManager | [utilities/font-manager.md](references/utilities/font-manager.md) |
| 平台抽象 | DPlatformHandle/DPlatformTheme (dtkgui) | — | — | [platform-abstraction.md](references/platform-abstraction.md) |
| QWidget 控件 | — | 55+ 控件 | — | [widgets/index.md](references/widgets/index.md) |
| QML 控件 | — | — | 60+ 控件 | [declarative/index.md](references/declarative/index.md) |
| 配置 DConfig | DConfig (dtkcore) | — | D.Config | [config/index.md](references/config/index.md) |
