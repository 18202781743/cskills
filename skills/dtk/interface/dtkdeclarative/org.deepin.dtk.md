# org.deepin.dtk QML 模块

org.deepin.dtk 是 dtkdeclarative 提供的 QML 声明式控件模块，为 DTK 应用提供一套完整的界面控件库。模块覆盖按钮、对话框与窗口、文本与数值输入、菜单与动作、列表与视图以及视觉效果与渲染这些常见交互场景，控件实现遵循 DTK 设计规范的主题色、圆角和交互反馈风格，可与 `org.deepin.dtk.style` 样式单例和 `org.deepin.dtk.settings` 设置模块配合使用。



## 集成

### 使用方式

QML 模块 URI 为 `org.deepin.dtk`，版本为 1.0。DTK6 使用 Qt6，主模块插件随 `libdtk6declarative` 安装；DTK5 使用 Qt5 和 `libdtkdeclarative5`。使用 Qt Quick Controls 的 Chameleon 风格时，分别安装 `qml6-module-qtquick-controls2-styles-chameleon` 或 `qml-module-qtquick-controls2-styles-chameleon`。

```qml
import org.deepin.dtk 1.0 as D
```

使用 `D.Button`、`D.DciIcon` 或 `D.DTK` 访问控件和公共对象。样式参数通过 `org.deepin.dtk.style 1.0` 的 `Style` 单例取得；设置界面另见 [org.deepin.dtk.settings](org.deepin.dtk.settings.md)，C++ 应用加载入口见 [dtkdeclarative-dev](dtkdeclarative-dev.md)。

本篇的控件清单以 DTK6 导出为主。对照 DTK5 的注册清单，`ArrowShapePopupWindow`、`ControlBackground`、`ControlGroup`、`ControlGroupItem`、`DragItemsImage`、`EditPanel`、`LicenseDialog`、`ListView`、`PlaceholderText`、`SliderHandle` 和 `SpinBoxIndicator` 只在 DTK6 主模块中导出；`BackdropBlitter`、`DBorderImage`、`PopupHandle`、`InWindowBlurImpl` 和 `SysInfo` 也是 DTK6 注册项。DTK5 的 `InWindowBlur` 使用不同实现。`ButtonPanel` 属于 `org.deepin.dtk.private`，不从本模块导入。

---

## 按钮控件


### Button

#### 定位

Qt Quick 按钮的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.Button，提供主题化文字、图标、背景、圆角与焦点反馈。textColor 根据 checked 和 highlighted 状态选择配色；动作绑定、可选中状态及 clicked 使用基类接口。

#### 使用场景

需要 DTK 风格的按钮控件时使用。

### RoundButton

#### 定位

FloatingButton 的圆形按钮变体。

#### 功能能力总结

继承 FloatingButton，沿用圆形背景、相同的隐式宽高和浮动按钮配色，没有额外的圆角半径属性。文字、图标与点击使用基类接口。

#### 使用场景

需要圆形浮动按钮外观时。


---

### DelayButton

#### 定位

Qt Quick 延迟按钮的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.DelayButton，以 delay 控制长按时间，以 progress 显示积累进度。进度达到阈值时使用基类 activated 信号确认操作；按钮样式包含进度填充和焦点边框。

#### 使用场景

需要防止误触发的关键操作按钮时使用。

### IconButton

#### 定位

采用图标操作外观的 Button 派生控件。

#### 功能能力总结

继承 Button，使用图标按钮的尺寸、内边距和背景样式，保留文字与图标接口；支持 checked、highlighted 和交互状态配色。

#### 使用场景

需要在工具栏、标题栏或列表中提供紧凑操作入口时。


---

### FloatingButton

#### 定位

圆形浮动操作按钮。

#### 功能能力总结

继承 Button，使用圆形背景并令隐式宽高一致，预设 checkable 为 false、checked 为 true，以浮动按钮配色强调操作。文字与图标仍通过 Button 接口设置。

#### 使用场景

需要圆形悬浮操作按钮时使用。

### WarningButton

#### 定位

Button 的警告操作变体。

#### 功能能力总结

继承 Button，使用警告按钮的文字和背景调色板；动作绑定、图标、文字与点击行为沿用基类。

#### 使用场景

在界面中标注删除或不可逆操作时使用。

### ToolButton

#### 定位

Qt Quick 按钮的工具按钮变体。

#### 功能能力总结

继承 QtQuick.Templates.ToolButton，使用工具按钮的尺寸和背景，按选中、高亮和交互状态设置文字颜色；文字、图标与点击行为使用基类。

#### 使用场景

在工具栏中放置操作按钮时使用。

### RecommandButton

#### 定位

Button 的推荐操作变体。

#### 功能能力总结

继承 Button，预设推荐操作的 highlighted 状态，使用突出显示的按钮配色。类型名按模块声明拼写为 RecommandButton。

#### 使用场景

在界面中标注主要推荐操作时使用。

### ButtonBox

#### 定位

水平排列的按钮容器。

#### 功能能力总结

继承 Control，排列按钮并以 buttons 和 group 暴露内部 ButtonGroup；互斥及选中管理通过 group 设置，支持多个按钮共享连续背景。

#### 使用场景

需要将多个按钮按水平方向分组排列时使用。

### ButtonGroup

#### 定位

Qt Quick 按钮组的 DTK 样式实现。

#### 功能能力总结

对 QtQuick.Controls.ButtonGroup 的包装，使用其 buttons、exclusive、checkedButton 与选中变化接口管理按钮组，本身不提供视觉布局。

#### 使用场景

需要对多个按钮进行分组管理时使用。

### ButtonIndicator

#### 定位

按钮指示器渲染项。

#### 功能能力总结

通过 control 关联按钮，按 ColorSelector 选择 backgroundColor，用作按钮中的状态指示背景；位置和大小由调用者设置。

#### 使用场景

作为按钮内部指示器组件使用，应用代码不直接实例化。

### AbstractButton

#### 定位

Qt Quick 抽象按钮类型的包装。

#### 功能能力总结

对 QtQuick.Controls.AbstractButton 的包装，提供抽象按钮的文字、图标、选中、动作绑定和交互信号。它不是本模块各按钮 QML 文件的统一样式基类，具体外观由具体控件定义。

#### 使用场景

DTK6 中需要使用 Qt Quick 抽象按钮的共同接口或构造自定义按钮时。


