--- 
name: dtk
description: |
  DTK (Deepin Tool Kit) 开发指南，覆盖 dtkcore/dtkgui/dtkwidget/dtkdeclarative/dtklog。
  触发场景：
  - 开发 DDE 应用需要选择 DTK 控件
  - 实现主题感知 UI（图标、配色、窗口装饰）
  - 使用 DConfig 管理配置
  - 需要遵循 DDE 日志规范
  - 图标/主题/窗口装饰相关问题
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
| 选择/显示图标 | [references/icons/index.md](references/icons/index.md) |
| 主题切换/配色 | [references/theming/index.md](references/theming/index.md) |
| 选择 QWidget 控件 | [references/widgets/index.md](references/widgets/index.md) |
| 选择 QML 控件 | [references/declarative/index.md](references/declarative/index.md) |
| 应用配置持久化 | [references/config/index.md](references/config/index.md) |
| 日志/DBus/通知/单实例 | [references/utilities/index.md](references/utilities/index.md) |

## 高频跨域场景

- **了解 DTK 架构和仓库依赖** → [architecture.md](references/architecture.md)
- **窗口圆角/阴影/模糊/无标题栏** → [platform-abstraction.md](references/platform-abstraction.md)
- **修改 DTK 源码并编译调试** → [dtksrc-compile-debug.md](references/dtksrc-compile-debug.md)
- **创建新的 DTK 项目** → [app-dev-with-dtk.md](references/app-dev-with-dtk.md)
- **自定义控件使用主题图标** → [icons/index.md](references/icons/index.md) + [theming/palette.md](references/theming/palette.md)
- **QML 中显示 dci 图标** → [declarative/dci-icon.md](references/declarative/dci-icon.md)
- **控件内嵌入消息提示** → [widgets/message.md](references/widgets/message.md) + [utilities/index.md](references/utilities/index.md)

## 核心模块速览

| 模块 | 基础层（dtkcore/dtkgui） | QWidget 层（dtkwidget/qt5integration） | QML 层（dtkdeclarative） | 入口文档 |
|------|--------------------------|----------------------------------------|--------------------------|----------|
| 架构与依赖 | 全部 8 个项目 | — | — | [architecture.md](references/architecture.md) |
| 图标 | DDciIcon/DIconTheme (dtkgui), DDciFile (dtkcore) | DStyle::standardIcon, DIcon | DciIcon, IconLabel | [icons/index.md](references/icons/index.md) |
| 主题/调色板 | DPalette/DGuiApplicationHelper (dtkgui), QDeepinTheme (qt5integration) | DStyle/DStyleHelper | Palette, ColorSelector | [theming/index.md](references/theming/index.md) |
| 字体 | DFontManager/DPlatformTheme (dtkgui) | DFontSizeManager | D.DTK.fontManager | [theming/index.md](references/theming/index.md) |
| 平台抽象 | DPlatformHandle/DPlatformTheme (dtkgui) | — | — | [platform-abstraction.md](references/platform-abstraction.md) |
| QWidget 控件 | — | 110+ 控件 | — | [widgets/index.md](references/widgets/index.md) |
| QML 控件 | — | — | 70+ 控件 | [declarative/index.md](references/declarative/index.md) |
| 配置 DConfig | DConfig (dtkcore) | — | D.Config | [config/index.md](references/config/index.md) |
| 工具类 | DLogManager/DDBusInterface 等 (dtkcore+dtklog) | DApplication 单实例 (dtkwidget) | — | [utilities/index.md](references/utilities/index.md) |
