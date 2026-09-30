# 插件管理器接口

dde-tray-loader 提供插件管理器接口，支持以编程方式枚举已加载的 Dock 插件、查询插件的项标识和元数据，以及在所有插件加载完成后接收通知信号。该接口供需要在运行时感知和管理插件状态的应用程序使用。接口以 header-only 形式发布，使用方包含头文件即可使用。

## 开发包

使用 dde-tray-loader 公开接口前，需要安装开发包 `dde-tray-loader-dev`。该开发包以 header-only 形式提供公开头文件和构建配置信息，不提供编译库文件。

## 集成

### CMake 配置

CMake 是推荐的集成方式。查找 `DdeTrayLoader` 包后，配置脚本会自动将 `dde-dock/` 头文件目录添加到全局包含路径，无需手动设置 `include_directories()` 或 `target_link_libraries()`：

```cmake
find_package(DdeTrayLoader REQUIRED)
```

由于开发包为 header-only 形式，不提供编译库文件，也不创建任何 IMPORTED 目标，因此不需要链接步骤。仍受支持的旧写法可查找 `DdeDock` 包，同样会自动添加头文件包含路径，此写法为兼容方式，新工程应使用 `DdeTrayLoader` 包。

开发包同时提供 pkg-config 模块 `dde-dock`，其 Cflags 指向 `dde-dock/` 头文件目录，提供所有公开接口头文件的搜索路径，无链接库（Libs）。

### 使用方式

在 C++ 源文件中通过以下方式引入公开头文件：

```cpp
#include <pluginmanagerinterface.h>
```

PluginManagerInterface 位于全局命名空间，继承自 QObject。使用方通过框架提供的插件管理器实例调用接口方法，枚举已加载的插件并查询插件信息。

## 模块API介绍

### PluginManagerInterface

#### 定位

插件管理器接口，提供插件加载和查询能力。位于全局命名空间，继承自 QObject。

#### 功能能力总结

- 枚举已加载的插件：查询所有已加载的插件列表、查询在控制中心设置中显示的插件列表、查询当前正在使用的插件列表
- 获取指定插件接口对象的项标识和元数据（JSON 格式），用于在编程层面识别和检视插件
- 在所有插件加载完成后发出通知信号，便于依赖其他插件就绪状态的后续操作

#### 使用场景

需要以编程方式查询已加载的插件、设置中的插件或当前使用的插件时，使用 plugins、pluginsInSetting 和 currentPlugins。需要获取插件的 itemKey 或元数据时，使用 itemKey 和 metaData。需要在插件加载完成后执行后续操作时，连接 pluginLoadFinished 信号。
