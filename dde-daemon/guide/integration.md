# 集成与构建配置

dde-daemon 以 DBus 服务方式运行，不安装 C++ 公共头文件，不导出 CMake 配置文件或库目标。使用方无需安装本项目的开发包，通过 DBus 接口与之交互即可。

## 开发包

dde-daemon 不提供 C++ 开发包。使用方只需确保运行环境中已安装 dde-daemon 服务，通过 DBus 连接访问其接口。

Go 项目使用 Makefile 构建，Go 模块路径为 `github.com/linuxdeepin/dde-daemon`。如需在 Go 项目中引用 dde-daemon 的包，可通过 Go 模块系统引入对应包路径。

## 引用公开接口

使用方通过 DBus 连接访问 dde-daemon 提供的各服务。各服务的服务名和对象路径参见[导出类型介绍](modules.md)中各接口章节。

使用 `dbus-send`、Qt DBus 或其他 DBus 客户端库连接对应的服务名和对象路径即可调用接口方法、读取属性和监听信号。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
