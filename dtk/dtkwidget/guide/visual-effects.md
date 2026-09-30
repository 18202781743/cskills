# 视觉效果与进度接口

dtkwidget 的视觉效果与进度接口提供 DTK 风格的模糊效果、裁剪效果、图形阴影效果、弹跳动画、水波进度、加载指示器和进度条。

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

### DBlurEffectWidget

#### 定位

带实时背景模糊效果的窗口控件。

#### 功能能力总结

对控件背后的窗口内容进行实时高斯模糊渲染，支持设置模糊半径、混合模式和是否带边框。可创建透明模糊的窗口或面板效果。

#### 使用场景

需要创建毛玻璃/磨砂效果的窗口或面板时；需要实时模糊背景的浮层时。

### DBlurEffectWithBorderWidget

#### 定位

带边框的模糊效果窗口控件。

#### 功能能力总结

在模糊效果基础上增加边框绘制。支持设置边框颜色和宽度。

#### 使用场景

需要带边框的毛玻璃效果窗口时。

### DClipEffectWidget

#### 定位

带裁剪效果的窗口控件。

#### 功能能力总结

对控件或窗口内容应用圆角裁剪效果，支持设置裁剪半径。可与模糊效果控件配合使用。

#### 使用场景

需要对窗口或控件内容进行圆角裁剪时。

### DGraphicsClipEffect

#### 定位

图形裁剪效果。

#### 功能能力总结

为控件提供图形裁剪效果，支持设置裁剪路径和圆角。 采用 DTK 私有类架构。

#### 使用场景

需要对控件内容进行自定义裁剪时。

### DGraphicsDropShadowEffect

#### 定位

图形阴影投射效果。

#### 功能能力总结

为控件添加投影阴影效果，支持设置阴影偏移、模糊半径、颜色和圆角。对应实际实现为 DGraphicsGlowEffect。

#### 使用场景

需要为控件添加投影或发光阴影效果时。

### DBounceAnimation

#### 定位

弹性反弹动画工具。

#### 功能能力总结

为控件提供弹性反弹动画效果，支持设置动画持续时间、弹跳幅度和方向。可对任意 Qt 窗口组件应用弹跳动画。

#### 使用场景

需要为控件添加弹性动画效果时，如按钮点击反馈、提示注意力。

### DWaterProgress

#### 定位

DTK 水波进度球控件。

#### 功能能力总结

以水波填充球体的动画形式显示进度，支持设置进度值、水波颜色和动画速度。

#### 使用场景

需要以视觉效果丰富的进度球显示加载或处理进度时。

### DSpinner

#### 定位

加载旋转动画控件。

#### 功能能力总结

提供旋转加载动画效果，支持设置动画速度、开始和停止。以圆形旋转动画表示加载状态。

#### 使用场景

需要显示加载中状态时，替代不确定进度条。

### DColoredProgressBar

#### 定位

支持分段着色的进度条控件。

#### 功能能力总结

在 Qt 标准进度条基础上支持按进度区间设置不同颜色，实现多色进度条效果。支持添加颜色区间和对应的进度范围。

#### 使用场景

需要按不同进度区间显示不同颜色的进度条时。

### DProgressBar

#### 定位

DTK 风格的进度条控件。

#### 功能能力总结

采用 DTK 私有类架构，提供 DTK 风格的进度条外观。

#### 使用场景

需要 DTK 风格的进度条时，替代 Qt 标准进度条使用。

### DIndeterminateProgressbar

#### 定位

不定状态进度条控件。

#### 功能能力总结

显示持续滚动的不定进度条动画，表示操作正在进行但无法确定具体进度。支持设置动画速度。

#### 使用场景

需要表示操作进行中但无法确定进度时。

### DPageIndicator

#### 定位

页面指示器控件。

#### 功能能力总结

显示页面导航指示点，支持设置页面数量、当前页面、指示点大小和颜色。支持点击切换页面。

#### 使用场景

需要显示多页面导航指示器时，如轮播图、引导页。

### DSegmentedControl

#### 定位

DTK5 分段选择控件。

#### 功能能力总结

提供水平排列的分段选择器，支持添加多个分段项、设置当前选中分段和分段切换信号。

#### 使用场景

仅在 DTK5 中使用。DTK6 中已移除。

### DSegmentedHighlight

#### 定位

DTK5 分段高亮控件。

#### 功能能力总结

为分段项提供高亮显示效果，与 DSegmentedControl 配合使用。

#### 使用场景

仅在 DTK5 中使用。DTK6 中已移除。
