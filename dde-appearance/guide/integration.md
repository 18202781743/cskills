# 集成与构建配置

dde-appearance 以 DBus 服务方式运行，不安装公共开发头文件，不导出 CMake 配置文件或库目标。使用方无需安装本项目的开发包，通过 DBus 接口与之交互即可。

## 开发包

dde-appearance 不提供开发包。使用方只需确保运行环境中已安装 dde-appearance 服务，通过 DBus 连接访问其接口。

## 引用公开接口

使用方通过 DBus 连接访问以下服务：

- 服务名 `org.deepin.dde.Appearance1`，对象路径 `/org/deepin/dde/Appearance1`
- 服务名 `com.deepin.wm`，对象路径 `/com/deepin/wm`

使用 `dbus-send`、Qt DBus 或其他 DBus 客户端库连接上述服务名和对象路径即可调用接口方法、读取属性和监听信号。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
