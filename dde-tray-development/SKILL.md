---
name: dde-tray-development
description: DDE 托盘插件开发指南，面向任务栏托盘与快捷面板插件的开发和维护，覆盖插件接口、界面与交互、消息与菜单、工程构建及问题排查，并支持插件类型与实现方式选择和加载、显示问题定位。
---

# DDE 托盘插件开发指南

DDE 托盘插件运行在任务栏托盘区域，继承 PluginsItemInterfaceV2 接口，可实现托盘图标、快捷面板控件、右键菜单等功能。

## 快速路由

| 场景 | 参考文档 |
|------|----------|
| 了解托盘插件接口规范 | [references/tray-plugin-spec.md](references/tray-plugin-spec.md) |
| 开发快捷面板插件 | [references/quick-panel-guide.md](references/quick-panel-guide.md) |
| 实现消息协议通信 | [references/message-protocol.md](references/message-protocol.md) |
| 实现右键菜单 | [references/context-menu.md](references/context-menu.md) |

## Evals 测试

验证 skill 有效性的测试用例，按 references 目录分类组织，见 [evals/README.md](evals/README.md)。

### 测试分类

| 目录 | 覆盖范围 | 数量 |
|------|----------|------|
| tray-plugin-spec/ | 托盘插件接口规范 | 4 |
| quick-panel/ | 快捷面板插件 | 3 |
| message-protocol/ | 消息协议 | 3 |
| context-menu/ | 右键菜单 | 3 |

**总计**: 13 个 evals
