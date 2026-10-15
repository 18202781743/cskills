# Eval: AppletItem QML 组件

## 任务

用户需要在 QML 中创建 Applet 插件的 UI。

指导用户使用 AppletItem 和附加属性。

## 期望输出

回答应：
1. 展示 AppletItem 作为根元素
2. 展示 Applet 附加属性的使用
3. 展示访问插件 ID 和父插件
4. 说明 implicitWidth/Height 的作用

## 验证要点

- [ ] AppletItem 作为 QML 根元素
- [ ] Applet.pluginId 获取插件 ID
- [ ] Applet.id 获取实例 ID
- [ ] Applet.parent 获取父插件
- [ ] Applet.rootObject 获取 QML 根对象

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] AppletItem 未指定 pluginId
- [ ] PanelPopup 未设置正确的 parent
