# 快速渲染接口

dtkdeclarative 的快速渲染接口提供 QML 场景中的帧缓冲区位块传输渲染和视口裁剪渲染能力。

## 开发包

当前版本使用 DTK6，开发包名为 `libdtk6declarative-dev`。该开发包提供 DTK6 的公开头文件和以下构建入口：

- CMake 包 `Dtk6Declarative` 与导出目标 `Dtk6::Declarative`
- pkg-config 模块 `dtk6declarative`
- qmake 模块 `dtkdeclarative`

仍需维护 DTK5 工程时，使用兼容开发包 `libdtkdeclarative-dev`。它提供 CMake 包 `DtkDeclarative`、导出目标 `Dtk::Declarative`、pkg-config 模块 `dtkdeclarative` 和同名 qmake 模块。

## 集成

### CMake 配置

CMake 是当前推荐的集成方式。DTK6 工程在已有构建目标上查找 `Dtk6Declarative` 并链接 `Dtk6::Declarative`：

```cmake
find_package(Dtk6Declarative REQUIRED)
target_link_libraries(your_target PRIVATE Dtk6::Declarative)
```

`your_target` 替换为使用方工程中的目标名。`Dtk6::Declarative` 会向该目标提供 dtkdeclarative 的头文件搜索路径、链接信息、编译定义和传递依赖，不需要再使用 `include_directories()`、`link_directories()` 或逐项链接 dtkdeclarative 所依赖的库。

仍使用 DTK5 的工程改为查找 `DtkDeclarative` 并链接 `Dtk::Declarative`：

```cmake
find_package(DtkDeclarative REQUIRED)
target_link_libraries(your_target PRIVATE Dtk::Declarative)
```

### 使用方式

构建目标链接 dtkdeclarative 后，可以直接包含所需类型的公开转发头：

```cpp
#include <DAppLoader>
```

也可以包含对应的实际公开头文件，例如 `#include <dapploader.h>`。公开 C++ 类型主要位于 `Dtk::Quick` 命名空间。QML 控件通过 `org.deepin.dtk` QML 模块使用，无需在 C++ 中包含头文件。

## 模块API介绍

### DQuickBlitFramebuffer

#### 定位

QML 场景中的帧缓冲区位块传输渲染项。

#### 功能能力总结

将离屏帧缓冲区内容通过位块传输方式渲染到 QML 场景中。

#### 使用场景

需要将离屏渲染的帧缓冲区内容高效地呈现到 QML 场景中时。

### DQuickItemViewport

#### 定位

QML 场景中的视口裁剪渲染项。

#### 功能能力总结

提供将指定源项的局部区域裁剪并渲染到视口的能力。

#### 使用场景

需要在 QML 中实现视口裁剪或局部区域渲染时。
