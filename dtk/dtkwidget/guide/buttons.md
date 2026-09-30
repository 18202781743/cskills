# 按钮接口

dtkwidget 的按钮接口提供 DTK 风格的图标按钮、建议按钮、警告按钮、工具按钮、命令链接按钮、开关按钮、按钮容器、浮动按钮和箭头按钮。

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

### DIconButton

#### 定位

DTK 风格的图标按钮控件。

#### 功能能力总结

提供 DTK 风格的图标按钮，支持设置图标、图标大小、按钮大小和可选中状态。 采用 DTK 私有类架构。是多个 DTK 按钮控件（浮动按钮、对话框关闭按钮、窗口控制按钮）的基类。

#### 使用场景

需要 DTK 风格的图标按钮时；需要创建自定义图标按钮时。

### DSuggestButton

#### 定位

DTK 建议按钮控件。

#### 功能能力总结

提供 DTK 风格的建议（主操作）按钮，视觉上突出于普通按钮。 采用 DTK 私有类架构。

#### 使用场景

需要突出显示主操作按钮时，如对话框中的"确定"按钮。

### DWarningButton

#### 定位

DTK 警告按钮控件。

#### 功能能力总结

提供 DTK 风格的警告按钮，视觉上以警告色突出。

#### 使用场景

需要突出显示危险或警告操作按钮时，如"删除"按钮。

### DToolButton

#### 定位

DTK 风格的工具按钮控件。

#### 功能能力总结

提供 DTK 风格的工具按钮外观。支持设置图标、文字和弹出模式。

#### 使用场景

需要 DTK 风格的工具按钮时，替代 Qt 标准工具按钮使用。

### DCommandLinkButton

#### 定位

命令链接按钮控件。

#### 功能能力总结

提供带有图标和描述文本的命令链接按钮，外观为带箭头的可点击文本。

#### 使用场景

需要展示命令链接式按钮时，如向导页面中的选项选择。

### DSwitchButton

#### 定位

DTK 开关按钮控件。

#### 功能能力总结

提供 DTK 风格的开关切换按钮，支持开/关状态切换和状态变化信号。 采用 DTK 私有类架构。

#### 使用场景

需要开关切换控件时，替代 Qt 标准复选框的开关样式。

### DButtonBox

#### 定位

DTK 风格的按钮组容器控件。

#### 功能能力总结

将多个按钮水平或垂直排列在统一容器中，按钮之间共享样式和间距。支持添加、插入和移除按钮，以及获取按钮列表。提供 DButtonBoxButton 作为组内按钮类型。

#### 使用场景

需要将多个操作按钮以统一样式成组排列时，如对话框底部按钮组。

### DFloatingButton

#### 定位

浮动按钮控件。

#### 功能能力总结

提供圆形浮动按钮外观，支持设置按钮大小和图标。

#### 使用场景

需要圆形浮动操作按钮时，如 Material Design 风格的 FAB。

### DArrowButton

#### 定位

带箭头方向的按钮控件。

#### 功能能力总结

提供四个方向（上、下、左、右）的箭头按钮，支持设置箭头方向和按钮样式。

#### 使用场景

需要方向箭头按钮控件时，如展开/收起指示器、滚动控制。

### DImageButton

#### 定位

DTK5 图片按钮控件。

#### 功能能力总结

通过设置不同状态（正常、悬停、按下、禁用）的图片来呈现按钮外观。支持设置各状态图片和按钮大小。

#### 使用场景

仅在 DTK5 中使用。DTK6 中已移除，替代方式为使用 DIconButton。
