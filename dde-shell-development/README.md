# DDE Shell Development Skill

面向 `dde-shell` 框架和插件开发的指南，帮助开发者理解 Shell 的插件层次、生命周期、QML/C++ 接口以及 LayerShell 窗口集成方式。

## 主要能力

- 理解 Applet、Containment、Panel 三层插件模型
- 创建纯 QML 或 C++ 后端插件
- 编写插件元数据、CMake 配置和安装规则
- 使用 Shell 提供的 C++ 与 QML API
- 使用 LayerShell 设置窗口锚点、层级、排斥区和键盘交互
- 排查插件扫描、加载、初始化和界面显示问题

## 适合使用的场景

- “为 dde-shell 创建一个 Applet 插件”
- “Containment 和 Panel 有什么区别？”
- “如何把窗口固定在屏幕顶部并保留排斥区？”
- “插件安装后为什么没有被 dde-shell 加载？”
- “如何在 QML 中访问 Applet 或 Panel 上下文？”

## 文档入口

| 需求 | 文档 |
|------|------|
| 架构与设计 | [design.md](design.md) |
| 插件开发流程 | [plugin-development.md](plugin-development.md) |
| LayerShell 窗口 | [layershell.md](layershell.md) |
| API 索引 | [api/index.md](api/index.md) |
| 核心 C++ API | [api/core.md](api/core.md) |
| QML API | [api/qml-api.md](api/qml-api.md) |

完整的任务路由见 [SKILL.md](SKILL.md)。

## 验证

该 skill 提供 19 个分类测试用例，并维护源码 API 验证计划：

- [Evals 说明](evals/README.md)
- [验证计划](verification-plan.md)