---

### ActionButton

#### 定位

标题栏中使用的紧凑操作按钮。

#### 功能能力总结

继承 QtQuick.Templates.Button，采用标题栏动作按钮的尺寸与内容布局，增加可配置的 textColor 调色板。

#### 使用场景

在标题栏或工具栏中放置需要自定义文字颜色的操作按钮时使用。

### WindowButton

#### 定位

窗口标题栏按钮控件。

#### 功能能力总结

继承 IconButton，增加右上角圆角以及位于窗口右侧边缘的状态判断；图标、点击和选中状态由基类提供。

#### 使用场景

在窗口标题栏中放置最小化、最大化、关闭按钮时使用。

### WindowButtonGroup

#### 定位

窗口标题栏按钮组组件。

#### 功能能力总结

横向排列窗口操作按钮，根据所属窗口和 DWindow 的功能标志控制最小化、最大化、关闭及全屏入口，支持 fullScreenButtonVisible、splitScreenEnabled 和 embedMode。提供最大化与还原切换动作。

#### 使用场景

在窗口标题栏中放置标准窗口操作按钮组时使用。

## 对话框与窗口控件


### DialogWindow

#### 定位

DTK 风格的对话框窗口。

#### 功能能力总结

继承 Window，提供 header 组件、icon、默认 content 子项、palette 和内容内边距，并结合 DWindow 设置对话框窗口外观。显示、关闭、标题与窗口模态使用 Window 接口。

#### 使用场景

需要以独立窗口形式显示对话框时使用。

### Dialog

#### 定位

Qt Quick 对话框的 DTK 样式实现。

#### 功能能力总结

对 QtQuick.Controls.Dialog 的包装，沿用标准按钮、header、footer、模态及 accepted、rejected 接口；属于 Popup 对话框，不是独立 Window。

#### 使用场景

需要弹出对话框与用户交互时使用。

### PopupWindow

#### 定位

带窗口模糊背景的弹出窗口。

#### 功能能力总结

继承 Window，以 DTK 窗口模糊装饰构造独立弹出窗口，暴露 blurControl 供配置模糊的所属控件；窗口定位和可见性通过 Window 接口控制。

#### 使用场景

需要带窗口模糊效果的弹出面板时使用。

### ArrowShapePopupWindow

#### 定位

DTK6 导出的箭头弹出窗口，当前源码实现尚未完整。

#### 功能能力总结

声明 Window 及箭头方向、宽高、位置和拐角连接半径的别名。当前实现引用未定义的 ArrowShapeContainer 和 loader，直接实例化前需要确认所用发行版本是否已经修复。

#### 使用场景

维护箭头弹出窗口代码并核查版本实现时；需要可用的箭头面板时可先选择 ArrowShapePopup。


---

### ArrowShapePopup

#### 定位

带箭头形状的弹出面板。

#### 功能能力总结

继承 Popup，暴露圆角、箭头方向、宽高和位置，使用 ArrowBoxPath 绘制指向目标的弹出面板。

#### 使用场景

需要带指向箭头的弹出面板（如工具提示、上下文菜单）时使用。

### Popup

#### 定位

DTK 风格的弹出面板。

#### 功能能力总结

继承 QtQuick.Templates.Popup，增加 closeOnInactive，在所属窗口失去活动状态时按设置关闭；open、close、内容、定位和关闭策略沿用基类。

#### 使用场景

需要 DTK 风格的弹出面板时使用。

### StyledArrowShapeWindow

#### 定位

导出的箭头窗口样式包装，当前源码实现尚未完整。

#### 功能能力总结

声明以 ArrowShapeWindow 为根对象，结合 StyledBehindWindowBlur 暴露 control 并配置主题边框。但当前源码没有定义或注册 ArrowShapeWindow，直接实例化前需要确认所用发行版本是否已经修复。

#### 使用场景

维护旧版箭头窗口样式并核查其根类型实现时。


---

### DWindow

#### 定位

提供 DTK 窗口附加属性的不可创建类型。

#### 功能能力总结

作为附加属性提供窗口圆角、边框、阴影、透明、模糊、系统移动与缩放、窗口类型和装饰功能标志。也可设置加载覆盖层与退出转场；DTK6 增加窗口主题和启动动效。不可直接创建 DWindow 对象，在 Window 或 Popup 上使用附加属性。

#### 使用场景

需要为 Window 或 Popup 配置 DTK 窗口装饰与效果时。


---

### ApplicationWindow

#### 定位

Qt Quick 应用窗口的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.ApplicationWindow，提供 DTK 应用窗口背景与标题栏；内容、菜单栏、header、footer、字体和调色板使用基类接口。

#### 使用场景

作为 DTK QML 应用的主窗口类型使用。

### TitleBar

#### 定位

DTK 风格的窗口标题栏。

#### 功能能力总结

提供标题、图标、左侧与中央组件、菜单组件和窗口按钮组组件。支持全屏按钮、分屏入口、嵌入模式、全屏自动隐藏、分隔线及窗口内模糊；暴露文字调色板、背景组件和悬停状态。

#### 使用场景

应用窗口需要 DTK 风格标题栏（含标题、图标、菜单、窗口按钮）时使用。

### DialogTitleBar

#### 定位

对话框标题栏组件。

#### 功能能力总结

提供标题、图标、左侧和中央自定义组件，可控制窗口内模糊背景显示；用于 DialogWindow 的默认标题区。

#### 使用场景

在自定义对话框中需要 DTK 风格标题栏时使用。

### Drawer

#### 定位

Qt Quick 抽屉的 DTK 样式实现。

#### 功能能力总结

对 QtQuick.Controls.Drawer 的包装，沿用 edge、position、dragMargin、interactive 及弹出控制，提供从窗口边缘展开的侧栏。

#### 使用场景

需要侧边滑出面板的场景中使用。

### AboutDialog

#### 定位

显示应用产品信息的标准关于对话框。

#### 功能能力总结

继承 DialogWindow，展示名称、图标、版本、描述、公司标志、许可证、网站名称和链接，可指定 licensePath 打开组件许可证内容。

#### 使用场景

应用需要展示标准关于对话框（产品名称、图标、版本号、描述、许可证、公司 Logo、官网链接）时使用。


---

### LicenseDialog

#### 定位

组件许可证查看窗口。

#### 功能能力总结

