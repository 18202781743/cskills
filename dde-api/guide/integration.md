# 集成与构建配置

使用 dde-api 的 C++ header-only 接口前，需要安装开发包 `dde-api-dev`。该开发包提供头文件搜索路径和 CMake 配置文件。

## 开发包

C++ 部分的开发包名为 `dde-api-dev`，提供安装在 `dde-api/` 目录下的公开头文件，以及安装到 `share/cmake/DDEAPI/` 目录下的 CMake 配置文件 `DDEAPIConfig.cmake`。

## CMake 集成

dde-api 的 C++ 部分为 header-only，无需链接库文件。推荐通过 `find_package` 查找 CMake 配置并链接导出目标，由导出目标自动提供头文件搜索路径：

```cmake
find_package(DDEAPI QUIET)
if(DDEAPI_FOUND)
    target_link_libraries(myapp PRIVATE DDEAPI::EventLogger)
endif()
```

`find_package(DDEAPI)` 查找成功后，使用方工程可通过 `target_link_libraries` 链接 `DDEAPI::EventLogger` 导出目标获取头文件搜索路径。该目标为 INTERFACE IMPORTED 目标，不引入实际链接库，仅传递头文件包含路径。

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

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](dde-api-dev.md)。
