---
name: dde-control-center
description: |
  DDE 控制中心开发指南，涵盖创建新控制中心插件、控制中心设计原理、插件开发与调试、Bug 修复。
  触发场景：
  - 开发控制中心新插件
  - 理解控制中心架构与设计原理
  - 修改控制中心框架代码
  - 控制中心插件中的 Bug 修复
  - 控制中心插件加载失败、不显示、搜索不生效等问题的定位
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

## 相关代码仓库

- 控制中心框架：https://github.com/linuxdeepin/dde-control-center
- 示例插件：`examples/plugin-example/`
