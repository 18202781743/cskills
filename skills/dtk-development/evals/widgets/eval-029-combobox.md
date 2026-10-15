# Eval: 下拉选择框

## 任务

创建下拉选择控件：
1. 添加选项
2. 设置默认选中
3. 监听选择变化

## 期望输出

代码应：
1. #include <DComboBox>
2. addItem() 或 addItems()
3. setCurrentIndex()
4. currentIndexChanged 信号
5. 未使用 QSS 硬编码颜色（应使用 DPalette）
6. 未使用 QApplication 替代 DApplication
7. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DComboBox>
- [ ] addItem() 或 addItems()
- [ ] setCurrentIndex()
- [ ] currentIndexChanged 信号

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
