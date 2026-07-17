# 自定义列表委托

## 任务

创建自定义列表项样式，要求：
1. 列表项有圆角背景
2. 选中时有高亮效果
3. hover 时有视觉反馈
4. 颜色随主题变化

## 验证要点

- [ ] 继承 DStyledItemDelegate
- [ ] 使用 DStyleHelper::getColor() 获取颜色
- [ ] 使用 DPaletteHelper 获取主题感知颜色
- [ ] 或使用 DStandardItem 属性接口而非重写 paint()
