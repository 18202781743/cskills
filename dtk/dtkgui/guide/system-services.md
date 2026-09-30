# 系统服务接口

dtkgui 的系统服务接口提供系统服务调用（打开文件管理器、播放系统提示音）、屏幕区域监视和任务栏进度与计数控制能力。

## 开发包

当前版本使用 DTK6，开发包名为 `libdtk6gui-dev`。该开发包提供 DTK6 的公开头文件和以下构建入口：

- CMake 包 `Dtk6Gui` 与导出目标 `Dtk6::Gui`
- pkg-config 模块 `dtk6gui`
- qmake 模块 `dtkgui`

仍需维护 DTK5 工程时，使用兼容开发包 `libdtkgui-dev`。它提供 CMake 包 `DtkGui`、导出目标 `Dtk::Gui`、pkg-config 模块 `dtkgui` 和同名 qmake 模块。

## 集成

### CMake 配置

CMake 是当前推荐的集成方式。DTK6 工程在已有构建目标上查找 `Dtk6Gui` 并链接 `Dtk6::Gui`：

```cmake
find_package(Dtk6Gui REQUIRED)
target_link_libraries(your_target PRIVATE Dtk6::Gui)
```

`your_target` 替换为使用方工程中的目标名。`Dtk6::Gui` 会向该目标提供 dtkgui 的头文件搜索路径、链接信息、编译定义和传递依赖，不需要再使用 `include_directories()`、`link_directories()` 或逐项链接 dtkgui 所依赖的库。

仍使用 DTK5 的工程改为查找 `DtkGui` 并链接 `Dtk::Gui`：

```cmake
find_package(DtkGui REQUIRED)
target_link_libraries(your_target PRIVATE Dtk::Gui)
```

### 使用方式

构建目标链接 dtkgui 后，可以直接包含所需类型的公开转发头：

```cpp
#include <DPalette>
```

也可以包含对应的实际公开头文件，例如 `#include <dpalette.h>`。公开类型主要位于 `Dtk::Gui` 命名空间，可使用完整限定名，也可在合适的作用域使用 `DGUI_USE_NAMESPACE`。开发包还提供便捷头 `DtkGuis`，一次引入所有已安装的公开头文件。

## 模块API介绍

### DDesktopServices

#### 定位

DTK 系统服务调用入口，提供静态方法集合。

#### 功能能力总结

通过静态方法打开文件管理器并定位文件、显示文件属性对话框、播放不同类型的系统提示音效。支持以本地路径或 URL 形式打开单个或多个文件（夹）。

#### 使用场景

需要在应用中调用文件管理器打开文件或播放系统提示音时。

### DRegionMonitor

#### 定位

屏幕区域监视器。

#### 功能能力总结

在指定屏幕坐标区域内监视鼠标和键盘事件。可灵活配置需要注册和监视的事件类型，支持在屏幕绝对坐标和相对坐标之间选择。提供区域进入、离开和按键信号。

#### 使用场景

需要在特定屏幕区域内全局监视输入事件时。

### DTaskbarControl

#### 定位

任务栏进度与计数控制接口。

#### 功能能力总结

为应用窗口设置任务栏上的进度条、进度计数器和计数器Overlay 图标。支持设置进度值、计数器值和计数器可见性，以及清除进度状态。

#### 使用场景

需要在任务栏上显示应用操作进度或消息计数时。
