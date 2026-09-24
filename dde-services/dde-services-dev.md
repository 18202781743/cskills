# dde-services 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-services |
| 版本 | 1.0.0 |
| 描述 | DDE 服务框架，通过 deepin-service-manager 管理的插件式服务，提供主题管理、壁纸缓存、快捷键、电源、环境设置等功能 |
| CMake target | 不适用（插件形式部署） |
| find_package 名 | 不适用 |
| 头文件安装路径 | 不适用（不安装公共开发头文件） |
| 仓库地址 | https://github.com/linuxdeepin/dde-services.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6widgets6, libqt6dbus6 (>= 6.x)
- libdtk6core, libdtk6gui, libdtk6widget
- deepin-service-manager

### 开发依赖
- Qt 6 Core, Gui, Widgets, DBus (>= 6.x)
- DTK6 Core, Gui, Widget
- CMake >= 3.16

## 3. CMake 集成

不适用（不导出 CMake 配置文件，不提供库 target 供外部链接）

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（不导出公共 C++ 命名空间）

## 6. 关键公共类及功能描述

dde-services 由多个插件服务组成：

| 插件 | 说明 |
|------|------|
| `thememanager` | 主题管理服务 |
| `wallpapercache` | 壁纸缓存服务，包含 `WallpaperCacheService`、`ImageEffect1Service`、`ImageBlur1Service` |
| `wallpaperslideshow` | 壁纸轮播服务 |
| `xsettings` | X 设置服务 |
| `ambient-brightness` | 环境亮度服务，`AmbientBrightnessService` |
| `power` | 电源管理服务 |
| `shortcut` | 快捷键服务，包含 `PluginShortcutManager` |
| `plugin-ipwatchd` | IP 冲突检测（sdbus 插件） |

### plugin-qt 类

| 类 | 功能 |
|------|------|
| `WallpaperCacheService` | 壁纸缓存管理 |
| `ImageEffect1Service` | 图像效果服务 |
| `ImageBlur1Service` | 图像模糊服务 |
| `AmbientBrightnessService` | 环境亮度管理 |
| `PluginShortcutManager` | 快捷键插件管理器 |

## 7. QML 模块

不适用

## 8. DBus 接口

### org.deepin.dde.WallpaperSlideshow

| 项目 | 内容 |
|------|------|
| 服务名 | `org.deepin.dde.WallpaperSlideshow` |
| 说明 | 壁纸轮播控制接口 |

### 其他服务接口

各插件通过 deepin-service-manager 启动并注册 DBus 服务，具体接口在各插件内部定义。

## 9. 插件开发

dde-services 支持两种插件类型：

### plugin-qt（Qt 插件）

- 安装路径：`${CMAKE_INSTALL_LIBDIR}/deepin-service-manager/`
- 配置文件路径：`share/deepin-service-manager/system/`
- JSON 配置文件描述插件元数据
- 示例：参见 `src/demo/plugin-qt/demo1`、`src/demo/plugin-qt/demo2`

### plugin-sdbus（sdbus 插件）

- 安装路径：`${CMAKE_INSTALL_LIBDIR}/deepin-service-manager/`
- 配置文件路径：`share/deepin-service-manager/user/`（用户级）或 `system/`（系统级）
- 通过 sdbus 框架与 DBus 交互
- 示例：参见 `src/demo/plugin-sdbus/demo1`
