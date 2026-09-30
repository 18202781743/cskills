# 打印预览接口

dtkwidget 的打印预览接口提供 DTK 风格的打印预览对话框及其设置信息与设置接口。

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

### DPrintPreviewDialog

#### 定位

DTK 风格的打印预览对话框。

#### 功能能力总结

提供 DTK 风格的打印预览界面，支持页面导航、缩放、打印设置和打印操作。可嵌入自定义打印预览设置界面。

#### 使用场景

需要为应用程序提供打印预览功能时。

### DPrintPreviewSettingInfo

#### 定位

打印预览设置信息基类。

#### 功能能力总结

作为打印预览设置项的信息载体基类，支持克隆和类型识别。子类携带具体的设置项数据（如纸张大小、方向、份数）。

#### 使用场景

需要向 DPrintPreviewDialog 传递打印设置项数据时；需要自定义打印设置项时。

### DPrintPreviewSettingInterface

#### 定位

打印预览设置界面接口。

#### 功能能力总结

定义打印预览设置界面的接口规范，支持创建设置控件、读取和写入设置值。子类实现具体设置界面的创建和数据交互。

#### 使用场景

需要为打印预览对话框自定义设置界面时。
