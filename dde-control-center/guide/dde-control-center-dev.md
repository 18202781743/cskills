# 导出类型介绍

dde-control-center 提供插件工厂接口，支持第三方开发设置模块插件并集成到控制中心界面框架。公开头文件 `dccfactory.h` 安装到 `${CMAKE_INSTALL_INCLUDEDIR}/dde-control-center` 目录下，定义了 `dccV25` 命名空间中的 `DccFactory` 类和 `DCC_FACTORY_CLASS` 宏。

## DccFactory

### 定位

插件工厂接口，所有控制中心插件需继承此类并注册，由框架通过 Qt 插件机制加载工厂并创建插件实例。

### 功能能力总结

- 提供虚方法 `create()`，返回插件实例的 `QObject` 指针，框架将该实例导出为 QML 上下文属性 `dccData`，供插件 QML 文件调用
- 提供虚方法 `dccObject()`，返回 `DccObject` 指针，用于插件不提供 QML 文件时自行构建配置对象树
- 提供 `DCC_FACTORY_CLASS(classname)` 宏，自动生成一个继承 `DccFactory` 的工厂类，在 `create()` 中返回 `new classname(parent)`，并通过 `Q_PLUGIN_METADATA` 和 `Q_INTERFACES` 完成 Qt 插件注册

### 使用场景

开发控制中心设置模块插件时，在插件 C++ 类的头文件或源文件中调用 `DCC_FACTORY_CLASS(YourClass)` 宏注册插件，框架加载插件后通过工厂的 `create()` 方法获取插件实例。如果插件需要返回 `DccObject` 配置对象树而非 QML 文件，则重写 `dccObject()` 方法。
