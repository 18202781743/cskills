# DccObject 基本用法

## 任务

在控制中心创建一个功能模块，要求：
1. 模块有内部名称和显示名称
2. 模块有图标
3. 模块添加到指定父模块下

## 期望输出

代码应：
1. #include <DccObject>
2. setName() 设置模块名
3. setDisplayName() 设置显示名
4. 父模块调用 addChild() 添加子模块

## 验证要点

- [ ] #include <DccObject>
- [ ] setName() 设置模块名
- [ ] setDisplayName() 设置显示名
- [ ] 父模块调用 addChild() 添加子模块

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未忘记调用 DCC_FACTORY_CLASS 注册
- [ ] DccObject 的 name 与 CMake PLUGIN_NAME 一致
