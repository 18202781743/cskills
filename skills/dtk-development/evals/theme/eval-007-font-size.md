# 字体大小层级

## 任务

使用系统字体大小层级，要求：
1. 获取指定层级的字体大小
2. 应用到标签控件
3. 监听系统字体变化并更新

## 期望输出

代码应：
1. #include <DFontSizeManager>
2. DFontSizeManager::instance()->t4() 获取字体
3. 或 bind(widget, SizeType) 绑定字体
4. 连接 fontChanged 信号监听变化
5. 未使用 QSS 替代 DPalette
6. 未使用绝对路径查找 DCI 图标
7. 未滥用 setDciThemeSearchPaths()

## 验证要点

- [ ] #include <DFontSizeManager>
- [ ] DFontSizeManager::instance()->t4() 获取字体
- [ ] 或 bind(widget, SizeType) 绑定字体
- [ ] 连接 fontChanged 信号监听变化

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
