# dde-tray-loader 二次开发文档 · 概览

## 项目定位

dde-tray-loader 是 DDE Dock（任务栏）的插件加载器，以 header-only 形式提供插件接口头文件。第三方开发者通过继承接口类实现自定义 Dock 插件，编译为共享库后安装到 Dock 插件目录，由 Dock 框架在运行时通过 Qt Plugin 机制加载。

## 导出类型

- [插件项接口](plugin-interface.md)涵盖 Dock 插件基础接口（V1）、V2 扩展接口和 V3 卡片 surface 扩展接口，是插件开发者需要实现的核心接口集合。

## 按功能查阅

- 将 dde-tray-loader 引入 CMake 或 pkg-config 工程：参见[插件项接口](plugin-interface.md#集成)。
- 开发 Dock 插件（V1 基础接口）：参见 [PluginsItemInterface](plugin-interface.md#pluginsiteminterface)。
- 使用 V2 扩展能力（插件标志、图标、消息通信）：参见 [PluginsItemInterfaceV2](plugin-interface.md#pluginsiteminterfacev2)。
- 使用 V3 卡片 surface 能力：参见 [PluginsItemInterfaceV3](plugin-interface.md#pluginsiteminterfacev3)。
