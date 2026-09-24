# dde-launchpad 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-launchpad |
| 版本 | 0.7.0 |
| 描述 | DDE 启动器，提供全屏和窗口模式的应用启动界面 |
| CMake target | `launchpadcommon`（共享库） |
| find_package 名 | 不适用（不导出 find_package 配置文件） |
| 头文件安装路径 | 不适用（库不安装公共头文件） |
| 仓库地址 | https://github.com/linuxdeepin/dde-launchpad.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6qml6, libqt6quick6, libqt6dbus6, libqt6svg6 (>= 6.x)
- libdtk6core, libdtk6gui
- libappstreamqt
- libdde-shell

### 开发依赖
- Qt 6 Core, Gui, Concurrent, DBus, Qml, Svg, Quick, QuickControls2 (>= 6.x)
- DTK6 Core, Gui
- AppStreamQt 1.0
- DDEShell
- ECM (Extra CMake Modules)
- CMake >= 3.10

## 3. CMake 集成

dde-launchpad 导出共享库 `launchpadcommon`，但不提供 find_package 配置文件。主要作为 dde-shell 的 applet 插件使用：

```cmake
# launchpadcommon 库安装到 ${CMAKE_INSTALL_LIBDIR}
# 但无 find_package 支持，不适用于外部 CMake 集成
```

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（内部使用，未导出公共命名空间）

## 6. 关键公共类及功能描述

| 类/组件 | 功能 |
|---------|------|
| `launchpadcommon` | 启动器共享库，包含 QML 模块和应用列表管理逻辑 |
| `gio-utils` | GLib/GIO 工具封装（OBJECT 库） |
| `dde-integration-dbus` | DDE DBus 集成（OBJECT 库） |
| `treeland-integration` | Treeland 集成（OBJECT 库） |
| `shell-launcher-applet` | dde-shell 启动器 applet 插件 |

## 7. QML 模块

| 项目 | 内容 |
|------|------|
| 模块 URI | 通过 `qt_add_qml_module(launchpadcommon)` 注册 |
| 关键组件 | `Main.qml`, `FullscreenFrame.qml`, `GridViewContainer.qml`, `DrawerFolder.qml` |

## 8. DBus 接口

### org.deepin.dde.Launcher1

| 项目 | 内容 |
|------|------|
| 服务名 | `org.deepin.dde.Launcher1` |
| 对象路径 | `/org/deepin/dde/Launcher1` |

#### 关键方法

| 方法 | 参数 | 说明 |
|------|------|------|
| `Show` | - | 显示启动器 |
| `Hide` | - | 隐藏启动器 |
| `Toggle` | - | 切换启动器显示/隐藏 |
| `ShowByMode` | `int64 mode` | 按指定模式显示 |
| `Exit` | - | 退出启动器 |

#### 关键属性

| 属性 | 类型 | 说明 |
|------|------|------|
| `Visible` | `b` | 启动器是否可见 |

#### 关键信号

| 信号 | 说明 |
|------|------|
| `Shown` | 启动器已显示 |
| `Closed` | 启动器已关闭 |
| `VisibleChanged(bool visible)` | 可见性变化 |

### 其他引用的 DBus 接口

dde-launchpad 内部还引用以下 DBus 接口：
- `org.deepin.dde.daemon.Launcher1` — 守护进程启动器接口
- `org.deepin.dde.daemon.Dock1` — Dock 接口
- `org.deepin.dde.Appearance1` — 外观管理接口
- `org.deepin.dde.Display1` — 显示管理接口

## 9. 插件开发

dde-launchpad 提供一个 dde-shell applet 插件（`shell-launcher-applet`）：

- 插件元数据：`shell-launcher-applet/package/metadata.json`
- 通过 dde-shell 的 `ds_install_package` 机制安装
- 插件 ID 定义在 `metadata.json` 中
