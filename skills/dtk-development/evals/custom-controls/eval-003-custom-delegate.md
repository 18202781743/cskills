# 自定义列表委托

## 任务

实现列表项的自定义外观效果，要求：
1. 列表项有圆角背景
2. 选中时有高亮效果
3. hover 时有视觉反馈
4. 颜色随主题变化

## 期望输出

代码应：
1. 继承 DStyledItemDelegate
2. 使用 DStyleHelper::getColor() 获取颜色
3. 使用 DPaletteHelper 获取主题感知颜色
4. 或使用 DStandardItem 属性接口而非重写 paint()
5. 未从鼠标位置判断状态（应使用 QStyleOption::state）
6. initFrom() 后手动设置了 checked/down/selected 状态
7. 未使用 QSS 替代 DPalette/DStyle 绘制

## 验证要点

- [ ] 继承 DStyledItemDelegate
- [ ] 使用 DStyleHelper::getColor() 获取颜色
- [ ] 使用 DPaletteHelper 获取主题感知颜色
- [ ] 或使用 DStandardItem 属性接口而非重写 paint()

## 参考

参见 [列表项委托](../../references/widgets/item-delegate.md) 了解：
- DStyledItemDelegate 继承与自定义绘制
- DStandardItem 属性接口的使用方式
- 两种自定义方式的适用场景

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
