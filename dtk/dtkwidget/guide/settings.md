# 设置界面接口

dtkwidget 的设置界面接口提供 DTK 风格的设置对话框和设置控件工厂，用于从设置模型生成界面控件。

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

### DSettingsDialog

#### 定位

DTK 设置对话框。

#### 功能能力总结

基于 DSettings 配置框架构建设置界面，支持分组、分页展示设置项。通过 DSettingsWidgetFactory 创建各设置项的编辑控件。

#### 使用场景

需要为应用程序设置界面时；使用 DTK 设置框架管理应用配置时。

### DSettingsWidgetFactory

#### 定位

DTK 设置控件工厂。

#### 功能能力总结

根据设置项类型和自定义键值创建对应的编辑控件，支持注册自定义控件创建函数。与 DSettingsDialog 配合使用，将设置项映射为具体的编辑控件。

#### 使用场景

需要自定义设置界面中的控件类型时；需要为设置项创建自定义编辑控件时。
