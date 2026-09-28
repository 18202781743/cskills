# 集成与构建配置

使用 dtkgui 公开接口前，需要安装与目标 DTK 主版本对应的开发包。开发包提供公开头文件、链接库以及 CMake、pkg-config 和 qmake 使用的构建信息；通过这些构建信息引入 dtkgui 后，无需手工填写头文件目录、库目录或其传递依赖。

## 开发包

当前版本使用 DTK6，开发包名为 `libdtk6gui-dev`。该开发包提供 DTK6 的公开头文件和以下构建入口：

- CMake 包 `Dtk6Gui` 与导出目标 `Dtk6::Gui`；
- pkg-config 模块 `dtk6gui`；
- qmake 模块 `dtkgui`。

仍需维护 DTK5 工程时，使用兼容开发包 `libdtkgui-dev`。它提供 CMake 包 `DtkGui`、导出目标 `Dtk::Gui`、pkg-config 模块 `dtkgui` 和同名 qmake 模块。

## CMake 集成

CMake 是当前推荐的集成方式。DTK6 工程在已有构建目标上查找 `Dtk6Gui` 并链接 `Dtk6::Gui`：

```cmake
find_package(Dtk6Gui REQUIRED)
target_link_libraries(your_target PRIVATE Dtk6::Gui)
```

`your_target` 替换为使用方工程中的目标名。`Dtk6::Gui` 会向该目标提供 dtkgui 的头文件搜索路径、链接信息、编译定义和传递依赖，不需要再使用 `include_directories()`、`link_directories()` 或逐项链接 dtkgui 所依赖的库。

### DTK5 兼容写法

仍使用 DTK5 的工程改为查找 `DtkGui` 并链接 `Dtk::Gui`：

```cmake
find_package(DtkGui REQUIRED)
target_link_libraries(your_target PRIVATE Dtk::Gui)
```

导出目标是首选写法。为兼容已有工程，包配置仍提供 `DtkGui_LIBRARIES`、`DtkGui_INCLUDE_DIRS`、`DtkGui_LIBRARY_DIRS` 和 `DtkGui_TOOL_DIRS`；旧名称 `DTKGUI_INCLUDE_DIR` 与 `DTKGUI_TOOL_DIR` 也仍可读取。新工程不应使用这些变量代替导出目标。

## 引用公开接口

构建目标链接 dtkgui 后，可以直接包含所需类型的公开转发头：

```cpp
#include <DPalette>
```

也可以包含对应的实际公开头文件，例如 `#include <dpalette.h>`。公开类型主要位于 `Dtk::Gui` 命名空间，可使用完整限定名，也可在合适的作用域使用 `DGUI_USE_NAMESPACE`。开发包还提供便捷头 `DtkGuis`，一次引入所有已安装的公开头文件。

## 其他受支持的构建入口

无法使用 CMake 导出目标时，可以读取开发包提供的 pkg-config 或 qmake 元数据。这些入口会给出相应主版本的头文件搜索路径、链接参数和编译定义。

### pkg-config

DTK6 使用 `dtk6gui` 模块：

```sh
pkg-config --cflags --libs dtk6gui
```

将 `--cflags` 与 `--libs` 的结果分别用于编译和链接阶段。DTK5 兼容工程将模块名改为 `dtkgui`。

### qmake

在与所选 DTK 主版本配套的 qmake 工程中添加：

```qmake
QT += dtkgui
```

qmake 模块名在 DTK6 与 DTK5 中保持不变，实际头文件路径和链接库由对应版本的模块元数据提供。

## 主版本选择

新工程优先使用 DTK6 的开发包、构建包名和导出目标。维护 DTK5 工程时，应成套使用 DTK5 的开发包和构建信息；同一构建目标不要混用两个主版本的头文件、CMake 目标或 pkg-config 参数。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
