# Eval: 插件动态加载

## 任务

用户需要在运行时动态加载其他插件。

指导用户使用插件加载器实现动态加载。

## 期望输出

回答应：
1. 展示获取加载器单例的方式
2. 展示查询插件列表的方法
3. 展示动态加载插件的方式
4. 说明添加自定义搜索路径

## 验证要点

- [ ] DPluginLoader::instance() 获取单例
- [ ] plugins() / rootPlugins() 获取插件列表
- [ ] childrenPlugin(pluginId) 获取子插件
- [ ] loadApplet(DAppletData) 动态加载
- [ ] addPackageDir() / addPluginDir() 添加搜索路径

## 参考

参见 [插件加载器](../../references/api/core.md) 了解插件动态加载的用法。

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未忘记 D_APPLET_CLASS + #include .moc
- [ ] 插件 ID 与 Plugin.Parent 一致
