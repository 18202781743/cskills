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
| QWidget 控件 | [widgets/index.md](references/widgets/index.md) |
| QML 控件 | [declarative/index.md](references/declarative/index.md) |
| 主题系统 | [theme-system.md](references/theme-system.md) |
| DConfig 配置管理 | [config-system.md](references/config-system.md) |
| 窗口装饰、模糊效果 | [platform-integration.md](references/platform-integration.md) |
| 工具类速查 | [utilities.md](references/utilities.md) |
| 可运行示例 | [examples.md](references/examples.md) |

## 高频场景直达

- **自定义控件绘制** → [widgets/style.md](references/widgets/style.md)
- **QML ColorSelector 取色器** → [declarative/color-selector.md](references/declarative/color-selector.md)
- **DPalette 调色板** → [theme/palette.md](references/theme/palette.md)
- **DCI 图标** → [theme/dci.md](references/theme/dci.md)
- **QWidget Chameleon 风格** → [widgets/chameleon.md](references/widgets/chameleon.md)
- **QML Chameleon 风格** → [declarative/chameleon.md](references/declarative/chameleon.md)

## Evals 测试用例

验证 skill 有效性的测试用例，共 77 个，按功能模块分类。详见 [evals/](evals/)。
