# 手动切换主题

## 任务

手动切换应用主题，要求：
1. 当前为亮色主题时切换到暗色
2. 当前为暗色主题时切换到亮色

## 期望输出

代码应：
1. #include <DGuiApplicationHelper>
2. themeType() 获取当前主题
3. setPaletteType() 设置主题
4. 未使用 QSS 替代 DPalette
5. 未使用绝对路径查找 DCI 图标
6. 未滥用 setDciThemeSearchPaths()

## 验证要点

- [ ] #include <DGuiApplicationHelper>
- [ ] themeType() 获取当前主题
- [ ] setPaletteType() 设置主题

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