继承 DialogWindow，通过 licenseProvider 接收 LicenseInfoProvider，展示组件名称、版本、版权与许可证条款。

#### 使用场景

DTK6 中需要展示应用依赖组件的许可证信息时。


---

### LicenseInfoProvider

#### 定位

许可证组件清单的数据入口。

#### 功能能力总结

从 path 加载许可文件，以 licenseList 暴露组件信息，valid 表示有效性；通过 licenseContent 取得指定许可证正文，并通知路径、有效性与清单变化。

#### 使用场景

需要为 LicenseDialog 或自定义许可证页面提供数据时。


---

### PopupHandle

#### 定位

弹出控件的窗口附加属性入口。

#### 功能能力总结

提供 DQuickWindowAttached，把窗口装饰、主题与系统交互参数关联到 Popup 的实际窗口；以附加属性使用，不能直接实例化。

#### 使用场景

DTK6 中需要为弹出控件设置 DWindow 同类的窗口参数时。


---

### ContextMenuWindow

#### 定位

上下文菜单使用的 Quick 窗口。

#### 功能能力总结

继承 QQuickWindow，处理上下文菜单相关事件；窗口可见性、位置和内容项使用基类接口，没有单独的菜单模型属性。

#### 使用场景

需要用独立 Quick 窗口承载上下文菜单内容时。


---


## 输入控件


### TextField

#### 定位

Qt Quick 单行文本输入框的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.TextField，提供 DTK 单行输入样式、占位文字调色板、背景颜色、清除与上下文菜单能力。增加 showAlert、alertText、alertDuration 和 contextMenuVisible；文本、回显、验证与编辑通知使用基类。

#### 使用场景

需要 DTK 风格的单行文本输入框并支持告警提示时使用。

### TextArea

#### 定位

Qt Quick 多行文本输入框的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.TextArea，提供 DTK 多行文本样式和 placeholderTextPalette；文本、只读、选择、换行和编辑通知使用基类接口。

#### 使用场景

需要 DTK 风格的多行文本输入控件时使用。

### SearchEdit

#### 定位

搜索输入控件。

#### 功能能力总结

继承 LineEdit，展示搜索图标和居中占位提示，使用 placeholder 设置提示文字；editting 表示焦点、上下文菜单或已有内容导致的编辑状态，检索由调用者处理。

#### 使用场景

需要带搜索占位提示的搜索输入框时使用。

### PasswordEdit

#### 定位

密码输入控件。

#### 功能能力总结

继承 LineEdit，提供密码与明文回显切换、isEchoMode 状态和 echoButtonVisible，并通过 toggleEchoMode 切换；文本和告警沿用基类。

#### 使用场景

需要输入密码并支持切换显示/隐藏密码时使用。

### IpV4LineEdit

#### 定位

IPv4 地址输入控件。

#### 功能能力总结

以四段输入组成 IPv4 地址，通过 text 同步完整地址，提供 showAlert、alertText、alertDuration 和 backgroundColor。控件处理分段编辑与焦点移动，业务验证结果可用告警属性展示。

#### 使用场景

需要输入和验证 IPv4 地址时使用。

### KeySequenceEdit

#### 定位

快捷键编辑控件。

#### 功能能力总结

使用 KeySequenceListener 记录按键，通过 keys、text 和 placeholderText 展示组合键与占位文字，提供背景和占位文字调色板；没有 QKeySequence 类型的 C++ 接口。

#### 使用场景

需要让用户输入或修改快捷键组合时使用。

### LineEdit

#### 定位

单行文本输入控件。

#### 功能能力总结

继承 TextField，添加清除按钮并通过 clearButton 暴露该按钮，适合进一步配置其可见性或外观。

#### 使用场景

需要带清除按钮的单行文本输入控件时使用。

### EditPanel

#### 定位

输入控件背景面板组件。

#### 功能能力总结

作为文本控件背景，关联 control，提供背景和告警背景调色板、showBorder、showAlert、alertText 与 alertDuration；告警提示跟随关联控件显示。

#### 使用场景

作为输入控件（TextField、SpinBox）的背景渲染组件使用，应用代码不直接实例化。

### PlaceholderText

#### 定位

Qt Quick 标签的占位文本变体。

#### 功能能力总结

包装 QtQuick.Controls.impl 的占位文字项，沿用其文字与字体属性，用作输入控件的提示内容。

#### 使用场景

在输入控件中显示灰色提示文字时使用。

### SpinBox

#### 定位

Qt Quick 数值输入框的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.SpinBox，提供 DTK 增减指示器、编辑背景及焦点反馈，并暴露告警文字、时长和状态。from、to、stepSize、value 以及文本数值转换使用基类接口。

#### 使用场景

需要 DTK 风格的数值输入框并支持告警提示时使用。

### PlusMinusSpinBox

#### 定位

带加减按钮的数值输入控件。

#### 功能能力总结

组合 SpinBox 和加减按钮，通过 spinBox 访问实际数值控件；可独立控制 upButtonVisible、downButtonVisible、resetButtonVisible，范围和当前值通过内部 SpinBox 设置。

#### 使用场景

需要带独立加减按钮和重置按钮的数值调节控件时使用。

### Dial

#### 定位

Qt Quick 旋钮的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.Dial，提供主题化旋钮、刻度与焦点反馈；范围、数值、步长、环绕和交互通知使用基类接口。

#### 使用场景

需要以旋转方式调节数值的场景中使用。

### SpinBoxIndicator

#### 定位

SpinBox 加减指示器组件。

#### 功能能力总结

关联 spinBox，设置按下状态、增减方向及是否单独显示指示器，以调色板渲染数值输入的操作背景。

#### 使用场景

作为 SpinBox 内部加减按钮组件使用，应用代码不直接实例化。

### CheckBox

#### 定位

Qt Quick 复选框的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.CheckBox，提供 DTK 勾选图标与焦点反馈；文字、checked、checkState、tristate 和交互通知使用基类接口。

#### 使用场景

需要在界面中提供二态选择控件时使用。

### RadioButton

#### 定位

Qt Quick 单选按钮的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.RadioButton，提供 DTK 单选指示外观；文字、checked、autoExclusive 及分组管理使用基类接口。

#### 使用场景

需要在互斥选项组中选择一个选项时使用。

### Switch

#### 定位

Qt Quick 开关的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.Switch，以 backgroundColor 和 handleColor 定义开关轨道和手柄配色；选中状态和交互通知使用基类接口。

