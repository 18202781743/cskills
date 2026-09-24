# dde-session 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-session |
| 版本 | （跟随仓库 master 分支） |
| 描述 | DDE 会话管理，负责会话启动、会话管理器和会话控制工具 |
| CMake target | 不适用（不导出库 target） |
| find_package 名 | 不适用 |
| 头文件安装路径 | 不适用（不安装公共开发头文件） |
| 仓库地址 | https://github.com/linuxdeepin/dde-session.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6dbus6 (>= 6.x)
- libdtk6core, libdtk6tools
- systemd

### 开发依赖
- Qt 6 Core, DBus (>= 6.x)
- DTK6 Core, Tools
- CMake >= 3.13

## 3. CMake 集成

不适用（不导出 CMake 配置文件，不提供库 target 供外部链接）

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（不导出公共 C++ 命名空间）

## 6. 关键公共类及功能描述

| 组件 | 说明 |
|------|------|
| `dde-session` | 会话管理器主程序，负责启动和管理 DDE 会话 |
| `dde-session-ctl` | 会话控制工具，用于会话状态查询和控制 |
| `dde-version-checker` | 版本检查工具 |
| `dde-oom-score-adj` | OOM 评分调整工具 |
| `dde-quick-login` | 快速登录工具 |
| `dde-keyring-checker` | 密钥环检查工具 |
| `dde-xsettings-checker` | X 设置检查工具 |

## 7. QML 模块

不适用

## 8. DBus 接口

### org.deepin.dde.Session1

| 项目 | 内容 |
|------|------|
| 服务名 | `org.deepin.dde.Session1` |
| 说明 | DDE 会话管理服务 |

### 引用的 DBus 接口

dde-session 内部引用以下 DBus 接口：

| DBus 服务 | 接口 | 说明 |
|-----------|------|------|
| `org.freedesktop.login1` | `org.freedesktop.login1.Manager` | systemd 登录管理器 |
| `org.freedesktop.login1` | `org.freedesktop.login1.User` | 用户会话管理 |
| `org.freedesktop.login1` | `org.freedesktop.login1.Session` | 会话管理 |
| `org.deepin.dde.Daemon1` | `org.deepin.dde.Daemon1` | DDE 守护进程 |
| `org.freedesktop.systemd1` | `org.freedesktop.systemd1.Job` | systemd 任务管理 |

## 9. 插件开发

不适用
