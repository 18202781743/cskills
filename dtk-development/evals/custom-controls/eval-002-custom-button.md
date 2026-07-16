# Eval: 自定义按钮

## 任务

创建一个自定义按钮控件：
1. 继承 QAbstractButton
2. 使用 DStyle 绘制背景
3. 支持 hover/pressed 状态

## 验证要点

- [ ] 重写 paintEvent
- [ ] 使用 style()->drawControl()
- [ ] 处理 QStyle::State_MouseOver 状态
