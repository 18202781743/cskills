---
name: dde-shell-development
description: dde-shell 开发指南，面向 DDE Shell 插件与 LayerShell 窗口的开发和维护，覆盖插件体系、架构设计、界面与窗口集成、工程构建及问题排查，并支持插件类型与实现方式选择、框架接口使用和加载问题定位。
---

# dde-shell 开发指南

dde-shell 是 DDE 桌面环境的 Shell 核心，负责 Dock、顶栏、侧栏等面板的插件化管理。采用三层插件模型（Applet → Containment → Panel），支持 QML 界面和 C++ 后端。

## 快速路由

| 场景 | 参考文档 |
|------|----------|
| 了解 dde-shell 架构与设计原理 | [design.md](design.md) |
| 开发 Applet/Containment/Panel 插件 | [plugin-development.md](plugin-development.md) |
| 使用 LayerShell 锚定窗口 | [layershell.md](layershell.md) |
| 查找 C++ 和 QML API | [api/index.md](api/index.md) |

## Evals 测试用例

验证 skill 有效性的测试用例，共 19 个，按功能模块分类组织。详见 [evals/README.md](evals/README.md)。
