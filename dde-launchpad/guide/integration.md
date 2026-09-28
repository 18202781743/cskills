# 集成与构建配置

dde-launchpad 以 dde-shell applet 插件形式部署，不安装公共开发头文件，不导出 CMake 配置文件或库目标。使用方无需安装本项目的开发包，通过 DBus 接口与之交互即可。

## 开发包

dde-launchpad 不提供开发包。使用方只需确保运行环境中已安装 dde-launchpad 及其依赖的 dde-shell 框架，通过 DBus 连接访问启动器控制接口。

## 引用公开接口

使用方通过 DBus 连接访问以下服务：

- 服务名 `org.deepin.dde.Launcher1`，对象路径 `/org/deepin/dde/Launcher1`

使用 `dbus-send`、Qt DBus 或其他 DBus 客户端库连接上述服务名和对象路径即可调用接口方法、读取属性和监听信号。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
