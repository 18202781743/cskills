# dde-clipboard 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-clipboard |
| 版本 | （跟随仓库 master 分支） |
| 描述 | DDE 剪贴板管理工具，包含剪贴板前端、守护进程和 Dock 插件 |
| CMake target | 不适用（不导出库 target） |
| find_package 名 | 不适用 |
| 头文件安装路径 | 不适用（不安装公共开发头文件） |
| 仓库地址 | https://github.com/linuxdeepin/dde-clipboard.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6widgets6, libqt6dbus6, libqt6waylandclient6 (>= 6.x)
- libdtk6widget, libdtk6core, libdtk6gui
- libdde-shell

### 开发依赖
- Qt 6 Core, Gui, Widgets, DBus, WaylandClient (>= 6.x)
- DTK6 Widget, Core, Tools
- DDEShell, DdeTrayLoader
- ECM (Extra CMake Modules)
- CMake >= 3.16

## 3. CMake 集成

不适用（不导出 CMake 配置文件，不提供库 target 供外部链接）

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（不导出公共 C++ 命名空间）

## 6. 关键公共类及功能描述

dde-clipboard 由三个组件构成：

| 组件 | 说明 |
|------|------|
| `dde-clipboard` | 剪贴板前端界面，展示剪贴板历史记录 |
| `dde-clipboard-daemon` | 剪贴板守护进程，监听 Wayland wlr-data-control 协议，管理剪贴板数据 |
| `dock-clipboard-plugin` | Dock 剪贴板插件，安装到 `lib/dde-dock/plugins` |

## 7. QML 模块

不适用

## 8. DBus 接口

### org.deepin.dde.Clipboard1

| 项目 | 内容 |
|------|------|
| 服务名 | `org.deepin.dde.Clipboard1` |
| 对象路径 | `/org/deepin/dde/Clipboard1` |

#### 关键方法

| 方法 | 说明 |
|------|------|
| `Toggle` | 切换剪贴板界面显示/隐藏 |
| `Show` | 显示剪贴板界面 |
| `Hide` | 隐藏剪贴板界面 |

#### 关键属性

| 属性 | 类型 | 说明 |
|------|------|------|
| `clipboardVisible` | `b` | 剪贴板界面是否可见 |

#### 关键信号

| 信号 | 说明 |
|------|------|
| `clipboardVisibleChanged(bool visible)` | 剪贴板可见性变化信号 |

## 9. 插件开发

dde-clipboard 包含一个 Dock 插件（`dock-clipboard-plugin`），通过 DdeTrayLoader 框架加载：

- 插件安装路径：`lib/dde-dock/plugins`
- 插件使用 DDEShell 和 DdeTrayLoader 框架
- 资源文件安装到 `share/dde-dock/icons/dcc-setting/`
