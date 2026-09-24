# Eval: 窗口模糊效果

## 任务

创建一个带模糊背景的窗口，要求：
1. 使用 DBlurEffectWidget
2. 模糊区域覆盖整个窗口
3. 圆角 10px

## 期望输出

代码应：
1. #include <DBlurEffectWidget>
2. setBlendMode(DBlurEffectWidget::BehindWindowBlend)
3. setRadius(10)
4. 未使用 QSS 硬编码颜色（应使用 DPalette）
5. 未使用 QApplication 替代 DApplication
6. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DBlurEffectWidget>
- [ ] setBlendMode(DBlurEffectWidget::BehindWindowBlend)
- [ ] setRadius(10)

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
