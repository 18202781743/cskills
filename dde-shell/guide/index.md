# dde-shell 二次开发文档 · 概览

## 项目定位

dde-shell 是 DDE Shell 框架库，提供三层插件模型（Applet → Containment → Panel）、元数据驱动的插件发现、Wayland Layer Shell 窗口管理、跨插件通信机制和 Dock 面板插件接口。使用方通过 CMake 集成框架库开发 applet 插件，或通过 Dock 接口开发 Dock 区域插件。

## 导出类型

[插件框架接口](plugin-framework.md)是本项目的 C++ 框架类型参考文档，[Dock 接口](dock-interface.md)是 Dock 面板 C++ 类型参考文档，QML 框架接口见[org.deepin.ds QML 模块](org.deepin.ds.md)，Dock QML 接口见[org.deepin.ds.dock QML 模块](org.deepin.ds.dock.md)。以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 按功能查阅

- 将 dde-shell 框架引入 CMake 工程：参见[插件框架接口](plugin-framework.md)。
- 将 Dock 接口引入 CMake 工程：参见 [Dock 接口](dock-interface.md)。
- 开发 Applet、Containment 或 Panel 插件：参见 [DApplet](plugin-framework.md#dapplet)、[DContainment](plugin-framework.md#dcontainment)、[DPanel](plugin-framework.md#dpanel)。
- 跨插件通信：参见 [DAppletBridge](plugin-framework.md#dappletbridge)。
- 插件发现与加载：参见 [DPluginLoader](plugin-framework.md#dpluginloader)、[DPluginMetaData](plugin-framework.md#dpluginmetadata)。
- Dock 面板插件开发：参见 [DAppletDock](dock-interface.md#dappletdock)、[DockItemInfo](dock-interface.md#dockiteminfo)。
- 使用 QML 模块开发插件界面：参见 [org.deepin.ds](org.deepin.ds.md)。
- 使用 Dock QML 模块开发 Dock 区域插件：参见 [org.deepin.ds.dock](org.deepin.ds.dock.md)。
