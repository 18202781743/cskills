# Eval: LayerShell 窗口

## 任务

用户需要在 Wayland 上创建锚定屏幕边缘的窗口。

指导用户使用 LayerShell 附加属性实现窗口锚定。

## 期望输出

回答应：
1. 展示锚定边设置方式
2. 展示层级设置
3. 展示排除区域设置
4. 说明键盘交互模式

## 验证要点

- [ ] DLayerShellWindow.anchors 设置锚定边
- [ ] DLayerShellWindow.layer 设置层级
- [ ] DLayerShellWindow.exclusionZone 设置排除区域
- [ ] DLayerShellWindow.keyboardInteractivity 设置键盘交互
- [ ] 说明 Anchor 枚举值可位或组合

## 参考

参见 [LayerShell 窗口](../../references/layershell.md) 了解 Wayland 窗口锚定的实现。

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] AppletItem 未指定 pluginId
- [ ] PanelPopup 未设置正确的 parent
