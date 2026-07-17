---
name: dde-control-center
description: DDE 控制中心开发指南，面向控制中心框架与插件的开发和维护，覆盖架构设计、插件开发、界面与数据交互、工程构建及问题排查，并支持框架与插件层的实现选择和共性问题定位。
---

# DDE 控制中心开发指南

DDE 控制中心（dde-control-center）是 DDE 桌面环境的系统设置面板，采用插件化架构，框架只负责模块树管理、导航、搜索和页面布局，所有具体功能均由插件实现。

## 快速路由

| 场景 | 参考文档 |
|------|----------|
| 了解控制中心架构与设计原理 | [references/architecture.md](references/architecture.md) |
| 从零开始创建新插件（CMake、打包、翻译、安装） | [references/plugin-development.md](references/plugin-development.md) |
| 查找 C++ API（DccObject、DccApp、DccFactory 等） | [references/cpp-api.md](references/cpp-api.md) |
| 查找 QML 组件（DccGroupView、DccRepeater、DccDBusInterface 等） | [references/qml-api.md](references/qml-api.md) |
| 调试技巧与常见问题排查 | [references/debugging.md](references/debugging.md) |

## Evals 测试用例

验证 skill 有效性的测试用例，共 21 个，按功能模块分类组织。详见 [evals/README.md](evals/README.md)。

## 相关代码仓库

- 控制中心框架：https://github.com/linuxdeepin/dde-control-center
- 示例插件：`examples/plugin-example/`
