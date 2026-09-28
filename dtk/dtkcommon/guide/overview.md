# dtkcommon 二次开发文档 · 概览

## 项目定位

dtkcommon 是 DTK 的公共资源项目，不构建 C++ 库，只安装 CMake 包配置、构建辅助函数和应用数据配置文件。其他 DTK 模块通过引入 dtkcommon 获得版本号定义、配置头文件生成和 CMake 包查找基础设施。

## 术语与缩写

- **DTK**：Deepin Tool Kit。
- **DTK5 / DTK6**：分别与 Qt5 / Qt6 配套的主版本。
- **DSG**：配置及应用数据相关的目录和环境变量前缀。
- **CMake 包配置**：以 `*Config.cmake` 命名的文件，供使用方通过 `find_package` 查找项目。
- **构建辅助函数**：由 dtkcommon 提供的 CMake 函数，供其他 DTK 模块在构建时调用。

## 功能能力

- 提供伞式 CMake 包 `Dtk`（DTK5）和 `Dtk6`（DTK6），通过组件机制聚合查找各 DTK 子模块。
- 提供构建辅助 CMake 包 `DtkBuildHelper`，其中包含 `dtk_gen_config_header`、`dtk_setup_code_coverage` 和 `dtk_check_and_add_definitions` 函数。
- 安装应用数据配置文件到 `share/dsg/` 目录。

## 导出类型

dtkcommon 不构建 C++ 库，不安装公开头文件，因此没有导出的 C++ 类型。导出类型介绍见[导出类型介绍](modules.md)。

## 全局约定

dtkcommon 安装的 CMake 包配置文件位于 `lib*/cmake/Dtk`（DTK5）和 `lib*/cmake/Dtk6`（DTK6）目录下，构建辅助包位于 `lib*/cmake/DtkBuildHelper` 下。跨主版本构建方式见[集成与构建配置](integration.md)。

## 按功能查阅

- 将 dtkcommon 引入 CMake 工程：参见[集成与构建配置](integration.md)。
- 查看导出类型：参见[导出类型介绍](modules.md)。
