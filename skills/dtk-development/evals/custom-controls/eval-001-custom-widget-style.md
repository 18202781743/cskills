# 自定义控件风格

## 任务

为自定义控件实现主题感知，要求：
1. 控件背景随主题变化
2. 背景色使用语义化颜色（如项背景色）
3. 支持 hover 和 pressed 状态视觉反馈

## 期望输出

代码应：
1. 继承 QWidget 并实现 paintEvent
2. 使用 style()->drawPrimitive() 绘制背景
3. 使用 DStyle::PE_ItemBackground 图元
4. 使用 DPaletteHelper 获取主题感知颜色
5. 未从鼠标位置判断状态（应使用 QStyleOption::state）
6. initFrom() 后手动设置了 checked/down/selected 状态
7. 未使用 QSS 替代 DPalette/DStyle 绘制

## 验证要点

- [ ] 继承 QWidget 并实现 paintEvent
- [ ] 使用 style()->drawPrimitive() 绘制背景
- [ ] 使用 DStyle::PE_ItemBackground 图元
- [ ] 使用 DPaletteHelper 获取主题感知颜色

## 参考

参见 [样式系统](../../references/widgets/style.md) 了解自定义绘制的正确方式。

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
