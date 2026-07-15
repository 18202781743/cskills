---
name: dde-shell-development
description: dde-shell 开发指南，面向 DDE Shell 插件与 LayerShell 窗口的开发和维护，覆盖插件体系、架构设计、界面与窗口集成、工程构建及问题排查，并支持插件类型与实现方式选择、框架接口使用和加载问题定位。
---

# dde-shell 开发指南

## 入口决策

| 用户意图 | 路由 |
|----------|------|
| 创建插件（Applet/Containment/Panel）、CMake 配置、Debian 打包、跨插件通信 | [plugin-development.md](plugin-development.md) |
| 独立使用 LayerShell 窗口（非插件场景） | [layershell.md](layershell.md) |
| 理解架构设计、加载机制、生命周期 | [design.md](design.md) |
| 查询导出 API 接口 | [api/index.md](api/index.md) |
