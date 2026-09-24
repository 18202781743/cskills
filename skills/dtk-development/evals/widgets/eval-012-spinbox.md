# Eval: 数值输入框

## 任务

创建一个整数输入框，要求：
1. 范围 0-100
2. 默认值 50
3. 步进值为 5

## 期望输出

代码应：
1. #include <DSpinBox>
2. setRange(0, 100)
3. setValue(50)
4. setSingleStep(5)
5. 未使用 QSS 硬编码颜色（应使用 DPalette）
6. 未使用 QApplication 替代 DApplication
7. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DSpinBox>
- [ ] setRange(0, 100)
- [ ] setValue(50)
- [ ] setSingleStep(5)

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
