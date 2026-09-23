# Eval: 创建 Containment 容器插件

## 任务

用户想创建一个应用抽屉插件，可以容纳多个子插件。

指导用户创建 Containment 插件。

## 期望输出

回答应：
1. 展示 DContainment 继承类实现
2. 展示 load() 中设置 groupList 的方式
3. 展示 QML 中使用 Repeater 遍历 appletItems
4. 说明子插件加载机制

## 验证要点

- [ ] 类继承 DContainment
- [ ] load() 中调用 DPluginLoader::instance()->childrenPlugin()
- [ ] 使用 DAppletData::fromPluginMetaData() 构建子插件数据
- [ ] QML 中使用 Containment.appletItems 作为 model
- [ ] 说明 ContainmentItem 作为 QML 根元素

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未混用 dde-tray-loader 的 IID
- [ ] 元数据中 pluginType 与实际类型匹配
