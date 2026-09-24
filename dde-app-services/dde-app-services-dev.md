# dde-app-services 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-app-services |
| 版本 | 1.0.0 |
| 描述 | DDE 应用服务，核心为 DConfig（DDE 配置中心），提供配置管理守护进程、命令行工具和图形编辑器 |
| CMake target | 不适用（不导出库 target） |
| find_package 名 | 不适用 |
| 头文件安装路径 | 不适用（不安装公共开发头文件） |
| 仓库地址 | https://github.com/linuxdeepin/dde-app-services.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6dbus6 (>= 6.x)
- libdtk6core

### 开发依赖
- Qt 6 Core, DBus (>= 6.x)
- DTK6 Core
- CMake >= 3.10

## 3. CMake 集成

不适用（不导出 CMake 配置文件，不提供库 target 供外部链接）

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（不导出公共 C++ 命名空间）

## 6. 关键公共类及功能描述

DConfig 系统主要通过 DBus 进行交互，核心组件包括：

| 组件 | 说明 |
|------|------|
| `dde-dconfig-daemon` | DConfig 守护进程，提供配置读写服务 |
| `dde-dconfig` | 命令行工具，用于读取和修改 DConfig 配置项 |
| `dde-dconfig-editor` | 图形化 DConfig 配置编辑器 |

### 命令行工具 `dde-dconfig`

```bash
# 读取配置
dde-dconfig get -a <appid> -k <key>

# 写入配置
dde-dconfig set -a <appid> -k <key> -v <value>

# 列出所有配置
dde-dconfig list -a <appid>
```

## 7. QML 模块

不适用

## 8. DBus 接口

### org.desktopspec.ConfigManager

DConfig 守护进程实现了 freedesktop 桌面规范配置管理接口。

| 项目 | 内容 |
|------|------|
| 服务名 | `org.desktopspec.ConfigManager` |
| 对象路径 | `/org/desktopspec/ConfigManager` |

#### 关键方法

| 方法 | 说明 |
|------|------|
| `GetValue(string appId, string key)` | 获取指定应用的配置值 |
| `SetValue(string appId, string key, variant value)` | 设置指定应用的配置值 |
| `List(string appId)` | 列出指定应用的所有配置项 |

### org.desktopspec.ConfigManager.Manager

管理接口，用于配置资源管理。

| 项目 | 内容 |
|------|------|
| 服务名 | `org.desktopspec.ConfigManager.Manager` |
| 对象路径 | `/org/desktopspec/ConfigManager/Manager` |

## 9. 插件开发

不适用
