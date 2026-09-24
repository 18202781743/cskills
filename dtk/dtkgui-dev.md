# dtkgui 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | libdtkgui-dev / libdtk6gui-dev |
| 版本 | 6.7.50 |
| 描述 | DTK GUI 层库，提供平台主题、DCI 图标、调色板、字体管理、任务栏控制等 GUI 相关功能 |
| CMake target | `Dtk::Gui`（DTK5）/ `Dtk6::Gui`（DTK6） |
| find_package 名 | `DtkGui`（DTK5）/ `Dtk6Gui`（DTK6） |
| 头文件安装路径 | `${CMAKE_INSTALL_INCLUDEDIR}/dtk6/DGui`（DTK6）/ `${CMAKE_INSTALL_INCLUDEDIR}/dtk/DGui`（DTK5） |
| 库文件 | `libdtk6gui.so`（DTK6）/ `libdtkgui.so`（DTK5） |
| 仓库地址 | https://github.com/linuxdeepin/dtkgui.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6 (>= 6.x)
- libdtk6core (>= 6.7.50)

### 开发依赖
- Qt 6 Core, Qt 6 Gui (>= 6.x)
- dtkcore (>= 6.7.50)
- CMake >= 3.13

## 3. CMake 集成

### find_package 用法

```cmake
find_package(Dtk6Gui REQUIRED)
target_link_libraries(your-target PRIVATE Dtk6::Gui)
```

### 安装的 CMake 配置文件

- `${CMAKE_INSTALL_LIBDIR}/cmake/Dtk6Gui/Dtk6GuiConfig.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/Dtk6Gui/Dtk6GuiConfigVersion.cmake`

## 4. pkg-config

| .pc 文件 | 内容 |
|----------|------|
| `dtk6gui.pc` | Libs: -ldtk6gui，Cflags: -I.../dtk6/DGui |
| `dtkgui.pc` | Libs: -ldtkgui，Cflags: -I.../dtk/DGui |

```bash
pkg-config --cflags --libs dtk6gui
```

## 5. 命名空间

`Dtk::Gui`（通过 `DGUI_USE_NAMESPACE` 宏引入）

```cpp
#include <DGuiApplicationHelper>
DGUI_USE_NAMESPACE
```

## 6. 关键公共类及功能描述

| 类名 | 功能 | 关键方法 |
|------|------|----------|
| `DGuiApplicationHelper` | GUI 应用辅助类，主题管理、调色板获取 | `instance()`, `applicationPalette()`, `setApplicationTheme()`, `themeType()` |
| `DPlatformTheme` | 平台主题，获取系统主题属性 | `activeAccentColor()`, `windowRadius()`, `transparency()` |
| `DDciIcon` | DCI 格式图标引擎 | `fromTheme()`, `paint()`, `pixmap()` |
| `DDesktopServices` | 桌面服务扩展 | `showFolder()`, `showItemInFolder()`, `trash()` |
| `DFontManager` | 字体管理 | `installFont()`, `uninstallFont()` |
| `DTaskbarControl` | 任务栏控制 | `setProgress()`, `setCounterVisible()`, `setUrgency()` |
| `DPalette` | DTK 调色板，扩展 QPalette | `setItemBackground()`, `color()` |
| `DRegionMonitor` | 屏幕区域监视 | `registerRegion()`, `unregisterRegion()` |
| `DFileDrag` | 文件拖拽支持 | `setMimeData()`, `start()` |
| `DIconColors` | DCI 图标颜色配置 | `commonColor()`, `stateColor()` |

## 7. QML 模块

不适用（dtkgui 为 C++ 库，QML 支持由 dtkdeclarative 提供）

## 8. DBus 接口

不适用（dtkgui 为本地库，不提供 DBus 服务）

## 9. 插件开发

不适用（dtkgui 不提供插件开发接口）
