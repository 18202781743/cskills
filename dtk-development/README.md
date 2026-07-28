# DTK Development Skill

面向 Deepin、UOS 和 DDE 桌面应用开发的 DTK 指南。该 skill 将 DTK Core、Gui、Widget、Declarative 等模块的常用能力按开发场景组织，便于快速选择正确的 API、控件和实现方式。

## 主要能力

- 创建 DTK 应用并配置 CMake 和模块依赖
- 选择和使用 QWidget、QML 控件
- 处理主题、调色板、字体、DCI 图标和 Chameleon 风格
- 使用 DConfig 管理应用配置
- 集成 DBus、系统通知、日志、单实例和桌面服务
- 处理窗口装饰、模糊效果及平台兼容问题
- 编译、修改和调试 DTK 源码
- 定位多个应用共同出现的 DTK 层问题

## 适合使用的场景

- “帮我创建一个 DTK6 应用”
- “这个 QWidget 怎样跟随深色主题切换颜色？”
- “QML 中怎样使用 DCI 图标？”
- “如何使用 DConfig 保存应用设置？”
- “多个 DDE 应用出现相同显示问题，应该从哪里排查？”

## 文档入口

| 需求 | 文档 |
|------|------|
| DTK 架构与项目关系 | [references/architecture.md](references/architecture.md) |
| 应用创建与构建 | [references/app-dev-with-dtk.md](references/app-dev-with-dtk.md) |
| QWidget 控件 | [references/widgets/index.md](references/widgets/index.md) |
| QML 控件 | [references/declarative/index.md](references/declarative/index.md) |
| 主题与视觉 | [references/theme/index.md](references/theme/index.md) |
| 配置管理 | [references/config/index.md](references/config/index.md) |
| 系统能力与工具类 | [references/utilities/index.md](references/utilities/index.md) |
| DTK 源码调试 | [references/dtksrc-compile-debug.md](references/dtksrc-compile-debug.md) |

完整的任务路由和高频场景入口见 [SKILL.md](SKILL.md)。

## 验证

该 skill 提供 77 个分类测试用例，用于检查文档能否正确指导常见 DTK 开发任务。详见 [evals/README.md](evals/README.md)。
