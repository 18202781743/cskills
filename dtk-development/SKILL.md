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
| QWidget 控件选择与使用 | [widgets-overview.md](references/widgets-overview.md) |
| QML 控件选择与使用 | [declarative-overview.md](references/declarative-overview.md) |
| 主题、调色板、DCI 图标 | [theme-system.md](references/theme-system.md) |
| DConfig 配置管理 | [config-system.md](references/config-system.md) |
| 窗口装饰、模糊效果、平台适配 | [platform-integration.md](references/platform-integration.md) |
| 应用入口、DBus、日志、系统信息 | [utilities.md](references/utilities.md) |
| 可运行示例 | [examples.md](references/examples.md) |

## Evals 测试用例

验证 skill 有效性的测试用例，共 77 个，按功能模块分类。详见 [evals/](evals/)。
