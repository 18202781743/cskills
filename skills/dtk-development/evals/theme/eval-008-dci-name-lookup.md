# Eval: DCI 图标按规范查找

## 任务

为 DTK 应用中的打开、关闭或添加按钮选择图标，要求：
1. 自有图标按 DCI 的主题、尺寸和状态规则组织
2. 控件通过基础名称查找图标
3. 主题切换时不由应用手动拼接资源路径

## 期望输出

代码应：
1. 控件使用 `DIconTheme::findQIcon("icon-name")` 按名称查找图标
2. 不使用 `:/icons/...`、`:/dsg/built-in-icons/...` 等资源绝对路径
3. 常规场景不调用 `DIconTheme::setDciThemeSearchPaths()` 解决资源组织或名称错误；确需自定义搜索根目录时说明原因
4. 通用操作优先复用 DTK 已有图标
5. DCI 的主题、尺寸和状态由图标规范和查找链路处理
6. 未使用 QSS 替代 DPalette
7. 未使用绝对路径查找 DCI 图标
8. 未滥用 setDciThemeSearchPaths()

## 验证要点

- [ ] 控件使用 `DIconTheme::findQIcon("icon-name")` 按名称查找图标
- [ ] 不使用 `:/icons/...`、`:/dsg/built-in-icons/...` 等资源绝对路径
- [ ] 常规场景不调用 `DIconTheme::setDciThemeSearchPaths()` 解决资源组织或名称错误；确需自定义搜索根目录时说明原因
- [ ] 通用操作优先复用 DTK 已有图标
- [ ] DCI 的主题、尺寸和状态由图标规范和查找链路处理

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
