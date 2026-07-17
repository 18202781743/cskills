# QWidget 控件选择决策树

## 触发关键词

创建对话框/主窗口/按钮、控件选择、输入框/下拉框/开关按钮、列表视图/树形视图、进度条/滑动条/消息提示

## 快速决策树

```
需要什么类型的控件？
    │
    ├─ 对话框 → DDialog / DInputDialog / DFileDialog
    ├─ 窗口 → DMainWindow / DTitlebar
    ├─ 按钮 → DSuggestButton / DWarningButton / DIconButton / DSwitchButton
    ├─ 输入 → DLineEdit / DSearchEdit / DPasswordEdit / DSpinBox
    ├─ 视图 → DListView / DTreeView / DStyledItemDelegate
    └─ 其他 → DProgressBar / DSlider / DMessageManager
```

## 详细文档

| 文档 | 内容 |
|------|------|
| [button.md](button.md) | 按钮类型、DCI 图标、颜色定制 |
| [dialog.md](dialog.md) | DDialog/DInputDialog/DFileDialog |
| [input.md](input.md) | DLineEdit/DSearchEdit/DPasswordEdit |
| [window.md](window.md) | DMainWindow/DTitlebar |
| [item-delegate.md](item-delegate.md) | DStyledItemDelegate 列表项 |
| [blur-effect.md](blur-effect.md) | DBlurEffectWidget |
| [style.md](style.md) | DStyle 控件绘制指南 |
| [chameleon.md](chameleon.md) | QWidget Chameleon 风格 |
