# Eval: DApplet 生命周期

## 任务

用户想了解 DApplet 插件的生命周期，以便正确初始化资源。

解释 DApplet 的生命周期和各阶段的作用。

## 期望输出

回答应：
1. 说明生命周期顺序：构造 → load() → init() → rootObjectChanged
2. 解释各阶段的职责
3. 说明 rootObjectChanged 信号的触发时机
4. 给出资源初始化的最佳实践

## 验证要点

- [ ] 说明构造函数中不应做复杂初始化
- [ ] load() 用于加载配置和数据
- [ ] init() 用于初始化 QML 和连接信号
- [ ] rootObjectChanged 表示 QML 根对象已创建
- [ ] 说明 DApplet::init() 需要调用父类实现

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未忘记 D_APPLET_CLASS + #include .moc
- [ ] 插件 ID 与 Plugin.Parent 一致
