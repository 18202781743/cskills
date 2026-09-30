# 文件拖拽、字体与缩略图接口

dtkgui 的文件拖拽、字体与缩略图接口提供跨进程文件拖拽的客户端与服务端、字体安装与管理和文件缩略图异步生成能力。

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

### DFileDrag

#### 定位

文件拖拽的基类，封装拖拽客户端与服务端的公共接口。

#### 功能能力总结

提供文件拖拽的基本接口，包括设置和获取 URL 列表、拖拽状态及对应的时间戳。拖拽状态覆盖失败、停滞、暂停、运行中、完成这些阶段，并支持自定义扩展状态。

#### 使用场景

作为 DFileDragClient 和 DFileDragServer 的基类使用，不直接实例化。

### DFileDragClient

#### 定位

文件拖拽的客户端，用于发起跨进程文件拖拽。

#### 功能能力总结

作为 DFileDrag 的子类，负责向服务端发起文件拖拽请求，设置目标 URL 列表并维护拖拽会话状态。

#### 使用场景

需要在应用中作为拖拽源发起跨进程文件拖拽时。

### DFileDragServer

#### 定位

文件拖拽的服务端，用于接收跨进程文件拖拽。

#### 功能能力总结

作为 DFileDrag 的子类，负责接收来自客户端的文件拖拽请求，读取 URL 列表并维护拖拽会话状态。

#### 使用场景

需要在应用中作为拖拽目标接收跨进程文件拖拽时。

### DFontManager

#### 定位

字体安装与管理的接口。

#### 功能能力总结

以命令行工具为后端，支持安装和卸载字体文件。提供从最小到最大共十级字体尺寸类型的查询能力。

#### 使用场景

需要在应用中安装或卸载系统字体时。

### DThumbnailProvider

#### 定位

文件缩略图异步生成器。

#### 功能能力总结

以单例线程方式运行，为指定文件和 MIME 类型异步生成缩略图。提供小、中、大三种缩略图尺寸选择。支持缓存已生成的缩略图并提供回调通知。

#### 使用场景

需要为文件生成预览缩略图时。
