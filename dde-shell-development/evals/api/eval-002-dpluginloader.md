# Eval: DPluginLoader 插件加载

## 任务

用户需要在运行时动态加载其他插件。

指导用户使用 DPluginLoader 单例。

## 期望输出

回答应：
1. 展示获取单例的方式
2. 展示查询插件列表的方法
3. 展示动态加载插件的方式
4. 说明添加自定义搜索路径

## 验证要点

- [ ] DPluginLoader::instance() 获取单例
- [ ] plugins() / rootPlugins() 获取插件列表
- [ ] childrenPlugin(pluginId) 获取子插件
- [ ] loadApplet(DAppletData) 动态加载
- [ ] addPackageDir() / addPluginDir() 添加搜索路径
