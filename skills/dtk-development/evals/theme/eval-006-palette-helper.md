# 控件调色板助手

## 任务

为控件设置自定义颜色，要求：
1. 设置按钮背景色为指定颜色
2. 设置按钮文字颜色
3. 确保主题切换时颜色仍然正确

## 期望输出

代码应：
1. #include <DPaletteHelper>
2. DPaletteHelper::instance()->palette(widget) 获取调色板
3. palette.setColor() 设置颜色
4. DPaletteHelper::instance()->setPalette(widget, palette) 应用调色板
5. 未使用 QSS 替代 DPalette
6. 未使用绝对路径查找 DCI 图标
7. 未滥用 setDciThemeSearchPaths()

## 验证要点

- [ ] #include <DPaletteHelper>
- [ ] DPaletteHelper::instance()->palette(widget) 获取调色板
- [ ] palette.setColor() 设置颜色
- [ ] DPaletteHelper::instance()->setPalette(widget, palette) 应用调色板

## 参考

参见 [调色板助手](../../references/widgets/palette-helper.md) 了解 DPaletteHelper 的用法。

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未使用 QSS 替代 DPalette
- [ ] 未使用绝对路径查找 DCI 图标
- [ ] 未滥用 setDciThemeSearchPaths()