#### 使用场景

需要在界面中提供开关切换控件时使用。

### ComboBox

#### 定位

Qt Quick 下拉组合框的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.ComboBox，提供图标数据角色、可见条目上限、分隔线和文本对齐，并增加输入告警属性。模型、文本角色、当前索引、可编辑性和 activated 使用基类接口。

#### 使用场景

需要 DTK 风格的下拉选择控件并支持图标显示和告警提示时使用。

### CheckDelegate

#### 定位

Qt Quick 复选委托项的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.CheckDelegate，增加自定义 content、backgroundColor、indicatorIcon 与 indicatorVisible；勾选状态与交互通知使用基类接口。

#### 使用场景

在列表视图中需要带复选框的委托项时使用。

### SwipeDelegate

#### 定位

Qt Quick 滑动委托项的 DTK 样式实现。

#### 功能能力总结

对 QtQuick.Controls.SwipeDelegate 的包装，沿用滑动区、滑动位置及左侧、右侧动作组件，用于可滑动的列表项。

#### 使用场景

列表项需要滑动显示操作按钮时使用。

### Slider

#### 定位

Qt Quick 滑动条的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.Slider，增加 grooveColor、handleType、虚线参数、已过区域高亮及 alignToTicks。范围、数值、方向、步长与交互使用基类接口。

#### 使用场景

需要 DTK 风格滑动条并支持自定义手柄类型和虚线样式时使用。

### SliderHandle

#### 定位

滑动条手柄组件。

#### 功能能力总结

继承 DciIcon，以 type 区分不同方向和箭头样式的滑块手柄，并按类型选择图标名；颜色和交互状态通过图标接口设置。

#### 使用场景

作为 Slider 内部手柄渲染组件使用，应用代码不直接实例化。

### SliderTipItem

#### 定位

滑动条刻度提示项。

#### 功能能力总结

显示 TipsSlider 的刻度及文字，可设置 text、文字对齐、方向、highlight、tickColor 和 textColor；默认从所属滑动条取得刻度方向和排列方式。

#### 使用场景

在带刻度的滑动条中显示刻度提示文字时使用。

### TipsSlider

#### 定位

带刻度提示的滑动条。

#### 功能能力总结

以 slider 暴露内部 Slider，以 ticks 接收刻度项目，并通过 tickDirection 指定前侧或后侧刻度；范围、数值与滑块外观通过内部 Slider 配置。

#### 使用场景

需要带刻度标记和提示文字的滑动条时使用。


---

## 菜单与动作控件


### Menu

#### 定位

DTK 风格的菜单控件。

#### 功能能力总结

继承 QtQuick.Templates.Menu，增加 closeOnInactive、可见条目上限、背景调色板及 header、footer 组件，可用 model 接入条目模型。菜单项管理与弹出控制使用基类接口。

#### 使用场景

需要 DTK 风格的右键菜单或下拉菜单时使用。

### MenuItem

#### 定位

Qt Quick 菜单项的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.MenuItem，按菜单内是否存在勾选项决定指示器留白，可配置文字和子菜单展开背景调色板；动作、图标、子菜单与触发信号沿用基类。

#### 使用场景

在菜单中放置可选项时使用。

### MenuBar

#### 定位

Qt Quick 菜单栏的 DTK 样式实现。

#### 功能能力总结

对 QtQuick.Controls.MenuBar 的包装，使用菜单列表及菜单增删接口构造菜单栏，外观由当前 Qt Quick Controls 样式提供。

#### 使用场景

应用窗口顶部需要菜单栏时使用。

### MenuSeparator

#### 定位

带可选标题的菜单分隔符。

#### 功能能力总结

继承 QtQuick.Templates.MenuSeparator，可使用 text 显示分组文字，空文字时显示分隔线，并支持文字调色板。

#### 使用场景

在菜单中分组分隔菜单项并显示分组标题时使用。

### ThemeMenu

#### 定位

主题切换菜单。

#### 功能能力总结

提供跟随系统、浅色和深色主题选项，根据 ApplicationHelper.paletteType 显示选中状态，并在触发时更新应用调色板类型。

#### 使用场景

需要在应用中提供主题切换菜单时使用。

### AboutAction

#### 定位

提供"关于"对话框触发入口的 Action 变体。

#### 功能能力总结

继承 Action，通过 aboutDialog 接收对话框组件，触发时创建或显示关于对话框，并使用所属窗口作为关联对象。

#### 使用场景

在菜单中添加"关于"选项并关联自定义关于对话框时使用。

### HelpAction

#### 定位

提供帮助页面跳转的 Action 变体。

#### 功能能力总结

继承 Action，触发时调用 ApplicationHelper.handleHelpAction 打开应用帮助入口。

#### 使用场景

在菜单中添加帮助入口时使用。

### QuitAction

#### 定位

Action 的退出操作变体。

#### 功能能力总结

继承 Action，触发时调用 Qt.quit 请求退出 QML 应用。

#### 使用场景

在菜单中添加退出应用选项时使用。

### Action

#### 定位

Qt Quick 动作的 DTK 样式实现。

#### 功能能力总结

对 QtQuick.Controls.Action 的包装，沿用 text、icon、shortcut、enabled、checkable、checked 与 triggered，在多个操作入口间共享动作。

#### 使用场景

在菜单、工具栏或上下文菜单中复用统一行为逻辑时使用。

### ActionGroup

#### 定位

Qt Quick 动作组的 DTK 样式实现。

#### 功能能力总结

对 QtQuick.Controls.ActionGroup 的包装，管理动作的 enabled、exclusive、checkedAction 和触发通知；本身不提供可见控件。

#### 使用场景

需要在菜单或工具栏中实现互斥选择的动作组时使用。


---

## 列表与视图控件


### ScrollView

#### 定位

Qt Quick 滚动视图的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.ScrollView，配置 DTK 滚动条与裁剪；内容尺寸和滚动位置通过基类及关联 Flickable 设置。

#### 使用场景

内容区域需要滚动浏览时使用。

### StackView

#### 定位

Qt Quick 堆叠视图的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.StackView，提供 DTK 页面转场；push、pop、replace、currentItem、depth 和 busy 使用基类接口。

#### 使用场景

需要实现页面导航栈时使用。

### SwipeView

#### 定位

Qt Quick 滑动视图的 DTK 样式实现。

