# 浮层与提示接口

dtkwidget 的浮层与提示接口提供 DTK 风格的浮动控件、浮动消息、消息管理器、提示标签、工具提示、警告控制和吐司提示。

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

### DFloatingWidget

#### 定位

浮动控件基类。

#### 功能能力总结

提供浮动控件的基类功能，支持设置浮动力向、偏移、边界限制和显示/隐藏动画。可包含任意子控件。 采用 DTK 私有类架构。

#### 使用场景

需要创建浮动在父窗口上的控件时，作为基类继承使用。

### DFloatingMessage

#### 定位

浮动消息提示控件。

#### 功能能力总结

以浮动控件形式显示消息提示，支持消息图标、文本、关闭按钮和操作按钮。可设置消息停留时间和消失动画。

#### 使用场景

需要在窗口内显示非阻塞的浮动消息提示时。

### DMessageManager

#### 定位

消息管理器，在窗口内显示浮动消息提示。

#### 功能能力总结

以单例方式管理窗口内的浮动消息提示，支持在指定窗口上发送和移除消息。消息以 DFloatingMessage 形式显示在窗口顶部。

#### 使用场景

需要在窗口内显示非模态的浮动消息提示时。

### DTipLabel

#### 定位

DTK 风格的提示标签控件。

#### 功能能力总结

提供 DTK 风格的提示标签外观，支持圆角和半透明背景。用于显示简短提示信息。

#### 使用场景

需要显示 DTK 风格的提示标签时，替代 Qt 标准提示标签。

### DToolTip

#### 定位

DTK 风格的工具提示控件。

#### 功能能力总结

提供 DTK 风格的工具提示气泡。支持设置提示文本、显示位置和停留时间。

#### 使用场景

需要显示 DTK 风格的工具提示气泡时。

### DAlertControl

#### 定位

行编辑控件的告警状态控制器。

#### 功能能力总结

为控件提供告警状态的显示与隐藏能力，支持设置告警消息文本、告警图标和颜色。告警状态下控件边框变色并显示提示消息。

#### 使用场景

需要在输入控件上显示验证错误或告警提示时；通常与 DLineEdit 配合使用。

### DToast

#### 定位

DTK5 浮动提示消息控件。

#### 功能能力总结

以浮动方式显示提示消息，支持设置消息文本、显示时长和消失动画。

#### 使用场景

仅在 DTK5 中使用。DTK6 中已移除，替代方式为使用 DMessageManager。
