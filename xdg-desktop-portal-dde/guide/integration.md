# 集成与构建配置

xdg-desktop-portal-dde 以 DBus 服务方式运行，不安装 C++ 公共头文件，不导出 CMake 配置文件或库目标。使用方无需安装本项目的开发包，通过 DBus 接口与之交互即可。

## 开发包

xdg-desktop-portal-dde 不提供 C++ 开发包。使用方只需确保运行环境中已安装 xdg-desktop-portal-dde 服务和 xdg-desktop-portal 前端，通过 DBus 连接访问其接口。

## 引用公开接口

使用方通过 DBus 连接访问 xdg-desktop-portal-dde 提供的服务。后端服务名为 `org.freedesktop.impl.portal.desktop.dde`，portal 配置文件声明了本后端支持的门户接口列表。

沙箱应用通常不直接连接后端，而是通过 xdg-desktop-portal 前端的 `org.freedesktop.portal.*` 接口发起请求，由前端转发到本后端。直接测试或调试后端时，可使用 `dbus-send`、Qt DBus 或其他 DBus 客户端库连接后端服务名。

服务名和接口列表参见[导出类型介绍](modules.md)中各接口章节。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
