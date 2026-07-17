# Eval: 创建控制中心插件

## 任务

创建一个简单的控制中心插件：
1. CMakeLists.txt 配置
2. 插件类继承控制中心基类
3. JSON 元数据文件

## 期望输出

代码应：
1. 使用 find_package(DdeControlCenter)
2. 继承正确的插件基类并实现接口
3. 创建正确的 JSON 元数据

## 验证要点

- [ ] find_package(Dtk6Core Dtk6Widget Dtk6Gui REQUIRED)
- [ ] Q_PLUGIN_METADATA 宏
- [ ] JSON 文件包含正确的 api 版本

## 参考

参见 [插件开发](../../../references/plugin-development.md) 了解控制中心插件开发流程。