#### 功能能力总结

对 QtQuick.Controls.SwipeView 的包装，使用 currentIndex、orientation 和 interactive 组织可滑动页面，并通过基类管理页面项目。

#### 使用场景

需要可滑动切换的分页视图时使用。

### ItemDelegate

#### 定位

Qt Quick 列表项委托的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.ItemDelegate，提供自定义 content、指示器和背景可见性、级联选中与内容流动布局。可指定 corners 圆角组合并启用拖动，使用 getCornersForBackground 生成连续分组的圆角配置。

#### 使用场景

在列表视图中需要 DTK 风格委托项并支持级联选中、圆角控制时使用。

### ArrowListView

#### 定位

带箭头指示的有限高度列表视图。

#### 功能能力总结

以 view 暴露内部 ListView，设置 maxVisibleItems 和 itemHeight 控制列表显示高度；溢出时显示上下滚动入口，模型与委托通过内部视图配置。

#### 使用场景

需要在弹出菜单或下拉框中显示有限项数并带滚动指示时使用。

### SortFilterModel

#### 定位

排序过滤代理模型。

#### 功能能力总结

继承 DelegateModel，使用 lessThan 和 filterAcceptsItem 回调排序与过滤源数据，visibleGroup 表示可见项集合。update 重新筛选和排序，模型或回调变化时自动更新。

#### 使用场景

需要对列表模型进行排序和过滤时使用。

### TabBar

#### 定位

Qt Quick 选项卡栏的 DTK 样式实现。

#### 功能能力总结

对 QtQuick.Controls.TabBar 的包装，管理页面切换按钮和当前索引，布局与外观沿用当前 Qt Quick Controls 样式。

#### 使用场景

需要标签页导航时使用。

### PageIndicator

#### 定位

Qt Quick 页面指示器的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.PageIndicator，提供 DTK 页面指示点外观；count、currentIndex、interactive 使用基类接口。

#### 使用场景

在分页浏览场景中指示当前页面位置时使用。

### Container

#### 定位

Qt Quick 容器的 DTK 样式实现。

#### 功能能力总结

对 QtQuick.Controls.Container 的包装，沿用内容项目、内容模型、当前索引和动态增删，用作自定义项目容器。

#### 使用场景

作为自定义容器控件的样式基类使用。

### Control

#### 定位

Qt Quick 控件的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.Control，提供 DTK 控件基础尺寸和样式约定；contentItem、background、padding、palette 与 font 使用基类接口。

#### 使用场景

作为自定义控件的样式基类使用。

### DialogButtonBox

#### 定位

Qt Quick 对话框按钮组的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.DialogButtonBox，提供 DTK 按钮布局与默认委托；standardButtons、buttonRole 和接受、拒绝通知使用基类接口。

#### 使用场景

在对话框底部放置标准按钮时使用。

### ScrollBar

#### 定位

Qt Quick 滚动条的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.ScrollBar，提供 DTK 活动状态与悬停外观；size、position、orientation、policy 和 Flickable 附加属性使用基类接口。

#### 使用场景

内容区域需要可交互滚动条时使用。

### ScrollIndicator

#### 定位

Qt Quick 滚动指示器的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.ScrollIndicator，提供 DTK 滚动位置提示；size、position、active、orientation 和 Flickable 附加属性使用基类接口。

#### 使用场景

在不需要交互滚动条仅提示可滚动时使用。


---

### ListView

#### 定位

支持分组背景与多项拖动的列表。

#### 功能能力总结

继承 QtQuick.ListView，提供 duration、bgVisible、hoveredItem、checkedItems 和 dragItem；可更新悬停项和选中项集合，配合 ItemDelegate 呈现连续背景与拖动预览。模型、委托和滚动使用基类接口。

#### 使用场景

DTK6 中需要带 DTK 选择反馈和多项拖动的列表时。


---

### ObjectModelProxy

#### 定位

对象模型的过滤代理。

#### 功能能力总结

通过 sourceModel 关联对象模型，使用 filterAcceptsItem 回调决定对象是否进入代理模型，并提供 update 重新过滤和源索引、代理索引互相映射。

#### 使用场景

需要对已有对象项目集合进行筛选时。


---

### SortFilterProxyModel

#### 定位

Qt 排序过滤代理模型的 QML 注册类型。

#### 功能能力总结

注册 QSortFilterProxyModel，提供源模型接入、排序角色、过滤角色和过滤条件属性。需要 QML 自定义比较或过滤回调时使用 SortFilterModel。

#### 使用场景

需要对 C++ 或 QML 项模型使用标准排序过滤代理时。


---

### DragItemsImage

#### 定位

多个拖动项目的组合预览。

#### 功能能力总结

通过 items 接收项目列表，对每个项目抓取图像并组合叠放；通过 aboutToGrabToImage 与 grabToImageFinished 通知抓取前后时机。

#### 使用场景

DTK6 中需要为多项拖动显示组合图像时；直接设置 items 列表。


---

### ControlGroup

#### 定位

带标题的可折叠内容组。

#### 功能能力总结

继承 ColumnLayout，使用 title 和 isExpanded 控制标题和展开状态，通过默认 childItem 收集内容。interval 控制内容动画间隔，titleHeight 表示标题区域高度。

#### 使用场景

DTK6 中需要将多个 ControlGroupItem 组织成可折叠设置分组时。


---

### ControlGroupItem

#### 定位

可折叠内容组中的布局行。

#### 功能能力总结

继承 RowLayout，以 isExpanded 调整位置、透明度和可见性，initY 保存展开位置；动画间隔取自所属 ControlGroup。

#### 使用场景

DTK6 中需要向 ControlGroup 添加可随分组折叠的内容行时。


---


## 视觉效果与渲染控件


### BoxShadow

#### 定位

盒模型外阴影渲染项。

#### 功能能力总结

显示矩形外投影，可设置统一或四角半径、shadowBlur、shadowOffsetX、shadowOffsetY、shadowColor、spread 和 hollow。

#### 使用场景

需要为控件渲染外阴影效果时使用。

### BoxInsetShadow

#### 定位

盒模型内阴影渲染项。

#### 功能能力总结

显示矩形内阴影，可设置统一或四角半径、模糊、偏移、颜色和扩展距离，用于面板内部的凹陷视觉效果。

#### 使用场景

