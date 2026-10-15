# Eval: 快捷面板控件尺寸

## 任务

用户的快捷面板控件显示不正常，可能尺寸设置有误。

指导用户正确设置快捷面板控件尺寸。

## 期望输出

回答应：
1. 说明只设置 setFixedHeight 不设置 setFixedSize
2. 展示各布局对应的宽度
3. 说明图标尺寸
4. 解释宽度由框架自动设置

## 验证要点

- [ ] 只用 setFixedHeight(Dock::QUICK_ITEM_HEIGHT)
- [ ] 不要使用 setFixedSize() 锁定宽度
- [ ] Quick_Panel_Single: 70x60
- [ ] Quick_Panel_Multi: 150x60
- [ ] Quick_Panel_Full: 310x60
- [ ] 图标尺寸: 24x24 (Dock::QUICK_PANEL_ICON_SIZE)

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] Type_Tray 与 Type_Quick 未互斥使用
- [ ] 快捷面板未选 Quick_Panel_* 布局标志
