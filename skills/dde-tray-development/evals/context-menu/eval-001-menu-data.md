# Eval: 实现右键菜单

## 任务

用户需要为托盘插件添加右键菜单。

指导用户实现 itemContextMenu 和 invokedMenuItem。

## 期望输出

回答应：
1. 展示 itemContextMenu 返回 JSON
2. 展示菜单项字段（itemId、itemText、isCheckable）
3. 展示 invokedMenuItem 处理点击
4. 说明预定义菜单项 ID

## 验证要点

- [ ] itemContextMenu 返回 { "items": [...] }
- [ ] 菜单项包含 itemId、itemText、isCheckable、isActive、checked
- [ ] invokedMenuItem(menuId, checked) 处理点击
- [ ] 不要使用保留 ID: dock-item-id、undock-item-id

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 菜单 JSON 未包含有效的 itemKey
- [ ] 未在 menuContent 中返回列表