需要为矩形或圆角矩形控件渲染内阴影效果时使用。

### BoxPanel

#### 定位

带内外阴影和边框的盒模型面板。

#### 功能能力总结

通过两组背景颜色、内外边框、外阴影和内阴影调色板构造圆角面板，支持 radius、阴影模糊和偏移、悬停跟随及外阴影开关。

#### 使用场景

需要渲染带渐变背景、内外边框和阴影的按钮面板时使用，通常作为按钮背景组件。

### FloatingPanel

#### 定位

浮动面板组件。

#### 功能能力总结

提供带圆角、边框和阴影的浮层背景，可配置模糊与非模糊背景调色板、radius、blurRadius、blurMultiplier，并通过 enableBlur 控制模糊。

#### 使用场景

需要显示浮动面板（如通知中心、控制面板）时使用。

### RectangularShadow

#### 定位

矩形阴影渲染项。

#### 功能能力总结

使用 GlowEffect 构造矩形阴影，支持 offsetX、offsetY、glowRadius、spread、color、cornerRadius 与 fill。

#### 使用场景

需要为矩形或圆角矩形控件渲染阴影效果时使用。

### HighlightPanel

#### 定位

高亮面板渲染项。

#### 功能能力总结

提供高亮背景、内外阴影和 radius 参数，由 ColorSelector 根据控件状态选择颜色。

#### 使用场景

作为控件高亮状态的背景渲染组件使用，应用代码不直接实例化。

### ControlBackground

#### 定位

控件焦点背景渲染项。

#### 功能能力总结

继承 Rectangle，增加 focusBorderSpace、focusBorder 和 focusBorderVisible，构造输入框或其他控件的焦点边框。

#### 使用场景

作为控件获得焦点时的背景渲染组件使用，应用代码不直接实例化。

### Frame

#### 定位

带圆角边框的框架容器。

#### 功能能力总结

继承 QtQuick.Templates.Frame，提供 DTK 圆角边框背景，可设置 radius，内容与内边距使用基类接口。

#### 使用场景

需要带圆角边框的内容容器时使用。

### Pane

#### 定位

Qt Quick 面板的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.Pane，提供 DTK 面板背景，承载子项目并沿用基类内边距、字体和调色板。

#### 使用场景

需要带背景的面板容器时使用。

### GroupBox

#### 定位

Qt Quick 分组框的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.GroupBox，提供 DTK 分组标题和背景，title、label、内容及内边距使用基类接口。

#### 使用场景

需要将相关控件用边框和标题分组时使用。

### OutsideBoxBorder

#### 定位

外边框渲染项。

#### 功能能力总结

在矩形外侧绘制边框，可设置 borderWidth、color 和 radius，用于控件背景的外轮廓。

#### 使用场景

作为控件外部边框渲染组件使用，应用代码不直接实例化。

### InsideBoxBorder

#### 定位

内边框渲染项。

#### 功能能力总结

在矩形内侧绘制边框，支持 borderWidth、color 和 radius；默认边框宽度按 Screen.devicePixelRatio 设置。

#### 使用场景

作为控件内部边框渲染组件使用，应用代码不直接实例化。

### FocusBoxBorder

#### 定位

焦点边框渲染项。

#### 功能能力总结

绘制焦点轮廓，可配置 color、borderWidth 和 radius；可见性由所属控件焦点状态控制。

#### 使用场景

作为控件获得焦点时的边框渲染组件使用，应用代码不直接实例化。

### BlitFramebuffer

#### 定位

QML 场景中的帧缓冲区位块传输渲染项，从 C++ 类 `DQuickBlitFramebuffer` 注册为 QML 类型。

#### 功能能力总结

捕获当前绘制位置下方的场景内容并提供纹理，供后续 ItemViewport 或模糊项读取；它不是接收任意外部帧缓冲区对象的接口。

#### 使用场景

需要将离屏渲染的帧缓冲区内容高效地呈现到 QML 场景中时使用。

### ItemViewport

#### 定位

QML 场景中的视口裁剪渲染项，从 C++ 类 `DQuickItemViewport` 注册为 QML 类型。

#### 功能能力总结

以 sourceItem 和 sourceRect 指定源项及区域，支持圆角、固定区域和隐藏源项；DTK6 增加 compositionMode 合成模式，用于局部画面复制与裁剪。

#### 使用场景

需要在 QML 中实现视口裁剪或局部区域渲染时使用。

### StyledBehindWindowBlur

#### 定位

DTK 样式的窗口模糊背景项。

#### 功能能力总结

继承 BehindWindowBlur，通过 control 关联所属控件，使用 DTK 样式设置圆角及混合颜色；模糊开关与有效性使用基类接口。

#### 使用场景

需要为控件或窗口添加 DTK 风格的模糊背景时使用。

### FlowStyle

#### 定位

DTK 控件尺寸与状态配色的样式参数集合。

#### 功能能力总结

保存控件尺寸、间距、圆角和各交互状态的 Palette 配色，并按按钮、输入、菜单、对话框、列表、进度和标题栏组织参数对象。它是样式数据类型，实际共享入口为 Style 单例。

#### 使用场景

应用需要自定义 DTK 控件样式参数或读取默认样式值时使用。

### BusyIndicator

#### 定位

Qt Quick 忙碌指示器的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.BusyIndicator，提供旋转等待动画和 fillColor 调色板，running 控制活动状态。

#### 使用场景

需要指示后台操作正在进行时使用。

### ProgressBar

#### 定位

Qt Quick 进度条的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.ProgressBar，提供 DTK 进度外观，增加 formatText 和 animationStop；from、to、value 与 indeterminate 使用基类接口。

#### 使用场景

需要展示操作进度并自定义进度文本时使用。

### WaterProgressBar

#### 定位

水波纹进度条控件。

#### 功能能力总结

显示整数 value 对应的水波进度，通过 running 控制水波动画；支持两层背景、阴影、气泡及文字调色板。

#### 使用场景

需要以水波纹动画形式展示进度的场景中使用。

### EmbeddedProgressBar

#### 定位

嵌入式进度条组件。

#### 功能能力总结

继承 QtQuick.Templates.ProgressBar，以 backgroundColor 与 progressBackgroundColor 提供嵌入式进度条配色；范围与当前值使用基类接口。

#### 使用场景

在控件内部嵌入进度指示（如按钮加载状态）时使用。

### CicleSpreadAnimation

