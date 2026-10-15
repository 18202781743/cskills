# 使用 StyleOption

## 任务

在自定义绘制中正确使用 StyleOption，要求：
1. 初始化样式选项对象
2. 设置控件状态（hover、pressed、enabled 等）
3. 传递给样式系统进行绘制

## 期望输出

代码应：
1. 使用 initFrom() 初始化 QStyleOption
2. 设置 state 的 hover/pressed 等标志
3. 使用正确的 QStyle::ControlElement 或 PrimitiveElement
4. 未从鼠标位置判断状态（应使用 QStyleOption::state）
5. initFrom() 后手动设置了 checked/down/selected 状态
6. 未使用 QSS 替代 DPalette/DStyle 绘制

## 验证要点

- [ ] 使用 initFrom() 初始化 QStyleOption
- [ ] 设置 state 的 hover/pressed 等标志
- [ ] 使用正确的 QStyle::ControlElement 或 PrimitiveElement

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
