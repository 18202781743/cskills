# dtkwidget-dev

dtkwidget 的按钮接口为各类交互操作提供 DTK 风格的按钮控件，覆盖从普通图标按钮、建议与警告等语义化按钮到开关切换、命令链接、浮动操作和方向箭头等不同交互模式，支持按钮组容器统一管理布局和样式。

dtkwidget 的容器与布局接口提供框架、分隔线、分组背景等结构化容器，以及抽屉、展开组等可折叠内容区域和锚点布局、标签页栏等布局工具，帮助开发者组织界面层级和空间分配。

dtkwidget 的对话框接口提供模态与非模态对话框的基类框架，并内置关于、文件选择、文本输入、许可证展示和功能特性介绍等常用专用对话框，统一遵循 DTK 圆角、阴影和布局规范。

dtkwidget 的浮层与提示接口提供浮动在主界面之上的临时消息和提示控件，支持消息停留、自动消失和吐司式通知，适用于不阻塞用户操作的轻量反馈场景。

dtkwidget 的输入控件接口为文本、数值和选择类输入提供 DTK 风格的编辑控件，涵盖单行与多行文本、密码、搜索、IP 地址、文件路径、快捷键、面包屑导航以及数值滑动和组合选择等场景。

dtkwidget 的列表与视图接口提供列表展示和项渲染能力，支持标准项和自定义样式化项代理，适用于设置面板、文件浏览等需要结构化数据展示的场景。

dtkwidget 的打印预览接口提供打印预览对话框及关联的页面设置能力，支持在预览界面中调整打印参数并实时查看效果。

dtkwidget 的设置界面接口提供从配置模型自动生成设置界面的框架，通过设置对话框和控件工厂将配置项映射为复选框、下拉框等界面控件。

dtkwidget 的样式与主题接口是 dtkwidget 的视觉基础设施，管理 DTK 样式引擎、调色板、主题切换、尺寸模式、字号规格和水印效果，并为无障碍检查提供开发辅助工具。

dtkwidget 的工具与辅助接口提供标签显示、图片查看、文件图标获取等辅助控件和控件操作工具函数，补充核心控件库未覆盖的通用界面需求。

dtkwidget 的视觉效果与进度接口为控件和窗口添加高斯模糊、圆角裁剪、投影阴影等视觉增强效果，并提供弹跳动画、水波进度、加载指示器和进度条等动态反馈控件。

dtkwidget 的窗口与标题栏接口提供 DTK 风格的主窗口框架和自定义标题栏，集成窗口圆角、阴影、拖拽、最大化/最小化/关闭按钮等窗口装饰和交互能力。

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


---

## 接口分类

- [按钮](dtkwidget-dev/buttons.md) — DIconButton 图标按钮、DSuggestButton 建议按钮、DWarningButton 警告按钮、DToolButton 工具按钮、DCommandLinkButton 命令链接按钮、DSwitchButton 开关切换按钮、DButtonBox 按钮组容器、DFloatingButton 浮动按钮、DArrowButton 方向箭头按钮、DImageButton 图片按钮
- [容器与布局](dtkwidget-dev/containers-and-layout.md) — DFrame 框架、DHorizontalLine 水平分隔线、DVerticalLine 垂直分隔线、DBackgroundGroup 分组背景、DShadowLine 阴影分隔线、DDrawer 抽屉、DDrawerGroup 抽屉组、DExpandGroup 展开组、DArrowLineDrawer 箭头抽屉、DArrowLineExpand 箭头展开、DArrowRectangle 箭头矩形、DAnchors 锚点布局、DTabBar 标签页栏
- [对话框](dtkwidget-dev/dialogs.md) — DAbstractDialog 对话框基类、DDialog 对话框、DDialogCloseButton 关闭按钮、DAboutDialog 关于对话框、DFileDialog 文件选择对话框、DInputDialog 文本输入对话框、DLicenseDialog 许可证对话框、DFeatureDisplayDialog 功能特性对话框
- [浮层与提示](dtkwidget-dev/overlays-and-tooltips.md) — DFloatingWidget 浮动控件、DFloatingMessage 浮动消息、DMessageManager 消息管理器、DTipLabel 提示标签、DToolTip 工具提示、DAlertControl 警告控制、DToast 吐司通知
- [输入控件](dtkwidget-dev/input-controls.md) — DLineEdit 单行文本输入、DPasswordEdit 密码输入、DSearchEdit 搜索输入、DIpv4LineEdit IP 地址输入、DFileChooserEdit 文件路径输入、DKeySequenceEdit 快捷键输入、DCrumbEdit 面包屑导航、DTextEdit 多行文本输入、DSpinBox 数值输入、DDoubleSpinBox 双精度数值输入、DSlider 滑动条、DComboBox 下拉框、DSearchComboBox 搜索下拉框、DFontComboBox 字体下拉框
- [列表与视图](dtkwidget-dev/list-and-views.md) — DListView 列表视图、DSimpleListView 简单列表视图、DSimpleListItem 简单列表项、DStandardItem 标准项、DStyledItemDelegate 样式化项代理
- [打印预览](dtkwidget-dev/print-preview.md) — DPrintPreviewDialog 打印预览对话框、DPrintPreviewSettingInfo 打印设置信息、DPrintPreviewSettingInterface 打印设置接口
- [设置界面](dtkwidget-dev/settings-ui.md) — DSettingsDialog 设置对话框、DSettingsWidgetFactory 设置控件工厂
- [样式与主题](dtkwidget-dev/style-and-theme.md) — DStyle 样式引擎、DStyleHelper 样式辅助、DStyleOption 样式选项及多个子类、DStyledIconEngine 样式化图标引擎、DStylePainter 样式绘制器、DApplicationHelper 应用辅助、DPaletteHelper 调色板辅助、DSizeMode 尺寸模式、DFontSizeManager 字号管理、DThemeManager 主题管理、DApplicationSettings 应用设置、DAccessibilityChecker 无障碍检查、DHiDPIHelper 高 DPI 辅助、DWaterMarkHelper 水印辅助
- [工具与辅助](dtkwidget-dev/tools-and-helpers.md) — DLabel 标签显示、DImageViewer 图片查看器、DFileIconProvider 文件图标获取、DWidgetUtil 控件工具函数
- [视觉效果与进度](dtkwidget-dev/visual-effects-and-progress.md) — DBlurEffectWidget 高斯模糊、DBlurEffectWithBorderWidget 带边框模糊、DClipEffectWidget 圆角裁剪、DGraphicsClipEffect 图形裁剪、DGraphicsDropShadowEffect 投影阴影、DBounceAnimation 弹跳动画、DWaterProgress 水波进度、DSpinner 加载指示器、DColoredProgressBar 彩色进度条、DProgressBar 进度条、DIndeterminateProgressbar 不定进度条、DPageIndicator 页面指示器
- [窗口与标题栏](dtkwidget-dev/window-and-titlebar.md) — DSegmentedControl 分段控件、DSegmentedHighlight 分段高亮、DMainWindow 主窗口、DTitlebar 标题栏、DPlatformWindowHandle 平台窗口句柄、DWindowCloseButton 关闭按钮、DWindowMaxButton 最大化按钮、DWindowMinButton 最小化按钮、DWindowOptionButton 选项按钮、DWindowQuitFullButton 退出全屏按钮、DTabletWindowOptionButton 平板选项按钮、DApplication 应用对象
