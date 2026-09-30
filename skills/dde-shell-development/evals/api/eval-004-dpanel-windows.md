# Eval: DPanel 窗口管理

## 任务

用户需要了解 Panel 插件的窗口管理能力。

解释 DPanel 提供的窗口接口。

## 期望输出

回答应：
1. 说明 Panel 有主窗口 + 3 个辅助窗口
2. 展示获取各窗口的接口
3. 说明各窗口的用途
4. 解释窗口标志设置

## 验证要点

- [ ] window() 主窗口
- [ ] popupWindow() 弹窗窗口
- [ ] toolTipWindow() 提示窗口
- [ ] menuWindow() 菜单窗口
- [ ] 说明信号 popupWindowChanged 等

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未忘记 D_APPLET_CLASS + #include .moc
- [ ] 插件 ID 与 Plugin.Parent 一致
