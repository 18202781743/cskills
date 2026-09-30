# DCI 图标接口

dtkgui 的 DCI 图标接口提供 DCI 图标资源的加载、渲染与动画播放能力，包括图标容器、单帧图像访问、图像序列播放器、内嵌调色板和整体动画播放器。

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

### DDciIcon

#### 定位

DCI 图标资源的容器与渲染入口。

#### 功能能力总结

从文件路径或数据加载 DCI 图标资源，按主题、模式、属性和匹配标志获取对应的图标图像或位图。支持多主题切换、多分辨率适配、高亮与禁用显示状态，以及内嵌调色板的前景、背景、高亮色设置。可判断图标是否包含动画帧序列。

##### 图像获取

按指定主题、模式、图标属性和匹配标志取得图标图像对象；也可直接获取指定尺寸的位图或图像数据。

##### 调色板

内嵌调色板支持前景、背景、高亮前景和高亮色四种角色，可为 DCI 图标提供主题感知的着色。

#### 使用场景

需要加载和渲染 DCI 格式图标时；需要支持多主题、多分辨率图标显示时。

### DDciIconImage

#### 定位

DCI 图标中单帧图像的访问接口。

#### 功能能力总结

表示 DCI 图标中的单张图像，可转换为图像对象或通过绘图接口绘制到指定区域。支持判断是否为空、是否包含调色板、是否支持动画，以及动画帧的跳转与逐帧推进。

#### 使用场景

需要对 DCI 图标的单帧图像进行自定义绘制或逐帧动画处理时。

### DDciIconImagePlayer

#### 定位

DCI 图标图像序列的动画播放器。

#### 功能能力总结

接收一组 DDciIconImage 并按帧序列播放动画。支持设置播放状态（Off、On）、播放标志（如自动循环）、循环次数、调色板，以及中止当前循环并读取当前帧图像。可清除缓存的帧数据。

#### 使用场景

需要播放 DCI 图标中的动画序列时。

### DDciIconPalette

#### 定位

DCI 图标内嵌调色板。

#### 功能能力总结

管理前景、背景、高亮前景和高亮四种调色板角色颜色。支持颜色设置与查询，以及与字符串之间的序列化转换。

#### 使用场景

需要为 DCI 图标设置自定义主题颜色时；需要序列化或反序列化 DCI 调色板时。

### DDciIconPlayer

#### 定位

DCI 图标整体的动画播放器。

#### 功能能力总结

以 DCI 图标和调色板为输入，按主题和模式播放图标动画。支持设置播放状态、标志、循环次数和调色板，中止循环并读取当前帧图像，以及清除缓存。

#### 使用场景

需要播放完整 DCI 图标（而非单帧序列）的动画时。
