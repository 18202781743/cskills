# 列表项委托

## 任务

实现自定义列表项的外观效果，要求：
1. 列表项有圆角背景
2. 某些项使用特殊背景色（如警告状态）
3. 某些项的文字使用特殊颜色（如警告文本）
4. 列表项右侧添加操作按钮（如编辑、删除图标）
5. 列表项中嵌入自定义控件（如开关按钮）

## 期望输出

代码应：
1. 使用 DTK 提供的属性接口完成自定义，而非重写 paint()
2. 背景色、文字颜色、操作按钮均通过 DStandardItem/DViewItemAction 设置
3. 自定义控件通过 DViewItemAction::setWidget() 嵌入
4. 未使用 QSS 硬编码颜色（应使用 DPalette）
5. 未使用 QApplication 替代 DApplication
6. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] 使用 DTK 提供的属性接口完成自定义，而非重写 paint()
- [ ] 背景色、文字颜色、操作按钮均通过 DStandardItem/DViewItemAction 设置
- [ ] 自定义控件通过 DViewItemAction::setWidget() 嵌入

## 参考

参见 [列表项委托](../../references/widgets/item-delegate.md) 了解：
- DStandardItem 属性设置方法
- DViewItemAction 操作按钮添加方法
- 列表项自定义绘制与属性接口的选择

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未使用 QSS 硬编码颜色（应使用 DPalette）
- [ ] 未使用 QApplication 替代 DApplication
- [ ] 未手动 setFont 而不使用 DFontSizeManager::bind
