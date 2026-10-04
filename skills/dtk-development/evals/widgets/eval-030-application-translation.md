# Eval: 应用身份与翻译加载

## 任务

为 DTK 应用配置应用身份和中文翻译，要求：
1. `applicationName` 与可执行文件名一致
2. 在创建窗口前加载翻译
3. 翻译文件 basename 与 `applicationName` 一致
4. `px` 作为专业单位不进入翻译

## 期望输出

代码应：
1. 设置了与可执行文件一致的 `applicationName`
2. `DApplication::loadTranslator()` 位于 UI 创建之前
3. 未将应用显示名称、应用 ID 和单实例 key 混为一个值
4. 使用 `QStringLiteral("px")`，而不是 `tr("px")`
5. 未使用 QSS 硬编码颜色（应使用 DPalette）
6. 未使用 QApplication 替代 DApplication
7. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] 设置了与可执行文件一致的 `applicationName`
- [ ] `DApplication::loadTranslator()` 位于 UI 创建之前
- [ ] 未将应用显示名称、应用 ID 和单实例 key 混为一个值
- [ ] 使用 `QStringLiteral("px")`，而不是 `tr("px")`

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
