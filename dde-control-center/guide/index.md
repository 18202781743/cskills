# dde-control-center 二次开发文档 · 概览

## 项目定位

dde-control-center 是 DDE 控制中心，提供系统设置界面框架和插件机制，允许第三方开发设置模块插件。使用方通过实现插件接口、注册插件工厂并安装到指定目录，将自定义设置页面集成到控制中心。

## 术语与缩写

- **dccV25**：控制中心 C++ 公开命名空间，公开类型和宏位于此命名空间或以 `Dcc` 前缀标记。
- **插件版本**：当前插件接口版本为 v1.1，插件安装目录名为 `plugins_v1.1`。
- **DccObject**：控制中心配置对象，描述设置项的层级结构，在 QML 中作为数据节点使用。
- **DccFactory**：插件工厂接口，所有插件需继承并注册，由框架通过工厂创建插件实例。
- **DccApp**：控制中心应用单例，提供对控制中心全局状态的访问入口，在 QML 中以单例形式可用。

## 导出类型

[插件工厂接口](plugin-factory.md)是本项目的 C++ 类型参考文档，QML 接口见[org.deepin.dcc QML 模块](org.deepin.dcc.md)。以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 全局约定

公开头文件安装在 `dde-control-center` 目录下。公开符号位于 `dccV25` 命名空间。插件通过宏注册，通过 `dcc_build_plugin` 构建和 `dcc_install_plugin` 安装。插件安装路径为 `lib/dde-control-center/plugins_v1.1/<plugin-name>/`，翻译文件安装路径为 `share/dde-control-center/translations/v1.1/`。

## 按功能查阅

- 将控制中心插件引入 CMake 工程：参见[插件工厂接口](plugin-factory.md)。
- 实现插件工厂：参见 [DccFactory](plugin-factory.md#dccfactory)。
- 描述设置项层级结构：参见 [DccObject](org.deepin.dcc.md#dccobject)。
- 使用 QML 模块构建设置页面：参见 [org.deepin.dcc](org.deepin.dcc.md)。
