# 集成与构建配置

使用 dde-api 的 C++ header-only 接口前，需要安装开发包 `dde-api-dev`。该开发包提供头文件搜索路径。Go 工具通过 Go 构建系统独立编译，无需额外开发包。

## 开发包

C++ 部分的开发包名为 `dde-api-dev`，提供安装在 `dde-api/` 目录下的公开头文件。

## CMake 集成

dde-api 的 C++ 部分为 header-only，无需链接库文件。使用方可以直接包含头文件，也可通过 `find_package` 获取头文件搜索路径：

```cmake
find_package(DDEAPI QUIET)
```

`DDEAPI` 为可选的 CMake 包名。查找成功后，使用方工程可获得头文件搜索路径；由于是 header-only，无需链接目标。

直接包含头文件时无需 CMake 配置：

```cpp
#include <dde-api/eventlogger.hpp>
```

## 引用公开接口

C++ header-only 接口的公开头文件位于 `dde-api/` 目录下。包含头文件后，使用 `DDE_EventLogger` 命名空间访问公开符号：

```cpp
#include <dde-api/eventlogger.hpp>
using namespace DDE_EventLogger;
```

## Go 工具构建

Go 工具位于各子目录中，通过 Go 构建系统编译。使用方如需调用这些工具，安装对应的可执行程序即可，无需在自身工程中链接 Go 代码。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
