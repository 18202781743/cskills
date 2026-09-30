# dde-tray-loader 二次开发文档 · 概览

## 项目定位

dde-tray-loader 是 DDE Dock（任务栏）的插件加载器，以 header-only 形式提供插件接口头文件。第三方开发者通过继承接口类实现自定义 Dock 插件，编译为共享库后安装到 Dock 插件目录，由 Dock 框架在运行时通过 Qt Plugin 机制加载。dde-tray-loader 同时提供插件代理接口和插件管理器接口，分别用于插件与 Dock 框架的双向通信以及编程方式的插件加载与查询。

## 导出类型

- [插件项接口](plugin-interface.md)涵盖 Dock 插件基础接口（V1）、V2 扩展接口和 V3 卡片 surface 扩展接口，是插件开发者需要实现的核心接口集合。
- [插件代理接口](plugin-proxy.md)涵盖插件与 Dock 框架通信的代理接口，插件通过此接口通知框架项变化、请求窗口行为和持久化配置。
- [插件管理器接口](plugin-manager.md)涵盖编程式插件加载与查询接口，用于枚举已加载插件和获取插件元数据。

## 按功能查阅

- 将 dde-tray-loader 引入 CMake 或 pkg-config 工程：参见[插件项接口](plugin-interface.md#集成)。
- 开发 Dock 插件（V1 基础接口）：参见 [PluginsItemInterface](plugin-interface.md#pluginsiteminterface)。
- 使用 V2 扩展能力（插件标志、图标、消息通信）：参见 [PluginsItemInterfaceV2](plugin-interface.md#pluginsiteminterfacev2)。
- 使用 V3 卡片 surface 能力：参见 [PluginsItemInterfaceV3](plugin-interface.md#pluginsiteminterfacev3)。
- 插件与 Dock 框架通信（项增删、窗口行为、配置持久化）：参见 [PluginProxyInterface](plugin-proxy.md#pluginproxyinterface)。
- 编程方式加载和查询插件：参见 [PluginManagerInterface](plugin-manager.md#pluginmanagerinterface)。
