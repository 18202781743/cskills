# Eval: 插件激活状态

## 任务

用户的插件需要报告自身是否处于激活状态（如蓝牙已连接）。

指导用户使用 MSG_ITEM_ACTIVE_STATE。

## 期望输出

回答应：
1. 展示发送激活状态消息
2. 说明 true/false 含义
3. 展示状态变化时发送
4. 说明用途

## 验证要点

- [ ] msgType: "itemActiveState"
- [ ] data: { "itemActiveState": true/false }
- [ ] 通过 m_messageCallback 发送
- [ ] true 表示激活状态（如蓝牙已连接）

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] MSG_GET_SUPPORT_FLAG 未返回正确标志
- [ ] 未处理 MSG_ITEM_ACTIVE_STATE
