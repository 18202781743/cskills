# dtkcore 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | libdtkcore-dev / libdtk6core-dev |
| 版本 | 6.7.50 |
| 描述 | DTK 核心库，提供 DConfig 配置系统、DSysInfo 系统信息、DSettings 设置框架、日志管理等基础工具 |
| CMake target | `Dtk::Core`（DTK5）/ `Dtk6::Core`（DTK6） |
| find_package 名 | `DtkCore`（DTK5）/ `Dtk6Core`（DTK6） |
| 头文件安装路径 | `${CMAKE_INSTALL_INCLUDEDIR}/dtk6/DCore`（DTK6）/ `${CMAKE_INSTALL_INCLUDEDIR}/dtk/DCore`（DTK5） |
| 库文件 | `libdtk6core.so`（DTK6）/ `libdtkcore.so`（DTK5） |
| 仓库地址 | https://github.com/linuxdeepin/dtkcore.git |

> **注**：dtklog 已废弃，日志功能已合并至 dtkcore，不再作为独立模块维护。

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6 (>= 6.x)
- libdtkcommon

### 开发依赖
- Qt 6 Core (>= 6.x)
- dtkcommon
- CMake >= 3.13
- pkg-config

## 3. CMake 集成

### find_package 用法

```cmake
# DTK6
find_package(Dtk6Core REQUIRED)
target_link_libraries(your-target PRIVATE Dtk6::Core)

# DTK5
find_package(DtkCore REQUIRED)
target_link_libraries(your-target PRIVATE Dtk::Core)
```

### DConfig 宏

dtkcore 还提供 DConfig 相关的 CMake 宏，需额外 find_package：

```cmake
find_package(Dtk6DConfig REQUIRED)
# 注册 DConfig 元数据文件
dtk_add_config_meta_files(APPID org.deepin.yourapp FILES config.json)
```

### 安装的 CMake 配置文件

- `${CMAKE_INSTALL_LIBDIR}/cmake/Dtk6Core/Dtk6CoreConfig.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/Dtk6Core/Dtk6CoreConfigVersion.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/Dtk6DConfig/Dtk6DConfigConfig.cmake`

## 4. pkg-config

| .pc 文件 | 内容 |
|----------|------|
| `dtk6core.pc` | DTK6 核心库（Libs: -ldtk6core，Cflags: -I.../dtk6/DCore） |
| `dtkcore.pc` | DTK5 核心库（Libs: -ldtkcore，Cflags: -I.../dtk/DCore） |

```bash
pkg-config --cflags --libs dtk6core
```

## 5. 命名空间

`Dtk::Core`（通过 `DCORE_USE_NAMESPACE` 宏引入）

```cpp
#include <DCore>
DCORE_USE_NAMESPACE
```

## 6. 关键公共类及功能描述

| 类名 | 功能 | 关键方法 |
|------|------|----------|
| `DConfig` | DConfig 配置系统，读写应用配置 | `create()`, `value()`, `setValue()`, `sync()` |
| `DSysInfo` | 系统信息获取 | `distributionName()`, `distributionVersion()`, `productType()`, `productVersion()` |
| `DSettings` | 应用设置框架，支持 JSON Schema 定义 | `fromJsonFile()`, `option()`, `value()`, `setValue()` |
| `DStandardPaths` | 标准路径获取 | `writableLocation()`, `standardLocations()` |
| `LogManager` / `DtkLogManager` | 日志管理（合并自 dtklog） | `registerFileAppender()`, `registerConsoleAppender()` |
| `DFileSystemWatcher` | 文件系统监视器 | `addPath()`, `removePath()`, `fileChanged()` |
| `DConfigFile` | DConfig 底层文件操作 | `load()`, `save()` |
| `DThreadUtil` | 线程工具 | `runInMainThread()` |
| `DFileInfo` | 文件信息扩展 | `mimeType()`, `mimeTypeDisplayName()` |
| `DDesktopEntry` | Desktop 文件解析 | `name()`, `icon()`, `exec()` |

## 7. QML 模块

不适用（dtkcore 不提供 QML 模块，QML 支持由 dtkdeclarative 提供）

## 8. DBus 接口

不适用（dtkcore 为本地库，不提供 DBus 服务）

## 9. 插件开发

不适用（dtkcore 不提供插件开发接口）

## dtklog 说明

dtklog 已废弃，日志功能已合并至 dtkcore。使用方式：

```cpp
#include <DCore>
DCORE_USE_NAMESPACE

// 日志使用
#include <DLog>
DLOG_USE_NAMESPACE
Dtk::Core::LogManager::registerConsoleAppender();
```
