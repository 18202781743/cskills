# xdg-desktop-portal-dde 二次开发文档 · 概览

## 项目定位

xdg-desktop-portal-dde 是 DDE 的 XDG Desktop Portal 后端，为 Flatpak、Snap 这类沙箱应用提供文件选择、通知、截图、壁纸设置、屏幕共享、远程桌面、访问控制和设置门户接口。使用方通过 DBus 接口与之交互。

## 术语与缩写

- **XDG Desktop Portal**：freedesktop.org 定义的桌面门户规范，沙箱应用通过门户接口访问桌面功能。
- **Portal 后端**：实现门户接口的进程，xdg-desktop-portal-dde 是 DDE 上的后端实现。
- **portal 配置文件**：`share/xdg-desktop-portal/portals/dde.portal`，声明本后端支持的门户接口。
- **DBus 属性**：远端接口上的具名值，使用方可读取或监听变化。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以 DBus 接口名为章节，说明其定位、功能能力和使用场景。

## 全局约定

xdg-desktop-portal-dde 是纯 DBus 服务，不安装 C++ 公共头文件，不导出 CMake 配置文件或库目标。使用方通过 DBus 连接访问其功能。后端服务名为 `org.freedesktop.impl.portal.desktop.dde`，portal 配置文件位于 `share/xdg-desktop-portal/portals/dde.portal`。

## 按功能查阅

- 将 xdg-desktop-portal-dde 引入使用方工程：参见[集成与构建配置](integration.md)。
- 使用文件选择、通知、截图或壁纸设置门户接口：参见 [org.freedesktop.impl.portal.desktop.dde](modules.md#orgfreedesktopimplportaldesktopdde)。
- 使用屏幕共享或远程桌面门户接口：参见 [org.freedesktop.impl.portal.desktop.dde](modules.md#orgfreedesktopimplportaldesktopdde)。
- 使用 freedesktop 通知接口：参见 [org.freedesktop.Notifications](modules.md#orgfreedesktopnotifications)。
