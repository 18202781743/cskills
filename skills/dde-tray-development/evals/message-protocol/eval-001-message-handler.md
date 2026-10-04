# Eval: 实现消息处理

## 任务

用户需要在插件中处理任务栏发来的消息。

指导用户实现 message() 接口和 setMessageCallback。

## 期望输出

回答应：
1. 展示 setMessageCallback 保存回调
2. 展示 message() 解析 JSON
3. 展示返回 JSON 格式
4. 说明消息类型常量

## 验证要点

- [ ] setMessageCallback(cb) 保存回调函数
- [ ] message() 解析 msgType 和 data 字段
- [ ] 使用 QJsonDocument 解析和构建
- [ ] 返回格式包含 msgType 和 data
- [ ] 说明 MessageCallbackFunc 是 C 函数指针

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] MSG_GET_SUPPORT_FLAG 未返回正确标志
- [ ] 未处理 MSG_ITEM_ACTIVE_STATE
