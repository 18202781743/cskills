# dde-tray-loader 二次开发文档 · 概览

## 项目定位

dde-tray-loader 是 DDE Dock（任务栏）的插件加载器，以 header-only 形式提供插件接口头文件。第三方开发者通过继承接口类实现自定义 Dock 插件，编译为共享库后安装到 Dock 插件目录，由 Dock 框架在运行时通过 Qt Plugin 机制加载。

dde-tray-loader 同时提供插件代理接口和插件管理器接口，分别用于插件与 Dock 框架的双向通信以及编程方式的插件加载与查询。

## 术语与缩写

- **header-only**：仅提供头文件、不提供编译库文件的发布形式，使用方包含头文件即可使用接口，无需链接额外的共享库。
- **Dock 插件**：挂载到 DDE Dock 任务栏区域的插件模块，通过实现 PluginsItemInterface 及其扩展接口提供 UI 部件和交互能力。
- **插件代理**：插件通过 PluginProxyInterface 与 Dock 框架进行通信的中间层，用于通知框架项变化、请求窗口行为和持久化配置。
- **插件管理器**：通过 PluginManagerInterface 提供的编程式插件加载与查询能力。
- **IID**：Qt Plugin 机制中的接口标识符，Dock 框架通过 IID 区分不同版本的插件接口。
- **卡片 surface**：V3 接口引入的插件卡片区域能力，插件可将原生窗口导出为 Wayland surface 在 Dock 卡片区展示。

## 全局约定

公开头文件安装在系统头文件目录的 `dde-dock/` 子目录下，使用方通过 CMake 或 pkg-config 集成后可直接包含。公开类型位于 `Dock` 命名空间。

插件通过 Qt Plugin 机制加载，声明 IID 标识接口版本：

- V1 接口 IID 为 `com.deepin.dock.PluginsItemInterface`
- V2 接口 IID 为 `com.deepin.dock.PluginsItemInterface_V2`
- V3 接口 IID 为 `com.deepin.dock.PluginsItemInterface_V3`

插件编译为共享库后安装到 `dde-dock/plugins/` 目录，Dock 框架在启动时扫描该目录并加载符合接口版本的插件。

API 版本号为 2.0.0，V2 接口方法标注 `@since 2.0.0`。插件可在编译期通过 `DOCK_API_VERSION` 宏和 `DOCK_API_VERSION_CHECK` 宏比对版本号，判断接口兼容性。

## 按功能查阅

- 将 dde-tray-loader 引入 CMake 或 pkg-config 工程：参见[集成与构建配置](integration.md)。
- 开发 Dock 插件（V1 基础接口）：参见 [PluginsItemInterface](dde-tray-loader-dev.md#pluginsiteminterface)。
- 使用 V2 扩展能力（插件标志、图标、消息通信）：参见 [PluginsItemInterfaceV2](dde-tray-loader-dev.md#pluginsiteminterfacev2)。
- 使用 V3 卡片 surface 能力：参见 [PluginsItemInterfaceV3](dde-tray-loader-dev.md#pluginsiteminterfacev3)。
- 插件与 Dock 框架通信（项增删、窗口行为、配置持久化）：参见 [PluginProxyInterface](dde-tray-loader-dev.md#pluginproxyinterface)。
- 编程方式加载和查询插件：参见 [PluginManagerInterface](dde-tray-loader-dev.md#pluginmanagerinterface)。
