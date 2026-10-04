# Eval: 列表视图

## 任务

创建一个列表视图，要求：
1. 显示 5 个列表项
2. 每项包含图标和文字
3. 支持选中状态

## 期望输出

代码应：
1. #include <DListView>
2. 使用 DStandardItem 设置项
3. setSelectionMode(QAbstractItemView::SingleSelection)
4. 未使用 QSS 硬编码颜色（应使用 DPalette）
5. 未使用 QApplication 替代 DApplication
6. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DListView>
- [ ] 使用 DStandardItem 设置项
- [ ] setSelectionMode(QAbstractItemView::SingleSelection)

## 参考

参见 [视图控件](../../references/widgets/view.md) 了解 DListView 的用法。

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
