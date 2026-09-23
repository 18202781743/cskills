# 自定义按钮

## 任务

创建一个自定义按钮控件，要求：
1. 按钮外观随主题变化
2. hover 时有高亮效果
3. pressed 时有按下效果
4. 支持键盘焦点

## 期望输出

代码应：
1. 继承 QAbstractButton
2. 重写 paintEvent 使用 style()->drawControl()
3. 处理 QStyle::State_MouseOver 状态
4. 处理 QStyle::State_Sunken 状态
5. 未从鼠标位置判断状态（应使用 QStyleOption::state）
6. initFrom() 后手动设置了 checked/down/selected 状态
7. 未使用 QSS 替代 DPalette/DStyle 绘制

## 验证要点

- [ ] 继承 QAbstractButton
- [ ] 重写 paintEvent 使用 style()->drawControl()
- [ ] 处理 QStyle::State_MouseOver 状态
- [ ] 处理 QStyle::State_Sunken 状态

## 参考

参见 [按钮规范](../../references/widgets/button.md) 了解 DTK 按钮的正确实现方式。

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未从鼠标位置判断状态（应使用 QStyleOption::state）
- [ ] initFrom() 后手动设置了 checked/down/selected 状态
- [ ] 未使用 QSS 替代 DPalette/DStyle 绘制
