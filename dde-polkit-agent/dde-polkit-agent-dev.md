# dde-polkit-agent 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-polkit-agent |
| 版本 | （跟随仓库 master 分支） |
| 描述 | DDE Polkit 认证代理，为需要提权的操作提供图形化认证对话框 |
| CMake target | 不适用（不导出库 target） |
| find_package 名 | 不适用 |
| 头文件安装路径 | `${CMAKE_INSTALL_INCLUDEDIR}/dpa/`（安装扩展接口头文件） |
| 仓库地址 | https://github.com/linuxdeepin/dde-polkit-agent.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6widgets6, libqt6dbus6 (>= 6.x)
- libdtk6widget, libdtk6core, libdtk6gui
- polkit-1

### 开发依赖
- Qt 6 Core, Gui, Widgets, DBus (>= 6.x)
- DTK6 Widget, Core
- CMake >= 3.16

## 3. CMake 集成

不适用（不导出 CMake 配置文件，不提供库 target 供外部链接）

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

- `dpa` — polkit agent 扩展接口命名空间

## 6. 关键公共类及功能描述

| 头文件 | 命名空间 | 类 | 功能 |
|--------|----------|-----|------|
| `agent-extension.h` | `dpa` | `AgentExtension` | 认证代理扩展接口，允许第三方扩展认证行为 |
| `agent-extension-proxy.h` | `dpa` | `AgentExtensionProxy` | 扩展代理，提供获取认证信息的接口 |

### AgentExtension 关键方法

| 方法 | 说明 |
|------|------|
| `initialize(AgentExtensionProxy *proxy)` | 使用代理对象初始化扩展 |
| `finalize()` | 释放扩展资源 |
| `interestedActions() const` | 声明感兴趣的认证动作 ID 列表 |
| `description() const` | 返回扩展的描述信息 |

### AgentExtensionProxy 关键方法

| 方法 | 说明 |
|------|------|
| `actionID() const` | 返回当前认证动作的 ID |
| `username() const` | 返回认证用户名 |
| `password() const` | 返回用户输入的密码 |

## 7. QML 模块

不适用

## 8. DBus 接口

### org.deepin.dde.Polkit1.AuthAgent

| 项目 | 内容 |
|------|------|
| 服务名 | `org.deepin.dde.Polkit1.AuthAgent` |
| 对象路径 | `/org/deepin/dde/Polkit1/AuthAgent` |

#### 关键方法

| 方法 | 参数 | 说明 |
|------|------|------|
| `setWIdForAction` | `string, uint64` | 为指定动作设置窗口 ID |

### 引用的 DBus 接口

- `org.deepin.dde.Accounts1` — 账户管理服务
- `org.deepin.dde.Accounts1.User` — 用户信息接口

## 9. 插件开发

dde-polkit-agent 支持通过 `AgentExtension` 接口进行扩展开发：

1. 继承 `dpa::AgentExtension` 类
2. 实现 `initialize`、`finalize`、`interestedActions`、`description` 方法
3. 通过 `AgentExtensionProxy` 获取认证信息
4. 头文件安装路径：`${CMAKE_INSTALL_INCLUDEDIR}/dpa/`
