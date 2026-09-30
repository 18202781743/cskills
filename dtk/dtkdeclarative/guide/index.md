# dtkdeclarative 二次开发文档 · 概览

## 项目定位

dtkdeclarative 是基于 Qt Quick 的 C++ 库，为 DTK QML 声明式控件提供底层支撑。它提供 DTK 应用的 QML 加载器、应用主窗口与预加载接口、QML 场景中的帧缓冲区位块传输与视口裁剪渲染、DTK 窗口附加属性以及平台主题代理。QML 控件本身以 `org.deepin.dtk` QML 模块的形式发布，设置控件以 `org.deepin.dtk.settings` QML 模块的形式发布。

## 导出类型

- [应用加载](dtkdeclarative-dev.md#应用加载)：DTK QML 应用加载器、应用主窗口接口与应用预加载扩展接口
- [快速渲染](dtkdeclarative-dev.md#快速渲染)：QML 场景中的帧缓冲区位块传输渲染与视口裁剪渲染
- [QML 窗口](dtkdeclarative-dev.md#qml-窗口)：DTK 窗口及其附加属性
- [DTK5 主题兼容](dtkdeclarative-dev.md#dtk5-主题兼容)：平台主题代理与系统调色板 QML 项（仅 DTK5）
- [org.deepin.dtk 按钮控件](org.deepin.dtk.md)：DTK 风格按钮、开关按钮与按钮容器
- [org.deepin.dtk 输入控件](org.deepin.dtk.md)：DTK 风格文本输入、数值输入、选择控件与滑动条
- [org.deepin.dtk 对话框与窗口控件](org.deepin.dtk.md)：DTK 风格对话框、弹出窗口、应用窗口与关于对话框
- [org.deepin.dtk 菜单与动作控件](org.deepin.dtk.md)：DTK 风格菜单、菜单项与动作
- [org.deepin.dtk 列表与视图控件](org.deepin.dtk.md)：DTK 风格滚动视图、堆栈视图、项代理与滚动条
- [org.deepin.dtk 视觉效果与渲染控件](org.deepin.dtk.md)：DTK 风格阴影、面板、进度条、标签提示与浮动消息
- [org.deepin.dtk.settings QML 模块](org.deepin.dtk.settings.md)：DTK 风格设置对话框与配置项控件

## 按功能查阅

- 加载 DTK QML 应用：参见 [DAppLoader](dtkdeclarative-dev.md#dapploader)
- QML 场景中的位块传输与视口渲染：参见 [DQuickBlitFramebuffer](dtkdeclarative-dev.md#dquickblitframebuffer) 与 [DQuickItemViewport](dtkdeclarative-dev.md#dquickitemviewport)
- DTK 窗口属性：参见 [DQuickWindow](dtkdeclarative-dev.md#dquickwindow) 与 [DQuickWindowAttached](dtkdeclarative-dev.md#dquickwindowattached)
- DTK 风格按钮：参见 [Button](org.deepin.dtk.md#button) 与 [IconButton](org.deepin.dtk.md#iconbutton)
- DTK 风格文本输入：参见 [TextField](org.deepin.dtk.md#textfield) 与 [SearchEdit](org.deepin.dtk.md#searchedit)
- DTK 风格滑动条：参见 [Slider](org.deepin.dtk.md#slider) 与 [TipsSlider](org.deepin.dtk.md#tipsslider)
- DTK 风格对话框与弹窗：参见 [DialogWindow](org.deepin.dtk.md#dialogwindow) 与 [PopupWindow](org.deepin.dtk.md#popupwindow)
- DTK 风格关于对话框：参见 [AboutDialog](org.deepin.dtk.md#aboutdialog)
- DTK 风格菜单：参见 [Menu](org.deepin.dtk.md#menu) 与 [MenuItem](org.deepin.dtk.md#menuitem)
- DTK 风格列表与视图：参见 [ScrollView](org.deepin.dtk.md#scrollview) 与 [ItemDelegate](org.deepin.dtk.md#itemdelegate)
- DTK 风格滚动条与滚动指示器：参见 [ScrollBar](org.deepin.dtk.md#scrollbar) 与 [ScrollIndicator](org.deepin.dtk.md#scrollindicator)
- DTK 风格阴影与面板：参见 [BoxShadow](org.deepin.dtk.md#boxshadow) 与 [FloatingPanel](org.deepin.dtk.md#floatingpanel)
- DTK 风格浮动消息提示：参见 [FloatingMessage](org.deepin.dtk.md#floatingmessage)
- DTK 设置对话框控件：参见 [SettingsDialog](org.deepin.dtk.settings.md#settingsdialog) 与 [OptionDelegate](org.deepin.dtk.settings.md#optiondelegate)
- 将 dtkdeclarative 引入 CMake 工程：参见 [dtkdeclarative-dev.md](dtkdeclarative-dev.md) 中的 `## 开发包` 与 `## 集成` 章节
- 将 DTK QML 控件引入 QML 工程：参见 [org.deepin.dtk.md](org.deepin.dtk.md) 中的 `## 集成` 章节
