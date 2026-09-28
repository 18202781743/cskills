# 集成与构建配置

dde-services 以插件形式部署，不安装公共开发头文件，不导出 CMake 配置文件或库目标。使用方无需安装本项目的开发包，通过 DBus 接口与之交互，或通过 deepin-service-manager 插件机制开发新服务。

## 开发包

dde-services 不提供开发包。使用方只需确保运行环境中已安装 dde-services 及其依赖的 deepin-service-manager，通过 DBus 连接访问各服务插件的功能。

## 引用公开接口

使用方通过 DBus 连接访问以下服务：

- 服务名 `org.deepin.dde.WallpaperSlideshow`

使用 `dbus-send`、Qt DBus 或其他 DBus 客户端库连接上述服务名即可调用接口方法。

开发新服务插件时，按 deepin-service-manager 的插件规范编写插件共享库和 JSON 配置文件，安装到 `deepin-service-manager/` 目录。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
