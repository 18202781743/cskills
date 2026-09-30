# 对话框接口

dtkwidget 的对话框接口提供 DTK 风格的对话框基类与多种专用对话框，包括关于对话框、文件对话框、输入对话框、许可证对话框、特性展示对话框和通用对话框。

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

### DAbstractDialog

#### 定位

DTK 对话框基类，为所有 DTK 对话框提供统一的窗口装饰和交互基础。

#### 功能能力总结

提供对话框的圆角、阴影、背景模糊这些窗口装饰效果，支持模态与非模态显示、对话框内容布局管理、窗口标志设置和关闭事件处理。 采用 DTK 私有类架构。

#### 使用场景

需要创建自定义 DTK 风格对话框时，作为基类继承使用。

### DDialog

#### 定位

DTK 风格的通用对话框。

#### 功能能力总结

提供 DTK 风格的对话框内容布局（标题、内容区、按钮区），支持添加内容控件和按钮、设置对话框图标和标题文字、模态显示和关闭。

#### 使用场景

需要创建自定义 DTK 风格对话框时；需要带标题、内容和按钮分区的对话框时。

### DDialogCloseButton

#### 定位

对话框关闭按钮控件。

#### 功能能力总结

提供 DTK 风格的关闭按钮，通常用于对话框标题栏。预设关闭图标。

#### 使用场景

需要在对话框或窗口标题栏中放置关闭按钮时。

### DAboutDialog

#### 定位

DTK 风格的"关于"对话框。

#### 功能能力总结

展示应用名称、版本号、图标和描述信息，提供 DTK 风格的关于对话框外观。

#### 使用场景

需要展示应用程序"关于"信息时。

### DFileDialog

#### 定位

DTK 风格的文件对话框。

#### 功能能力总结

并提供 DTK 风格外观，支持文件选择和保存对话框模式、文件过滤器设置、多选模式。

#### 使用场景

需要 DTK 风格的文件打开/保存对话框时，替代 Qt 标准文件对话框使用。

### DInputDialog

#### 定位

DTK 风格的输入对话框。

#### 功能能力总结

提供 DTK 风格的输入对话框，支持文本输入、整数输入、双精度输入和列表选择模式。支持设置输入范围、步长和默认值。

#### 使用场景

需要弹出对话框让用户输入文本、数值或从列表中选择时，替代 Qt 标准输入对话框使用。

### DLicenseDialog

#### 定位

许可证信息对话框。

#### 功能能力总结

展示应用程序的许可证信息，包括许可证类型、条款内容和版权声明。

#### 使用场景

需要展示应用程序许可证信息时。

### DFeatureDisplayDialog

#### 定位

功能特性展示对话框。

#### 功能能力总结

以列表形式展示应用程序的功能特性，支持添加功能项（图标、标题、描述）。

#### 使用场景

需要向用户展示应用程序功能特性或更新内容时。
