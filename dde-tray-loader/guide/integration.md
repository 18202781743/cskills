# 集成与构建配置

使用 dde-tray-loader 公开接口前，需要安装对应的开发包。开发包以 header-only 形式提供公开头文件和构建信息，不提供编译库文件。

## 开发期依赖

使用方编译 Dock 插件所需安装的本项目开发包为 `dde-tray-loader-dev`。该开发包为 header-only 形式，提供以下内容：

- 公开头文件，安装在系统头文件目录的 `dde-dock/` 子目录下
- Wayland 协议描述文件，安装在 `dde-tray-loader/protocol/` 子目录下
- CMake 配置包 `DdeTrayLoader`，安装在 `cmake/DdeTrayLoader/` 目录下
- pkg-config 模块 `dde-tray-loader` 和 `dde-dock`，安装在 `pkgconfig/` 目录下

## CMake 集成

CMake 是推荐的集成方式。查找 `DdeTrayLoader` 包后，配置脚本会自动将 `dde-dock/` 头文件目录添加到全局包含路径，无需手动设置 `include_directories()` 或 `target_link_libraries()`：

```cmake
find_package(DdeTrayLoader REQUIRED)
```

由于开发包为 header-only 形式，不提供编译库文件，因此不需要链接任何导入目标。`find_package` 执行后即可直接包含公开头文件。

### 兼容写法

仍受支持的旧写法查找 `DdeDock` 包，同样会自动添加头文件包含路径：

```cmake
find_package(DdeDock REQUIRED)
```

此写法为兼容方式，新工程应使用 `DdeTrayLoader` 包。

## pkg-config

使用 `dde-dock` 模块获取 API 头文件搜索路径：

```sh
pkg-config --cflags dde-dock
```

该模块的 Cflags 指向 `dde-dock/` 头文件目录，提供所有公开接口头文件的搜索路径，无链接库（Libs）。

`dde-tray-loader` 模块提供 Wayland 协议描述文件的搜索路径，其 Cflags 指向 `dde-tray-loader/` 目录，可用于包含协议 XML 文件。如需同时引用 API 头文件和协议文件，可组合使用两个模块：

```sh
pkg-config --cflags dde-dock dde-tray-loader
```

## 引用公开接口

集成开发包后，可以直接包含所需类型的公开头文件：

```cpp
#include <pluginsiteminterface.h>
```

其他公开头文件包括 `pluginsiteminterface_v2.h`、`pluginsiteminterface_v3.h`、`pluginproxyinterface.h`、`pluginmanagerinterface.h`、`constants.h`、`common.h`。辅助类型（枚举与常量）位于 `Dock` 命名空间，接口类位于全局命名空间。

插件编译为共享库后安装到 `dde-dock/plugins/` 目录。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](dde-tray-loader-dev.md)。
