# 集成与构建配置

使用 dde-tray-loader 公开接口前，需要安装对应的开发包。开发包以 header-only 形式提供公开头文件和构建信息。

## 开发包

开发包名为 `dde-tray-loader-dev`。该开发包为 header-only 形式，提供安装在 `dde-tray-loader/` 目录下的公开头文件，以及以下构建入口：

- CMake 包 `DdeTrayLoader` 与导出目标 `Dde::TrayLoader`
- pkg-config 模块 `dde-tray-loader`

## CMake 集成

CMake 是推荐的集成方式。在已有构建目标上查找 `DdeTrayLoader` 并链接 `Dde::TrayLoader`：

```cmake
find_package(DdeTrayLoader REQUIRED)
target_link_libraries(your-plugin PRIVATE Dde::TrayLoader)
```

`Dde::TrayLoader` 会向该目标提供头文件搜索路径，不需要再使用 `include_directories()`。

### 兼容写法

仍受支持的旧写法查找 `DdeDock` 并链接 `Dde::Dock`：

```cmake
find_package(DdeDock REQUIRED)
target_link_libraries(your-plugin PRIVATE Dde::Dock)
```

此写法为兼容方式，新工程应使用 `DdeTrayLoader` 和 `Dde::TrayLoader`。

## 其他受支持的构建入口

### pkg-config

使用 `dde-tray-loader` 模块：

```sh
pkg-config --cflags dde-tray-loader
```

该模块为 header-only，仅提供头文件搜索路径（Cflags），无链接库（Libs）。

兼容旧接口时使用 `dde-dock` 模块：

```sh
pkg-config --cflags dde-dock
```

## 引用公开接口

构建目标链接 dde-tray-loader 后，可以直接包含所需类型的公开头文件：

```cpp
#include <pluginsiteminterface.h>
```

公开类型位于 `Dock` 命名空间。

插件编译为共享库后安装到 `dde-dock/plugins/` 目录。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
