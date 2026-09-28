# 导出类型介绍

dtkdeclarative 提供 DTK QML 应用的加载器、应用主窗口接口与预加载接口、QML 场景中的帧缓冲区位块传输渲染与视口裁剪渲染、DTK 窗口及其附加属性。DTK5 还提供平台主题代理和系统调色板 QML 项。

## DAppLoader

### 定位

DTK QML 应用的加载器。

### 功能能力总结

以单例方式运行，负责初始化 QML 引擎、加载 QML 主文件并创建应用主窗口。支持设置应用元数据、QML 上下文属性和翻译加载。内部管理 QML 引擎生命周期，并在窗口关闭时处理应用退出逻辑。

### 使用场景

作为 DTK QML 应用的入口点使用，通常由 DTK 应用模板自动调用，无需直接实例化。

## DQmlAppMainWindowInterface

### 定位

DTK QML 应用主窗口的 C++ 扩展接口。

### 功能能力总结

纯虚接口（使用 `Q_DECLARE_INTERFACE` 声明），定义 DTK QML 应用主窗口可供 C++ 插件扩展的行为契约。插件通过实现此接口向主窗口注入自定义功能。

### 使用场景

C++ 插件需要扩展 DTK QML 应用主窗口行为时实现此接口。

## DQmlAppPreloadInterface

### 定位

DTK QML 应用预加载的 C++ 扩展接口。

### 功能能力总结

纯虚接口（使用 `Q_DECLARE_INTERFACE` 声明），定义在 QML 引擎加载主文件前执行预加载逻辑的契约。插件通过实现此接口在应用启动早期完成资源预加载、配置初始化操作。

### 使用场景

C++ 插件需要在 QML 应用启动早期执行预加载逻辑时实现此接口。

## DQuickBlitFramebuffer

### 定位

QML 场景中的帧缓冲区位块传输渲染项。

### 功能能力总结

继承 QQuickItem，将离屏帧缓冲区内容通过位块传输（blit）方式渲染到 QML 场景中。在 DTK6 中通过 `QML_NAMED_ELEMENT(BlitFramebuffer)` 注册为 QML 类型 `BlitFramebuffer`，可在 QML 中直接使用。

### 使用场景

需要将离屏渲染的帧缓冲区内容高效地呈现到 QML 场景中时。

## DQuickItemViewport

### 定位

QML 场景中的视口裁剪渲染项。

### 功能能力总结

继承 QQuickItem，提供将指定源项的局部区域裁剪并渲染到视口的能力。在 DTK6 中通过 `QML_NAMED_ELEMENT(ItemViewport)` 注册为 QML 类型 `ItemViewport`，可在 QML 中直接使用。

### 使用场景

需要在 QML 中实现视口裁剪或局部区域渲染时。

## DQuickWindow

### 定位

DTK QML 窗口类型。

### 功能能力总结

继承 QQuickWindow，提供 DTK 窗口特有的属性和行为，包括窗口圆角、模糊效果、窗口阴影在内的平台视觉属性的 QML 接口。在 DTK6 中通过 `QML_NAMED_ELEMENT(DWindow)` 注册为 QML 类型 `DWindow`，可在 QML 中直接使用。

### 使用场景

QML 中需要使用 DTK 扩展窗口属性（圆角、模糊、阴影）时。

## DQuickWindowAttached

### 定位

DTK 窗口附加属性提供者。

### 功能能力总结

继承 QObject，通过 `QML_ATTACHED` 机制为任意 QML Item 提供 DTK 窗口附加属性。使普通 QML Item 能够访问其所属 DTK 窗口的平台属性。

### 使用场景

需要在普通 QML Item 中访问所属 DTK 窗口的平台属性时。

## DPlatformThemeProxy

### 定位

平台主题的 QML 代理接口（仅 DTK5）。

### 功能能力总结

继承 QObject，将 DPlatformTheme 的平台主题属性（主题色、字号、图标主题）暴露为 QML 可访问的属性和信号。DTK6 已移除此类型，相关功能由 QML 层直接提供。

### 使用场景

DTK5 QML 应用中需要读取或监听平台主题属性变化时。

## DQuickSystemPalette

### 定位

QML 系统调色板项（仅 DTK5，已废弃）。

### 功能能力总结

继承 QObject，将系统调色板暴露为 QML 可访问的属性，支持 Active、Inactive、Disabled 三种颜色组。已废弃，应使用 `DQMLGlobalObject::palette` 替代。DTK6 已移除此类型。

### 使用场景

已废弃，DTK5 中如需在 QML 中访问系统调色板时可使用，新代码应迁移至 `DQMLGlobalObject::palette`。
## org.deepin.dtk

DTK 声明式控件的 QML 模块，提供基于 Qt Quick 的 DTK 风格控件库。导入方式为 `import org.deepin.dtk`。模块包含按钮、输入框、对话框、菜单、窗口、进度指示、滑动条、列表视图、阴影渲染、浮动面板、标题栏在内的 DTK 风格 QML 控件类型，以及通过 C++ 注册的 `BlitFramebuffer`、`ItemViewport`、`DWindow` 三个 QML 类型。样式参数通过 `org.deepin.dtk.style` 子模块的 `Style` 单例提供，设置对话框控件通过 `org.deepin.dtk.settings` 子模块提供。

### BlitFramebuffer

#### 定位

QML 场景中的帧缓冲区位块传输渲染项，通过 `QML_NAMED_ELEMENT(BlitFramebuffer)` 从 C++ 类 `DQuickBlitFramebuffer` 注册。

#### 功能能力总结

