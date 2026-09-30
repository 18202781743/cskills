# 图标与 SVG 渲染接口

dtkgui 的图标与 SVG 渲染接口提供 DTK 图标加载、图标主题缓存管理、SVG 渲染和图像格式处理能力。

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

### DIcon

#### 定位

DTK 图标类型，扩展 Qt 图标的图标加载能力。

#### 功能能力总结

提供从高分辨率资源文件加载位图的静态方法。

#### 使用场景

需要加载多分辨率位图图标时。

### DIconTheme::Cached

#### 定位

DTK 图标主题查找的缓存管理器。

#### 功能能力总结

DTK 图标主题命名空间中的嵌套类，管理图标查找缓存。支持设置最大缓存容量、清空缓存，以及按图标名和选项查找 Qt 图标和 DCI 图标文件。查找选项可控制是否从 Qt 图标退回查找、是否忽略内置图标、DCI 图标和图标缓存。DTK 图标主题命名空间还提供 DCI 主题搜索路径管理、图标来源判断和图标引擎创建这些自由函数。

#### 使用场景

需要高性能重复查找图标时；需要管理 DCI 主题搜索路径时。

### DSvgRenderer

#### 定位

SVG 图像渲染器。

#### 功能能力总结

加载 SVG 文件或数据，提供默认尺寸和视图区域查询，并支持通过绘图接口将 SVG 绘制到指定矩形区域。

#### 使用场景

需要加载和渲染 SVG 图像到自定义绘制设备时。

### DImageHandler

#### 定位

图像格式处理工具（已废弃）。

#### 功能能力总结

提供图像格式检测、格式支持列表查询、图像旋转和保存这些静态方法。

#### 使用场景

已废弃，应使用图像读写库或其他图像库替代。
