# dtkdeclarative 二次开发文档 · 概览

## 项目定位

dtkdeclarative 是基于 Qt Quick 的 C++ 库，为 DTK QML 声明式控件提供底层支撑。它提供 DTK 应用的 QML 加载器、应用主窗口与预加载接口、QML 场景中的帧缓冲区位块传输与视口裁剪渲染、DTK 窗口附加属性以及平台主题代理。QML 控件本身以 `org.deepin.dtk` QML 模块的形式发布。

## 术语与缩写

- **DTK**：Deepin Tool Kit。
- **DTK5 / DTK6**：分别与 Qt5 / Qt6 配套的主版本。
- **DDeclarative**：公开头文件安装目录名。
- **QML URI**：DTK 声明式控件的 QML 模块标识，固定为 `org.deepin.dtk`。
- **转发头**：以公开类型名命名的无后缀头文件，转而引入实际声明所在的头文件。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。它以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 全局约定

公开头文件安装在按主版本区分的 DDeclarative 目录。C++ 公开符号位于 `Dtk::Quick` 命名空间。QML 模块安装到 Qt 的 QML 插件目录下 `org/deepin/dtk` 路径。版本判断和跨主版本构建方式见[集成与构建配置](integration.md)。

## 按功能查阅

- 将 dtkdeclarative 引入 CMake、pkg-config 或 qmake 工程：参见[集成与构建配置](integration.md)。
- 加载 DTK QML 应用：参见 [DAppLoader](modules.md#dapploader)。
- 自定义 DTK 应用主窗口行为：参见 [DQmlAppMainWindowInterface](modules.md#dqmlappmainwindowinterface)。
- 应用预加载扩展：参见 [DQmlAppPreloadInterface](modules.md#dqmlapppreloadinterface)。
- QML 场景中的帧缓冲区位块传输与视口渲染：参见 [DQuickBlitFramebuffer](modules.md#dquickblitframebuffer) 与 [DQuickItemViewport](modules.md#dquickitemviewport)。
- DTK 窗口属性：参见 [DQuickWindow](modules.md#dquickwindow) 与 [DQuickWindowAttached](modules.md#dquickwindowattached)。
- DTK5 平台主题代理：参见 [DPlatformThemeProxy](modules.md#dplatformthemeproxy)。
- 在 DTK5 与 DTK6 之间迁移构建配置：参见[集成与构建配置](integration.md)；迁移公开类型：参见对应的[导出类型介绍](modules.md)。
- DTK QML 模块导入与类型范围：参见 [org.deepin.dtk](modules.md#orgdeepindtk)。
- DTK 风格按钮：参见 [Button](modules.md#button)、[RoundButton](modules.md#roundbutton)、[DelayButton](modules.md#delaybutton)、[IconButton](modules.md#iconbutton)、[FloatingButton](modules.md#floatingbutton)。
- DTK 风格文本输入：参见 [TextField](modules.md#textfield)、[TextArea](modules.md#textarea)、[SearchEdit](modules.md#searchedit)、[PasswordEdit](modules.md#passwordedit)、[IpV4LineEdit](modules.md#ipv4lineedit)、[KeySequenceEdit](modules.md#keysequenceedit)。
- DTK 风格数值输入：参见 [SpinBox](modules.md#spinbox)、[PlusMinusSpinBox](modules.md#plusminusspinbox)、[Dial](modules.md#dial)。
- DTK 风格选择控件：参见 [CheckBox](modules.md#checkbox)、[RadioButton](modules.md#radiobutton)、[Switch](modules.md#switch)、[ComboBox](modules.md#combobox)。
- DTK 风格滑动条与进度指示：参见 [Slider](modules.md#slider)、[TipsSlider](modules.md#tipsslider)、[ProgressBar](modules.md#progressbar)、[WaterProgressBar](modules.md#waterprogressbar)、[BusyIndicator](modules.md#busyindicator)。
- DTK 风格对话框与弹窗：参见 [DialogWindow](modules.md#dialogwindow)、[Dialog](modules.md#dialog)、[PopupWindow](modules.md#popupwindow)、[ArrowShapePopupWindow](modules.md#arrowshapepopupwindow)。
- DTK 风格窗口与标题栏：参见 [DWindow](modules.md#dwindow)、[ApplicationWindow](modules.md#applicationwindow)、[TitleBar](modules.md#titlebar)。
- DTK 风格菜单：参见 [Menu](modules.md#menu)、[MenuItem](modules.md#menuitem)、[MenuBar](modules.md#menubar)。
- DTK 风格列表与视图：参见 [ScrollView](modules.md#scrollview)、[StackView](modules.md#stackview)、[SwipeView](modules.md#swipeview)、[ItemDelegate](modules.md#itemdelegate)。
- DTK 风格阴影与面板渲染：参见 [BoxShadow](modules.md#boxshadow)、[BoxInsetShadow](modules.md#boxinsetshadow)、[BoxPanel](modules.md#boxpanel)、[FloatingPanel](modules.md#floatingpanel)。
- DTK 风格标签与提示：参见 [Label](modules.md#label)、[ToolTip](modules.md#tooltip)、[AlertToolTip](modules.md#alerttooltip)。
- DTK 设置对话框控件：参见 [SettingsDialog](modules.md#settingsdialog)、[OptionDelegate](modules.md#optiondelegate)、[NavigationTitle](modules.md#navigationtitle)。
- DTK 样式参数：参见 [Style](modules.md#style)。
- QML 场景中的帧缓冲区位块传输与视口渲染（QML 侧）：参见 [BlitFramebuffer](modules.md#blitframebuffer) 与 [ItemViewport](modules.md#itemviewport)。
