# dde-application-manager 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-application-manager |
| 版本 | 0.2.2 |
| 描述 | DDE 应用管理器，提供应用生命周期管理、启动/停止应用、应用间通信等能力，基于 Desktop Specification 实现 |
| CMake target | 不适用（不导出 CMake target） |
| find_package 名 | 不适用 |
| 头文件安装路径 | 不适用（不安装开发头文件） |
| 仓库地址 | https://github.com/linuxdeepin/dde-application-manager.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6dbus6, libqt6concurrent6, libqt6waylandclient6 (>= 6.x)
- libdtk6core

### 开发依赖
- Qt 6 Core, DBus, Concurrent, WaylandClient, Gui (>= 6.x)
- Dtk6 Core
- TreelandProtocols
- CMake >= 3.20

## 3. CMake 集成

不适用（dde-application-manager 不导出 CMake 配置文件或 target。二次开发通过 DBus 接口与应用管理器交互）

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（不安装公共头文件）

## 6. 关键公共类及功能描述

dde-application-manager 为运行时服务，不提供公共 C++ API 类。核心功能通过 DBus 接口暴露：

| 功能 | 说明 |
|------|------|
| 应用生命周期管理 | 启动、停止、查询应用状态 |
| 应用实例管理 | 支持多实例应用 |
| Job 管理 | 异步操作通过 Job 接口跟踪 |
| 对象管理 | 通过 ObjectManager 接口管理应用对象 |

## 7. QML 模块

不适用

## 8. DBus 接口

### org.desktopspec.ApplicationManager1

| 属性 | 内容 |
|------|------|
| 服务名 | `org.desktopspec.ApplicationManager1` |
| 对象路径 | `/org/desktopspec/ApplicationManager1` |

关键方法：

| 方法 | 说明 |
|------|------|
| `Launch` | 启动应用 |
| `LaunchApp` | 通过 desktop file 启动应用 |
| `Identify` | 标识应用 |
| `AddToLauncher` | 添加应用到启动器 |
| `RemoveFromLauncher` | 从启动器移除应用 |
| `Hide` | 隐藏应用 |
| `Show` | 显示应用 |
| `RequestClipboard` | 请求剪贴板访问 |

关键信号：

| 信号 | 说明 |
|------|------|
| `ApplicationLaunched` | 应用已启动 |
| `ApplicationClosed` | 应用已关闭 |
| `ApplicationAdded` | 应用已添加 |
| `ApplicationRemoved` | 应用已移除 |

### org.desktopspec.ApplicationManager1.Application

| 属性 | 内容 |
|------|------|
| 对象路径 | `/org/desktopspec/ApplicationManager1/{app-id}` |

关键属性/方法：
- `id` — 应用 ID
- `applicationName` — 应用名称
- `iconName` — 图标名
- `display` — 显示名
- `Launch(...)` — 启动此应用
- `IsRunning()` — 是否运行中
- `GetWindow()` — 获取窗口信息

### org.desktopspec.JobManager1.Job

| 属性 | 内容 |
|------|------|
| 对象路径 | `/org/desktopspec/JobManager1/{job-id}` |

用于跟踪异步操作（如应用启动），提供 `Cancel()`、`Status` 等接口。

### org.desktopspec.ObjectManager1

标准 ObjectManager 接口，管理 Application 对象的创建和删除，提供 `GetManagedObjects()` 方法。

## 9. 插件开发

不适用（dde-application-manager 不提供插件开发接口）
