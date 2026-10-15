# Eval: 快捷面板子页面显示

## 任务

用户的快捷面板控件点击后需要显示详情页面。

指导用户实现 itemPopupApplet 和 requestSetAppletVisible。

## 期望输出

回答应：
1. 展示 itemPopupApplet 返回详情控件
2. 展示控件发出点击信号
3. 展示连接信号调用 requestSetAppletVisible
4. 说明与托盘弹出面板的区别

## 验证要点

- [ ] itemPopupApplet(Dock::QUICK_ITEM_KEY) 返回详情控件
- [ ] 快捷面板控件发出 requestShowDetail 信号
- [ ] 插件连接信号调用 requestSetAppletVisible(this, itemKey, true)
- [ ] 说明 Dock 不会自动显示，需主动请求

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] Type_Tray 与 Type_Quick 未互斥使用
- [ ] 快捷面板未选 Quick_Panel_* 布局标志
