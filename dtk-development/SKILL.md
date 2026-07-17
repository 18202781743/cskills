---
name: dtk-development
description: DTK（Deepin Tool Kit）桌面应用开发指南，面向 Deepin/UOS/DDE 应用的开发与维护，覆盖界面与交互、主题与视觉、配置与系统集成、窗口与平台适配、工程构建及问题排查，并支持应用层与 DTK 层的实现选择和共性问题定位。
---

# DTK 开发指南

DTK 是深度桌面环境的核心开发框架，覆盖应用界面与交互、主题与视觉、配置、系统集成、工程构建和源码调试。按功能快速定位对应文档。

## 文档路由

| 场景 | 参考文档 |
|------|----------|
| 了解 DTK 架构、项目关系或定位跨应用共性问题 | [architecture.md](references/architecture.md) |
| 创建 DTK 应用、配置 CMake 与依赖 | [app-dev-with-dtk.md](references/app-dev-with-dtk.md) |
| 修改、编译和调试 DTK 源码 | [dtksrc-compile-debug.md](references/dtksrc-compile-debug.md) |
| 选择和使用 QWidget 控件 | [widgets/index.md](references/widgets/index.md) |
| 选择和使用 QML 控件 | [declarative/index.md](references/declarative/index.md) |
| 查看 QWidget 与 QML 可运行示例 | [examples.md](references/examples.md) |
| 处理主题、配色、图标、字体和控件风格 | [theme/index.md](references/theme/index.md) |
| 处理窗口装饰、模糊效果和平台兼容 | [platform-abstraction.md](references/platform-abstraction.md) |
| 管理应用配置和 DConfig | [config/index.md](references/config/index.md) |
| 使用应用入口、日志、DBus、通知、单实例及系统服务 | [widgets/application.md](references/widgets/application.md)、[utilities/index.md](references/utilities/index.md) |

## 按需加载指南

**仅加载完成任务所需的最少文档**，避免全量搜索。

| 任务类型 | 直接跳转 | 避免加载 |
|----------|----------|----------|
| 使用标准控件 | 控件对应文档（如 `button.md`） | 不要加载 `style.md`、`style-impl.md` |
| 修改控件颜色 | `theme/palette.md` | 不要加载 `style-impl.md` |
| 自绘控件 | `widgets/style.md` | `style-impl.md` 仅在排查问题时加载 |
| 添加配置项 | `config/dconfig-cpp.md` | 不要加载 architecture.md |
| 窗口圆角/模糊 | `platform-abstraction.md` | 不要加载 theme/ 下所有文件 |
| QML 控件使用 | 对应控件文档 | 不要加载 QWidget 文档 |

## 高频场景直达

- **自定义控件使用主题图标** → [theme/palette.md](references/theme/palette.md)
- **QML 中显示 dci 图标** → [declarative/dci-icon.md](references/declarative/dci-icon.md)
- **DGuiApplicationHelper 主题/调色板** → [utilities/gui-helper.md](references/utilities/gui-helper.md)
- **DSysInfo 系统版本判断** → [utilities/sysinfo.md](references/utilities/sysinfo.md)
- **DDBusSender DBus 通信** → [utilities/dbus.md](references/utilities/dbus.md)
- **DWindowManagerHelper 窗口管理** → [utilities/window-manager.md](references/utilities/window-manager.md)
- **QML D.DTK 全局对象** → [declarative/dtk-global.md](references/declarative/dtk-global.md)
- **DBlurEffectWidget 模糊效果** → [widgets/blur-effect.md](references/widgets/blur-effect.md)
- **DStyledItemDelegate 列表项** → [widgets/item-delegate.md](references/widgets/item-delegate.md)
- **DProgressBar 进度条** → [widgets/progress.md](references/widgets/progress.md)
- **DInputDialog 输入对话框** → [widgets/dialog.md](references/widgets/dialog.md)

## Evals 测试用例

验证 skill 有效性的测试用例，共 77 个，按 references 目录分类组织。详见 [evals/README.md](evals/README.md)。

| 前缀 | 目录 | 覆盖范围 | 数量 |
|------|------|----------|------|
| W- | evals/widgets/ | QWidget 控件 | 29 |
| Q- | evals/declarative/ | QML 控件 | 12 |
| T- | evals/theme/ | 主题系统 | 7 |
| C- | evals/config/ | DConfig 配置 | 4 |
| U- | evals/utilities/ | 工具类 | 6 |
| D- | evals/debugging/ | 调试场景 | 5 |
| X- | evals/custom-controls/ | 自定义控件 | 6 |
| P- | evals/project-setup/ | 工程配置 | 1 |
| A- | evals/architecture/ | 架构理解 | 4 |
| L- | evals/platform/ | 平台抽象 | 3 |
