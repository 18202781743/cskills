# 自定义控件主题感知

## 任务

创建一个主题感知的自定义控件，要求：
1. 系统主题切换时自动更新颜色
2. 使用语义化颜色（如文字颜色、背景颜色）
3. 支持自定义调色板扩展

## 期望输出

代码应：
1. 连接 DGuiApplicationHelper::themeTypeChanged 信号
2. 使用 DPalette::ColorType 获取语义颜色
3. 在 paintEvent 中使用 DStyleHelper 或 DPaletteHelper
4. 未从鼠标位置判断状态（应使用 QStyleOption::state）
5. initFrom() 后手动设置了 checked/down/selected 状态
6. 未使用 QSS 替代 DPalette/DStyle 绘制

## 验证要点

- [ ] 连接 DGuiApplicationHelper::themeTypeChanged 信号
- [ ] 使用 DPalette::ColorType 获取语义颜色
- [ ] 在 paintEvent 中使用 DStyleHelper 或 DPaletteHelper

## 参考

参见 [调色板规范](../../references/theme/palette.md) 了解主题感知的实现方式。

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
