# Eval: 调试风格问题

## 任务

调试 QWidget 控件样式不正确的问题：
1. 检查当前使用的 QStyle
2. 确认 Chameleon 风格已加载
3. 检查样式绘制

## 期望输出

代码应：
1. 使用 widget->style()->objectName() 检查风格名
2. 确认风格为 "chameleon"
3. 使用 QT_DEBUG_PLUGINS=1 排查插件加载
4. 只加载 QWidget Chameleon 专篇，不加载 QML 风格文档
5. 排查思路遵循 DTK 分层架构（gui → widget/declarative → 应用层）
6. 未修改系统安装文件进行调试（应使用临时环境变量）

## 验证要点

- [ ] 使用 widget->style()->objectName() 检查风格名
- [ ] 确认风格为 "chameleon"
- [ ] 使用 QT_DEBUG_PLUGINS=1 排查插件加载
- [ ] 只加载 QWidget Chameleon 专篇，不加载 QML 风格文档

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 排查思路遵循 DTK 分层架构（gui → widget/declarative → 应用层）
- [ ] 未修改系统安装文件进行调试（应使用临时环境变量）
