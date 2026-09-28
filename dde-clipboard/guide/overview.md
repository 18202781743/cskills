# dde-clipboard 二次开发文档 · 概览

## 项目定位

dde-clipboard 是 DDE 剪贴板管理工具，包含剪贴板前端界面、剪贴板守护进程和 Dock 剪贴板插件。使用方通过 DBus 接口控制剪贴板界面的显示与隐藏，并监听可见性变化。

## 术语与缩写

- **剪贴板前端**：展示剪贴板历史记录的界面组件。
- **剪贴板守护进程**：监听 Wayland wlr-data-control 协议、管理剪贴板数据的后台进程。
- **Dock 插件**：挂载到 Dock 面板的剪贴板入口插件。
- **DBus 属性**：远端接口上的具名值，使用方可读取或监听变化。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以 DBus 接口名为章节，逐一说明各接口的定位、功能能力和使用场景。

## 全局约定

dde-clipboard 不安装公共开发头文件，不导出 C++ 命名空间或库目标。使用方通过 DBus 接口访问其功能。Dock 剪贴板插件通过 DdeTrayLoader 框架加载，安装到 `lib/dde-dock/plugins` 目录。

## 按功能查阅

- 通过 DBus 控制剪贴板界面显示与隐藏：参见 [org.deepin.dde.Clipboard1](modules.md#orgdeepinddeclipboard1)。
- 监听剪贴板可见性变化：参见 [org.deepin.dde.Clipboard1](modules.md#orgdeepinddeclipboard1)。
