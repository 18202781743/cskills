# Eval: 自定义控件主题感知

## 任务

创建一个主题感知的自定义控件：
1. 监听主题切换
2. 自动更新颜色
3. 支持调色板扩展

## 验证要点

- [ ] 连接 themeTypeChanged 信号
- [ ] 使用 DPalette::ColorType 获取颜色
- [ ] 在 paintEvent 中使用 DStyleHelper
