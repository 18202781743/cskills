# 集成与构建配置

使用 dde-control-center 公开接口前，需要安装开发包 `dde-control-center-dev`。该开发包提供公开头文件、链接库以及 CMake 构建信息。

## 开发包

当前版本使用开发包 `dde-control-center-dev`。该开发包提供：

- 公共头文件，安装路径 `${CMAKE_INSTALL_INCLUDEDIR}/dde-control-center`
- 链接库 `libdde-control-center.so`
- CMake 包 `DdeControlCenter` 与导出目标 `Dde::Control-Center`

## CMake 集成

CMake 是当前推荐的集成方式。在已有构建目标上查找 `DdeControlCenter` 并链接 `Dde::Control-Center`：

```cmake
find_package(DdeControlCenter REQUIRED)
target_link_libraries(your-plugin PRIVATE Dde::Control-Center)
```

`Dde::Control-Center` 会向该目标提供 dde-control-center 的头文件搜索路径和链接信息，不需要再使用 `include_directories()`、`link_directories()` 或逐项链接依赖库。

开发包还提供以下 CMake 变量：

- `DDE_CONTROL_CENTER_PLUGIN_VERSION`：插件版本（1.1）
- `DDE_CONTROL_CENTER_PLUGIN_DIR`：插件目录名（plugins_v1.1）
- `DDE_CONTROL_CENTER_PLUGIN_INSTALL_DIR`：插件安装完整路径
- `DDE_CONTROL_CENTER_TRANSLATION_INSTALL_DIR`：翻译文件安装路径

## 构建与安装插件

开发包提供以下 CMake 宏用于构建和安装插件：

- `dcc_build_plugin(NAME <name> TARGET <target> [QML_ROOT_DIR <dir>] [QML_FILES <files...>] [RESOURCE_FILES <files...>])`：构建插件的 QML 模块和 C++ 库，自动处理 QML 资源。`NAME` 指定插件名（仅允许字母和数字），`TARGET` 指定 C++ 库目标名，`QML_ROOT_DIR` 指定 QML 文件根目录（默认为 `${CMAKE_CURRENT_SOURCE_DIR}/qml`），`QML_FILES` 和 `RESOURCE_FILES` 可显式指定 QML 文件和资源文件（未指定时自动搜索）。
- `dcc_install_plugin(NAME <name> TARGET <target> [QML_ROOT_DIR <dir>] [QML_FILES <files...>] [RESOURCE_FILES <files...>])`：调用 `dcc_build_plugin` 完成构建后，额外将 `TARGET` 指定的 C++ 库安装到插件目录。
- `dcc_handle_plugin_translation(NAME <name> [SOURCE_DIR <dir>] [QML_FILES <files...>] [SOURCE_FILES <files...>])`：处理插件翻译，生成 `.ts` 翻译源文件和 `.qm` 编译翻译文件并安装。`NAME` 指定插件名，`SOURCE_DIR` 指定源文件根目录（默认为 `${CMAKE_CURRENT_SOURCE_DIR}`），`QML_FILES` 和 `SOURCE_FILES` 可显式指定 QML 文件和源文件（未指定时自动搜索）。

插件安装路径为 `${CMAKE_INSTALL_LIBDIR}/dde-control-center/plugins_v1.1/<plugin-name>/`，翻译文件安装路径为 `${CMAKE_INSTALL_DATAROOTDIR}/dde-control-center/translations/v1.1/`。

## QML 模块集成

控制中心 QML 模块 URI 为 `org.deepin.dcc`，导入版本为 `1.0`。该模块为 STATIC 模块，由控制中心运行时提供，使用方无需安装额外的 QML 模块包。在 QML 文件中通过以下方式导入：

```qml
import org.deepin.dcc 1.0
```

导入后可使用 `DccObject`、`DccModel`、`DccRepeater`、`DccDBusInterface`、`Repeater` 以及控制中心提供的 QML 组件类型。`DccApp` 单例在控制中心运行时注册到该 URI，可直接在 QML 中访问。

## 引用公开接口

构建目标链接 dde-control-center 后，可以直接包含所需类型的公开头文件：

```cpp
#include <dccfactory.h>
```

公开类型位于 `dccV25` 命名空间，可使用完整限定名，也可在合适的作用域使用 `using namespace dccV25`。

## 关联文档

- 插件工厂接口的能力与使用场景见[插件工厂接口](plugin-factory.md)。
- QML 导出类型的能力与使用场景见[org.deepin.dcc QML 模块](org.deepin.dcc.md)。
