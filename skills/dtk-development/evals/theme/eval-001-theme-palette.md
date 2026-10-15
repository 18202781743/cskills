# 控件颜色跟随主题切换

## 任务

创建一个自定义标签，要求：
1. 背景色使用项背景色语义
2. 文字颜色使用标题文字颜色语义
3. 当系统主题切换时自动更新颜色

## 期望输出

代码应：
1. 使用 #include <DPalette> 和 #include <DGuiApplicationHelper>
2. 连接 themeTypeChanged 信号监听主题变化
3. 使用 DPalette::ItemBackground 获取背景色
4. 使用 DPalette::TextTitle 获取文字颜色
5. 未使用 QSS 替代 DPalette
6. 未使用绝对路径查找 DCI 图标
7. 未滥用 setDciThemeSearchPaths()

## 验证要点

- [ ] 使用 #include <DPalette> 和 #include <DGuiApplicationHelper>
- [ ] 连接 themeTypeChanged 信号监听主题变化
- [ ] 使用 DPalette::ItemBackground 获取背景色
- [ ] 使用 DPalette::TextTitle 获取文字颜色

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
