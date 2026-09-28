# 集成与构建配置

使用 dtklog 公开接口前，需要安装与目标 DTK 主版本对应的开发包。开发包提供公开头文件、链接库以及 CMake、pkg-config 和 qmake 使用的构建信息；通过这些构建信息引入 dtklog 后，无需手工填写头文件目录、库目录或其传递依赖。

## 开发包

当前版本使用 DTK6，开发包名为 `libdtk6log-dev`。该开发包提供 DTK6 的公开头文件和以下构建入口：

- CMake 包 `Dtk6Log` 与导出目标 `Dtk6::Log`；
- pkg-config 模块 `dtk6log`；
- qmake 模块 `dtklog`。

仍需维护 DTK5 工程时，使用兼容开发包 `libdtklog-dev`。它提供 CMake 包 `DtkLog`、导出目标 `Dtk::Log`、pkg-config 模块 `dtklog` 和同名 qmake 模块。

## CMake 集成

CMake 是当前推荐的集成方式。DTK6 工程在已有构建目标上查找 `Dtk6Log` 并链接 `Dtk6::Log`：

```cmake
find_package(Dtk6Log REQUIRED)
target_link_libraries(your_target PRIVATE Dtk6::Log)
```

`your_target` 替换为使用方工程中的目标名。`Dtk6::Log` 会向该目标提供 dtklog 的头文件搜索路径、链接信息和传递依赖，不需要再使用 `include_directories()` 或逐项链接 dtklog 所依赖的库。

### DTK5 兼容写法

仍使用 DTK5 的工程改为查找 `DtkLog` 并链接 `Dtk::Log`：

```cmake
find_package(DtkLog REQUIRED)
target_link_libraries(your_target PRIVATE Dtk::Log)
```

## 引用公开接口

构建目标链接 dtklog 后，可以直接包含所需类型的公开头文件：

```cpp
#include <Logger>
#include <ConsoleAppender>
```

也可以包含对应的实际公开头文件，例如 `#include <Logger.h>`。公开类型主要位于 `Dtk` 命名空间，可使用完整限定名，也可在合适的作用域使用 `DLOG_USE_NAMESPACE`。

## 其他受支持的构建入口

无法使用 CMake 导出目标时，可以读取开发包提供的 pkg-config 或 qmake 元数据。

### pkg-config

DTK6 使用 `dtk6log` 模块：

```sh
pkg-config --cflags --libs dtk6log
```

将 `--cflags` 与 `--libs` 的结果分别用于编译和链接阶段。DTK5 兼容工程将模块名改为 `dtklog`。

### qmake

在与所选 DTK 主版本配套的 qmake 工程中添加：

```qmake
QT += dtklog
```

qmake 模块名在 DTK6 与 DTK5 中保持不变，实际头文件路径和链接库由对应版本的模块元数据提供。

## 主版本选择

新工程优先使用 DTK6 的开发包、构建包名和导出目标。维护 DTK5 工程时，应成套使用 DTK5 的开发包和构建信息；同一构建目标不要混用两个主版本的头文件、CMake 目标或 pkg-config 参数。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
