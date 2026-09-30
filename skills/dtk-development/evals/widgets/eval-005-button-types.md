# Eval: 按钮类型选择

## 任务

创建一个包含三种按钮类型的界面：
1. 蓝色推荐按钮 "保存"
2. 红色警告按钮 "删除"
3. 普通图标按钮（关闭图标）

## 期望输出

代码应使用正确的按钮类型。

## 验证要点

- [ ] DSuggestButton 用于推荐操作
- [ ] DWarningButton 用于危险操作
- [ ] DIconButton 使用 DStyle::StandardPixmap

## 参考

参见 [按钮控件](../../references/widgets/button.md) 了解 DTK 按钮类型的选择。

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
