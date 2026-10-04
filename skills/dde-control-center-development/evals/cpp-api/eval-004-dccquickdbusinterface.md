# DccQuickDBusInterface 使用

## 任务

在 QML 中调用系统 DBus 服务，要求：
1. 创建 DBus 接口实例
2. 调用远程方法
3. 监听 DBus 信号

## 期望输出

代码应：
1. #include <DccQuickDBusInterface>
2. 设置 service、path、interface 属性
3. call() 调用方法
4. 连接信号处理返回值

## 验证要点

- [ ] #include <DccQuickDBusInterface>
- [ ] 设置 service、path、interface 属性
- [ ] call() 调用方法
- [ ] 连接信号处理返回值

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未忘记调用 DCC_FACTORY_CLASS 注册
- [ ] DccObject 的 name 与 CMake PLUGIN_NAME 一致
