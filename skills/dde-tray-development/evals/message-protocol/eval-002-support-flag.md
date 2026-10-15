# Eval: 插件可用性通知

## 任务

用户的插件可能在某些情况下不可用，需要通知任务栏。

指导用户使用 MSG_GET_SUPPORT_FLAG 和 MSG_SUPPORT_FLAG_CHANGED。

## 期望输出

回答应：
1. 展示 message() 处理 MSG_GET_SUPPORT_FLAG
2. 展示主动发送 MSG_SUPPORT_FLAG_CHANGED
3. 说明返回格式
4. 说明触发时机

## 验证要点

- [ ] message() 处理 "getSupportFlag"
- [ ] 返回 { "supportFlag": true/false }
- [ ] 状态变化时通过回调发送 "supportFlagChanged"
- [ ] 说明使用场景（如蓝牙未开启时）

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] MSG_GET_SUPPORT_FLAG 未返回正确标志
- [ ] 未处理 MSG_ITEM_ACTIVE_STATE
