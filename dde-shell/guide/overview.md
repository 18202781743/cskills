# dde-shell 二次开发文档 · 概览

## 项目定位

dde-shell 是 DDE Shell 框架库，提供三层插件模型（Applet → Containment → Panel）、元数据驱动的插件发现、Wayland Layer Shell 窗口管理、跨插件通信机制和 Dock 面板插件接口。使用方通过 CMake 集成框架库开发 applet 插件，或通过 Dock 接口开发 Dock 区域插件。

## 术语与缩写

- **Applet**：最基础的功能部件插件类型，不含子插件。
- **Containment**：容器插件类型，可管理子 Applet。
- **Panel**：顶级面板插件类型，继承自 Containment，管理窗口，可含子插件。
- **metadata.json**：插件元数据文件，描述插件 ID、版本、入口和父子关系。
- **Layer Shell**：Wayland 协议中用于实现面板、锁屏这类覆盖层窗口的协议。
- **DConfig**：DDE 配置中心，插件可通过其读写配置。
- **插件 ID**：以反向域名格式标识的插件唯一标识。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 全局约定

公开头文件安装在 `dde-shell/` 目录下。主要公开符号位于 `ds` 命名空间（`DS_NAMESPACE`），使用 `DS_USE_NAMESPACE` 引入。插件通过 `D_APPLET_CLASS` 宏注册，框架通过 `QPluginLoader` 加载 `.so` 文件。插件包资源安装到 `share/dde-shell/` 目录，插件库安装到 `lib/dde-shell/` 目录。QML 模块 URI 为 `org.deepin.ds`，导入版本 1.0。

## 按功能查阅

- 将 dde-shell 引入 CMake 工程：参见[集成与构建配置](integration.md)。
- 开发 Applet、Containment 或 Panel 插件：参见 [DApplet](modules.md#dapplet)、[DContainment](modules.md#dcontainment)、[DPanel](modules.md#dpanel)。
- 跨插件通信：参见 [DAppletBridge](modules.md#dappletbridge)。
- 插件发现与加载：参见 [DPluginLoader](modules.md#dpluginloader)、[DPluginMetaData](modules.md#dpluginmetadata)。
- Dock 面板插件开发：参见 [DAppletDock](modules.md#dappletdock)、[DockItemInfo](modules.md#dockiteminfo)。
- QML 模块使用：参见 [org.deepin.ds](modules.md#orgdeepinds)。
- 插件安装宏：参见[集成与构建配置](integration.md)。
