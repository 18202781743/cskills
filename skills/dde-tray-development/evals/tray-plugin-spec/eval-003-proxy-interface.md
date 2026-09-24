# Eval: 使用 PluginProxyInterface

## 任务

用户需要在插件中主动通知任务栏刷新控件。

指导用户使用 m_proxyInter 与任务栏交互。

## 期望输出

回答应：
1. 展示 itemAdded 添加控件
2. 展示 itemUpdate 刷新控件
3. 展示 itemRemoved 移除控件
4. 展示 saveValue/getValue 保存配置

## 验证要点

- [ ] init() 中保存 proxyInter 到 m_proxyInter
- [ ] itemAdded(this, itemKey) 添加控件
- [ ] itemUpdate(this, itemKey) 通知刷新
- [ ] itemRemoved(this, itemKey) 移除控件
- [ ] saveValue(this, key, value) 保存配置
- [ ] getValue(this, key, fallback) 读取配置

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未保存 PluginProxyInterface 指针
- [ ] Attribute_CanSetting 未实现控制中心图标接口
