# Eval: 创建 Dock 底部面板

## 任务

用户需要创建一个锚定屏幕底部的 Dock 面板窗口。

指导用户配置 DLayerShellWindow 创建底部面板。

## 期望输出

回答应：
1. 展示 anchors 设置（底部 + 左侧 + 右侧）
2. 展示 exclusionZone 设置
3. 展示完整的 QML 示例
4. 说明窗口高度设置

## 验证要点

- [ ] anchors: AnchorBottom | AnchorLeft | AnchorRight
- [ ] layer: LayerTop
- [ ] exclusionZone: 窗口高度
- [ ] Window 高度设置

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未设置排他区域给不需要保留工作区的窗口
- [ ] 多屏场景下未验证锚点和热插拔
