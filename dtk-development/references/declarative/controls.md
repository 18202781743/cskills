# QML 控件

dtkdeclarative 对 Qt Quick Controls 进行 DTK 主题封装并提供自定义控件。

## 按分类查阅

| 分类 | 文档 | 控件 |
|------|------|------|
| 按钮 | [buttons.md](buttons.md) | Button, RecommandButton, WarningButton, ToolButton, IconButton, ActionButton, FloatingButton, DelayButton, RadioButton, CheckBox, Switch |
| 输入 | [inputs.md](inputs.md) | TextField, LineEdit, SearchEdit, PasswordEdit, SpinBox, PlusMinusSpinBox, IpV4LineEdit, KeySequenceEdit, ComboBox |
| 菜单 | [menus.md](menus.md) | Menu, MenuItem, MenuSeparator, ThemeMenu |
| 对话框与窗口 | [dialogs.md](dialogs.md) | ApplicationWindow, DialogWindow, DialogTitleBar, AboutDialog, TitleBar, WindowButtonGroup, Popup, ArrowShapePopup, FloatingMessage, AlertToolTip |
| 面板与视觉 | [panels.md](panels.md) | BoxPanel, ButtonPanel, ButtonBox, FloatingPanel, HighlightPanel, BoxShadow 等阴影边框组件 |
| 列表 | [lists.md](lists.md) | ItemDelegate, CheckDelegate, ArrowListView |
| 进度与滑动 | [progress.md](progress.md) | ProgressBar, EmbeddedProgressBar, WaterProgressBar, BusyIndicator, ScrollBar, Slider, TipsSlider |

以下 Qt Quick Controls 类型仅做简单 DTK 样式封装，与标准 Qt 用法一致，无需单独介绍：

`TabBar`, `TabButton`, `StackView`, `SwipeView`, `Drawer`, `Dialog`, `Frame`, `GroupBox`, `Pane`, `Dial`, `PageIndicator`, `ScrollView`, `ScrollIndicator`, `SwipeDelegate`, `AbstractButton`, `Container`, `Action`, `ActionGroup`, `ButtonGroup`, `Label`, `MenuBar`, `TextArea`

## 独立功能模块

| 文档 | 内容 |
|------|------|
| [color-selector.md](color-selector.md) | ColorSelector 取色器与 Palette 调色板 |
| [dci-icon.md](dci-icon.md) | QML 中使用 dci 图标 |
| [effects.md](effects.md) | InWindowBlur, BehindWindowBlur, GlowEffect, ColorOverlay, OpacityMask 等视觉效果 |

## 快速参考

所有样式封装控件均自动集成 `ColorSelector`（状态感知调色板）和 `DciIcon`（主题感知图标），支持 `import org.deepin.dtk 1.0`。

```qml
import org.deepin.dtk 1.0

ApplicationWindow {
    visible: true
    width: 800; height: 600

    Button {
        anchors.centerIn: parent
        text: "DTK 按钮"
        onClicked: console.log("clicked")
    }
}
```
