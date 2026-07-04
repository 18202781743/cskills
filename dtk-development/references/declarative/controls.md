# QML 控件详细规范

## 1. 概述

dtkdeclarative 提供两类 QML 控件：
- **样式封装**（style-wrapper）：包装 Qt Quick Controls 控件，加入 DTK 主题样式、`ColorSelector` 状态感知和 `DciIcon` 图标系统
- **自定义控件**（custom）：DTK 特有的复合控件，提供对话框、浮动面板、搜索框等高级功能

所有控件通过 `import org.deepin.dtk 1.0` 或 `import org.deepin.dtk.controls 1.0` 引入。

---

## 2. 按钮类

### 2.1 Button

标准按钮，继承 `T.Button`，带渐变背景、阴影、内边框，通过 `ColorSelector` 自动跟随主题和状态。

```qml
Button {
    text: "确定"
    icon.source: "qrc:/icons/icon.dci"
    onClicked: console.log("clicked")
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `textColor` | `Palette` | 文本和图标颜色调色板 |

**注意事项：**
- `icon.name` 优先通过 `D.DTK.makeIcon()` 查找 dci 图标路径
- 禁用状态下自动设置 `opacity: 0.4`
- `contentItem` 使用 `D.IconLabel`，支持 `TextUnderIcon` 等显示模式

### 2.2 RecommandButton

推荐按钮（主操作按钮），继承 `Button`，固定 `highlighted: true`，使用高亮样式。

```qml
RecommandButton {
    text: "保存"
    highlighted: true
}
```

### 2.3 WarningButton

警告/危险操作按钮，继承 `Button`，文本调色板指向 `DS.Style.warningButton.text`（红色/橙色系）。

```qml
WarningButton {
    text: "删除"
}
```

### 2.4 ToolButton

工具栏按钮，继承 `T.ToolButton`。默认 `flat: true`、`display: TextUnderIcon`、使用 `CrystalColor` 颜色族。适合工具栏场景。

```qml
ToolButton {
    text: "工具"
    icon.name: "action_tool"
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `textColor` | `Palette` | 文本颜色调色板 |

### 2.5 IconButton

纯图标按钮，继承 `Button`。正方形、`contentItem` 直接使用 `D.DciIcon`。

```qml
IconButton {
    icon.name: "entry_clear"
}
```

### 2.6 ActionButton

透明图标按钮，继承 `T.Button`。无背景（`background: null`），仅在按下时显示文本颜色变化。适合输入框内的清除按钮等。

```qml
ActionButton {
    icon.name: "entry_clear"
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `textColor` | `Palette` | 图标颜色调色板 |

### 2.7 FloatingButton / RoundButton

圆形浮动按钮，继承 `Button`。不可复选，始终 `checked: true`，背景圆角为 `width/2`。

```qml
FloatingButton {
    icon.name: "action_add"
}
```

### 2.8 DelayButton

长按确认按钮，继承 `T.DelayButton`。按住时显示从左到右的进度动画，进度条颜色为 `palette.highlight`，释放后触发 `activated`。

```qml
DelayButton {
    text: "长按确认"
    delay: 1000  // 毫秒
    onActivated: console.log("confirmed")
}
```

### 2.9 RadioButton

单选按钮，继承 `T.RadioButton`。使用 dci 图标 `radio_checked`/`radio_unchecked` 作为指示器，聚焦时显示 `radio_focus`。

```qml
RadioButton {
    text: "选项A"
    checked: true
}
```

### 2.10 CheckBox

复选框，继承 `T.CheckBox`。使用 dci 图标 `checkbox_checked`/`checkbox_unchecked`/`checkbox_mix` 作为指示器，支持三态 `checkState`。

```qml
CheckBox {
    text: "启用"
    checkState: Qt.Checked
}
```

### 2.11 Switch

开关按钮，继承 `T.Switch`。带平滑动画的滑动开关，使用 `switch_button` dci 图标作为滑块。

```qml
Switch {
    text: "WiFi"
    checked: true
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `backgroundColor` | `Palette` | 轨道背景颜色 |
| `handleColor` | `Palette` | 滑块颜色 |

---

## 3. 输入类

### 3.1 TextField

文本输入框，继承 `T.TextField`。使用 `EditPanel` 背景，支持 alert 状态，内置右键菜单（复制/粘贴/全选等）。

```qml
TextField {
    placeholderText: "请输入..."
    onTextChanged: console.log(text)
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `placeholderTextColor` | `Palette` | 占位文本颜色 |
| `backgroundColor` | `Palette` | 背景颜色 |
| `alertText` | `string` | 警告文本 |
| `alertDuration` | `int` | 警告显示时长（ms） |
| `showAlert` | `bool` | 是否显示警告 |

**注意事项：** 禁用状态 opacity 0.4，自带右键上下文菜单。

### 3.2 LineEdit

带清除按钮的输入框，继承 `TextField`。输入内容后自动显示清除按钮。

```qml
LineEdit {
    placeholderText: "搜索..."
}
```

### 3.3 SearchEdit

搜索输入框，继承 `LineEdit`。未激活时在中央显示搜索图标和占位文本，激活后图标和焦点动画平滑移到左侧。

```qml
SearchEdit {
    placeholder: "搜索设置"
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `placeholder` | `string` | 未激活时显示的占位文本 |
| `editting` | `bool` | 是否处于编辑状态（只读） |

### 3.4 PasswordEdit

密码输入框，继承 `LineEdit`。带密码显隐切换按钮（`entry_password_shown`/`entry_password_hide` 图标）。

```qml
PasswordEdit {
    width: 200
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `isEchoMode` | `bool` | 当前是否明文显示（只读） |
| `echoButtonVisible` | `bool` | 是否显示切换按钮 |

### 3.5 TextArea

多行文本编辑区，继承 `T.TextArea`。使用 `EditPanel` 背景和 `PlaceholderText` 占位组件。

```qml
TextArea {
    placeholderText: "请输入内容..."
}
```

### 3.6 SpinBox

数字输入框，继承 `T.SpinBox`。使用 `EditPanel` 背景和 `SpinBoxIndicator` 上下箭头，支持 alert 状态。内置 `IntValidator`。

```qml
SpinBox {
    from: 0
    to: 100
    value: 50
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `alertText` / `alertDuration` / `showAlert` | — | Alert 状态控制 |

### 3.7 PlusMinusSpinBox

带加减重置按钮的 SpinBox，继承 `FocusScope`。左侧显示减号/复位按钮，中间 SpinBox，右侧加号按钮。

```qml
PlusMinusSpinBox {
    spinBox.from: 0
    spinBox.to: 100
    upButtonVisible: true
    downButtonVisible: true
    resetButtonVisible: true
}
```

### 3.8 IpV4LineEdit

IPv4 地址输入框，继承 `FocusScope`。4 个 0-255 的数字输入域，用点分隔。

```qml
IpV4LineEdit {
    text: "192.168.1.1"
}
```

### 3.9 KeySequenceEdit

快捷键编辑控件，继承 `Control`。捕获按键组合并以 `KeySequenceLabel` 显示。

```qml
KeySequenceEdit {
    placeholderText: "设置快捷键..."
    keys: ["Ctrl+Shift+T"]
}
```

### 3.10 ComboBox

下拉选择框，继承 `T.ComboBox`。支持图标（`iconNameRole`）、可编辑模式、alert 状态。弹窗使用 `FloatingPanel` + `ArrowListView`，委托使用 `MenuItem`。

```qml
ComboBox {
    model: ["选项1", "选项2", "选项3"]
    iconNameRole: "icon"
    currentIndex: 0
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `iconNameRole` | `string` | 模型中的图标名称字段 |
| `alertText` / `alertDuration` / `showAlert` | — | Alert 状态控制 |
| `maxVisibleItems` | `int` | 弹出列表最多可见项数 |
| `separatorColor` | `Palette` | 编辑模式下分隔符颜色 |

---

## 4. 菜单类

### 4.1 Menu

菜单，继承 `T.Menu`。使用 `FloatingPanel` 背景，`ArrowListView` 内容滚动，支持 `header`/`footer` 自定义组件。当父窗口失去激活时自动关闭。

```qml
Menu {
    model: ListModel {
        ListElement { text: "新建" }
        ListElement { text: "打开" }
    }
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `closeOnInactive` | `bool` | 是否在窗口失活时关闭（默认 true） |
| `maxVisibleItems` | `int` | 最多可见菜单项数 |
| `backgroundColor` | `Palette` | 背景颜色 |
| `header` / `footer` | `Component` | 头部/底部自定义组件 |

### 4.2 MenuItem

菜单项，继承 `T.MenuItem`。选中时显示 `menu_select` 勾选图标，子菜单项带 `menu_arrow` 箭头，hover/press 时 `HighlightPanel` 高亮。支持 `useIndicatorPadding` 为勾选图标留白。

```qml
MenuItem {
    text: "复制"
    icon.name: "action_copy"
    onTriggered: console.log("copy")
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `useIndicatorPadding` | `bool` | 是否为勾选指示器预留空间 |
| `textColor` | `Palette` | 文本颜色 |
| `subMenuBackgroundColor` | `Palette` | 子菜单打开时背景色 |

### 4.3 MenuSeparator

菜单分隔线，继承 `T.MenuSeparator`。支持带文本标题的分隔线。

```qml
MenuSeparator { }
MenuSeparator { text: "编辑" }
```

### 4.4 ThemeMenu

主题切换菜单，继承 `Menu`。内置亮色/暗色/系统三种主题选项，使用 `ActionGroup` 互斥。

```qml
ThemeMenu { }
```

---

## 5. 对话框与窗口类

### 5.1 DialogWindow

对话框窗口，继承 `Window`。`ColorSelector.family: CrystalColor`（水晶颜色族），禁用系统缩放，使用 `DialogType` 窗口类型。包含 `DialogTitleBar` 标题栏和内容区域。

```qml
DialogWindow {
    width: 400
    height: 300
    icon: "dialog-icon"
    header: DialogTitleBar { title: "设置" }
    ColumnLayout {
        // 对话框内容
    }
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `header` | `Component` | 自定义标题栏组件 |
| `icon` | `string` | 窗口图标 |
| `content` | 默认属性 | 对话框内容区域 |

### 5.2 DialogTitleBar

对话框标题栏，继承 `Control`。支持标题、图标、自定义内容，右键弹出系统窗口菜单，支持 `InWindowBlur` 模糊背景。

```qml
DialogTitleBar {
    title: "确认"
    icon.name: "app-icon"
}
```

### 5.3 AboutDialog

关于对话框，继承 `DialogWindow`。显示产品名称、版本、描述、公司标志、网站链接、许可证信息。

```qml
AboutDialog {
    productName: "我的应用"
    version: "1.0.0"
    description: "这是一个示例应用"
    companyLogo: "company-logo"
    websiteName: "官方网站"
    websiteLink: "https://example.com"
}
```

### 5.4 ApplicationWindow

应用主窗口，继承 `T.ApplicationWindow`。自动设置 DTK 调色板和默认字体，是 QML 应用的根窗口。

```qml
ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "My App"
}
```

### 5.5 TitleBar

应用标题栏，继承 `Control`。包含应用图标、标题、左右内容区、选项菜单（主题/帮助/关于/退出）、窗口控制按钮组。支持双击切换最大化、右键弹出系统菜单、全屏自动隐藏。

```qml
ApplicationWindow {
    TitleBar {
        title: "My App"
        icon.name: "app-icon"
        fullScreenButtonVisible: true
        autoHideOnFullscreen: true
        leftContent: RowLayout { /* 自定义左侧控件 */ }
        content: Label { text: "自定义标题" }
    }
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `title` | `string` | 标题文本 |
| `icon` | 别名 | 图标 DciIcon 组件 |
| `leftContent` | `Component` | 左侧自定义组件 |
| `content` | `Component` | 中央自定义组件 |
| `menu` | `Component` | 选项菜单组件 |
| `menuDisabled` | `bool` | 禁用选项菜单 |
| `aboutDialog` | `Component` | 关于对话框组件 |
| `fullScreenButtonVisible` | `bool` | 是否显示全屏按钮 |
| `autoHideOnFullscreen` | `bool` | 全屏时自动隐藏 |
| `separatorVisible` | `bool` | 是否显示底部分隔线 |
| `enableInWindowBlendBlur` | `bool` | 是否启用窗口内模糊 |

### 5.6 WindowButtonGroup

窗口按钮组，继承 `RowLayout`。包含最小化/退出全屏/最大化/关闭按钮，自动根据窗口状态切换图标。检测 `FUNC_RESIZE` 等 motif 装饰来决定按钮可用性。

```qml
WindowButtonGroup {
    textColor: Palette { normal: "white" }
    fullScreenButtonVisible: true
}
```

### 5.7 WindowButton

单个窗口控制按钮，继承 `Control`。使用 dci 图标，hover 时显示彩色背景。

### 5.8 Popup

弹出层，继承 `T.Popup`。使用 `FloatingPanel` 背景，当父窗口失去激活时自动关闭。

```qml
Popup {
    width: 200
    height: 100
    closeOnInactive: true
}
```

### 5.9 ArrowShapePopup

带箭头弹出层，继承 `Popup`。使用 `ArrowBoxPath` 裁剪形状指向目标控件，带内窗口模糊和阴影。

```qml
ArrowShapePopup {
    arrowDirection: ArrowBoxPath.Down
    arrowX: 100
    arrowY: 0
}
```

### 5.10 FloatingMessage

浮动消息（Toast），继承 `C++ FloatingMessageContainer`。显示图标+文本+关闭按钮，默认 4 秒自动消失。

```qml
FloatingMessage {
    icon: "dialog-warning"
    message: "操作成功"
}
```

### 5.11 AlertToolTip

警告提示框，继承 `ToolTip`。红色文本、带三角箭头指向目标控件，显示时带动画过渡，不自动关闭。

```qml
AlertToolTip {
    text: "密码不能为空"
    target: passwordField
    visible: true
}
```

---

## 6. 面板与容器类

### 6.1 BoxPanel

盒模型背景面板，组合了渐变背景、外阴影（`BoxShadow`）、内阴影 x2（`BoxInsetShadow`）、内边框（`InsideBoxBorder`）、外边框（`OutsideBoxBorder`）。是 DTK 按钮/面板的核心背景组件。

| 属性 | 类型 | 说明 |
|------|------|------|
| `radius` | `int` | 圆角半径 |
| `color1` / `color2` | `Palette` | 渐变背景颜色 |
| `insideBorderColor` / `outsideBorderColor` | `Palette` | 内外边框颜色 |
| `dropShadowColor` | `Palette` | 外阴影颜色 |
| `innerShadowColor1` / `innerShadowColor2` | `Palette` | 内阴影颜色 |
| `boxShadowBlur` / `boxShadowOffsetY` | `int` | 阴影模糊和偏移 |
| `backgroundFlowsHovered` | `bool` | hover 状态是否影响背景渐变（默认 true） |

### 6.2 ButtonPanel

按钮面板，继承 `BoxPanel`。根据 `checked`/`highlighted` 状态自动切换调色板源，按下时减少阴影，hover 时启动 `CicleSpreadAnimation` 圆形扩散动画。

```qml
ButtonPanel {
    button: parentButton
    radius: 8
}
```

### 6.3 ButtonBox

按钮组容器，继承 `Control`。将多个按钮放在 `RowLayout` 中，使用 `ButtonPanel` 统一背景。

```qml
ButtonBox {
    Button { text: "左"; checkable: true }
    Button { text: "中"; checkable: true }
    Button { text: "右"; checkable: true }
}
```

### 6.4 FloatingPanel

浮动面板，继承 `Control`。半透明模糊背景（`InWindowBlur`）+ 外阴影（`BoxShadow`）+ 圆角剪切（`ItemViewport`）+ 内外边框。用于 Popup/Menu/ToolTip 背景。

```qml
FloatingPanel {
    radius: 12
    blurRadius: 12
    backgroundColor: Palette { normal: Qt.rgba(1, 1, 1, 0.8) }
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `backgroundColor` | `Palette` | 背景颜色 |
| `dropShadowColor` | `Palette` | 阴影颜色 |
| `outsideBorderColor` / `insideBorderColor` | `Palette` | 内外边框颜色 |
| `radius` | `int` | 圆角半径 |
| `blurRadius` | `int` | 模糊半径 |

### 6.5 HighlightPanel

高亮选中面板，组合高亮色矩形 + 外阴影 + 内阴影。用于 MenuItem 和 ItemDelegate 的选中背景。

```qml
HighlightPanel {
    anchors.fill: parent
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `backgroundColor` | `Palette` | 高亮背景颜色 |
| `outerShadowColor` / `innerShadowColor` | `Palette` | 外/内阴影颜色 |

### 6.6 Frame

框架容器，继承 `T.Frame`。透明背景，`palette.mid` 颜色边框。

```qml
Frame {
    radius: 8
    Rectangle { /* 内容 */ }
}
```

### 6.7 GroupBox

分组框，继承 `T.GroupBox`。带标题标签的分组容器。

```qml
GroupBox {
    title: "常规设置"
    ColumnLayout { /* 内容 */ }
}
```

### 6.8 Pane

面板，继承 `T.Pane`。基本容器，DTK 风格内边距。

### 6.9 ControlBackground

控件背景，一个带 `FocusBoxBorder` 的透明 `Rectangle`。在控件获得焦点时显示高亮边框。

---

## 7. 列表类

### 7.1 ItemDelegate

列表项委托，继承 `T.ItemDelegate`。支持选中高亮（`HighlightPanel`）、级联选中（`RoundRectangle`）、勾选指示器（`menu_select` 图标）、自定义内容组件、四角独立控制。

```qml
ListView {
    model: 10
    delegate: ItemDelegate {
        text: "列表项 " + index
        checked: index === currentIndex
        indicatorVisible: true
        backgroundVisible: true
    }
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `indicatorVisible` | `bool` | 是否显示勾选指示器 |
| `backgroundVisible` | `bool` | 是否显示背景（默认 true） |
| `cascadeSelected` | `bool` | 级联选中样式 |
| `contentFlow` | `bool` | 内容是否填充剩余空间 |
| `content` | `Component` | 自定义内容组件 |
| `checkedTextColor` | `Palette` | 选中时文本颜色 |
| `corners` | `int` | 四角控制位掩码 |

### 7.2 CheckDelegate

可勾选委托，继承 `T.CheckDelegate`。带 `menu_select` 勾选指示器。

```qml
ListView {
    model: ListModel { ListElement { name: "Apple" } }
    delegate: CheckDelegate {
        text: model.name
        checked: model.checked
    }
}
```

### 7.3 SwipeDelegate

可滑动委托，继承 `QtQuick.Controls SwipeDelegate`。支持左右滑动操作。

### 7.4 ArrowListView

带箭头按钮的列表视图，继承 `FocusScope`。当内容超过可见区时，显示上下箭头用于滚动导航。用于 Menu/ComboBox 弹出内容。

```qml
ArrowListView {
    maxVisibleItems: 6
    itemHeight: 30
    view.model: myModel
}
```

---

## 8. 滚动与进度类

### 8.1 ScrollView

滚动视图，继承 `T.ScrollView`。自动绑定 DTK `ScrollBar` 为水平和垂直滚动条。

```qml
ScrollView {
    width: 400; height: 300
    ListView { /* 内容 */ }
}
```

### 8.2 ScrollBar

滚动条，继承 `T.ScrollBar`。4 种状态动画过渡：hide（窄条 + 渐变透明）→ normal（窄条）→ hover（宽条）→ active（按下宽条），带内外边框。

| 状态 | 宽度 | 说明 |
|------|------|------|
| hide | 窄 | 不活动或内容未超出时渐变透明 |
| normal | 窄 | 滚动时显示 |
| hover | 宽 | 鼠标悬停 |
| active | 宽 | 拖动中 |

### 8.3 ProgressBar

进度条，继承 `T.ProgressBar`。使用内部 `ProgressBarImpl` 和 `ProgressBarPanel` 渲染。

```qml
ProgressBar {
    from: 0; to: 100
    value: 75
    formatText: "%p%"
}
```

### 8.4 EmbeddedProgressBar

嵌入式小进度条，继承 `T.ProgressBar`。默认 48x6 尺寸，适合在列表项或小块区域使用。

### 8.5 WaterProgressBar

水波进度条，继承 `Control`。使用 `WaterProgressAttribute` C++ 类型驱动水波动画，带气泡弹出效果和 `ItemViewport` 圆角裁剪。

```qml
WaterProgressBar {
    value: 60
    running: true
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `value` | `real` | 进度值 0-100 |
| `running` | `bool` | 是否运行动画 |
| `backgroundColor1` / `backgroundColor2` | `Palette` | 背景渐变色 |
| `dropShadowColor` / `popBackgroundColor` / `textColor` | `Palette` | 阴影/气泡/文字颜色 |

### 8.6 BusyIndicator

加载指示器，继承 `T.BusyIndicator`。使用 webp 动画 spinner 图片，通过 `D.ColorOverlay` 叠加主题色，无限旋转动画。

```qml
BusyIndicator {
    running: true
    fillColor: Palette { normal: "blue" }
}
```

---

## 9. 滑动与刻度类

### 9.1 Slider

滑块，继承 `T.Slider`。使用 `ShapePath` 绘制虚线滑槽，支持 6 种把手类型（`HandleType` 枚举），可选高亮已通过区域。

```qml
Slider {
    from: 0; to: 100
    value: 50
    handleType: Slider.ArrowUp
    highlightedPassedGroove: true
    dashPattern: [0.5, 0.25]
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `grooveColor` | `Palette` | 滑槽颜色 |
| `handleType` | `enum` | 把手方向类型 |
| `dashOffset` / `dashPattern` | `real` / `var` | 虚线偏移和模式 |
| `highlightedPassedGroove` | `bool` | 高亮已通过区域 |

**HandleType 枚举：** `NoArrowHorizontal` / `NoArrowVertical` / `ArrowUp` / `ArrowLeft` / `ArrowBottom` / `ArrowRight`

### 9.2 TipsSlider

带刻度标签的滑块，继承 `Control`。内置 `Slider` + `Grid` 排列的 `SliderTipItem` 刻度，可控制刻度在滑块前/后端。

```qml
TipsSlider {
    slider.value: 50
    tickDirection: TipsSlider.Front
    SliderTipItem { text: "0" }
    SliderTipItem { text: "50" }
    SliderTipItem { text: "100" }
}
```

### 9.3 Dial

旋钮，继承 `T.Dial`。使用 DTK 高亮色和自定义手柄矩形。

---

## 10. 导航类

### 10.1 TabBar

标签栏，负责提供标签切换。通常与 `StackView` 配合使用。

```qml
TabBar {
    id: tabBar
    TabButton { text: "常规" }
    TabButton { text: "高级" }
    onCurrentIndexChanged: stackView.currentIndex = currentIndex
}
```

### 10.2 StackView

页面堆栈，继承 `T.StackView`。带 push/pop/replace 滑入滑出动画，配置持续时间和缓动曲线。

```qml
StackView {
    id: stackView
    currentIndex: tabBar.currentIndex
    Item { /* 常规页 */ }
    Item { /* 高级页 */ }
}
```

### 10.3 SwipeView

可滑动页面容器，继承 `QtQuick.Controls SwipeView`。

### 10.4 PageIndicator

页面指示器（圆点），继承 `T.PageIndicator`。选中项使用高亮色，带透明度动画过渡。

---

## 11. 视觉效果类

### 11.1 BoxShadow

外阴影组件，通过 `D.DTK.makeShadowImageUrl()` 生成阴影图片，使用 `BorderImage` 九宫格渲染。

```qml
BoxShadow {
    anchors.fill: parent
    shadowBlur: 10
    shadowOffsetY: 4
    shadowColor: "#20000000"
    cornerRadius: 8
    hollow: true
}
```

| 属性 | 类型 | 说明 |
|------|------|------|
| `shadowBlur` | `int` | 模糊半径 |
| `shadowOffsetX` / `shadowOffsetY` | `int` | 阴影偏移 |
| `shadowColor` | `color` | 阴影颜色 |
| `cornerRadius` | `int` | 圆角 |
| `topLeftRadius` ... `bottomRightRadius` | `int` | 四角独立半径 |
| `spread` | `int` | 扩散 |
| `hollow` | `bool` | 是否中空（镂空阴影） |

### 11.2 BoxInsetShadow

内阴影组件，参数同 `BoxShadow`，`inset: true`。

### 11.3 RectangularShadow

矩形光晕阴影，基于 `GlowEffect` 实现。

### 11.4 InsideBoxBorder / OutsideBoxBorder

内外边框组件。使用半像素 `Rectangle` 绘制边框，`InsideBoxBorder` 向内收缩，`OutsideBoxBorder` 向外扩展。

```qml
InsideBoxBorder {
    radius: 8
    color: "#10000000"
    borderWidth: 1
}
```

### 11.5 FocusBoxBorder

焦点指示边框，继承 `Item`。使用镂空 `BoxShadow` 实现发光焦点环。

```qml
FocusBoxBorder {
    color: control.palette.highlight
    radius: 8
    borderWidth: 2
}
```

### 11.6 CicleSpreadAnimation

圆形扩散动画，继承 `Item`。从指定中心点向外扩散的遮罩动画。

```qml
CicleSpreadAnimation {
    centerPoint: Qt.point(mouse.x, mouse.y)
    // start() / stop()
}
```

### 11.7 StyledBehindWindowBlur

窗口背景模糊，继承 `C++ BehindWindowBlur`。根据主题（亮/暗/不模糊）自动调整混合颜色。

---

## 12. C++ 注册的独立 QML 类型

以下类型由 C++ 类注册，提供底层能力。

### 12.1 DciIcon

dci 图标组件，继承 `QQuickItem`。支持主题感知、状态感知、调色板控制。

```qml
D.DciIcon {
    name: "action_search"
    mode: D.DTK.HoveredState
    theme: D.DTK.DarkType
    palette: D.DTK.makeIconPalette(control.palette)
    sourceSize: Qt.size(24, 24)
}
```

### 12.2 QtIcon

标准 QIcon 组件，继承 `QQuickImage`。支持 mode（Normal/Disabled/Active/Selected）、state（On/Off）。

```qml
D.QtIcon {
    name: "edit-copy"
    mode: D.QtIcon.Normal
    color: "black"
}
```

### 12.3 IconLabel

图标+文本标签，支持 5 种布局模式：`IconOnly`、`TextOnly`、`TextBesideIcon`、`TextUnderIcon`、`IconBesideText`。

```qml
D.IconLabel {
    text: "搜索"
    icon: D.DTK.makeIcon(control.icon, control.D.DciIcon)
    display: D.IconLabel.TextUnderIcon
    spacing: 4
}
```

### 12.4 RoundRectangle

圆角矩形，支持四角独立控制。

```qml
D.RoundRectangle {
    color: "red"
    radius: 8
    corners: D.RoundRectangle.TopLeftCorner | D.RoundRectangle.TopRightCorner
}
```

### 12.5 ArrowBoxPath

箭头形状路径，用于 `ShapePath.path`。支持上下左右四个方向和箭头尺寸/位置/圆角。

```qml
ShapePath {
    strokeColor: "white"
    fillColor: "transparent"
    path: ArrowBoxPath {
        width: 200; height: 100
        arrowDirection: ArrowBoxPath.Down
        arrowX: 100; arrowY: 0
        arrowWidth: 20; arrowHeight: 10
        roundedRadius: 8
    }
}
```

### 12.6 InWindowBlur

窗口内模糊，位于此组件下的子元素被模糊渲染。

```qml
D.InWindowBlur {
    radius: 20
    offscreen: true
    Rectangle { /* 被模糊的内容 */ }
}
```

### 12.7 BehindWindowBlur

窗口后模糊，显示窗口下方内容的模糊效果。

```qml
D.BehindWindowBlur {
    cornerRadius: 0
    blendColor: "#80ffffff"
}
```

### 12.8 GlowEffect

光晕效果，对源项添加外围光晕。

```qml
D.GlowEffect {
    glowRadius: 10
    color: "blue"
    spread: 0.2
    fill: false
}
```

### 12.9 ColorOverlay / OpacityMask

颜色叠加和透明度遮罩效果。

```qml
D.SoftwareColorOverlay {
    source: someItem
    color: "red"
}
D.SoftwareOpacityMask {
    source: someItem
    maskSource: maskItem
    invert: false
}
```

### 12.10 ItemViewport

圆角裁剪视口，将 `sourceItem` 按指定半径裁剪。

```qml
D.ItemViewport {
    sourceItem: parent
    radius: 12
    fixed: true
    hideSource: false
}
```

### 12.11 BackdropBlitter

截取并重绘窗口背景内容。

### 12.12 WaterProgressAttribute

水波进度驱动（C++ 实现），控制水波动画的波浪偏移和气泡属性。

### 12.13 Config

DConfig 配置访问。绑定 DConfig key 到 QML 属性。

```qml
D.Config {
    id: config
    name: "my-app"
    property string theme: config.value("theme", "light")
}
```

### 12.14 KeySequenceListener

快捷键监听器。监听目标控件上的特定按键组合。

```qml
D.KeySequenceListener {
    target: someItem
    keys: ["Ctrl+S"]
}
```

### 12.15 FloatingMessageContainer

浮动消息容器（C++ 实现），管理 Toast 消息的显示和关闭。

---

## 13. Action 系统

### 13.1 Action / ActionGroup

标准 Qt Quick Controls Action 封装。

### 13.2 AboutAction / HelpAction / QuitAction

预置菜单动作。`AboutAction` 自动弹出 `AboutDialog`，`HelpAction` 调用 `D.ApplicationHelper.handleHelpAction()`，`QuitAction` 调用 `Qt.quit()`。

```qml
Menu {
    AboutAction { aboutDialog: aboutComponent }
    HelpAction { }
    QuitAction { }
}
```

---

## 14. SortFilterModel

排序过滤代理模型。对 `DelegateModel` 中的项进行排序和过滤。

```qml
SortFilterModel {
    model: myDelegateModel
    filterAcceptsItem: function(item) {
        return item.visible
    }
    lessThan: function(left, right) {
        return left.x < right.x
    }
}
```

## 15. 相关文档

- [index.md](index.md) — QML 控件选择决策树
- [color-selector.md](color-selector.md) — ColorSelector 取色器与 Palette 调色板
- [dci-icon.md](dci-icon.md) — QML 中使用 dci 图标
- [effects.md](effects.md) — QML 效果组件
