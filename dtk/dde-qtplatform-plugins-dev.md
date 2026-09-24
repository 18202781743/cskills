# dde-qtplatform-plugins 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-qtplatform-plugins |
| 版本 | 6.7.50 |
| 描述 | DTK Qt 平台插件（QPA），为 Qt 应用提供 XCB 和 Wayland 平台支持，集成 DDE 平台特性 |
| CMake target | 不适用（安装平台插件，不导出 CMake target） |
| find_package 名 | 不适用 |
| 头文件安装路径 | 不适用（使用 Qt 私有 API，不安装公共头文件） |
| 仓库地址 | https://github.com/linuxdeepin/dde-qtplatform-plugins.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6xcbqpa6 (>= 6.x)
- libdtk6core, libdtk6gui

### 开发依赖
- Qt 6 Core, Qt 6 Gui, Qt 6 GuiPrivate (>= 6.x)
- dtkcore, dtkgui
- CMake >= 3.16

## 3. CMake 集成

不适用（dde-qtplatform-plugins 安装 Qt 平台插件，不提供 CMake 配置文件或导出 target。应用通过设置 `QT_QPA_PLATFORM` 环境变量使用）

### 使用方式

```bash
# 使用 XCB 平台插件
QT_QPA_PLATFORM=dpp

# 使用 Wayland 平台插件
QT_QPA_PLATFORM=dwayland
```

或在代码中：

```cpp
qputenv("QT_QPA_PLATFORM", "dpp");
```

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（不安装公共头文件）

## 6. 关键公共类及功能描述

dde-qtplatform-plugins 不提供公共 API 类，它通过 Qt 平台插件机制工作，为 Qt 应用提供以下增强功能：

| 插件 | 功能 |
|------|------|
| `dpp`（XCB） | XCB 平台插件，集成 DDE 窗口管理特性（圆角窗口、无边框模式等） |
| `dwayland`（Wayland） | Wayland 平台插件，集成 DDE Wayland 特性 |

插件安装路径：
- `${CMAKE_INSTALL_LIBDIR}/qt6/plugins/platforms/`（平台插件）
- `${CMAKE_INSTALL_LIBDIR}/qt6/plugins/wayland-shell-integration/`（Wayland Shell 集成）

## 7. QML 模块

不适用

## 8. DBus 接口

不适用

## 9. 插件开发

dde-qtplatform-plugins 本身是 Qt 平台插件，不提供二次开发插件接口。如需自定义平台行为，需直接修改源码并重新编译。

### 捆绑的 Qt 私有 API

项目在 `xcb/libqt6xcbqpa-dev/` 目录下捆绑了 Qt6 XCB QPA 私有头文件，用于实现 XCB 平台增强。
