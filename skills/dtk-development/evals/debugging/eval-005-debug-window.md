# Eval: 调试窗口效果问题

## 任务

调试窗口模糊效果不显示的问题：
1. 检查平台支持
2. 检查窗口属性设置
3. 检查合成器状态

## 期望输出

代码应：
1. 确认 DGuiApplicationHelper::isXWindowPlatform()
2. 检查 DPlatformHandle 设置
3. 验证合成器（compositor）是否启用
4. 排查思路遵循 DTK 分层架构（gui → widget/declarative → 应用层）
5. 未修改系统安装文件进行调试（应使用临时环境变量）

## 验证要点

- [ ] 确认 DGuiApplicationHelper::isXWindowPlatform()
- [ ] 检查 DPlatformHandle 设置
- [ ] 验证合成器（compositor）是否启用

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 排查思路遵循 DTK 分层架构（gui → widget/declarative → 应用层）
- [ ] 未修改系统安装文件进行调试（应使用临时环境变量）
