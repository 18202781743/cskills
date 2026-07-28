# DDE Control Center Development Skill

面向 DDE 控制中心框架和插件开发的指南。该 skill 介绍控制中心的插件化架构，并提供创建插件、使用 C++/QML API、构建安装和调试加载问题所需的参考资料。

## 主要能力

- 理解控制中心模块树、导航、搜索和页面加载机制
- 从零创建 C++、QML 或混合控制中心插件
- 使用 `DccObject`、`DccApp`、`DccFactory` 等核心接口
- 使用 DccGroupView、DccRepeater、DccDBusInterface 等 QML 组件
- 处理数据绑定、DBus 调用、翻译、安装与 Debian 打包
- 调试插件搜索路径、动态库、QML 模块和缓存问题

## 适合使用的场景

- “为控制中心新增一个设置模块”
- “DccObject 的 pageType 应该怎样选择？”
- “控制中心 QML 页面怎样调用 DBus？”
- “插件如何加入搜索和导航？”
- “使用 `--spec` 调试插件时为什么仍然加载旧文件？”

## 文档入口

| 需求 | 文档 |
|------|------|
| 架构与设计 | [references/architecture.md](references/architecture.md) |
| 插件开发流程 | [references/plugin-development.md](references/plugin-development.md) |
| C++ API | [references/cpp-api.md](references/cpp-api.md) |
| QML API | [references/qml-api.md](references/qml-api.md) |
| 调试与排错 | [references/debugging.md](references/debugging.md) |

完整的任务路由见 [SKILL.md](SKILL.md)。

## 验证

该 skill 提供 21 个分类测试用例，并维护逐项源码验证计划：

- [Evals 说明](evals/README.md)
- [验证计划](verification-plan.md)