#### 定位

圆形扩散动画效果项。

#### 功能能力总结

使用 centerPoint 指定扩散中心，通过 start 和 stop 控制圆形扩散动画。类型名按模块声明拼写为 CicleSpreadAnimation。

#### 使用场景

需要实现水波纹或圆形扩散动画效果时使用。

### Label

#### 定位

Qt Quick 标签的 DTK 样式实现。

#### 功能能力总结

对 QtQuick.Controls.Label 的包装，沿用文字、字体、颜色、换行、省略及对齐接口，外观由当前 Qt Quick Controls 样式提供。

#### 使用场景

需要显示 DTK 风格文本标签时使用。

### ToolTip

#### 定位

Qt Quick 提示标签的 DTK 样式实现。

#### 功能能力总结

继承 QtQuick.Templates.ToolTip，提供 DTK 提示背景、文字与延迟动画；text、delay、timeout、show、hide 和附加属性使用基类接口。

#### 使用场景

需要为控件提供悬浮提示信息时使用。

### AlertToolTip

#### 定位

带连接线的告警提示气泡。

#### 功能能力总结

关联 target 控件，设置告警 text 和 timeout，按目标位置显示提示并在到期后隐藏；可见性由调用者与到期状态共同决定。

#### 使用场景

需要在输入控件旁显示告警提示并通过连接线指向目标控件时使用。

### FloatingMessage

#### 定位

浮动消息提示组件。

#### 功能能力总结

继承 FloatingMessageContainer，提供主题化 panel、contentItem 和 button 组件，以 message 承载消息内容；closeMessage 请求关闭，可由 MessageManager 或 DTK.sendMessage 创建。

#### 使用场景

需要在屏幕角落显示带图标和操作按钮的浮动消息提示时使用。

### BackdropBlitter

#### 定位

带内容容器的背景捕获项。

#### 功能能力总结

通过 content 提供内容容器，以 blitterEnabled 控制背景捕获，以 offscreen 选择离屏处理；供子项采样背景并叠加效果。

#### 使用场景

DTK6 中需要在一组内容下捕获背景纹理时。


---

### InWindowBlur

#### 定位

窗口内部背景模糊控件。

#### 功能能力总结

DTK6 通过 BackdropBlitter 与模糊效果捕获背景，提供 radius、multiplier、content、offscreen 和只读 valid；默认内容进入背景容器，valid 反映当前模糊能力。DTK5 使用自己的窗口内模糊实现。

#### 使用场景

需要在窗口内容上叠加模糊面板时。


---

### InWindowBlurImpl

#### 定位

DTK6 窗口内模糊的渲染项。

#### 功能能力总结

提供 radius 与 offscreen，处理所在场景的背景模糊；它是 QML 注册项，其 C++ 私有头文件不是开发包的公开接口。

#### 使用场景

DTK6 中需要直接组合窗口内模糊渲染项时，通常优先使用 InWindowBlur。


---

### BehindWindowBlur

#### 定位

请求窗口背后模糊的区域。

#### 功能能力总结

设置 cornerRadius、blendColor 和 blurEnabled，通过 valid 查询模糊区域是否有效。

#### 使用场景

需要使窗口背后的桌面内容模糊并叠加颜色时。


---

### RoundRectangle

#### 定位

支持按角选择圆角的矩形。

#### 功能能力总结

通过 color、radius 和 corners 配置颜色、圆角半径及四角组合，未选中的角保持直角。

#### 使用场景

需要连续列表分组或只让部分角变圆时。


---

### GlowEffect

#### 定位

矩形光晕渲染项。

#### 功能能力总结

设置 glowRadius、color、spread、relativeSizeX、relativeSizeY 和 fill，形成可扩展的光晕区域。

#### 使用场景

需要为矩形或圆角面板构造阴影或光晕时。


---

### DBorderImage

#### 定位

Qt BorderImage 的 DTK 注册类型。

#### 功能能力总结

继承 QQuickBorderImage，沿用图像源、九宫格边距及水平与垂直平铺属性，没有额外的公开 QML 属性。

#### 使用场景

DTK6 中需要在 DTK 模块内使用九宫格背景图时。


---

### SoftwareColorOverlay

#### 定位

适用于软件渲染的颜色覆盖项。

#### 功能能力总结

使用 source 指定源项目，设置覆盖 color，并通过 cached 控制缓存；提供相应属性变化通知。

#### 使用场景

需要在软件渲染场景中给项目覆盖颜色时。


---

### SoftwareOpacityMask

#### 定位

适用于软件渲染的透明度遮罩项。

#### 功能能力总结

通过 source 与 maskSource 指定源和遮罩，invert 控制遮罩反转。

#### 使用场景

需要在软件渲染场景中按另一项目的透明度裁剪内容时。


---

### ColorOverlay

#### 定位

按渲染后端选择实现的颜色覆盖控件。

#### 功能能力总结

使用 source 与 color 配置颜色覆盖，软件后端使用 SoftwareColorOverlay，其他后端使用相应图形效果实现。

#### 使用场景

需要给图像或场景项统一着色时。


---

### OpacityMask

#### 定位

按渲染后端选择实现的透明度遮罩控件。

#### 功能能力总结

通过 source、maskSource 和 invert 应用遮罩；软件后端使用 SoftwareOpacityMask，其他后端使用相应图形效果实现。

#### 使用场景

需要以另一个项目的透明度定义显示形状时。


---

### WaterProgressAttribute

#### 定位

水波进度的动画属性对象。

#### 功能能力总结

关联 waterProgress，设置图像宽高及 running，提供前后层偏移与 pops 气泡集合，供 WaterProgressBar 的水波图像和气泡绘制使用。

#### 使用场景

需要自定义水波进度外观并保留水波动画数据时。


---

### ArrowBoxPath

#### 定位

带箭头的圆角矩形路径。

#### 功能能力总结

设置箭头方向、位置、宽高、矩形宽高、圆角半径和 spread，生成可供 Shape 或窗口裁剪使用的路径。

#### 使用场景

需要为弹出面板或提示窗口构造带指向箭头的边界时。


---


## 图标、主题与公共对象

### DTK

#### 定位

QML 应用的共享 DTK 能力入口。

#### 功能能力总结

单例提供主题类型、字体管理器、活动与非活动调色板、窗口管理器及模糊和动画能力状态。可合成颜色、创建图标和图标调色板、查询光标位置、发送与关闭窗口消息或发送系统通知。

