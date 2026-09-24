# Eval: 树形视图

## 任务

创建一个树形视图，要求：
1. 根节点 "项目"
2. 两个子节点 "模块1" 和 "模块2"
3. 展开/折叠功能

## 期望输出

代码应：
1. #include <DTreeView>
2. 使用 QStandardItemModel
3. expand()/collapse() 展开/折叠
4. 未使用 QSS 硬编码颜色（应使用 DPalette）
5. 未使用 QApplication 替代 DApplication
6. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DTreeView>
- [ ] 使用 QStandardItemModel
- [ ] expand()/collapse() 展开/折叠

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
