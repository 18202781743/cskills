# 导出类型介绍

dde-session-shell 提供登录插件接口、托盘插件接口和 assist_login C 接口，包括模块基础接口定义、模块类型与加载类型枚举、V2 登录模块接口支持认证回调、托盘模块接口，以及 C 语言辅助认证接口。

## BaseModuleInterface

### 定位

所有模块的基础接口，位于 `dss::module` 命名空间。定义模块的初始化、标识、内容和类型，是登录插件和托盘插件的共同基类。

### 功能能力总结

提供以下能力：

- 界面相关初始化（`init` 方法，在主线程调用）
- 返回插件唯一标识（`key` 方法）
- 返回模块的 QWidget（`content` 方法）
- 返回模块类型（`type` 方法，返回值包括 LoginType、TrayType、FullManagedLoginType、IpcAssistLoginType、PasswordExtendLoginType）
- 返回加载类型（`loadPluginType` 方法，返回 Load 或 Notload）

### 使用场景

开发登录插件或托盘插件时，作为插件基类继承。

## LoginModuleInterfaceV2

### 定位

V2 登录模块接口，位于 `dss::module_v2` 命名空间。替代已过时的 V1 接口 `dss::module::LoginModuleInterface`，支持认证回调。

### 功能能力总结

提供以下能力：

- 设置认证回调函数（`setAuthCallback` 方法，参数为 `AuthCallbackFun`）
- 返回插件图标（`icon` 方法）
- 重置 UI 和验证状态（`reset` 方法）

### 使用场景

需要开发登录界面认证插件并使用认证回调时。从 V1 迁移时，改用 V2 接口并实现 `setAuthCallback`、`icon`、`reset` 方法。

## TrayModuleInterface

### 定位

托盘模块接口，位于 `dss::module` 命名空间。定义托盘插件需要实现的接口，包括图标、项部件、提示部件和上下文菜单。

### 功能能力总结

提供以下能力：

- 返回托盘插件图标（`icon` 方法）
- 返回托盘项部件（`itemWidget` 方法）
- 返回托盘项提示部件（`itemTipsWidget` 方法）
- 返回托盘项上下文菜单（`itemContextMenu` 方法）

### 使用场景

需要开发登录或锁屏界面中的托盘插件时。

## assist_login_interface

### 定位

C 语言辅助认证接口，面向需要以 C 函数形式实现厂商密码接收的调用者。头文件为 `assist_login_interface.h`，无命名空间。

### 功能能力总结

提供以下能力：

- 发送账号密码进行认证（`sendAuth` 函数，参数为 `const char *account`、`unsigned char *pw`、`int len`）
- 判断认证服务是否已开启（`authServiceStarted` 函数）
- 获取非对称加密公钥（`getPublicEncrypt` 函数）

### 使用场景

需要实现厂商密码接收插件并通过 C 接口与认证服务交互时。
