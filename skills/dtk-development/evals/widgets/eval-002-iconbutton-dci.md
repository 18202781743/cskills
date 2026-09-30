# Eval: 图标按钮使用 DCI 图标

## 任务

创建一个图标按钮，要求：
1. 按 DCI 规范组织动态资源
2. 通过图标名称查找图标，不拼接资源路径
3. 点击时输出日志

## 期望输出

代码应：
1. 创建图标按钮
2. 使用 DCI 图标格式设置图标
3. 连接点击信号

## 验证要点

- [ ] #include <DIconButton>
- [ ] #include <DDciIcon>
- [ ] 使用 `DIconTheme::findQIcon("action")` 按名称查找图标
- [ ] 常规场景未调用 `setDciThemeSearchPaths()`；如确需自定义搜索根目录，说明调用原因和影响范围
- [ ] button->setIcon(icon)

## 参考

参见 [按钮控件](../../references/widgets/button.md) 了解 DIconButton 和 DCI 图标的用法。

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
