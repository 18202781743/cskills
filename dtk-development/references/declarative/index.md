# QML 控件

## 1. 概述

dtkdeclarative 对 Qt Quick Controls 进行 DTK 主题封装并提供自定义控件，用于 Qt Quick 应用。

**适用场景：** DDE Shell 插件、QML 应用、需要动态 UI 的场景。

**CMake 依赖（仅当使用 dtkdeclarative 的 C++ API 时需要）：** 详见 [app-dev-with-dtk.md](../app-dev-with-dtk.md)

```cmake
find_package(Dtk6Declarative REQUIRED)
target_link_libraries(your_target Dtk6::Declarative)
```

纯 QML 应用通过 `import org.deepin.dtk 1.0` 即可。

## 2. 快速决策树

```
需要什么类型的 QML 控件？
    │
    ├─ 窗口 → ApplicationWindow / DialogWindow
    │
    ├─ 按钮 → Button / RecommandButton / WarningButton / FloatingButton / DelayButton
    │
    ├─ 图标按钮 → ToolButton / IconButton / ActionButton
    │
    ├─ 选择 → CheckBox / RadioButton / Switch
    │
    ├─ 输入 → TextField / LineEdit / SearchEdit / PasswordEdit / SpinBox / ComboBox
    │
    ├─ 高级输入 → IpV4LineEdit / KeySequenceEdit / PlusMinusSpinBox
    │
    ├─ 菜单 → Menu / MenuItem / ThemeMenu
    │
    ├─ 对话框 → DialogWindow / AboutDialog / Popup / ArrowShapePopup
    │
    ├─ 消息 → FloatingMessage / AlertToolTip / ToolTip
    │
    ├─ 标题栏 → TitleBar / DialogTitleBar
    │
    ├─ 列表 → ItemDelegate / CheckDelegate
    │
    ├─ 进度 → ProgressBar / WaterProgressBar / BusyIndicator
    │
    ├─ 滑动 → Slider / TipsSlider / ScrollBar
    │
    └─ 面板 → BoxPanel / FloatingPanel / HighlightPanel / Frame
```

## 3. 按分类查阅

| 分类 | 文档 | 控件 |
|------|------|------|
| 按钮 | [buttons.md](buttons.md) | Button, RecommandButton, WarningButton, ToolButton, IconButton, ActionButton, FloatingButton, DelayButton, RadioButton, CheckBox, Switch |
| 输入 | [inputs.md](inputs.md) | TextField, LineEdit, SearchEdit, PasswordEdit, SpinBox, PlusMinusSpinBox, IpV4LineEdit, KeySequenceEdit, ComboBox |
| 菜单 | [menus.md](menus.md) | Menu, MenuItem, MenuSeparator, ThemeMenu |
| 对话框与窗口 | [dialogs.md](dialogs.md) | ApplicationWindow, DialogWindow, DialogTitleBar, AboutDialog, TitleBar, WindowButtonGroup, Popup, ArrowShapePopup, FloatingMessage, AlertToolTip |
| 面板与视觉 | [panels.md](panels.md) | BoxPanel, ButtonPanel, ButtonBox, FloatingPanel, HighlightPanel, BoxShadow 等阴影边框组件 |
| 列表 | [lists.md](lists.md) | ItemDelegate, CheckDelegate, ArrowListView |
| 进度与滑动 | [progress.md](progress.md) | ProgressBar, EmbeddedProgressBar, WaterProgressBar, BusyIndicator, ScrollBar, Slider, TipsSlider |

以下 Qt Quick Controls 类型仅做简单 DTK 样式封装，与标准 Qt 用法一致：

`TabBar`, `TabButton`, `StackView`, `SwipeView`, `Drawer`, `Dialog`, `Frame`, `GroupBox`, `Pane`, `Dial`, `PageIndicator`, `ScrollView`, `ScrollIndicator`, `SwipeDelegate`, `AbstractButton`, `Container`, `Action`, `ActionGroup`, `ButtonGroup`, `Label`, `MenuBar`, `TextArea`

## 4. 代码模板

```qml
import org.deepin.dtk 1.0

ApplicationWindow {
    visible: true
    width: 800; height: 600
    title: "My App"

    Button {
        anchors.centerIn: parent
        text: "DTK 按钮"
        onClicked: console.log("clicked")
    }
}
```

## 5. 相关文档

- [color-selector.md](color-selector.md) — ColorSelector 取色器与 Palette 调色板
- [dci-icon.md](dci-icon.md) — QML 中使用 dci 图标
- [effects.md](effects.md) — QML 视觉效果（模糊/光晕/叠加/遮罩）
- [dtk-global.md](dtk-global.md) — D.DTK 全局对象（字体/主题/颜色）
- [dwindow.md](dwindow.md) — D.DWindow 窗口附加属性
