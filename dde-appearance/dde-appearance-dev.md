# dde-appearance 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-appearance |
| 版本 | （跟随仓库 master 分支） |
| 描述 | DDE 外观管理服务，负责主题、图标、光标、字体、壁纸、缩放等外观设置的 DBus 服务 |
| CMake target | 不适用（不导出库 target） |
| find_package 名 | 不适用 |
| 头文件安装路径 | 不适用（不安装公共开发头文件） |
| 仓库地址 | https://github.com/linuxdeepin/dde-appearance.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6dbus6, libqt6widgets6 (>= 6.x)
- libdtk6core, libdtk6gui

### 开发依赖
- Qt 6 Core, Gui, Widgets, DBus (>= 6.x)
- DTK6 Core, Gui
- CMake >= 3.16

## 3. CMake 集成

不适用（不导出 CMake 配置文件，不提供库 target 供外部链接）

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（不导出公共 C++ 命名空间）

## 6. 关键公共类及功能描述

dde-appearance 以 DBus 服务方式运行，核心类在内部使用：

| 类 | 功能 |
|------|------|
| `AppearanceManager` | 外观管理核心类，实现 `org.deepin.dde.Appearance1` DBus 接口 |
| `FakeWM` | 窗口管理器代理，实现 `com.deepin.wm` DBus 接口 |

## 7. QML 模块

不适用

## 8. DBus 接口

### org.deepin.dde.Appearance1

| 项目 | 内容 |
|------|------|
| 服务名 | `org.deepin.dde.Appearance1` |
| 对象路径 | `/org/deepin/dde/Appearance1` |

#### 关键方法

| 方法 | 参数 | 说明 |
|------|------|------|
| `Set` | `string ty, string value` | 设置外观项（类型可为 theme、icon、cursor、font、fontSize、wallpaper 等） |
| `Get` | `string ty` | 获取外观项当前值 |
| `List` | `string ty` | 列出指定类型的可选项 |
| `Show` | `string ty, string[] names` | 显示指定类型的外观预览 |
| `Thumbnail` | `string ty, string name` | 获取缩略图路径 |
| `Delete` | `string ty, string name` | 删除自定义外观项 |
| `SetScaleFactor` | `double scale` | 设置缩放比例 |
| `GetScaleFactor` | - | 获取缩放比例 |
| `SetCurrentWorkspaceBackground` | `string uri` | 设置当前工作区壁纸 |
| `GetCurrentWorkspaceBackground` | - | 获取当前工作区壁纸 |
| `SetCurrentWorkspaceBackgroundForMonitor` | `string uri, string monitorName` | 为指定显示器设置壁纸 |
| `SetWallpaperSlideShow` | `string monitorName, string slideShow` | 设置壁纸轮播 |
| `Reset` | - | 重置所有外观设置 |

### com.deepin.wm

| 项目 | 内容 |
|------|------|
| 服务名 | `com.deepin.wm` |
| 对象路径 | `/com/deepin/wm` |

#### 关键属性

| 属性 | 类型 | 说明 |
|------|------|------|
| `compositingEnabled` | `b` | 合成是否启用 |
| `compositingPossible` | `b` | 是否支持合成 |
| `compositingAllowSwitch` | `b` | 是否允许切换合成 |
| `zoneEnabled` | `b` | 热区是否启用 |
| `cursorTheme` | `s` | 光标主题 |
| `cursorSize` | `i` | 光标大小 |

#### 关键方法

| 方法 | 说明 |
|------|------|
| `SwitchApplication(bool backward)` | 切换应用 |
| `ToggleActiveWindowMaximize` | 切换当前窗口最大化 |
| `MinimizeActiveWindow` | 最小化当前窗口 |
| `ShowWorkspace` | 显示工作区 |
| `ShowAllWindow` | 显示所有窗口 |
| `PerformAction(int type)` | 执行指定操作 |

## 9. 插件开发

不适用
