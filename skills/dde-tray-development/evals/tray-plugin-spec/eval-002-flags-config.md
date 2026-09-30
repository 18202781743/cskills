# Eval: 配置插件 flags

## 任务

用户想创建一个可以在控制中心设置显隐的托盘插件。

指导用户正确配置 PluginFlags。

## 期望输出

回答应：
1. 列出 Type 标志及其含义
2. 列出 Attribute 标志及其含义
3. 展示 Type_Tray 与 Attribute_CanSetting 组合
4. 说明 icon() 方法的实现要求

## 验证要点

- [ ] Type_Tray (0x10) 用于托盘区
- [ ] Attribute_CanSetting (0x800) 允许控制中心显隐
- [ ] 设置 Attribute_CanSetting 时必须实现 icon()
- [ ] icon() 需要处理亮色/暗色主题
- [ ] 图标需安装到 share/dde-dock/icons/dcc-setting/

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未保存 PluginProxyInterface 指针
- [ ] Attribute_CanSetting 未实现控制中心图标接口
