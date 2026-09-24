# deepin-screensaver 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | deepin-screensaver |
| 版本 | （跟随仓库 master 分支） |
| 描述 | DDE 屏幕保护程序，提供屏保启动/停止、预览、配置等功能 |
| CMake target | 不适用（不导出库 target） |
| find_package 名 | 不适用 |
| 头文件安装路径 | 不适用（不安装公共开发头文件） |
| 仓库地址 | https://github.com/linuxdeepin/deepin-screensaver.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6widgets6, libqt6dbus6 (>= 6.x)
- libdtk6widget, libdtk6core, libdtk6gui

### 开发依赖
- Qt 6 Core, Gui, Widgets, DBus (>= 6.x)
- DTK6 Widget, Core, Gui
- CMake >= 3.16

## 3. CMake 集成

不适用（不导出 CMake 配置文件，不提供库 target 供外部链接）

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（不导出公共 C++ 命名空间）

## 6. 关键公共类及功能描述

| 组件 | 说明 |
|------|------|
| `deepin-screensaver` | 屏幕保护主程序，通过 DBus 接口控制屏保的启动、停止、预览和配置 |

## 7. QML 模块

不适用

## 8. DBus 接口

### com.deepin.ScreenSaver

| 项目 | 内容 |
|------|------|
| 服务名 | `com.deepin.ScreenSaver` |
| 对象路径 | `/com/deepin/ScreenSaver` |

#### 关键方法

| 方法 | 参数 | 说明 |
|------|------|------|
| `Start` | - | 启动屏保 |
| `Stop` | - | 停止屏保 |
| `Preview` | `string name, int staysOn` | 预览指定屏保（0=底层，1=顶层） |
| `GetScreenSaverCover` | `string name` | 获取屏保封面图路径 |
| `StartCustomConfig` | `string name` | 启动自定义配置 |
| `ConfigurableItems` | - | 获取可配置项列表 |
| `IsConfigurable` | `string name` | 判断指定屏保是否可配置 |
| `RefreshScreenSaverList` | - | 刷新屏保列表 |

#### 关键属性

| 属性 | 类型 | 说明 |
|------|------|------|
| `isRunning` | `b` | 屏保是否正在运行 |
| `currentScreenSaver` | `s` | 当前屏保名称（可读写） |
| `allScreenSaver` | `as` | 所有可用屏保列表 |

## 9. 插件开发

不适用