#### 使用场景

需要在 QML 中访问应用级主题、图标、字体或消息服务时，直接使用 DTK 单例。


---

### ApplicationHelper

#### 定位

图形应用辅助器的 QML 单例。

#### 功能能力总结

暴露 DGuiApplicationHelper 的主题与调色板类型、相关枚举和 QML 可调用的帮助入口；paletteType 可设置跟随系统、浅色或深色主题。

#### 使用场景

需要在 QML 中读取应用主题或实现主题切换菜单时。


---

### WindowManagerHelper

#### 定位

窗口管理器能力的 QML 单例。

#### 功能能力总结

暴露模糊、合成、无标题栏和壁纸能力属性、变化通知，以及窗口功能、装饰和窗口类型枚举。

#### 使用场景

需要根据窗口管理器能力选择视觉效果或设置 DWindow 功能标志时。


---

### FontManager

#### 定位

按 DTK 字号层级生成字体的对象。

#### 功能能力总结

提供 T1 至 T11 字号、baseFont、字号像素值读写与 fontChanged；DTK.fontManager 提供共享实例，也可创建独立对象。

#### 使用场景

需要在 QML 中使用统一字号或设置局部字体规格时。


---

### Palette

#### 定位

按控件状态与主题选择颜色的调色板对象。

#### 功能能力总结

分别保存 normal、hovered、pressed、disabled 及对应深色主题值，支持 enabled 和颜色家族枚举；颜色可用普通 QColor 或 DTK 颜色值指定。

#### 使用场景

需要为自定义控件定义浅色、深色及交互状态的配色时。


---

### ColorSelector

#### 定位

把 Palette 转为当前状态颜色的附加属性。

#### 功能能力总结

关联 control，推导只读 controlTheme 和 controlState，可覆写 hovered、pressed、disabled、inactived 及 family，并为控件的 Palette 属性提供选定颜色。不能直接创建对象。

#### 使用场景

需要使自定义控件的背景、文字或边框跟随主题与交互状态时。


---

### Color

#### 定位

DTK 颜色语义的枚举入口。

#### 功能能力总结

提供颜色类型枚举，颜色值由 DTK.makeColor 构造并交给 Palette 使用；不作为普通 QML 对象实例化。

#### 使用场景

需要用语义颜色代替固定色值时。


---

### DciIcon

#### 定位

DCI 图标显示与动画项。

#### 功能能力总结

通过 name、sourceSize、mode、theme 和 palette 设置图标，可镜像、异步加载、缓存、保留旧图像及控制填充方式，并选择是否回退到 QIcon；play 按指定交互状态播放动画。

#### 使用场景

需要显示支持主题、状态和动画的 DCI 图标时。


---

### QtIcon

#### 定位

Qt 图标主题的显示项。

#### 功能能力总结

通过 name、mode、state、color 和 fallbackSource 设置图标来源、交互状态、着色和回退图片，图像显示参数沿用图像项接口。

#### 使用场景

需要显示普通图标主题资源并提供回退图像时。


---

### IconLabel

#### 定位

组合图标与文字的布局项。

#### 功能能力总结

接收 DTK 图标值、文字、字体和颜色，可选择仅图标、仅文字、横向或纵向组合，并设置间距、镜像、对齐与内边距。

#### 使用场景

需要在按钮或列表中复用图标文字布局时。


---

### Style

#### 定位

共享的 DTK 控件样式单例。

#### 功能能力总结

由 FlowStyle 提供尺寸和调色板参数，同时注册到 org.deepin.dtk 与 org.deepin.dtk.style；通过参数对象取得按钮、输入、列表、面板和窗口外观配置。

#### 使用场景

需要让自定义控件与 DTK 控件保持相同的尺寸和配色时。


---

### SysInfo

#### 定位

系统信息枚举的 QML 入口。

#### 功能能力总结

DTK6 注册 DSysInfo 命名空间中的系统类型枚举，没有独立的系统信息查询对象；发行版标志和网站信息可从 DTK 单例读取。

#### 使用场景

DTK6 中需要在 QML 中引用系统类型常量时。


---

### PlatformHandle

#### 定位

平台窗口效果枚举的 QML 入口。

#### 功能能力总结

注册 DPlatformHandle 的窗口效果、场景与相关枚举，不能直接创建对象；窗口参数通过 DWindow 附加属性设置。

#### 使用场景

需要为窗口效果使用 DTK 平台枚举值时。


---


## 配置、按键与消息对象

### Config

#### 定位

DConfig 的 QML 配置入口。

#### 功能能力总结

以 name 和 subpath 选择配置资源，支持 async 初始化，提供值读取、写入、恢复默认值、键列表、有效性与默认值判断；initialized 和 valueChanged 通知初始化与值变化，配置键可映射为动态属性。

#### 使用场景

需要在 QML 中保存应用配置或为设置模块提供 config 对象时。


---

### KeySequenceListener

#### 定位

关联输入项目的按键序列记录器。

#### 功能能力总结

通过 target 监听按键，读写 keys 并设置 maxKeyCount，clearKeys 清除记录，相关属性变化发出通知。

#### 使用场景

需要实现快捷键编辑器或展示用户输入的组合键时。


---

### MessageManager

#### 定位

窗口内消息管理的附加属性。

#### 功能能力总结

设置消息 delegate、layout 和 capacity，查询 count；可发送文本消息或自定义委托消息，按消息对象或标识关闭。消息管理器作为窗口附加对象使用，不能直接实例化。

#### 使用场景

需要控制一个 Quick 窗口内的消息布局、容量和关闭时机时。


---

### FloatingMessageContainer

#### 定位

窗口消息的非可视数据与面板容器。

#### 功能能力总结

保存 panel、message、duration 和 immediateClose，close 请求关闭，delayClose 通知延迟关闭流程；默认内容属性为 panel。

#### 使用场景

需要为 MessageManager 实现自定义消息委托时。


---

### AppLoader

#### 定位

QML 应用加载进度的场景项。

#### 功能能力总结

提供 window、loaded、progress 和 asynchronous 属性，反映 DAppLoader 的主组件加载状态并控制异步加载；与 DWindow 的加载覆盖层配合使用。

#### 使用场景

使用 DAppLoader 时，在预加载窗口中展示加载进度或覆盖层。


---
