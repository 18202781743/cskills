# Eval: 按钮组布局

## 任务

创建对话框底部的按钮组，要求：
1. 包含 "确定"（推荐样式）和 "取消" 按钮
2. 使用 DButtonBox 布局

## 期望输出

代码应：
1. #include <DButtonBox>
2. setButtonList() 设置按钮列表
3. 使用 DSuggestButton 作为推荐按钮
4. 未使用 QSS 硬编码颜色（应使用 DPalette）
5. 未使用 QApplication 替代 DApplication
6. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DButtonBox>
- [ ] setButtonList() 设置按钮列表
- [ ] 使用 DSuggestButton 作为推荐按钮

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
