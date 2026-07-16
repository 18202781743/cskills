# Eval: 控件调色板助手

## 任务

使用 DPaletteHelper 设置控件颜色：
1. 设置按钮背景色为 #FF6600
2. 设置按钮前景色为白色
3. 确保主题切换时颜色正确

## 验证要点

- [ ] #include <DPaletteHelper>
- [ ] DPaletteHelper::instance()->palette(widget)
- [ ] palette.setColor(QPalette::Button, QColor("#FF6600"))
- [ ] DPaletteHelper::instance()->setPalette(widget, palette)
