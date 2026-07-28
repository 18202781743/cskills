# DDE Tray Development Skill

面向 DDE 任务栏托盘和快捷面板插件开发的指南，覆盖插件接口、图标与交互、消息通信和菜单实现。

## 主要能力

- 基于 `PluginsItemInterfaceV2` 创建托盘插件
- 实现托盘图标、工具提示和点击交互
- 为快捷面板提供独立控件和状态
- 在插件与任务栏之间传递消息
- 构造和处理右键菜单
- 排查插件加载、显示、排序和交互问题

## 适合使用的场景

- “创建一个显示网络状态的 DDE 托盘插件”
- “给托盘插件增加快捷面板入口”
- “托盘插件怎样接收任务栏发来的消息？”
- “如何动态生成托盘右键菜单？”
- “插件已安装但托盘区域没有显示”

## 文档入口

| 需求 | 文档 |
|------|------|
| 插件接口规范 | [references/tray-plugin-spec.md](references/tray-plugin-spec.md) |
| 快捷面板开发 | [references/quick-panel-guide.md](references/quick-panel-guide.md) |
| 消息协议 | [references/message-protocol.md](references/message-protocol.md) |
| 右键菜单 | [references/context-menu.md](references/context-menu.md) |

完整的任务路由见 [SKILL.md](SKILL.md)。

## 验证

该 skill 提供 13 个分类测试用例。详见 [evals/README.md](evals/README.md)。
