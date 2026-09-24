# dde-session-shell 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-session-shell |
| 版本 | API 2.0.0 |
| 描述 | DDE 登录锁屏壳，提供登录界面（lightdm-deepin-greeter）和锁屏界面（dde-lock），支持登录插件和托盘插件扩展 |
| CMake target | 不适用（不导出库 target） |
| find_package 名 | 不适用 |
| 头文件安装路径 | `/usr/include/dde-session-shell/`（仅 assist_login_interface.h） |
| 仓库地址 | https://github.com/linuxdeepin/dde-session-shell.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6widgets6, libqt6dbus6 (>= 6.x)
- libdtk6widget, libdtk6core, libdtk6gui
- lightdm

### 开发依赖
- Qt 6 Core, Gui, Widgets, DBus (>= 6.x)
- DTK6 Widget, Core, Gui
- CMake >= 3.16

## 3. CMake 集成

不适用（不导出 CMake 配置文件，不提供库 target 供外部链接）

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

- `dss::module` — 登录/托盘插件接口命名空间
- `dss::module_v2` — V2 登录插件接口命名空间

## 6. 关键公共类及功能描述

### 基础模块接口

| 头文件 | 命名空间 | 类 | 功能 |
|--------|----------|-----|------|
| `base_module_interface.h` | `dss::module` | `BaseModuleInterface` | 所有模块的基础接口，定义模块类型、加载类型等 |
| `login_module_interface.h` | `dss::module` | （已过时，请使用 V2） | V1 登录模块接口 |
| `login_module_interface_v2.h` | `dss::module_v2` | `LoginModuleInterfaceV2` | V2 登录模块接口，支持认证回调 |
| `tray_module_interface.h` | `dss::module` | `TrayModuleInterface` | 托盘模块接口 |

### BaseModuleInterface 关键方法

| 方法 | 说明 |
|------|------|
| `init()` | 界面相关初始化（在主线程调用） |
| `key() const` | 返回插件唯一标识 |
| `content()` | 返回模块的 QWidget |
| `type() const` | 返回模块类型（LoginType/TrayType/FullManagedLoginType 等） |
| `loadPluginType() const` | 返回加载类型（Load/Notload） |

### 模块类型枚举

| 类型 | 说明 |
|------|------|
| `LoginType` | 登录插件 |
| `TrayType` | 托盘插件 |
| `FullManagedLoginType` | 全托管插件 |
| `IpcAssistLoginType` | 厂商密码接收插件 |
| `PasswordExtendLoginType` | 密码认证扩展插件 |

### LoginModuleInterfaceV2 关键方法

| 方法 | 说明 |
|------|------|
| `setAuthCallback(AuthCallbackFun)` | 设置认证回调函数 |
| `icon() const` | 返回插件图标 |
| `reset()` | 重置 UI 和验证状态 |

### assist_login_interface.h（C 接口）

| 函数 | 说明 |
|------|------|
| `sendAuth(const char *account, unsigned char *pw, int len)` | 发送账号密码进行认证 |
| `authServiceStarted()` | 判断认证服务是否已开启 |
| `getPublicEncrypt()` | 获取非对称加密公钥 |

## 7. QML 模块

不适用

## 8. DBus 接口

不适用（dde-session-shell 作为 DBus 服务消费者，不导出 DBus 服务接口）

## 9. 插件开发

dde-session-shell 支持以下插件类型：

### 登录插件

1. 继承 `dss::module_v2::LoginModuleInterfaceV2`（推荐）或 `dss::module::LoginModuleInterface`（已过时）
2. 实现 `init()`、`key()`、`content()`、`type()`、`setAuthCallback()` 等方法
3. 使用 `Q_DECLARE_INTERFACE` 声明接口：`com.deepin.dde.shell.Modules`
4. 使用 `Q_PLUGIN_METADATA` 注册插件

### 托盘插件

1. 继承 `dss::module::TrayModuleInterface`
2. 实现 `icon()`、`itemWidget()`、`itemTipsWidget()`、`itemContextMenu()` 等方法
3. 插件通过 Qt Plugin 机制加载

### assist_login 插件

1. 实现 `assist_login_interface.h` 中的 C 函数接口
2. 头文件安装路径：`/usr/include/dde-session-shell/`
