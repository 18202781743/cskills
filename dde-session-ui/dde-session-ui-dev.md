# dde-session-ui 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-session-ui |
| 版本 | （跟随仓库 master 分支） |
| 描述 | DDE 会话 UI 组件集合，提供多种对话框和工具，包括黑屏提示、蓝牙对话框、许可证对话框、OSD、欢迎页等 |
| CMake target | 不适用（不导出库 target） |
| find_package 名 | 不适用 |
| 头文件安装路径 | 不适用（不安装公共开发头文件） |
| 仓库地址 | https://github.com/linuxdeepin/dde-session-ui.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6widgets6, libqt6dbus6 (>= 6.x)
- libdtk6widget, libdtk6core, libdtk6gui

### 开发依赖
- Qt 6 Core, Gui, Widgets, DBus (>= 6.x)
- DTK6 Widget, Core, Gui
- CMake >= 3.13

## 3. CMake 集成

不适用（不导出 CMake 配置文件，不提供库 target 供外部链接）

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（不导出公共 C++ 命名空间）

## 6. 关键公共类及功能描述

dde-session-ui 由多个独立组件构成：

| 组件 | 安装路径 | 功能 |
|------|----------|------|
| `dde-blackwidget` | `lib/deepin-daemon` | 黑屏/全屏遮罩组件 |
| `dde-bluetooth-dialog` | `lib/deepin-daemon` | 蓝牙设备对话框 |
| `dde-touchscreen-dialog` | `lib/deepin-daemon` | 触摸屏校准对话框 |
| `dde-license-dialog` | `bin` | 许可证对话框 |
| `dde-pixmix` | `bin` | 图片混合工具 |
| `dde-wm-chooser` | `bin` | 窗口管理器选择器 |
| `dde-hints-dialog` | `bin` | 提示对话框 |
| `dde-welcome` | `lib/deepin-daemon` | 欢迎页面 |
| `dde-suspend-dialog` | - | 挂起确认对话框 |
| `dde-osd` | - | 屏幕显示（OSD）通知 |
| `dde-lowpower` | - | 低电量警告 |
| `dde-warning-dialog` | - | 警告对话框 |
| `dde-switchtogreeter` | `bin` | 切换到 Greeter |
| `dmemory-warning-dialog` | `bin` | 内存警告对话框 |

## 7. QML 模块

不适用

## 8. DBus 接口

不适用（dde-session-ui 各组件主要通过命令行调用，部分组件消费 DBus 服务但不导出 DBus 接口）

## 9. 插件开发

不适用
