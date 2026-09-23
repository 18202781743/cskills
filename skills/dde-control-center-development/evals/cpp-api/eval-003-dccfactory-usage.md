# DccFactory 使用

## 任务

为控制中心模块创建 QML 页面，要求：
1. 注册自定义 QML 组件类型
2. 创建 QML 页面组件
3. 将页面绑定到模块

## 期望输出

代码应：
1. DccFactory::registerType() 注册类型
2. create() 创建组件
3. 设置 pageType 属性指定页面类型

## 验证要点

- [ ] DccFactory::registerType() 注册类型
- [ ] create() 创建组件
- [ ] 设置 pageType 属性指定页面类型

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未忘记调用 DCC_FACTORY_CLASS 注册
- [ ] DccObject 的 name 与 CMake PLUGIN_NAME 一致
