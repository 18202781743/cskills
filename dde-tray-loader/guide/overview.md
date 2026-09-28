# dde-tray-loader 二次开发文档 · 概览

## 项目定位

dde-tray-loader 是 DDE 托盘/Dock 插件加载器，提供 header-only 接口头文件，允许第三方开发 Dock 托盘插件。使用方通过 CMake 或 pkg-config 集成头文件，继承插件接口类实现自定义 Dock 插件。

## 术语与缩写

- **header-only**：仅提供头文件、不提供编译库文件的发布形式。
- **Dock 插件**：挂载到 Dock 任务栏区域的插件模块。
- **插件代理**：插件通过代理接口与 Dock 框架通信。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 全局约定

公开头文件安装在 `dde-tray-loader/` 目录下。公开类型位于 `Dock` 命名空间。插件通过 Qt Plugin 机制加载，使用 `Q_PLUGIN_METADATA` 声明 IID `com.deepin.dock.PluginsItemInterface`。插件安装到 `dde-dock/plugins/` 目录。

## 按功能查阅

- 将 dde-tray-loader 引入 CMake 或 pkg-config 工程：参见[集成与构建配置](integration.md)。
- 开发 Dock 插件：参见 [PluginsItemInterface](modules.md#pluginsiteminterface)、[PluginsItemInterfaceV2](modules.md#pluginsiteminterfacev2)、[PluginsItemInterfaceV3](modules.md#pluginsiteminterfacev3)。
- 插件与 Dock 框架通信：参见 [PluginProxyInterface](modules.md#pluginproxyinterface)。
- 插件管理：参见 [PluginManagerInterface](modules.md#pluginmanagerinterface)。
