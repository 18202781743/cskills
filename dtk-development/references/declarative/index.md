# QML 控件概览

dtkdeclarative 对 Qt Quick Controls 进行 DTK 主题封装，用于 DDE Shell 插件和 QML 应用。

## 触发关键词

QML 按钮/对话框/输入框、QML 菜单/列表/进度条、org.deepin.dtk、DTK QML 控件

## 控件选择决策树

```
需要什么类型的 QML 控件？
    │
    ├─ 窗口 → ApplicationWindow / DialogWindow
    ├─ 按钮 → Button / RecommandButton / WarningButton / IconButton
    ├─ 选择 → CheckBox / RadioButton / Switch
    ├─ 输入 → TextField / LineEdit / SearchEdit / PasswordEdit / SpinBox
    ├─ 菜单 → Menu / MenuItem / ThemeMenu
    ├─ 对话框 → DialogWindow / AboutDialog
    ├─ 列表 → ItemDelegate / CheckDelegate
    ├─ 进度 → ProgressBar / WaterProgressBar
    └─ 滑动 → Slider / TipsSlider
```


## 详细文档

| 文档 | 内容 |
|------|------|
| [color-selector.md](color-selector.md) | Palette/ColorSelector 取色器 |
| [dci-icon.md](dci-icon.md) | QML 中使用 dci 图标 |
| [dtk-global.md](dtk-global.md) | D.DTK 全局对象 |
| [dialogs.md](dialogs.md) | DialogWindow/AboutDialog |
