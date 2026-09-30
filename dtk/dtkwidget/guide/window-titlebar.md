# 窗口与标题栏接口

dtkwidget 的窗口与标题栏接口提供 DTK 风格的主窗口、标题栏、平台窗口句柄和窗口控制按钮。

## 开发包

当前版本使用 DTK6，开发包名为 `libdtk6widget-dev`。该开发包提供 DTK6 的公开头文件和以下构建入口：

- CMake 包 `Dtk6Widget` 与导出目标 `Dtk6::Widget`
- pkg-config 模块 `dtk6widget`
- qmake 模块 `DtkWidget`

仍需维护 DTK5 工程时，使用兼容开发包 `libdtkwidget-dev`。它提供 CMake 包 `DtkWidget`、导出目标 `Dtk::Widget`、pkg-config 模块 `dtkwidget` 和同名 qmake 模块。

## 集成

### CMake 配置

CMake 是当前推荐的集成方式。DTK6 工程在已有构建目标上查找 `Dtk6Widget` 并链接 `Dtk6::Widget`：

```cmake
find_package(Dtk6Widget REQUIRED)
target_link_libraries(your_target PRIVATE Dtk6::Widget)
```

`your_target` 替换为使用方工程中的目标名。`Dtk6::Widget` 会向该目标提供 dtkwidget 的头文件搜索路径、链接信息、编译定义和传递依赖，不需要再使用 `include_directories()`、`link_directories()` 或逐项链接 dtkwidget 所依赖的库。

仍使用 DTK5 的工程改为查找 `DtkWidget` 并链接 `Dtk::Widget`：

```cmake
find_package(DtkWidget REQUIRED)
target_link_libraries(your_target PRIVATE Dtk::Widget)
```

### 使用方式

构建目标链接 dtkwidget 后，可以直接包含所需类型的公开转发头：

```cpp
#include <DLineEdit>
```

也可以包含对应的实际公开头文件，例如 `#include <dlineedit.h>`。公开类型主要位于 `Dtk::Widget` 命名空间，可使用完整限定名，也可在合适的作用域使用 `DWIDGET_USE_NAMESPACE`。开发包还提供便捷头 `DtkWidgets`，一次引入所有已安装的公开头文件。

## 模块API介绍

### DMainWindow

#### 定位

DTK 风格的主窗口控件。

#### 功能能力总结

并提供 DTK 风格的窗口装饰，包括自定义标题栏、圆角、阴影和窗口按钮。支持设置标题栏控件、窗口拖拽和最大化/最小化按钮管理。

#### 使用场景

DTK Widgets 应用程序的主窗口基类，替代 Qt 标准主窗口使用；需要 DTK 风格窗口装饰时。

### DTitlebar

#### 定位

DTK 风格的自定义标题栏控件。

#### 功能能力总结

提供 DTK 风格的窗口标题栏，支持自定义标题内容、嵌入控件、窗口按钮（关闭、最小化、最大化）、菜单栏和分割线。支持窗口拖拽、双击最大化/还原和按钮图标自定义。 采用 DTK 私有类架构。

#### 使用场景

需要自定义窗口标题栏时；与 DMainWindow 配合实现 DTK 风格窗口装饰时。

### DPlatformWindowHandle

#### 定位

平台窗口句柄管理器，为窗口启用 DTK 平台级装饰。

#### 功能能力总结

为 Qt 窗口组件启用 DTK 平台窗口装饰（圆角、阴影、模糊），支持设置窗口圆角、阴影、透明度和窗口标志。是与 dde-qtplatform-plugins 通信的桥梁。

#### 使用场景

需要为窗口启用 DTK 平台装饰效果时；需要手动控制窗口圆角和阴影时。

### DWindowCloseButton

#### 定位

DTK 窗口关闭按钮控件。

#### 功能能力总结

提供 DTK 风格的窗口关闭按钮外观和交互。预设关闭图标。

#### 使用场景

需要在自定义窗口标题栏中放置关闭按钮时。

### DWindowMaxButton

#### 定位

DTK 窗口最大化按钮控件。

#### 功能能力总结

提供 DTK 风格的窗口最大化/还原按钮外观和交互。支持最大化与还原状态图标切换。

#### 使用场景

需要在自定义窗口标题栏中放置最大化按钮时。

### DWindowMinButton

#### 定位

DTK 窗口最小化按钮控件。

#### 功能能力总结

提供 DTK 风格的窗口最小化按钮外观和交互。预设最小化图标。

#### 使用场景

需要在自定义窗口标题栏中放置最小化按钮时。

### DWindowOptionButton

#### 定位

DTK 窗口选项按钮控件。

#### 功能能力总结

提供 DTK 风格的窗口选项按钮外观和交互。预设选项（菜单）图标。

#### 使用场景

需要在自定义窗口标题栏中放置选项/菜单按钮时。

### DWindowQuitFullButton

#### 定位

DTK 退出全屏按钮控件。

#### 功能能力总结

提供 DTK 风格的退出全屏按钮，支持设置退出全屏提示文本。

#### 使用场景

需要在全屏窗口中显示退出全屏按钮时。

### DTabletWindowOptionButton

#### 定位

平板模式窗口选项按钮控件。

#### 功能能力总结

提供平板模式下的窗口选项按钮外观和行为。

#### 使用场景

需要在平板模式窗口标题栏中显示选项按钮时。

### DApplication

#### 定位

DTK 应用程序类，为 Qt Widgets 应用提供 DTK 全局配置和应用级功能。

#### 功能能力总结

管理应用程序全局设置，包括主题跟随、自动退出隐藏窗口、高分辨率缩放、应用程序元信息（名称、版本、描述、图标）设置。提供获取 DTK 风格窗口装饰和主题的能力。支持设置应用程序的产品名称和许可证信息。 采用 DTK 私有类架构。

#### 使用场景

DTK Widgets 应用程序的主入口类，替代 Qt 标准应用程序入口使用；需要设置 DTK 应用元信息和全局行为时。
