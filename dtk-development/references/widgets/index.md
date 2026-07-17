# QWidget 控件概览

DTK 提供丰富的 QWidget 控件，本文档提供控件选择决策和核心 API 速查。

## 触发关键词

创建对话框/主窗口/按钮、控件选择、输入框/下拉框/开关按钮、列表视图/树形视图、进度条/滑动条/消息提示

## 控件选择决策树

```
需要什么类型的控件？
    │
    ├─ 对话框 → DDialog（简单交互）、DInputDialog（输入）、DFileDialog（文件选择）
    │
    ├─ 窗口 → DMainWindow（主窗口）、DTitlebar（标题栏）
    │
    ├─ 按钮 → 推荐样式？→ DSuggestButton
    │         警告样式？→ DWarningButton
    │         仅图标？→ DIconButton
    │         开关？→ DSwitchButton
    │         按钮组？→ DButtonBox
    │
    ├─ 输入 → DLineEdit（单行）、DSearchEdit（搜索）、DPasswordEdit（密码）
    │         DTextEdit（多行）、DSpinBox（数值）、DComboBox（下拉）
    │
    ├─ 视图 → DListView（列表）、DTreeView（树形）、DStyledItemDelegate（项委托）
    │
    └─ 其他 → DProgressBar（进度）、DSlider（滑动）、DMessageManager（消息）
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
| [style.md](style.md) | DStyle/ChameleonStyle 自定义绘制 |
