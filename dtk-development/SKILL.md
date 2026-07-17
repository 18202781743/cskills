---
name: dtk-development
description: DTK（Deepin Tool Kit）桌面应用开发指南，面向 Deepin/UOS/DDE 应用的开发与维护，覆盖界面与交互、主题与视觉、配置与系统集成、窗口与平台适配、工程构建及问题排查。
---

# DTK 开发指南

DTK 是深度桌面环境的核心开发框架，覆盖应用界面与交互、主题与视觉、配置、系统集成、工程构建和源码调试。按功能快速定位对应文档。

## 文档路由

| 场景 | 参考文档 |
|------|----------|
| DTK 架构与核心系统 | [architecture.md](references/architecture.md) |
| 创建项目、CMake 配置 | [project-setup.md](references/project-setup.md) |
| QWidget 控件概览 | [widgets-overview.md](references/widgets-overview.md) |
| QML 控件概览 | [declarative-overview.md](references/declarative-overview.md) |
| 主题系统概览 | [theme-system.md](references/theme-system.md) |
| DConfig 配置管理 | [config-system.md](references/config-system.md) |
| 窗口装饰、模糊效果 | [platform-integration.md](references/platform-integration.md) |
| 工具类速查 | [utilities.md](references/utilities.md) |
| 可运行示例 | [examples.md](references/examples.md) |

## 详细参考文档

| 分类 | 文档 |
|------|------|
| **QWidget 控件** | |
| 按钮 | [widgets-button.md](references/widgets-button.md) |
| 对话框 | [widgets-dialog.md](references/widgets-dialog.md) |
| 输入控件 | [widgets-input.md](references/widgets-input.md) |
| 窗口 | [widgets-window.md](references/widgets-window.md) |
| 列表项委托 | [widgets-item-delegate.md](references/widgets-item-delegate.md) |
| 模糊效果 | [widgets-blur-effect.md](references/widgets-blur-effect.md) |
| DStyle 风格 | [widgets-style.md](references/widgets-style.md) |
| **QML 控件** | |
| ColorSelector | [declarative-color-selector.md](references/declarative-color-selector.md) |
| DCI 图标 | [declarative-dci-icon.md](references/declarative-dci-icon.md) |
| D.DTK 全局对象 | [declarative-dtk-global.md](references/declarative-dtk-global.md) |
| 对话框 | [declarative-dialogs.md](references/declarative-dialogs.md) |
| **主题系统** | |
| DPalette 调色板 | [theme-palette.md](references/theme-palette.md) |
| DCI 图标格式 | [theme-dci.md](references/theme-dci.md) |
| Chameleon 风格 | [theme-chameleon.md](references/theme-chameleon.md) |

## Evals 测试用例

验证 skill 有效性的测试用例，共 77 个，按功能模块分类。详见 [evals/](evals/)。