继承 QQuickItem，将离屏帧缓冲区内容通过位块传输方式渲染到 QML 场景中。C++ 侧的详细接口说明参见本文档 [DQuickBlitFramebuffer](#dquickblitframebuffer) 章节。

#### 使用场景

需要将离屏渲染的帧缓冲区内容高效地呈现到 QML 场景中时使用。

### ItemViewport

#### 定位

QML 场景中的视口裁剪渲染项，通过 `QML_NAMED_ELEMENT(ItemViewport)` 从 C++ 类 `DQuickItemViewport` 注册。

#### 功能能力总结

继承 QQuickItem，提供将指定源项的局部区域裁剪并渲染到视口的能力。C++ 侧的详细接口说明参见本文档 [DQuickItemViewport](#dquickitemviewport) 章节。

#### 使用场景

需要在 QML 中实现视口裁剪或局部区域渲染时使用。

### DWindow

#### 定位

DTK QML 窗口类型，通过 `QML_NAMED_ELEMENT(DWindow)` 从 C++ 类 `DQuickWindow` 注册，同时通过 `QML_ATTACHED` 提供窗口附加属性。

#### 功能能力总结

继承 QQuickWindow，提供 DTK 窗口特有的属性和行为，包括窗口圆角、模糊效果、窗口阴影、边框颜色在内的平台视觉属性。通过附加属性机制，任意 QML Item 可访问其所属 DTK 窗口的平台属性。C++ 侧的详细接口说明参见本文档 [DQuickWindow](#dquickwindow) 与 [DQuickWindowAttached](#dquickwindowattached) 章节。

#### 使用场景

QML 中需要使用 DTK 扩展窗口属性（圆角、模糊、阴影、边框颜色）时使用，或通过附加属性在普通 Item 中访问所属窗口的平台属性。

### AboutAction

#### 定位

提供"关于"对话框触发入口的 Action 变体。

#### 功能能力总结

继承 Action，新增 `aboutDialog` 属性（Component 类型）用于指定点击时显示的关于对话框组件。

公开属性：
- aboutDialog（Component）

#### 使用场景

在菜单中添加"关于"选项并关联自定义关于对话框时使用。

### AboutDialog

#### 定位

显示应用产品信息的标准关于对话框。

#### 功能能力总结

继承 DialogWindow，提供 `windowTitle`、`productName`、`productIcon`、`version`、`description`、`license`、`companyLogo` 别名属性用于配置产品信息，以及 `websiteName` 和 `websiteLink` 字符串属性用于显示官网链接。

公开属性：
- websiteName（string）
- websiteLink（string）
- windowTitle（alias）
- productName（alias）
- productIcon（alias）
- version（alias）
- description（alias）
- license（alias）
- companyLogo（alias）

#### 使用场景

应用需要展示标准关于对话框（产品名称、图标、版本号、描述、许可证、公司 Logo、官网链接）时使用。

### AbstractButton

#### 定位

QtQuick.Templates.AbstractButton 的 DTK 样式实现。

#### 功能能力总结

为抽象按钮提供 DTK 主题色、圆角边框和交互视觉反馈，不直接使用，由具体按钮类型继承。

#### 使用场景

作为 Button、CheckBox、RadioButton 在内的具体按钮类型的样式基类，应用代码不直接实例化。

### Action

#### 定位

QtQuick.Templates.Action 的 DTK 样式实现。

#### 功能能力总结

为 Action 提供统一的 DTK 主题外观，支持作为菜单项或工具按钮的行为后端。

#### 使用场景

在菜单、工具栏或上下文菜单中复用统一行为逻辑时使用。

### ActionButton

#### 定位

标题栏中使用的紧凑操作按钮。

#### 功能能力总结

继承 QtQuick.Templates.Button，新增 `textColor` 属性（D.Palette 类型）用于自定义按钮文字颜色。

公开属性：
- textColor（D.Palette）

#### 使用场景

在标题栏或工具栏中放置需要自定义文字颜色的操作按钮时使用。

### ActionGroup

#### 定位

QtQuick.Templates.ActionGroup 的 DTK 样式实现。

#### 功能能力总结

为互斥动作组提供 DTK 主题外观，管理一组 Action 的选中状态。

#### 使用场景

需要在菜单或工具栏中实现互斥选择的动作组时使用。

### AlertToolTip

#### 定位

带连接线的告警提示气泡。

#### 功能能力总结

继承 ToolTip，新增 `target` 属性（Item 类型）指定提示指向的目标控件，提供 `backgroundColor`、`borderColor`、`textColor`、`dropShadowColor`、`backgroundColor` 调色板属性控制气泡和连接线的颜色。

公开属性：
- target（Item）
- backgroundColor（D.Palette）
- borderColor（D.Palette）
- textColor（D.Palette）
- dropShadowColor（D.Palette）

#### 使用场景

需要在输入控件旁显示告警提示并通过连接线指向目标控件时使用。

### ApplicationWindow

#### 定位

QtQuick.Templates.ApplicationWindow 的 DTK 样式实现。

#### 功能能力总结

为应用主窗口提供 DTK 主题样式，包含标题栏、菜单栏和内容区域的统一外观。

#### 使用场景

作为 DTK QML 应用的主窗口类型使用。

### ArrowListView

#### 定位

带箭头指示的有限高度列表视图。

#### 功能能力总结

继承 FocusScope，提供 `maxVisibleItems` 属性控制最大可见项数，`itemHeight` 属性设置单项高度，`view` 别名暴露内部列表视图。

公开属性：
- maxVisibleItems（int）
- itemHeight（int）
- view（alias）

#### 使用场景

需要在弹出菜单或下拉框中显示有限项数并带滚动指示时使用。

### ArrowShapePopup

#### 定位

带箭头形状的弹出面板。

#### 功能能力总结

继承 Popup，提供 `roundedRadius`、`arrowWidth`、`arrowHeight`、`arrowDirection` 别名属性控制箭头形状和圆角，以及 `arrowX`、`arrowY` 属性定位箭头位置。

公开属性：
- arrowX（real）
- arrowY（real）
- roundedRadius（alias）
- arrowWidth（alias）
- arrowHeight（alias）
- arrowDirection（alias）

#### 使用场景

需要带指向箭头的弹出面板（如工具提示、上下文菜单）时使用。

### ArrowShapePopupWindow

#### 定位

带箭头形状的弹出窗口。

#### 功能能力总结

继承 Window，提供 `roundJoinRadius`、`arrowWidth`、`arrowHeight`、`arrowX`、`arrowY`、`arrowDirection` 别名属性控制箭头形状和位置。

公开属性：
- roundJoinRadius（alias）
- arrowWidth（alias）
- arrowHeight（alias）
- arrowX（alias）
- arrowY（alias）
- arrowDirection（alias）

#### 使用场景

需要独立窗口形式的带箭头弹出面板时使用。

### BoxInsetShadow

#### 定位

盒模型内阴影渲染项。

#### 功能能力总结

继承 Item，提供 `cornerRadius`、`topLeftRadius`、`topRightRadius`、`bottomLeftRadius`、`bottomRightRadius` 属性控制各角圆角，`shadowBlur`、`shadowOffsetX`、`shadowOffsetY`、`shadowColor`、`spread` 属性控制阴影外观。

公开属性：
- cornerRadius（real）
- topLeftRadius（variant）
- topRightRadius（variant）
- bottomLeftRadius（variant）
- bottomRightRadius（variant）
- shadowBlur（real）
- shadowOffsetX（real）
- shadowOffsetY（real）
- shadowColor（color）
- spread（real）
公开函数：
- shadowRadius()
- bound()

#### 使用场景

需要为矩形或圆角矩形控件渲染内阴影效果时使用。

### BoxPanel

#### 定位

带内外阴影和边框的盒模型面板。

#### 功能能力总结

继承 Item，提供 `radius`、`color1`、`color2`、`insideBorderColor`、`outsideBorderColor`、`dropShadowColor`、`innerShadowColor1`、`innerShadowColor2` 调色板属性控制面板外观，`boxShadowBlur`、`boxShadowOffsetY`、`innerShadowOffsetY1` 控制阴影参数，`backgroundFlowsHovered` 控制背景是否跟随悬浮状态变化。

公开属性：
- radius（int）
- color1（D.Palette）
- color2（D.Palette）
- insideBorderColor（D.Palette）
- outsideBorderColor（D.Palette）
- dropShadowColor（D.Palette）
- innerShadowColor1（D.Palette）
- innerShadowColor2（D.Palette）
- boxShadowBlur（int）
- boxShadowOffsetY（int）
- innerShadowOffsetY1（int）
- backgroundFlowsHovered（bool）
- innerShadowColor（color）

#### 使用场景

需要渲染带渐变背景、内外边框和阴影的按钮面板时使用，通常作为按钮背景组件。

### BoxShadow

#### 定位

盒模型外阴影渲染项。

#### 功能能力总结

继承 Item，提供 `cornerRadius`、`topLeftRadius`、`topRightRadius`、`bottomLeftRadius`、`bottomRightRadius` 属性控制各角圆角，`shadowBlur`、`shadowOffsetX`、`shadowOffsetY`、`shadowColor`、`spread` 属性控制阴影外观，`hollow` 属性控制是否为空心阴影。

公开属性：
- cornerRadius（real）
- topLeftRadius（variant）
- topRightRadius（variant）
- bottomLeftRadius（variant）
- bottomRightRadius（variant）
- shadowBlur（real）
- shadowOffsetX（real）
- shadowOffsetY（real）
- shadowColor（color）
- spread（real）
- hollow（bool）
公开函数：
- shadowRadius()
- bound()

#### 使用场景

需要为控件渲染外阴影效果时使用。

### BusyIndicator

#### 定位

QtQuick.Templates.BusyIndicator 的 DTK 样式实现。

#### 功能能力总结

为忙指示器提供 DTK 主题色，新增 `fillColor` 属性（D.Palette 类型）控制旋转指示器颜色。

公开属性：
- fillColor（D.Palette）

#### 使用场景

需要指示后台操作正在进行时使用。

### Button

#### 定位

QtQuick.Templates.Button 的 DTK 样式实现。

#### 功能能力总结

为按钮提供 DTK 主题色、圆角边框和交互视觉反馈，新增 `textColor` 属性（D.Palette 类型）根据按钮状态（普通、选中、高亮）切换文字颜色，提供 `updateIndicatorAnchors()` 函数更新指示器锚点。

公开属性：
- textColor（D.Palette）
公开函数：
- updateIndicatorAnchors()

#### 使用场景

需要 DTK 风格的按钮控件时使用。

### ButtonBox

#### 定位

水平排列的按钮容器。

#### 功能能力总结

继承 Control，`buttons` 默认属性接受多个按钮，`group` 别名暴露内部 ButtonGroup。

公开属性：
- group（alias）

#### 使用场景

需要将多个按钮按水平方向分组排列时使用。

### ButtonGroup

#### 定位

QtQuick.Templates.ButtonGroup 的 DTK 样式实现。

#### 功能能力总结

为按钮组提供 DTK 主题样式，管理一组按钮的互斥或非互斥状态。

#### 使用场景

需要对多个按钮进行分组管理时使用。

### ButtonIndicator

#### 定位

按钮指示器渲染项。

#### 功能能力总结

继承 Rectangle，提供 `backgroundColor` 调色板属性控制指示器背景色，`control` 属性关联所属控件以读取颜色选择器状态。

公开属性：
- backgroundColor（D.Palette）
- control（Item）

#### 使用场景

作为按钮内部指示器组件使用，应用代码不直接实例化。

### ButtonPanel

#### 定位

按钮背景面板组件。

#### 功能能力总结

继承 BoxPanel，提供 `button` 属性关联所属按钮控件，`selectValue()` 函数根据普通、选中、高亮三种状态选择对应的视觉属性值。

公开属性：
- button（Item）
公开函数：
- selectValue()

#### 使用场景

作为按钮背景渲染组件使用，应用代码不直接实例化。

### CheckBox

#### 定位

QtQuick.Templates.CheckBox 的 DTK 样式实现。

#### 功能能力总结

为复选框提供 DTK 主题色、指示器样式和圆角边框。

#### 使用场景

需要在界面中提供二态选择控件时使用。

### CheckDelegate

#### 定位

QtQuick.Templates.CheckDelegate 的 DTK 样式实现。

#### 功能能力总结

为带复选框的列表委托项提供 DTK 主题样式，新增 `content` 属性（Component 类型）自定义内容组件，`backgroundColor` 调色板属性控制背景色。

公开属性：
- content（Component）
- backgroundColor（D.Palette）

#### 使用场景

在列表视图中需要带复选框的委托项时使用。

### CicleSpreadAnimation

#### 定位

圆形扩散动画效果项。

#### 功能能力总结

继承 Item，提供 `centerPoint` 属性指定扩散中心点，`start()` 和 `stop()` 函数控制动画的开始和停止。

公开属性：
- centerPoint（point）
公开函数：
- start()
- stop()

#### 使用场景

需要实现水波纹或圆形扩散动画效果时使用。

### ComboBox

#### 定位

QtQuick.Templates.ComboBox 的 DTK 样式实现。

#### 功能能力总结

为下拉组合框提供 DTK 主题样式，新增 `iconNameRole` 属性指定模型中图标名称的数据角色，`alertText`、`alertDuration`、`showAlert` 属性支持告警提示，`maxVisibleItems` 属性控制下拉列表最大可见项数，`separatorColor` 调色板属性控制分隔线颜色，`iconName` 属性提供当前项图标名称。

公开属性：
- iconNameRole（string）
- alertText（string）
- alertDuration（int）
- showAlert（bool）
- maxVisibleItems（int）
- separatorColor（D.Palette）
- iconName（string）
- comboBox（alias）

#### 使用场景

需要 DTK 风格的下拉选择控件并支持图标显示和告警提示时使用。

### Container

#### 定位

QtQuick.Templates.Container 的 DTK 样式实现。

#### 功能能力总结

为容器控件提供 DTK 主题背景和边框样式，管理子项的布局。

#### 使用场景

作为自定义容器控件的样式基类使用。

### Control

#### 定位

QtQuick.Templates.Control 的 DTK 样式实现。

#### 功能能力总结

为基础控件提供 DTK 主题背景、边框和焦点视觉样式。

#### 使用场景

作为自定义控件的样式基类使用。

### ControlBackground

#### 定位

控件焦点背景渲染项。

#### 功能能力总结

继承 Rectangle，提供 `focusBorderSpace` 属性控制焦点边框间距，`focusBorder` 和 `focusBorderVisible` 别名属性控制焦点边框及其可见性。

公开属性：
- focusBorderSpace（int）
- focusBorder（alias）
- focusBorderVisible（alias）

#### 使用场景

作为控件获得焦点时的背景渲染组件使用，应用代码不直接实例化。

### DelayButton

#### 定位

QtQuick.Templates.DelayButton 的 DTK 样式实现。

#### 功能能力总结

为延迟按钮提供 DTK 主题色和进度动画样式，需长按一段时间才触发。

#### 使用场景

需要防止误触发的关键操作按钮时使用。

### Dial

#### 定位

QtQuick.Templates.Dial 的 DTK 样式实现。

#### 功能能力总结

为旋钮控件提供 DTK 主题色和圆形手柄样式，支持拖动旋转选择值。

#### 使用场景

需要以旋转方式调节数值的场景中使用。

### Dialog

#### 定位

QtQuick.Templates.Dialog 的 DTK 样式实现。

#### 功能能力总结

为对话框提供 DTK 主题背景、圆角边框和阴影样式，支持模态和非模态显示。

#### 使用场景

需要弹出对话框与用户交互时使用。

### DialogButtonBox

#### 定位

QtQuick.Templates.DialogButtonBox 的 DTK 样式实现。

#### 功能能力总结

为对话框按钮盒提供 DTK 主题样式，按标准布局排列确认和取消按钮。

#### 使用场景

在对话框底部放置标准按钮时使用。

### DialogTitleBar

#### 定位

对话框标题栏组件。

#### 功能能力总结

继承 Control，提供 `content` 别名属性自定义标题栏中间内容，`icon` 别名属性设置图标，`title` 属性设置标题文字，`enableInWindowBlendBlur` 别名属性控制窗口内混合模糊背景的显示。

公开属性：
- title（string）
- hasWindowFlag（bool）：: (Window.window.flags & Qt.WindowCloseButtonHint)
- content（alias）
- icon（alias）
- enableInWindowBlendBlur（alias）

#### 使用场景

在自定义对话框中需要 DTK 风格标题栏时使用。

### DialogWindow

#### 定位

DTK 风格的对话框窗口。

#### 功能能力总结

继承 Window，提供 `header` 别名属性自定义标题栏组件，`icon` 属性设置窗口图标，`content` 默认属性接受对话框内容，`palette` 别名属性暴露内容项调色板。

公开属性：
- icon（string）
- header（alias）
- palette（alias）

#### 使用场景

需要以独立窗口形式显示对话框时使用。

### Drawer

#### 定位

QtQuick.Templates.Drawer 的 DTK 样式实现。

#### 功能能力总结

为抽屉控件提供 DTK 主题背景和滑动动画样式，支持从屏幕边缘滑入滑出。

#### 使用场景

需要侧边滑出面板的场景中使用。

### EditPanel

#### 定位

输入控件背景面板组件。

#### 功能能力总结

继承 Rectangle，提供 `control` 属性关联所属输入控件，`backgroundColor` 和 `alertBackgroundColor` 调色板属性控制正常和告警状态背景色，`showBorder` 别名属性控制边框显示，`showAlert`、`alertText`、`alertDuration` 属性支持告警提示。

公开属性：
- control（Item）
- backgroundColor（D.Palette）
- alertBackgroundColor（D.Palette）
- showAlert（bool）
- alertText（string）
- alertDuration（int）
- showBorder（alias）

#### 使用场景

作为输入控件（TextField、SpinBox）的背景渲染组件使用，应用代码不直接实例化。

### EmbeddedProgressBar

#### 定位

嵌入式进度条组件。

#### 功能能力总结

继承 QtQuick.Templates.ProgressBar，提供 `backgroundColor` 和 `progressBackgroundColor` 调色板属性控制进度条背景和进度背景色。

公开属性：
- backgroundColor（D.Palette）
- progressBackgroundColor（D.Palette）

#### 使用场景

在控件内部嵌入进度指示（如按钮加载状态）时使用。

### FloatingButton

#### 定位

圆形浮动操作按钮。

#### 功能能力总结

继承 Button，将按钮设为圆形且默认选中状态，隐式宽高一致，不可勾选。

#### 使用场景

需要圆形悬浮操作按钮时使用。

### FloatingMessage

#### 定位

浮动消息提示组件。

#### 功能能力总结

继承 org.deepin.dtk.impl.FloatingMessageContainer，提供 `contentItem` 属性（Component 类型）自定义消息内容，`button` 属性（Component 类型）自定义操作按钮，`iconName` 属性设置消息图标，`maxContentWidth` 属性控制最大内容宽度。

公开属性：
- contentItem（Component）
- button（Component）
- iconName（string）
- maxContentWidth（int）

#### 使用场景

需要在屏幕角落显示带图标和操作按钮的浮动消息提示时使用。

### FloatingPanel

#### 定位

浮动面板组件。

#### 功能能力总结

继承 Control，提供 `backgroundColor`、`dropShadowColor`、`outsideBorderColor`、`insideBorderColor` 调色板属性控制面板外观，`radius` 和 `blurRadius` 属性控制圆角和模糊半径。

公开属性：
- backgroundColor（D.Palette）
- dropShadowColor（D.Palette）
- outsideBorderColor（D.Palette）
- insideBorderColor（D.Palette）
- radius（int）
- blurRadius（int）

#### 使用场景

需要显示浮动面板（如通知中心、控制面板）时使用。

### FlowStyle

#### 定位

DTK 控件流式布局样式定义。

#### 功能能力总结

继承 QtObject，提供 `control` 子对象包含 `radius`、`spacing`、`padding`、`borderWidth`、`focusBorderWidth`、`focusBorderPaddings` 布局参数和 `border` 调色板属性，`settings` 子对象包含 `title` 和 `content` 的字体与边距配置，以及多个布局计算函数。

公开属性：
- control（QtObject）
- radius（int）
- spacing（int）
- padding（int）
- borderWidth（int）
- focusBorderWidth（real）
- focusBorderPaddings（real）
- border（D.Palette）
- settings（QtObject）
- title（QtObject）
- marginL1（int）
- marginL2（int）
- marginLOther（int）
- content（QtObject）
- margin（int）
- marginOther（int）
- resetButtonHeight（int）
- navigation（QtObject）
- width（int）
- height（int）
- textVPadding（int）
- background（D.Palette）
- button（QtObject）
- hPadding（int）
- vPadding（int）
- iconSize（int）
- background1（D.Palette）
- background2（D.Palette）
- dropShadow（D.Palette）
- innerShadow1（D.Palette）
- innerShadow2（D.Palette）
- insideBorder（D.Palette）
- outsideBorder（D.Palette）
- text（D.Palette）
- highlightedButton（QtObject）
- checkedButton（QtObject）
- innerShadow（D.Palette）
- windowButton（QtObject）
- warningButton（QtObject）
- switchButton（QtObject）
- indicatorWidth（int）
- indicatorHeight（int）
- handleWidth（int）
- handleHeight（int）
- iconName（string）
- handle（D.Palette）
- floatingButton（QtObject）
- size（int）
- iconButton（QtObject）
- backgroundSize（int）
- toolButton（QtObject）
- indicatorRightMargin（int）
- radioButton（QtObject）
- indicatorSize（int）
- topPadding（int）
- bottomPadding（int）
- checkBox（QtObject）
- focusRadius（int）
- buttonBox（QtObject）
- comboBox（QtObject）
- maxVisibleItems（int）
- edit（QtObject）
- indicatorSpacing（int）
- separator（D.Palette）
- actionIconSize（int）
- textFieldHeight（int）
- textAreaHeight（int）
- alertBackground（D.Palette）
- placeholderText（D.Palette）
- searchEdit（QtObject）
- iconLeftMargin（int）
- iconRightMargin（int）
- animationDuration（int）
- ipEdit（QtObject）
- fieldWidth（int）
- passwordEdit（QtObject）
- echoActionSpacing（int）
- keySequenceEdit（QtObject）
- label（QtObject）
- leftRightPadding（int）
- topBottomPadding（int）
- shadowInner1（D.Palette）
- shadowInner2（D.Palette）
- shadowOuter（D.Palette）
- spinBox（QtObject）
- indicator（QtObject）
- focusIconSize（int）
- plusMinusSpinBox（QtObject）
- buttonIconSize（int）
- dialogWindow（QtObject）
- contentHMargin（int）
- footerMargin（int）
- titleBarHeight（int）
- aboutDialog（QtObject）
- leftAreaWidth（int）
- productIconHeight（int）
- popup（QtObject）
- floatingMessage（QtObject）
- maximumWidth（int）
- minimumHeight（int）
- closeButtonSize（int）
- floatingPanel（QtObject）
- toolTip（QtObject）
- verticalPadding（int）
- horizontalPadding（int）
- alertToolTip（QtObject）
- connectorWidth（int）
- connectorHeight（int）
- connecterdropShadow（D.Palette）
- connecterBackground（D.Palette）
- menu（QtObject）
- margins（int）
- overlap（int）
- item（QtObject）
- count（int）
- lineTopPadding（int）
- lineBottomPadding（int）
- lineHeight（int）
- lineColor（D.Palette）
- subMenuOpenedBackground（D.Palette）
- itemText（D.Palette）
- separatorText（D.Palette）
- highlightPanel（QtObject）
- behindWindowBlur（QtObject）
- lightColor（color）
- lightNoBlurColor（color）
- darkColor（color）
- darkNoBlurColor（color）
- arrowRectangleBlur（QtObject）
- roundJoinRadius（int）
- outBorderColor（color）
- darkOutBorderColor（color）
- inBorderColor（color）
- darkInBorderColor（color）
- backgroundColor（color）
- darkBackgroundColor（color）
- shadowColor（color）
- darkShadowColor（color）
- arrowListView（QtObject）
- stepButtonSize（size）
- stepButtonIconSize（size）
- itemHeight（int）
- upButtonIconName（string）
- downButtonIconName（string）
- itemDelegate（QtObject）
- normalColor（color）
- cascadeColor（color）
- checkIndicatorIconSize（int）
- checkBackgroundColor（D.Palette）
- checkedColor（color）
- stackView（QtObject）
- animationEasingType（int）
- busyIndicator（QtObject）
- paddingFactor（int）
- fillColor（D.Palette）
- spinnerSource（string）
- buttonIndicator（QtObject）
- scrollBar（QtObject）
- activeWidth（int）
- hideOpacity（real）
- hidePauseDuration（int）
- hideDuration（int）
- progressBar（QtObject）
- indeterminateProgressBarWidth（int）
- indeterminateProgressBarAnimationDuration（int）
- handleGradientColor（D.Palette）
- embeddedProgressBar（QtObject）
- contentHeight（int）
- backgroundRadius（int）
- contentRadius（int）
- progressBackground（D.Palette）
- waterProgressBar（QtObject）
- waterFrontImagePath（string）
- waterBackImagePath（string）
- popBackground（D.Palette）
- textColor（D.Palette）
- titleBar（QtObject）
- leftMargin（int）
- slider（QtObject）
- highlightMargin（int）
- groove（QtObject）
- tick（QtObject）
- textMargin（int）
- dial（QtObject）
- pageIndicator（QtObject）
公开函数：
- implicitWidth()
- implicitHeight()
- backgroundImplicitWidth()
- contentImplicitWidth()
- selectColor()

#### 使用场景

应用需要自定义 DTK 控件样式参数或读取默认样式值时使用。

### FocusBoxBorder

#### 定位

焦点边框渲染项。

#### 功能能力总结

继承 Item，提供 `color` 属性控制边框颜色，`borderWidth` 属性控制边框宽度，`radius` 属性控制圆角。

公开属性：
- color（color）
- borderWidth（real）
- radius（real）
- paddings（real）

#### 使用场景

作为控件获得焦点时的边框渲染组件使用，应用代码不直接实例化。

### Frame

#### 定位

带圆角边框的框架容器。

#### 功能能力总结

继承 QtQuick.Templates.Pane，新增 `radius` 属性控制框架圆角。

公开属性：
- radius（int）

#### 使用场景

需要带圆角边框的内容容器时使用。

### GroupBox

#### 定位

QtQuick.Templates.GroupBox 的 DTK 样式实现。

#### 功能能力总结

为分组框提供 DTK 主题边框和标题样式，将相关控件视觉上分组。

#### 使用场景

需要将相关控件用边框和标题分组时使用。

### HelpAction

#### 定位

提供帮助页面跳转的 Action 变体。

#### 功能能力总结

继承 Action，文本默认为"Help"，触发时调用 `D.ApplicationHelper.handleHelpAction()` 打开帮助页面。

#### 使用场景

在菜单中添加帮助入口时使用。

### HighlightPanel

#### 定位

高亮面板渲染项。

#### 功能能力总结

继承 Item，提供 `backgroundColor`、`outerShadowColor`、`innerShadowColor` 调色板属性控制面板高亮外观。

公开属性：
- backgroundColor（D.Palette）
- outerShadowColor（D.Palette）
- innerShadowColor（D.Palette）

#### 使用场景

作为控件高亮状态的背景渲染组件使用，应用代码不直接实例化。

### IconButton

#### 定位

QtQuick.Templates.AbstractButton 的图标按钮变体。

#### 功能能力总结

为图标按钮提供 DTK 主题色，以图标为主要视觉元素的紧凑按钮。

#### 使用场景

在标题栏或工具栏中放置图标操作按钮时使用。

### InsideBoxBorder

#### 定位

内边框渲染项。

#### 功能能力总结

继承 Rectangle，提供 `borderWidth` 属性控制边框宽度，`color` 属性控制边框颜色，`radius` 别名属性控制圆角。

公开属性：
- borderWidth（real）
- color（color）
- radius（alias）

#### 使用场景

作为控件内部边框渲染组件使用，应用代码不直接实例化。

### IpV4LineEdit

#### 定位

IPv4 地址输入控件。

#### 功能能力总结

继承 Item，提供 `text` 属性获取完整地址文本，`alertText`、`alertDuration`、`showAlert` 属性支持输入验证告警，`backgroundColor` 调色板属性控制背景色，内部提供 `updateText()`、`clearText()`、`updateByText()` 函数管理各段输入。

公开属性：
- text（string）
- alertText（string）
- alertDuration（int）
- showAlert（bool）
- backgroundColor（D.Palette）
公开函数：
- updateText()
- clearText()
- updateByText()

#### 使用场景

需要输入和验证 IPv4 地址时使用。

### ItemDelegate

#### 定位

QtQuick.Templates.ItemDelegate 的 DTK 样式实现。

#### 功能能力总结

为列表委托项提供 DTK 主题样式，新增 `indicatorVisible` 属性控制指示器可见性，`backgroundVisible` 属性控制背景可见性，`cascadeSelected` 属性支持级联选中，`contentFlow` 属性支持内容流式布局，`content` 属性（Component 类型）自定义内容组件，`checkedTextColor` 调色板属性控制选中文字颜色，`corners` 属性控制圆角方向，`getCornersForBackground()` 函数根据索引和总数计算圆角。

公开属性：
- indicatorVisible（bool）
- backgroundVisible（bool）
- cascadeSelected（bool）
- contentFlow（bool）
- content（Component）
- checkedTextColor（D.Palette）
- corners（int）
公开函数：
- getCornersForBackground()

#### 使用场景

在列表视图中需要 DTK 风格委托项并支持级联选中、圆角控制时使用。

### KeySequenceEdit

#### 定位

快捷键编辑控件。

#### 功能能力总结

继承 QtQuick.Templates.Control，提供 `text` 属性获取快捷键文本，`placeholderText` 属性设置占位提示，`keys` 别名属性暴露捕获的按键序列，`backgroundColor` 和 `placeholderTextColor` 调色板属性控制背景和占位文字颜色。

公开属性：
- text（string）
- placeholderText（string）
- backgroundColor（D.Palette）
- placeholderTextColor（D.Palette）
- keys（alias）

#### 使用场景

需要让用户输入或修改快捷键组合时使用。

### Label

#### 定位

QtQuick.Templates.Label 的 DTK 样式实现。

#### 功能能力总结

为文本标签提供 DTK 主题文字颜色样式。

#### 使用场景

需要显示 DTK 风格文本标签时使用。

### LineEdit

#### 定位

单行文本输入控件。

#### 功能能力总结

继承 QtQuick.Templates.TextField，新增 `clearButton` 只读别名属性暴露清除按钮控件。

公开属性：
- clearButton（alias）

#### 使用场景

需要带清除按钮的单行文本输入控件时使用。

### Menu

#### 定位

DTK 风格的菜单控件。

#### 功能能力总结

继承 QtQuick.Templates.Menu，新增 `closeOnInactive` 属性控制失去焦点时是否自动关闭，`maxVisibleItems` 属性控制最大可见项数，`backgroundColor` 调色板属性控制菜单背景色，`model` 属性暴露内容模型，`header` 和 `footer` 属性支持自定义头部和底部组件，`existsChecked` 只读属性指示是否存在选中项，`active` 只读属性指示菜单是否在活动窗口中。

公开属性：
- closeOnInactive（bool）
- maxVisibleItems（int）
- backgroundColor（D.Palette）
- model（var）
- header（Component）
- footer（Component）
- existsChecked（bool）
- active（bool）
- count（int）
公开函数：
- refreshContentItemWidth()

#### 使用场景

需要 DTK 风格的右键菜单或下拉菜单时使用。

### MenuBar

#### 定位

QtQuick.Templates.MenuBar 的 DTK 样式实现。

#### 功能能力总结

为菜单栏提供 DTK 主题样式，横向排列菜单项。

#### 使用场景

应用窗口顶部需要菜单栏时使用。

### MenuItem

#### 定位

QtQuick.Templates.MenuItem 的 DTK 样式实现。

#### 功能能力总结

为菜单项提供 DTK 主题样式，新增 `useIndicatorPadding` 属性控制是否为指示器预留间距，`textColor` 和 `subMenuBackgroundColor` 调色板属性控制文字颜色和子菜单背景色。

公开属性：
- useIndicatorPadding（bool）
- textColor（D.Palette）
- subMenuBackgroundColor（D.Palette）
- arrowPadding（real）
- indicatorPadding（real）

#### 使用场景

在菜单中放置可选项时使用。

### MenuSeparator

#### 定位

带可选标题的菜单分隔符。

#### 功能能力总结

继承 QtQuick.Templates.MenuSeparator，新增 `text` 属性设置分隔符标题文字，`textColor` 调色板属性控制标题文字颜色。

公开属性：
- text（string）
- textColor（D.Palette）
- separatorColor（D.Palette）

#### 使用场景

在菜单中分组分隔菜单项并显示分组标题时使用。

### OutsideBoxBorder

#### 定位

外边框渲染项。

#### 功能能力总结

继承 Item，提供 `borderWidth` 属性控制边框宽度，`color` 属性控制边框颜色，`radius` 属性控制圆角。

公开属性：
- borderWidth（real）
- color（color）
- radius（real）

#### 使用场景

作为控件外部边框渲染组件使用，应用代码不直接实例化。

### PageIndicator

#### 定位

QtQuick.Templates.PageIndicator 的 DTK 样式实现。

#### 功能能力总结

为分页指示器提供 DTK 主题圆点样式，显示当前页和总页数。

#### 使用场景

在分页浏览场景中指示当前页面位置时使用。

### Pane

#### 定位

QtQuick.Templates.Pane 的 DTK 样式实现。

#### 功能能力总结

为面板提供 DTK 主题背景和边框样式，作为内容容器使用。

#### 使用场景

需要带背景的面板容器时使用。

### PasswordEdit

#### 定位

密码输入控件。

#### 功能能力总结

继承 LineEdit，提供 `isEchoMode` 只读属性指示当前是否明文显示，`echoButtonVisible` 别名属性控制显示/隐藏按钮的可见性，`toggleEchoMode()` 函数切换明文与密文显示模式。

公开属性：
- isEchoMode（bool）
- echoButtonVisible（alias）
公开函数：
- toggleEchoMode()

#### 使用场景

需要输入密码并支持切换显示/隐藏密码时使用。

### PlaceholderText

#### 定位

QtQuick.Templates.Label 的占位文本变体。

#### 功能能力总结

为占位文本提供 DTK 主题颜色样式，显示在输入控件中的提示文字。

#### 使用场景

在输入控件中显示灰色提示文字时使用。

### PlusMinusSpinBox

#### 定位

带加减按钮的数值输入控件。

#### 功能能力总结

继承 FocusScope，提供 `spinBox` 别名属性暴露内部 SpinBox 控件，`upButtonVisible` 和 `downButtonVisible` 别名属性控制加减按钮可见性，`resetButtonVisible` 别名属性控制重置按钮可见性。

公开属性：
- spinBox（alias）
- upButtonVisible（alias）
- downButtonVisible（alias）
- resetButtonVisible（alias）

#### 使用场景

需要带独立加减按钮和重置按钮的数值调节控件时使用。

### Popup

#### 定位

DTK 风格的弹出面板。

#### 功能能力总结

继承 QtQuick.Templates.Popup，新增 `closeOnInactive` 属性控制失去焦点时是否自动关闭，`active` 只读属性指示弹出面板是否在活动窗口中。

公开属性：
- closeOnInactive（bool）
- active（bool）

#### 使用场景

需要 DTK 风格的弹出面板时使用。

### PopupWindow

#### 定位

带窗口模糊背景的弹出窗口。

#### 功能能力总结

继承 QtQuick.Templates.Popup，新增 `blurControl` 别名属性关联窗口模糊控制项。

公开属性：
- blurControl（alias）

#### 使用场景

需要带窗口模糊效果的弹出面板时使用。

### ProgressBar

#### 定位

QtQuick.Templates.ProgressBar 的 DTK 样式实现。

#### 功能能力总结

为进度条提供 DTK 主题色和进度动画样式，新增 `formatText` 属性自定义进度文本格式，`animationStop` 属性控制动画停止状态。

公开属性：
- formatText（string）
- animationStop（bool）

#### 使用场景

需要展示操作进度并自定义进度文本时使用。

### QuitAction

#### 定位

Action 的退出操作变体。

#### 功能能力总结

继承 Action，提供应用退出行为，文本默认为"退出"。

#### 使用场景

在菜单中添加退出应用选项时使用。

### RadioButton

#### 定位

QtQuick.Templates.RadioButton 的 DTK 样式实现。

#### 功能能力总结

为单选按钮提供 DTK 主题色和圆形指示器样式。

#### 使用场景

需要在互斥选项组中选择一个选项时使用。

### RecommandButton

#### 定位

Button 的推荐操作变体。

#### 功能能力总结

继承 Button，使用推荐按钮的主题色样式，视觉上突出于普通按钮。

#### 使用场景

在界面中标注主要推荐操作时使用。

### RectangularShadow

#### 定位

矩形阴影渲染项。

#### 功能能力总结

继承 Item，提供 `offsetX` 和 `offsetY` 属性控制阴影偏移，`glowRadius` 属性控制阴影扩散范围，`spread` 属性控制阴影边缘增强程度，`color` 属性控制阴影颜色，`cornerRadius` 属性控制圆角，`fill` 别名属性控制是否填充整个区域。

公开属性：
- offsetX（real）：This property defines the offset of the shadow in the x-axis direction.
- offsetY（real）：This property defines the offset of the shadow in the y-axis direction.
- glowRadius（real）：This property defines how many pixels outside(or inside) the item area are reached by the shadow.
- spread（real）：This property defines how large part of the shadow color is strengthened near the source edges.
- color（color）：This property defines the the shadow color.
- cornerRadius（real）：This property defines corners size of the control that draws the shadow.
- inverseSpread（real）
- fill（alias）：This property defines does the shadow fill the entire area.

#### 使用场景

需要为矩形或圆角矩形控件渲染阴影效果时使用。

### RoundButton

#### 定位

FloatingButton 的圆形按钮变体。

#### 功能能力总结

继承 FloatingButton，提供圆形按钮的 DTK 主题样式。

#### 使用场景

需要圆形按钮控件时使用。

### ScrollBar

#### 定位

QtQuick.Templates.ScrollBar 的 DTK 样式实现。

#### 功能能力总结

为滚动条提供 DTK 主题样式，新增 `backgroundColor`、`insideBorderColor`、`outsideBorderColor` 调色板属性控制滚动条外观。

公开属性：
- moving（bool）
- backgroundColor（D.Palette）
- insideBorderColor（D.Palette）
- outsideBorderColor（D.Palette）

#### 使用场景

内容区域需要可交互滚动条时使用。

### ScrollIndicator

#### 定位

QtQuick.Templates.ScrollIndicator 的 DTK 样式实现。

#### 功能能力总结

为滚动指示器提供 DTK 主题样式，轻量指示可滚动区域。

#### 使用场景

在不需要交互滚动条仅提示可滚动时使用。

### ScrollView

#### 定位

QtQuick.Templates.ScrollView 的 DTK 样式实现。

#### 功能能力总结

为滚动视图提供 DTK 主题滚动条样式，支持内容超出视口时滚动浏览。

#### 使用场景

内容区域需要滚动浏览时使用。

### SearchEdit

#### 定位

搜索输入控件。

#### 功能能力总结

继承 LineEdit，新增 `placeholder` 别名属性设置搜索占位提示文字，`editting` 只读属性指示当前是否处于编辑或聚焦状态。

公开属性：
- editting（bool）
- placeholder（alias）

#### 使用场景

需要带搜索占位提示的搜索输入框时使用。

### Slider

#### 定位

QtQuick.Templates.Slider 的 DTK 样式实现。

#### 功能能力总结

为滑动条提供 DTK 主题样式，新增 `grooveColor` 调色板属性控制滑槽颜色，`handleType` 别名属性设置手柄类型，`dashOffset` 和 `dashPattern` 属性控制虚线样式，`highlightedPassedGroove` 属性控制是否高亮已滑过的滑槽部分。提供 `HandleType` 枚举，值为 `NoArrowHorizontal`、`NoArrowVertical`、`ArrowUp`、`ArrowLeft`、`ArrowBottom`、`ArrowRight`。

公开属性：
- grooveColor（D.Palette）
- dashOffset（real）
- dashPattern（var）
- highlightedPassedGroove（bool）
- handleType（alias）
枚举 HandleType：NoArrowHorizontal、NoArrowVertical、ArrowUp、ArrowLeft、ArrowBottom、ArrowRight

#### 使用场景

需要 DTK 风格滑动条并支持自定义手柄类型和虚线样式时使用。

### SliderHandle

#### 定位

滑动条手柄组件。

#### 功能能力总结

继承 org.deepin.dtk.impl.DciIcon，提供 `type` 属性设置手柄类型（使用 `Slider.HandleType` 枚举值），`getIconNameByType()` 函数根据手柄类型返回对应图标名称。

公开属性：
- type（int）
公开函数：
- getIconNameByType()

#### 使用场景

作为 Slider 内部手柄渲染组件使用，应用代码不直接实例化。

### SliderTipItem

#### 定位

滑动条刻度提示项。

#### 功能能力总结

继承 Control，提供 `text` 属性设置提示文字，`textHorizontalAlignment` 属性控制文字水平对齐，`direction` 只读属性获取刻度方向，`horizontal` 只读属性指示是否水平方向，`highlight` 属性控制是否高亮，`tickColor` 和 `textColor` 调色板属性控制刻度和文字颜色。

公开属性：
- text（string）
- textHorizontalAlignment（int）
- direction（int）
- horizontal（bool）
- highlight（bool）
- tickColor（D.Palette）
- textColor（D.Palette）

#### 使用场景

在带刻度的滑动条（TipsSlider）中显示刻度提示文字时使用。

### SortFilterModel

#### 定位

排序过滤代理模型。

#### 功能能力总结

继承 DelegateModel，提供 `lessThan` 属性设置排序比较函数，`filterAcceptsItem` 属性设置过滤判断函数，`visibleGroup` 别名属性暴露可见项组，`update()` 函数触发重新排序和过滤。

公开属性：
- lessThan（var）
- filterAcceptsItem（var）
- visibleGroup（alias）
公开函数：
- update()

#### 使用场景

需要对列表模型进行排序和过滤时使用。

### SpinBox

#### 定位

QtQuick.Templates.SpinBox 的 DTK 样式实现。

#### 功能能力总结

为数值输入框提供 DTK 主题样式，新增 `alertText`、`alertDuration`、`showAlert` 别名属性支持输入验证告警。

公开属性：
- alertText（alias）
- alertDuration（alias）
- showAlert（alias）

#### 使用场景

需要 DTK 风格的数值输入框并支持告警提示时使用。

### SpinBoxIndicator

#### 定位

SpinBox 加减指示器组件。

#### 功能能力总结

继承 Control，提供 `spinBox` 属性关联所属 SpinBox 控件，`pressed` 属性指示按下状态，`singleIndicator` 属性控制是否为单独指示器模式，`direction` 属性设置指示器方向，`inactiveBackgroundColor` 调色板属性控制非激活背景色。提供 `IndicatorDirection` 枚举，值为 `UpIndicator`、`DownIndicator`。

公开属性：
- spinBox（Item）
- pressed（bool）
- singleIndicator（bool）
- direction（int）
- inactiveBackgroundColor（D.Palette）
枚举 IndicatorDirection：UpIndicator、DownIndicator

#### 使用场景

作为 SpinBox 内部加减按钮组件使用，应用代码不直接实例化。

### StackView

#### 定位

QtQuick.Templates.StackView 的 DTK 样式实现。

#### 功能能力总结

为栈视图提供 DTK 主题过渡动画样式，支持页面压入和弹出。

#### 使用场景

需要实现页面导航栈时使用。

### StyledArrowShapeWindow

#### 定位

带 DTK 样式的箭头形状窗口。

#### 功能能力总结

继承 ArrowShapeWindow，新增 `control` 别名属性关联模糊控制项，通过 `D.DWindow.borderColor` 附加属性设置窗口边框颜色。

公开属性：
- control（alias）

#### 使用场景

需要 DTK 风格的带箭头弹出窗口时使用。

### StyledBehindWindowBlur

#### 定位

DTK 样式的窗口模糊背景项。

#### 功能能力总结

继承 org.deepin.dtk.impl.BehindWindowBlur，新增 `control` 属性关联需要模糊背景的控件，根据控件调色板自动选择模糊混合色。

公开属性：
- control（var）

#### 使用场景

需要为控件或窗口添加 DTK 风格的模糊背景时使用。

### SwipeDelegate

#### 定位

QtQuick.Templates.SwipeDelegate 的 DTK 样式实现。

#### 功能能力总结

为滑动委托提供 DTK 主题样式，支持左右滑动显示附加操作。

#### 使用场景

列表项需要滑动显示操作按钮时使用。

### SwipeView

#### 定位

QtQuick.Templates.SwipeView 的 DTK 样式实现。

#### 功能能力总结

为滑动视图提供 DTK 主题样式，支持横向滑动切换页面。

#### 使用场景

需要可滑动切换的分页视图时使用。

### Switch

#### 定位

QtQuick.Templates.Switch 的 DTK 样式实现。

#### 功能能力总结

为开关控件提供 DTK 主题样式，新增 `backgroundColor` 和 `handleColor` 调色板属性控制开关背景和手柄颜色。

公开属性：
- backgroundColor（D.Palette）
- handleColor（D.Palette）

#### 使用场景

需要在界面中提供开关切换控件时使用。

### TabBar

#### 定位

QtQuick.Templates.TabBar 的 DTK 样式实现。

#### 功能能力总结

为标签栏提供 DTK 主题样式，横向排列标签项。

#### 使用场景

需要标签页导航时使用。

### TextArea

#### 定位

QtQuick.Templates.TextArea 的 DTK 样式实现。

#### 功能能力总结

为多行文本输入框提供 DTK 主题样式，新增 `placeholderTextColor` 调色板属性控制占位文字颜色，提供 `effectiveHorizontalAlignmentChanged` 信号通知有效水平对齐方式变化。

公开属性：
- placeholderTextColor（D.Palette）
公开信号：
- effectiveHorizontalAlignmentChanged()

#### 使用场景

需要 DTK 风格的多行文本输入控件时使用。

### TextField

#### 定位

QtQuick.Templates.TextField 的 DTK 样式实现。

#### 功能能力总结

为单行文本输入框提供 DTK 主题样式，新增 `placeholderTextColor` 调色板属性控制占位文字颜色，`backgroundColor` 别名属性控制背景色，`alertText`、`alertDuration`、`showAlert` 别名属性支持输入验证告警，提供 `effectiveHorizontalAlignmentChanged` 信号通知有效水平对齐方式变化。

公开属性：
- placeholderTextColor（D.Palette）
- backgroundColor（alias）
- alertText（alias）
- alertDuration（alias）
- showAlert（alias）
公开信号：
- effectiveHorizontalAlignmentChanged()

#### 使用场景

需要 DTK 风格的单行文本输入框并支持告警提示时使用。

### ThemeMenu

#### 定位

主题切换菜单。

#### 功能能力总结

继承 Menu，提供浅色（LightType）、深色（DarkType）、自动（UnknownType）三种主题类型的菜单项，通过 `D.ApplicationHelper` 的主题类型常量实现切换。

公开属性：
- themeType（int）

#### 使用场景

需要在应用中提供主题切换菜单时使用。

### TipsSlider

#### 定位

带刻度提示的滑动条。

#### 功能能力总结

继承 Control，提供 `slider` 别名属性暴露内部 Slider 控件，`ticks` 别名属性接受刻度提示项集合，`tickDirection` 属性控制刻度方向。提供 `TickDirection` 枚举，值为 `Front`、`Back`。

公开属性：
- tickDirection（int）
- slider（alias）
- ticks（alias）
枚举 TickDirection：Front、Back

#### 使用场景

需要带刻度标记和提示文字的滑动条时使用。

### TitleBar

#### 定位

DTK 风格的窗口标题栏。

#### 功能能力总结

继承 Control，提供 `title` 属性设置标题文字，`icon` 别名属性设置图标，`leftContent` 和 `content` 别名属性自定义左侧和中间内容组件，`menu` 别名属性设置菜单组件，`menuDisabled` 属性控制菜单是否禁用，`aboutDialog` 属性关联关于对话框组件，`fullScreenButtonVisible` 属性控制全屏按钮可见性，`windowButtonGroup` 别名属性自定义窗口按钮组，`autoHideOnFullscreen` 属性控制全屏时是否自动隐藏，`separatorVisible` 属性控制底部分隔线可见性，`enableInWindowBlendBlur` 别名属性控制窗口内混合模糊背景，`textColor` 调色板属性控制文字颜色，`toggleWindowState()` 信号通知窗口状态切换请求。

公开属性：
- title（string）
- menuDisabled（bool）
- aboutDialog（Component）
- fullScreenButtonVisible（bool）
- autoHideOnFullscreen（bool）
- embedMode（bool）
- separatorVisible（bool）
- textColor（D.Palette）
- hasWindowFlag（bool）：: (Window.window.flags & Qt.WindowTitleHint)
- icon（alias）
- leftContent（alias）
- content（alias）
- menu（alias）
- windowButtonGroup（alias）
- enableInWindowBlendBlur（alias）
公开信号：
- toggleWindowState()

#### 使用场景

应用窗口需要 DTK 风格标题栏（含标题、图标、菜单、窗口按钮）时使用。

### ToolButton

#### 定位

QtQuick.Templates.Button 的工具按钮变体。

#### 功能能力总结

为工具按钮提供 DTK 主题样式，新增 `textColor` 调色板属性根据按钮状态（普通、选中、高亮）切换文字颜色，提供 `updateIndicatorAnchors()` 函数更新指示器锚点。

公开属性：
- textColor（D.Palette）
公开函数：
- updateIndicatorAnchors()

#### 使用场景

在工具栏中放置操作按钮时使用。

### ToolTip

#### 定位

QtQuick.Templates.ToolTip 的 DTK 样式实现。

#### 功能能力总结

为工具提示提供 DTK 主题背景和文字颜色样式。

#### 使用场景

需要为控件提供悬浮提示信息时使用。

### WarningButton

#### 定位

Button 的警告操作变体。

#### 功能能力总结

继承 Button，使用警告按钮的主题色样式，视觉上提示风险操作。

#### 使用场景

在界面中标注删除或不可逆操作时使用。

### WaterProgressBar

#### 定位

水波纹进度条控件。

#### 功能能力总结

继承 Control，提供 `value` 属性（0 到 100）设置进度值，`running` 属性控制动画是否运行，`backgroundColor1`、`backgroundColor2`、`dropShadowColor`、`popBackgroundColor`、`textColor` 调色板属性控制水波纹和文字颜色。

公开属性：
- value（int）：0~100
- running（bool）
- backgroundColor1（D.Palette）
- backgroundColor2（D.Palette）
- dropShadowColor（D.Palette）
- popBackgroundColor（D.Palette）
- textColor（D.Palette）
- xoffset（real）

#### 使用场景

需要以水波纹动画形式展示进度的场景中使用。

### WindowButton

#### 定位

窗口标题栏按钮控件。

#### 功能能力总结

继承 Control，提供 `icon` 别名属性设置按钮图标，`pressed` 只读属性指示按下状态，`textColor` 和 `backgroundColor` 调色板属性控制按钮颜色，`clicked` 信号通知点击事件。

公开属性：
- pressed（bool）
- textColor（D.Palette）
- backgroundColor（D.Palette）
- icon（alias）
公开信号：
- clicked()

#### 使用场景

在窗口标题栏中放置最小化、最大化、关闭按钮时使用。

### WindowButtonGroup

#### 定位

窗口标题栏按钮组组件。

#### 功能能力总结

继承 RowLayout，提供 `textColor` 调色板属性控制按钮文字颜色，`fullScreenButtonVisible` 属性控制全屏按钮可见性，`embedMode` 属性控制嵌入模式，`maxOrWinded()` 信号通知最大化/还原请求。根据窗口标志自动判断最小化、最大化、关闭按钮的可用性。

公开属性：
- textColor（D.Palette）
- fullScreenButtonVisible（bool）
- embedMode（bool）
- hasWindowFlag（bool）：: (Window.window.flags & Qt.WindowMinimizeButtonHint)
- maxSize（size）
- minSize（size）
- isMaximized（bool）
公开信号：
- maxOrWinded()

#### 使用场景

在窗口标题栏中放置标准窗口操作按钮组时使用。

### WindowQuitFullButton

#### 定位

Button 的全屏退出按钮变体。

#### 功能能力总结

继承 Button，提供窗口全屏退出按钮的 DTK 主题样式。

#### 使用场景

窗口全屏状态下显示退出全屏按钮时使用。

### CheckBox

#### 定位

继承 Settings.OptionDelegate 的 DTK 控件。

#### 功能能力总结

提供 DTK 主题样式。

#### 使用场景

需要使用 DTK 主题样式的 settings/CheckBox 控件时使用。

### ComboBox

#### 定位

继承 Settings.OptionDelegate 的 DTK 控件。

#### 功能能力总结

提供 DTK 主题样式。

公开属性：
- valueRole（string）
- impl（alias）
- model（alias）

#### 使用场景

需要使用 DTK 主题样式的 settings/ComboBox 控件时使用。

### ContentBackground

#### 定位

继承 Rectangle 的 DTK 控件。

#### 功能能力总结

提供 DTK 主题样式。

#### 使用场景

需要使用 DTK 主题样式的 settings/ContentBackground 控件时使用。

### ContentTitle

#### 定位

继承 Label 的 DTK 控件。

#### 功能能力总结

提供 DTK 主题样式。

#### 使用场景

需要使用 DTK 主题样式的 settings/ContentTitle 控件时使用。

### LineEdit

#### 定位

继承 Settings.OptionDelegate 的 DTK 控件。

#### 功能能力总结

提供 DTK 主题样式。

#### 使用场景

需要使用 DTK 主题样式的 settings/LineEdit 控件时使用。

### NavigationTitle

#### 定位

继承 Control 的 DTK 控件。

#### 功能能力总结

提供 DTK 主题样式。

公开属性：
- checked（bool）
- backgroundColor（D.Palette）
- checkedTextColor（D.Palette）
公开信号：
- clicked()

#### 使用场景

需要使用 DTK 主题样式的 settings/NavigationTitle 控件时使用。

### OptionDelegate

#### 定位

继承 RowLayout 的 DTK 控件。

#### 功能能力总结

提供 DTK 主题样式。

公开属性：
- leftVisible（bool）

#### 使用场景

需要使用 DTK 主题样式的 settings/OptionDelegate 控件时使用。

### SettingsDialog

#### 定位

继承 DialogWindow 的 DTK 控件。

#### 功能能力总结

提供 DTK 主题样式。

公开属性：
- groups（list<Settings.SettingsGroup>）
- config（QtObject）
- container（Settings.SettingsContainer）
- navigationView（alias）
- contentView（alias）

#### 使用场景

需要使用 DTK 主题样式的 settings/SettingsDialog 控件时使用。

### Style

#### 定位

继承 FlowStyle 的 DTK 控件。

#### 功能能力总结

提供 DTK 主题样式。

#### 使用场景

需要使用 DTK 主题样式的 style/Style 控件时使用。

