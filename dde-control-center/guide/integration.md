# 集成与构建配置

使用 dde-control-center 公开接口前，需要安装开发包 `dde-control-center-dev`。该开发包提供公开头文件、链接库以及 CMake 构建信息。

## 开发包

当前版本使用开发包 `dde-control-center-dev`。该开发包提供：

- 公共头文件，安装路径 `${CMAKE_INSTALL_INCLUDEDIR}/dde-control-center`
- 链接库 `libdde-control-center_frame.so`
- CMake 包 `DdeControlCenter` 与导出目标 `Dde::ControlCenter`

## CMake 集成

CMake 是当前推荐的集成方式。在已有构建目标上查找 `DdeControlCenter` 并链接 `Dde::ControlCenter`：

```cmake
find_package(DdeControlCenter REQUIRED)
target_link_libraries(your-plugin PRIVATE Dde::ControlCenter)
```

`Dde::ControlCenter` 会向该目标提供 dde-control-center 的头文件搜索路径和链接信息，不需要再使用 `include_directories()`、`link_directories()` 或逐项链接依赖库。

开发包还提供以下 CMake 变量：

- `DDE_CONTROL_CENTER_PLUGIN_VERSION`：插件版本（1.1）
- `DDE_CONTROL_CENTER_PLUGIN_DIR`：插件目录名（plugins_v1.1）
- `DDE_CONTROL_CENTER_PLUGIN_INSTALL_DIR`：插件安装完整路径
- `DDE_CONTROL_CENTER_TRANSLATION_INSTALL_DIR`：翻译文件安装路径

## 构建与安装插件

开发包提供以下 CMake 宏用于构建和安装插件：

- `dcc_build_plugin(NAME <name> TARGET <target> ...)`：构建插件，自动处理 QML 资源
- `dcc_install_plugin(...)`：安装插件到控制中心插件目录
- `dcc_handle_plugin_translation(PACKAGE <name>)`：处理插件翻译

插件安装路径为 `${CMAKE_INSTALL_LIBDIR}/dde-control-center/plugins_v1.1/<plugin-name>/`，翻译文件安装路径为 `${CMAKE_INSTALL_DATAROOTDIR}/dde-control-center/translations/v1.1/`。

## 引用公开接口

构建目标链接 dde-control-center 后，可以直接包含所需类型的公开头文件：

```cpp
#include <dccfactory.h>
```

公开类型位于 `dccV25` 命名空间，可使用完整限定名，也可在合适的作用域使用 `using namespace dccV25`。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
