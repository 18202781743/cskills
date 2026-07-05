---
name: dde-shell-development
description: |
  dde-shell 开发指南，涵盖插件开发、设计原理、导出 API 参考、LayerShell 独立使用。
  触发场景：
  - 创建 dde-shell 插件（Applet/Containment/Panel）
  - 使用 dde-shell API（DApplet/DContainment/DPanel/DAppletBridge 等）
  - 理解 dde-shell 架构设计
  - 查询 dde-shell 导出 API 接口
  - 独立使用 LayerShell 窗口功能
---

# dde-shell 开发指南

## 入口决策

| 用户意图 | 路由 |
|----------|------|
| 创建插件（Applet/Containment/Panel）、CMake 配置、Debian 打包、跨插件通信 | [plugin-development.md](plugin-development.md) |
| 独立使用 LayerShell 窗口（非插件场景） | [layershell.md](layershell.md) |
| 理解架构设计、加载机制、生命周期 | [design.md](design.md) |
| 查询导出 API 接口 | [api/index.md](api/index.md) |
