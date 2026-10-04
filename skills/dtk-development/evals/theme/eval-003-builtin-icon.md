# 内置图标

## 任务

使用系统内置图标，要求：
1. 查找一个常用图标（如"确定"图标）
2. 判断该图标是否为系统内置
3. 应用到按钮上

## 期望输出

代码应：
1. #include <DIconTheme>
2. DIconTheme::findQIcon("dialog-ok") 查找图标
3. DIconTheme::isBuiltinIcon() 判断是否内置
4. 未使用 QSS 替代 DPalette
5. 未使用绝对路径查找 DCI 图标
6. 未滥用 setDciThemeSearchPaths()

## 验证要点

- [ ] #include <DIconTheme>
- [ ] DIconTheme::findQIcon("dialog-ok") 查找图标
- [ ] DIconTheme::isBuiltinIcon() 判断是否内置

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
