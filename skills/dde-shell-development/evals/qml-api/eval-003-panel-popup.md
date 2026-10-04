# Eval: PanelPopup 和 PanelMenu

## 任务

用户需要在 Panel 插件中创建弹出菜单。

指导用户使用 PanelPopup、PanelToolTip、PanelMenu 组件。

## 期望输出

回答应：
1. 展示 PanelPopup 的基本用法
2. 展示 PanelMenu 的基本用法
3. 说明窗口标志和圆角设置
4. 展示 PanelToolTip 的用法

## 验证要点

- [ ] PanelPopup 用于弹窗内容
- [ ] PanelMenu 用于菜单内容
- [ ] PanelToolTip 用于提示内容
- [ ] 说明 PanelPopupWindow 等窗口类

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] AppletItem 未指定 pluginId
- [ ] PanelPopup 未设置正确的 parent
