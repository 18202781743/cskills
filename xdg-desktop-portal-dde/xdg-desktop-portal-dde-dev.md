# xdg-desktop-portal-dde 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | xdg-desktop-portal-dde |
| 版本 | （跟随仓库 master 分支） |
| 描述 | DDE 的 XDG Desktop Portal 后端，为 Flatpak/Snap 等沙箱应用提供文件选择、通知、截图、壁纸、屏幕共享等门户接口 |
| CMake target | 不适用（不导出库 target） |
| find_package 名 | 不适用 |
| 头文件安装路径 | 不适用（不安装公共开发头文件） |
| 仓库地址 | https://github.com/linuxdeepin/xdg-desktop-portal-dde.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6widgets6, libqt6dbus6 (>= 6.x)
- libdtk6widget, libdtk6core, libdtk6gui
- xdg-desktop-portal

### 开发依赖
- Qt 6 Core, Gui, Widgets, DBus (>= 6.x)
- DTK6 Widget, Core
- CMake >= 3.16

## 3. CMake 集成

不适用（不导出 CMake 配置文件，不提供库 target 供外部链接）

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（不导出公共 C++ 命名空间）

## 6. 关键公共类及功能描述

| 类 | 功能 |
|------|------|
| `FileChooser` | 文件选择门户后端 |
| `Notification` | 通知门户后端 |
| `Screenshot` | 截图门户后端 |
| `Wallpaper` | 壁纸设置门户后端 |
| `Settings` | 设置门户后端 |
| `ScreenCast` | 屏幕共享门户后端 |
| `RemoteDesktop` | 远程桌面门户后端 |
| `Access` | 访问控制门户后端 |
| `Background` | 后台运行门户后端 |
| `Secret` | 密钥门户后端 |
| `GlobalShortcut` | 全局快捷键门户后端 |
| `Lockdown` | 锁定门户后端 |
| `Request` | 请求处理基类 |

## 7. QML 模块

不适用

## 8. DBus 接口

### org.freedesktop.impl.portal.desktop.dde

| 项目 | 内容 |
|------|------|
| 服务名 | `org.freedesktop.impl.portal.desktop.dde` |
| 配置文件 | `share/xdg-desktop-portal/portals/dde.portal` |
| 使用环境 | DDE |

#### 支持的 Portal 接口

| 接口 | 说明 |
|------|------|
| `org.freedesktop.impl.portal.Screenshot` | 截图 |
| `org.freedesktop.impl.portal.Notification` | 通知 |
| `org.freedesktop.impl.portal.FileChooser` | 文件选择 |
| `org.freedesktop.impl.portal.Wallpaper` | 壁纸设置 |
| `org.freedesktop.impl.portal.ScreenCast` | 屏幕共享 |
| `org.freedesktop.impl.portal.RemoteDesktop` | 远程桌面 |
| `org.freedesktop.impl.portal.Access` | 访问控制 |
| `org.freedesktop.impl.portal.Settings` | 设置 |

### org.freedesktop.Notifications

| 项目 | 内容 |
|------|------|
| 服务名 | `org.freedesktop.Notifications` |
| 说明 | freedesktop 通知规范接口 |

## 9. 插件开发

不适用
