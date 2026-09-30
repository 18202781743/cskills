# 容器与布局接口

dtkwidget 的容器与布局接口提供 DTK 风格的框架、水平与垂直分隔线、背景分组、阴影线、抽屉、抽屉组、展开组、箭头线抽屉、箭头线展开、箭头矩形、锚点布局和标签页栏。

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

### DFrame

#### 定位

DTK 风格的框架控件。

#### 功能能力总结

采用 DTK 私有类架构，提供 DTK 风格的框架背景和边框样式。支持设置圆角和背景色。

#### 使用场景

需要 DTK 风格的框架容器时，替代 Qt 标准框架容器使用。

### DHorizontalLine

#### 定位

水平分隔线控件。

#### 功能能力总结

提供水平分隔线，可设置线宽和颜色。

#### 使用场景

需要在界面中添加水平分隔线时。

### DVerticalLine

#### 定位

垂直分隔线控件。

#### 功能能力总结

提供垂直分隔线，可设置线宽和颜色。

#### 使用场景

需要在界面中添加垂直分隔线时。

### DBackgroundGroup

#### 定位

带背景样式的分组容器控件。

#### 功能能力总结

为子控件提供 DTK 风格的分组背景，支持圆角、边框和背景色样式。通过样式选项控制背景外观。

#### 使用场景

需要将多个控件分组并以统一背景样式展示时。

### DShadowLine

#### 定位

带阴影的分隔线控件。

#### 功能能力总结

提供带投影效果的分隔线，采用 DTK 私有类架构。支持设置阴影方向和外观。

#### 使用场景

需要带阴影效果的界面分隔线时。

### DDrawer

#### 定位

可展开/收起的抽屉容器控件。

#### 功能能力总结

提供可展开和收起的容器，展开时显示内容区域。支持设置展开方向、动画效果、标题控件和内容控件。

#### 使用场景

需要可折叠展开的内容区域时，如设置面板、高级选项区域。

### DDrawerGroup

#### 定位

抽屉控件组管理器。

#### 功能能力总结

管理多个 DDrawer 的展开状态，实现互斥展开（同一时间只有一个抽屉展开）或自由展开模式。支持添加、移除抽屉控件和设置展开模式。

#### 使用场景

需要管理多个可展开/收起区域并控制其展开行为时。

### DExpandGroup

#### 定位

DTK5 展开控件组管理器。

#### 功能能力总结

管理多个可展开控件的展开状态，支持互斥展开模式。

#### 使用场景

仅在 DTK5 中使用。DTK6 中已移除，替代方式为使用 DDrawerGroup。

### DArrowLineDrawer

#### 定位

带箭头指示器的抽屉式展开行控件。

#### 功能能力总结

在 DDrawer 基础上增加箭头指示器，显示展开/收起状态。支持设置箭头方向、展开标题和内容控件。

#### 使用场景

需要可展开/收起的行控件并带有箭头状态指示时。

### DArrowLineExpand

#### 定位

DTK5 带箭头的展开行控件。

#### 功能能力总结

在展开行控件上提供箭头指示器，显示展开/收起状态。

#### 使用场景

仅在 DTK5 中使用。DTK6 中已移除，替代方式为使用 DArrowLineDrawer。

### DArrowRectangle

#### 定位

带箭头的矩形浮层控件。

#### 功能能力总结

在矩形窗口上绘制指定方向的箭头，支持设置箭头方向、箭头大小、圆角半径、边框宽度和背景色。可作为提示框或浮层容器使用。

#### 使用场景

需要带箭头指向的浮层提示或弹出面板时。

### DAnchors

#### 定位

Qt 控件的锚点布局管理器，提供类似 QML Anchors 的声明式布局能力。

#### 功能能力总结

通过设置控件之间的锚点关系（上、下、左、右、水平居中、垂直居中、边距、居中偏移）实现声明式布局。支持锚点对齐、居中和填充关系，以及锚点边距和偏移设置。

#### 使用场景

需要以锚点方式声明控件相对位置关系时；需要在 C++ 中使用类似 QML Anchors 的布局方式时。

### DTabBar

#### 定位

DTK 风格的选项卡栏控件。

#### 功能能力总结

采用 DTK 私有类架构，提供 DTK 风格的选项卡栏外观。支持添加、移除选项卡、设置当前选项卡和选项卡样式。

#### 使用场景

需要 DTK 风格的选项卡栏时。
