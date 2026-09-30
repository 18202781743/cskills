# 工具与辅助接口

dtkwidget 的工具与辅助接口提供 DTK 风格的标签、图像查看器、文件图标提供者和控件工具函数。

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

### DLabel

#### 定位

DTK 风格的标签控件。

#### 功能能力总结

并集成 DTK 主题和样式，提供 DTK 风格的文本和图标显示。支持前景色和背景色随主题变化。

#### 使用场景

需要 DTK 风格的标签控件时，替代 Qt 标准标签控件使用。

### DImageViewer

#### 定位

图片查看器控件。

#### 功能能力总结

提供图片显示和交互能力，支持图片缩放、旋转、平移操作，支持设置最大/最小缩放比例和缩放步长。

#### 使用场景

需要在界面中展示图片并支持交互操作时。

### DFileIconProvider

#### 定位

DTK 风格的文件图标提供者。

#### 功能能力总结

为文件和目录提供 DTK 风格的图标，支持按文件类型、大小和主题返回对应图标。

#### 使用场景

需要在文件视图或对话框中显示 DTK 风格文件图标时。

### DWidgetUtil

#### 定位

DTK 控件工具函数集合。

#### 功能能力总结

提供控件相关的辅助工具函数，如窗口移动、窗口居中和便捷的控件操作。

#### 使用场景

需要使用 DTK 控件辅助工具函数时。
