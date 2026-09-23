# Eval: 创建浮动覆盖层

## 任务

用户需要创建一个不占排除区域的浮动覆盖窗口（如通知弹窗）。

指导用户配置 DLayerShellWindow 创建浮动覆盖层。

## 期望输出

回答应：
1. 展示不设置 exclusionZone
2. 展示 LayerOverlay 层级
3. 展示键盘交互模式设置
4. 说明与面板的区别

## 验证要点

- [ ] layer: LayerOverlay
- [ ] 不设置或 exclusionZone: 0
- [ ] keyboardInteractivity: KeyboardInteractivityOnDemand
- [ ] 说明浮动窗口不阻止其他窗口

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未设置排他区域给不需要保留工作区的窗口
- [ ] 多屏场景下未验证锚点和热插拔
