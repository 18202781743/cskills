# Eval: 自定义控件风格

## 任务

为自定义控件实现主题感知：
1. 使用 DStyle::drawPrimitive 绘制背景
2. 使用 DPaletteHelper 获取颜色
3. 支持 hover/pressed 状态

## 验证要点

- [ ] 继承 QWidget 并实现 paintEvent
- [ ] 使用 style()->drawPrimitive()
- [ ] 使用 DStyle::PE_ItemBackground
