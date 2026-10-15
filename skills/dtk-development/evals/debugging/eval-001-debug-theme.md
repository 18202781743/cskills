# Eval: 调试主题问题

## 任务

调试控件颜色不跟随主题切换的问题：
1. 检查当前主题类型
2. 检查控件调色板
3. 检查信号连接

## 期望输出

代码应：
1. 使用 DGuiApplicationHelper::instance()->themeType()
2. 检查 DPaletteHelper::instance()->palette(widget)
3. 验证 themeTypeChanged 信号是否连接
4. 排查思路遵循 DTK 分层架构（gui → widget/declarative → 应用层）
5. 未修改系统安装文件进行调试（应使用临时环境变量）

## 验证要点

- [ ] 使用 DGuiApplicationHelper::instance()->themeType()
- [ ] 检查 DPaletteHelper::instance()->palette(widget)
- [ ] 验证 themeTypeChanged 信号是否连接

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 排查思路遵循 DTK 分层架构（gui → widget/declarative → 应用层）
- [ ] 未修改系统安装文件进行调试（应使用临时环境变量）
