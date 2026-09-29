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

[导出类型介绍](dtk6declarative-dev.md)是本项目的 C++ 类型参考文档，QML 控件见[dtkdeclarative-qml-controls.md](dtkdeclarative-qml-controls.md)，QML 设置控件见[dtkdeclarative-qml-settings.md](dtkdeclarative-qml-settings.md)。它以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 全局约定

公开头文件安装在按主版本区分的 DDeclarative 目录。C++ 公开符号位于 `Dtk::Quick` 命名空间。QML 模块安装到 Qt 的 QML 插件目录下 `org/deepin/dtk` 路径。版本判断和跨主版本构建方式见[集成与构建配置](integration.md)。

## 按功能查阅

- 将 dtkdeclarative 引入 CMake、pkg-config 或 qmake 工程：参见[集成与构建配置](integration.md)。
- 加载 DTK QML 应用：参见 [DAppLoader](dtk6declarative-dev.md#dapploader)。
- 自定义 DTK 应用主窗口行为：参见 [DQmlAppMainWindowInterface](dtk6declarative-dev.md#dqmlappmainwindowinterface)。
- 应用预加载扩展：参见 [DQmlAppPreloadInterface](dtk6declarative-dev.md#dqmlapppreloadinterface)。
- QML 场景中的帧缓冲区位块传输与视口渲染：参见 [DQuickBlitFramebuffer](dtk6declarative-dev.md#dquickblitframebuffer) 与 [DQuickItemViewport](dtk6declarative-dev.md#dquickitemviewport)。
- DTK 窗口属性：参见 [DQuickWindow](dtk6declarative-dev.md#dquickwindow) 与 [DQuickWindowAttached](dtk6declarative-dev.md#dquickwindowattached)。
- DTK5 平台主题代理：参见 [DPlatformThemeProxy](dtk6declarative-dev.md#dplatformthemeproxy)。
- 在 DTK5 与 DTK6 之间迁移构建配置：参见[集成与构建配置](integration.md)；迁移公开类型：参见对应的[导出类型介绍](dtk6declarative-dev.md)。
- DTK QML 模块导入与类型范围：参见 [org.deepin.dtk](dtkdeclarative-qml-controls.md#org-deepin-dtk)。
- DTK 风格按钮：参见 [Button](dtkdeclarative-qml-controls.md#button)、[RoundButton](dtkdeclarative-qml-controls.md#roundbutton)、[DelayButton](dtkdeclarative-qml-controls.md#delaybutton)、[IconButton](dtkdeclarative-qml-controls.md#iconbutton)、[FloatingButton](dtkdeclarative-qml-controls.md#floatingbutton)。
- DTK 风格文本输入：参见 [TextField](dtkdeclarative-qml-controls.md#textfield)、[TextArea](dtkdeclarative-qml-controls.md#textarea)、[SearchEdit](dtkdeclarative-qml-controls.md#searchedit)、[PasswordEdit](dtkdeclarative-qml-controls.md#passwordedit)、[IpV4LineEdit](dtkdeclarative-qml-controls.md#ipv4lineedit)、[KeySequenceEdit](dtkdeclarative-qml-controls.md#keysequenceedit)。
- DTK 风格数值输入：参见 [SpinBox](dtkdeclarative-qml-controls.md#spinbox)、[PlusMinusSpinBox](dtkdeclarative-qml-controls.md#plusminusspinbox)、[Dial](dtkdeclarative-qml-controls.md#dial)。
- DTK 风格选择控件：参见 [CheckBox](dtkdeclarative-qml-controls.md#checkbox)、[RadioButton](dtkdeclarative-qml-controls.md#radiobutton)、[Switch](dtkdeclarative-qml-controls.md#switch)、[ComboBox](dtkdeclarative-qml-controls.md#combobox)。
- DTK 风格滑动条与进度指示：参见 [Slider](dtkdeclarative-qml-controls.md#slider)、[TipsSlider](dtkdeclarative-qml-controls.md#tipsslider)、[ProgressBar](dtkdeclarative-qml-controls.md#progressbar)、[WaterProgressBar](dtkdeclarative-qml-controls.md#waterprogressbar)、[BusyIndicator](dtkdeclarative-qml-controls.md#busyindicator)。
- DTK 风格对话框与弹窗：参见 [DialogWindow](dtkdeclarative-qml-controls.md#dialogwindow)、[Dialog](dtkdeclarative-qml-controls.md#dialog)、[PopupWindow](dtkdeclarative-qml-controls.md#popupwindow)、[ArrowShapePopupWindow](dtkdeclarative-qml-controls.md#arrowshapepopupwindow)。
- DTK 风格窗口与标题栏：参见 [DWindow](dtkdeclarative-qml-controls.md#dwindow)、[ApplicationWindow](dtkdeclarative-qml-controls.md#applicationwindow)、[TitleBar](dtkdeclarative-qml-controls.md#titlebar)。
- DTK 风格菜单：参见 [Menu](dtkdeclarative-qml-controls.md#menu)、[MenuItem](dtkdeclarative-qml-controls.md#menuitem)、[MenuBar](dtkdeclarative-qml-controls.md#menubar)。
- DTK 风格列表与视图：参见 [ScrollView](dtkdeclarative-qml-controls.md#scrollview)、[StackView](dtkdeclarative-qml-controls.md#stackview)、[SwipeView](dtkdeclarative-qml-controls.md#swipeview)、[ItemDelegate](dtkdeclarative-qml-controls.md#itemdelegate)。
- DTK 风格阴影与面板渲染：参见 [BoxShadow](dtkdeclarative-qml-controls.md#boxshadow)、[BoxInsetShadow](dtkdeclarative-qml-controls.md#boxinsetshadow)、[BoxPanel](dtkdeclarative-qml-controls.md#boxpanel)、[FloatingPanel](dtkdeclarative-qml-controls.md#floatingpanel)。
- DTK 风格标签与提示：参见 [Label](dtkdeclarative-qml-controls.md#label)、[ToolTip](dtkdeclarative-qml-controls.md#tooltip)、[AlertToolTip](dtkdeclarative-qml-controls.md#alerttooltip)。
- DTK 设置对话框控件：参见 [SettingsDialog](dtkdeclarative-qml-settings.md#settingsdialog)、[OptionDelegate](dtkdeclarative-qml-settings.md#optiondelegate)、[NavigationTitle](dtkdeclarative-qml-settings.md#navigationtitle)。
- DTK 样式参数：参见 [Style](dtkdeclarative-qml-settings.md#style)。
- QML 场景中的帧缓冲区位块传输与视口渲染（QML 侧）：参见 [BlitFramebuffer](dtkdeclarative-qml-controls.md#blitframebuffer) 与 [ItemViewport](dtkdeclarative-qml-controls.md#itemviewport)。
