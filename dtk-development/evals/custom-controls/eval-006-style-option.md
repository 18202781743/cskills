# Eval: 使用 StyleOption

## 任务

在自定义绘制中正确使用 StyleOption：
1. 创建 QStyleOption 对象
2. 初始化状态和属性
3. 传递给 style()->drawXXX()

## 验证要点

- [ ] 使用 initFrom() 初始化
- [ ] 设置 state 的 hover/pressed 等标志
- [ ] 使用正确的 QStyle::ControlElement
