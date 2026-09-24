# Eval: 处理任务栏位置变化

## 任务

用户的托盘图标需要根据任务栏位置调整显示方向。

指导用户实现 positionChanged 接口。

## 期望输出

回答应：
1. 展示 positionChanged 接口实现
2. 展示 Dock::Position 枚举值
3. 展示根据位置更新控件
4. 说明刷新控件的时机

## 验证要点

- [ ] 覆写 positionChanged(const Dock::Position)
- [ ] Position::Top/Right/Bottom/Left 枚举值
- [ ] 更新控件显示后调用 itemUpdate
- [ ] 说明位置变化时的刷新流程

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未保存 PluginProxyInterface 指针
- [ ] Attribute_CanSetting 未实现控制中心图标接口
