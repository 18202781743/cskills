# QML DccDBusInterface 使用

## 任务

在控制中心 QML 中调用 DBus 服务，要求：
1. 创建 DBus 接口
2. 调用远程方法
3. 处理返回结果

## 期望输出

代码应：
1. DccDBusInterface 组件
2. service、path、iface 属性指定服务
3. call() 方法调用

## 验证要点

- [ ] DccDBusInterface 组件
- [ ] service、path、iface 属性指定服务
- [ ] call() 方法调用

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] QML 中未直接访问未初始化的 dccData
- [ ] DccDBusInterface 未检查连接状态
