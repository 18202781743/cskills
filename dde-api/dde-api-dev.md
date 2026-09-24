# dde-api 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-api |
| 版本 | 6.0.16 |
| 描述 | DDE API 库，提供 header-only C++ 接口和一组 Go 工具程序，用于图像处理、输入设备配置、声音主题等 |
| CMake target | 不适用（header-only C++ + Go 工具） |
| find_package 名 | `DDEAPI`（可选，QUIET） |
| 头文件安装路径 | `${CMAKE_INSTALL_INCLUDEDIR}/dde-api/` |
| 仓库地址 | https://github.com/linuxdeepin/dde-api.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6 (>= 6.x)
- libdtk6core, libdtk6gui

### 开发依赖
- Qt 6 Core, Gui (>= 6.x)
- Go (>= 1.20)（构建 Go 工具时）
- CMake >= 3.16

## 3. CMake 集成

### C++ header-only 用法

dde-api 的 C++ 部分为 header-only，无需 link 库，直接包含头文件：

```cpp
#include <dde-api/eventlogger.hpp>
```

### find_package（可选）

```cmake
find_package(DDEAPI QUIET)
```

### Go 工具构建

Go 工具位于各子目录中，通过 Makefile 或 Go 构建系统编译。

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

C++ header-only 部分：

- `DDE_EventLogger`（事件日志命名空间）

```cpp
#include <dde-api/eventlogger.hpp>
using namespace DDE_EventLogger;
```

## 6. 关键公共类及功能描述

### C++ header-only

| 头文件 | 命名空间 | 功能 |
|--------|----------|------|
| `eventlogger.hpp` | `DDE_EventLogger` | 事件日志记录，支持将事件日志发送到后端 |

### Go 工具

| 工具 | 功能 |
|------|------|
| `blurimage` | 图片模糊处理 |
| `drandr` | 显示器配置（RandR） |
| `dxinput` | 输入设备配置 |
| `sound-theme-player` | 声音主题播放 |
| `cursor` | 光标设置 |
| `wmcompatible` | 窗口管理器兼容性检查 |
| `sni_stub` | Status Notifier Item 代理 |
| `localehelper` | 区域设置辅助 |
| `theme` | 主题设置 |
| `soundeffect` | 音效设置 |
| `xevent_monitor` | X 事件监视 |

Go 包路径：`github.com/linuxdeepin/dde-api/<tool>`

## 7. QML 模块

不适用

## 8. DBus 接口

dde-api 的 Go 工具通过 DBus 与系统服务交互，但不直接导出 DBus 服务接口。

## 9. 插件开发

不适用（dde-api 为工具库和 header-only 接口，不提供插件机制）
