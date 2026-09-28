# 集成与构建配置

dde-app-services 以 DBus 服务和命令行工具方式运行，不安装公共开发头文件，不导出 CMake 配置文件或库目标。使用方无需安装本项目的开发包，通过 DBus 接口或命令行工具与之交互即可。

## 开发包

dde-app-services 不提供开发包。使用方只需确保运行环境中已安装 dde-app-services 服务和 `dde-dconfig` 命令行工具，通过 DBus 连接或命令行调用访问其功能。

## 引用公开接口

使用方通过 DBus 连接访问以下服务：

- 服务名 `org.desktopspec.ConfigManager`，对象路径 `/org/desktopspec/ConfigManager`
- 服务名 `org.desktopspec.ConfigManager.Manager`，对象路径 `/org/desktopspec/ConfigManager/Manager`

使用 `dbus-send`、Qt DBus 或其他 DBus 客户端库连接上述服务名和对象路径即可调用接口方法、读取属性和监听信号。

使用命令行工具时，直接调用 `dde-dconfig` 命令并传入子命令和参数。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
