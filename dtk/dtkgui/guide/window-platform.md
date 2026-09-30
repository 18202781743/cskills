# 窗口与平台接口

dtkgui 的窗口与平台接口提供窗口平台属性控制、窗口管理器功能查询、跨进程窗口分组和外部窗口引用能力。

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

### DPlatformHandle

#### 定位

窗口平台属性控制接口。

#### 功能能力总结

为 Qt 窗口设置和管理 DTK 平台级窗口属性，包括窗口圆角、半透明、不同场景和类型的模糊效果、窗口阴影、壁纸缩放与填充模式、启用或禁用窗口管理器装饰。提供属性变更信号。DTK6 中标记为待移除，后续将由新的窗口管理接口替代。

#### 使用场景

需要控制 DTK 窗口的圆角、模糊、阴影这些平台视觉效果时。

### DWindowManagerHelper

#### 定位

窗口管理器功能查询接口。

#### 功能能力总结

查询当前窗口管理器支持的功能（如窗口移动、缩放、最大化和最小化按钮）、装饰样式、窗口管理器名称和窗口类型支持情况。提供窗口管理器名称变化信号。

#### 使用场景

需要查询当前窗口管理器能力以决定窗口行为时。

### DWindowGroupLeader

#### 定位

窗口组 leader，用于跨进程窗口分组。

#### 功能能力总结

创建窗口组 leader 对象，将多个窗口关联到同一分组，使窗口管理器将它们视为一组。

#### 使用场景

需要将多个应用窗口组织到同一窗口组时。

### DForeignWindow

#### 定位

外部窗口的引用与事件监听。

#### 功能能力总结

通过窗口 ID 绑定到一个已存在的外部窗口，使其事件可被当前进程接收和处理。

#### 使用场景

需要监听或交互其他进程创建的窗口时。
