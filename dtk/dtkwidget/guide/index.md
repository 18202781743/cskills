# dtkwidget 二次开发文档 · 概览

## 项目定位

dtkwidget 是基于 Qt Widgets 模块的 C++ 控件库，提供 DTK 风格的对话框、窗口、按钮、输入框、列表、视图、样式、动画效果、打印预览、设置界面和辅助工具这些控件级别的功能。图形界面层面的非控件能力（调色板、DCI 图标、窗口装饰）由下层 dtkgui 提供。

## 导出类型

- [按钮](dtkwidget-dev/buttons.md)：图标按钮、建议按钮、警告按钮、工具按钮、开关按钮与浮动按钮
- [容器与布局](dtkwidget-dev/containers-and-layout.md)：框架、分隔线、背景分组、抽屉、展开组与箭头矩形
- [对话框](dtkwidget-dev/dialogs.md)：对话框基类、通用对话框、关于对话框、文件对话框、输入对话框、许可证对话框与特性展示对话框
- [浮层与提示](dtkwidget-dev/overlays-and-tooltips.md)：浮动控件、浮动消息、消息管理器、提示标签与吐司提示
- [输入控件](dtkwidget-dev/input-controls.md)：单行编辑、密码编辑、搜索编辑、数值输入、滑动条与组合框
- [列表与视图](dtkwidget-dev/list-and-views.md)：列表视图、简单列表视图、标准项与样式化项代理
- [打印预览](dtkwidget-dev/print-preview.md)：打印预览对话框及其设置信息与设置接口
- [设置界面](dtkwidget-dev/settings-ui.md)：设置对话框与设置控件工厂
- [样式与主题](dtkwidget-dev/style-and-theme.md)：样式引擎、样式选项、应用主题辅助、调色板辅助、尺寸模式与字号管理
- [工具与辅助](dtkwidget-dev/tools-and-helpers.md)：标签、图像查看器、文件图标提供者与控件工具函数
- [视觉效果与进度](dtkwidget-dev/visual-effects-and-progress.md)：模糊效果、裁剪效果、图形阴影效果、进度条与加载指示器
- [窗口与标题栏](dtkwidget-dev/window-and-titlebar.md)：主窗口、标题栏、平台窗口句柄与窗口控制按钮

## 按功能查阅

- 使用对话框：参见 [DDialog](dtkwidget-dev/dialogs.md#ddialog) 与 [DFileDialog](dtkwidget-dev/dialogs.md#dfiledialog)
- 使用窗口与标题栏：参见 [DMainWindow](dtkwidget-dev/window-and-titlebar.md#dmainwindow) 与 [DTitlebar](dtkwidget-dev/window-and-titlebar.md#dtitlebar)
- 使用按钮：参见 [DIconButton](dtkwidget-dev/buttons.md#diconbutton) 与 [DSwitchButton](dtkwidget-dev/buttons.md#dswitchbutton)
- 使用输入控件：参见 [DLineEdit](dtkwidget-dev/input-controls.md#dlineedit) 与 [DComboBox](dtkwidget-dev/input-controls.md#dcombobox)
- 使用列表与视图：参见 [DListView](dtkwidget-dev/list-and-views.md#dlistview) 与 [DStandardItem](dtkwidget-dev/list-and-views.md#dstandarditem)
- 管理样式与主题：参见 [DStyle](dtkwidget-dev/style-and-theme.md#dstyle) 与 [DApplicationHelper](dtkwidget-dev/style-and-theme.md#dapplicationhelper)
- 使用视觉效果与进度：参见 [DBlurEffectWidget](dtkwidget-dev/visual-effects-and-progress.md#dblureffectwidget) 与 [DProgressBar](dtkwidget-dev/visual-effects-and-progress.md#dprogressbar)
- 使用容器与布局：参见 [DFrame](dtkwidget-dev/containers-and-layout.md#dframe) 与 [DDrawer](dtkwidget-dev/containers-and-layout.md#ddrawer)
- 使用浮层与提示：参见 [DFloatingWidget](dtkwidget-dev/overlays-and-tooltips.md#dfloatingwidget) 与 [DMessageManager](dtkwidget-dev/overlays-and-tooltips.md#dmessagemanager)
- 使用设置界面：参见 [DSettingsDialog](dtkwidget-dev/settings-ui.md#dsettingsdialog) 与 [DSettingsWidgetFactory](dtkwidget-dev/settings-ui.md#dsettingswidgetfactory)
- 使用打印预览：参见 [DPrintPreviewDialog](dtkwidget-dev/print-preview.md#dprintpreviewdialog)
- 将 dtkwidget 引入 CMake 工程：参见 [dtkwidget-dev.md](dtkwidget-dev.md) 中的 `## 开发包` 与 `## 集成` 章节
