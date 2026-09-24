# Eval: 搜索输入框

## 任务

创建一个搜索输入框，要求：
1. 包含清除按钮
2. 监听文本变化，实时搜索
3. 文本为空时禁用清除按钮

## 期望输出

代码应：
1. #include <DSearchEdit>
2. 连接 textChanged 信号
3. 使用 placeholderText 提示
4. 未使用 QSS 硬编码颜色（应使用 DPalette）
5. 未使用 QApplication 替代 DApplication
6. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DSearchEdit>
- [ ] 连接 textChanged 信号
- [ ] 使用 placeholderText 提示

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
