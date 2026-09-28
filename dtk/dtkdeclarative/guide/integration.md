# 集成与构建配置

使用 dtkdeclarative 公开接口前，需要安装与目标 DTK 主版本对应的开发包。开发包提供公开头文件、链接库以及 CMake、pkg-config 和 qmake 使用的构建信息；通过这些构建信息引入 dtkdeclarative 后，无需手工填写头文件目录、库目录或其传递依赖。

## 开发包

当前版本使用 DTK6，开发包名为 `libdtk6declarative-dev`。该开发包提供 DTK6 的公开头文件和以下构建入口：

- CMake 包 `Dtk6Declarative` 与导出目标 `Dtk6::Declarative`；
- pkg-config 模块 `dtk6declarative`；
- qmake 模块 `dtkdeclarative`。

仍需维护 DTK5 工程时，使用兼容开发包 `libdtkdeclarative-dev`。它提供 CMake 包 `DtkDeclarative`、导出目标 `Dtk::Declarative`、pkg-config 模块 `dtkdeclarative` 和同名 qmake 模块。

## CMake 集成

CMake 是当前推荐的集成方式。DTK6 工程在已有构建目标上查找 `Dtk6Declarative` 并链接 `Dtk6::Declarative`：

```cmake
find_package(Dtk6Declarative REQUIRED)
target_link_libraries(your_target PRIVATE Dtk6::Declarative)
```

`your_target` 替换为使用方工程中的目标名。`Dtk6::Declarative` 会向该目标提供 dtkdeclarative 的头文件搜索路径、链接信息、编译定义和传递依赖，不需要再使用 `include_directories()`、`link_directories()` 或逐项链接 dtkdeclarative 所依赖的库。

### DTK5 兼容写法

仍使用 DTK5 的工程改为查找 `DtkDeclarative` 并链接 `Dtk::Declarative`：

```cmake
find_package(DtkDeclarative REQUIRED)
target_link_libraries(your_target PRIVATE Dtk::Declarative)
```

导出目标是首选写法。为兼容已有工程，包配置仍提供 `DtkDeclarative_LIBRARIES`、`DtkDeclarative_INCLUDE_DIRS`、`DtkDeclarative_LIBRARY_DIRS` 以及 `DTKDeclarative_INCLUDE_DIR` 变量。新工程不应使用这些变量代替导出目标。

## 引用公开接口

构建目标链接 dtkdeclarative 后，可以直接包含所需类型的公开转发头：

```cpp
#include <DAppLoader>
```

也可以包含对应的实际公开头文件，例如 `#include <dapploader.h>`。公开 C++ 类型主要位于 `Dtk::Quick` 命名空间。QML 控件通过 `org.deepin.dtk` QML 模块使用，无需在 C++ 中包含头文件。

## 其他受支持的构建入口

无法使用 CMake 导出目标时，可以读取开发包提供的 pkg-config 或 qmake 元数据。

### pkg-config

DTK6 使用 `dtk6declarative` 模块：

```sh
pkg-config --cflags --libs dtk6declarative
```

将 `--cflags` 与 `--libs` 的结果分别用于编译和链接阶段。DTK5 兼容工程将模块名改为 `dtkdeclarative`。

### qmake

在与所选 DTK 主版本配套的 qmake 工程中添加：

```qmake
QT += dtkdeclarative
```

qmake 模块名在 DTK6 与 DTK5 中保持不变，实际头文件路径和链接库由对应版本的模块元数据提供。

## 主版本选择

新工程优先使用 DTK6 的开发包、构建包名和导出目标。维护 DTK5 工程时，应成套使用 DTK5 的开发包和构建信息；同一构建目标不要混用两个主版本的头文件、CMake 目标或 pkg-config 参数。

DTK5 包含 DPlatformThemeProxy 和 DQuickSystemPalette 两个 C++ 类型，DTK6 已移除这两个类型。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
