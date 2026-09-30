# dde-control-center 二次开发文档 · 概览

## 项目定位

dde-control-center 是 DDE 控制中心，提供系统设置界面框架和插件机制，允许第三方开发设置模块插件。使用方通过实现插件接口、注册插件工厂并安装到指定目录，将自定义设置页面集成到控制中心。

## 导出类型

[插件工厂接口](plugin-factory.md)是本项目的 C++ 类型参考文档，QML 接口见[org.deepin.dcc QML 模块](org.deepin.dcc.md)。以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 全局约定

公开符号位于 `dccV25` 命名空间。

## 按功能查阅

- 将控制中心插件引入 CMake 工程：参见[插件工厂接口](plugin-factory.md)。
- 实现插件工厂：参见 [DccFactory](plugin-factory.md#dccfactory)。
- 描述设置项层级结构：参见 [DccObject](org.deepin.dcc.md#dccobject)。
- 访问控制中心全局状态和页面导航：参见 [DccApp](org.deepin.dcc.md#dccapp)。
- 使用 QML 模块构建设置页面：参见 [org.deepin.dcc](org.deepin.dcc.md)。
