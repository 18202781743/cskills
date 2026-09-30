# DccApp 使用

## 任务

获取控制中心应用实例并操作模块树，要求：
1. 获取应用单例
2. 获取根模块
3. 在根模块下添加新模块

## 期望输出

代码应：
1. DccApp::instance() 获取单例
2. rootObject() 获取根模块
3. addChild() 添加子模块

## 验证要点

- [ ] DccApp::instance() 获取单例
- [ ] rootObject() 获取根模块
- [ ] addChild() 添加子模块

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未忘记调用 DCC_FACTORY_CLASS 注册
- [ ] DccObject 的 name 与 CMake PLUGIN_NAME 一致
