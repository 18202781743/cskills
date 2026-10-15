# Eval: ContainmentItem QML 组件

## 任务

用户需要在 Containment 插件中显示子插件的 UI。

指导用户使用 ContainmentItem 和 appletItems。

## 期望输出

回答应：
1. 展示 ContainmentItem 作为根元素
2. 展示 Repeater 遍历 Containment.appletItems
3. 展示 delegate 中使用 model.data
4. 说明子插件 UI 的嵌入方式

## 验证要点

- [ ] ContainmentItem 作为根元素
- [ ] Containment.appletItems 作为 model
- [ ] delegate 中 model.data 是子插件根元素
- [ ] 说明子插件 UI 自动嵌入

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] AppletItem 未指定 pluginId
- [ ] PanelPopup 未设置正确的 parent
