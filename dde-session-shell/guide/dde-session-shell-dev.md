# 导出类型介绍

dde-session-shell 提供登录插件接口、托盘插件接口和 assist_login C 接口，包括模块基础接口定义、模块类型与加载类型枚举、V2 登录模块接口支持认证回调与消息通信、托盘模块接口支持菜单响应与消息通信，以及 C 语言辅助认证接口。

## BaseModuleInterface

### 定位

所有模块的基础接口，位于 `dss::module` 命名空间。定义模块的初始化、标识、内容和类型，是登录插件和托盘插件的共同基类。

### 功能能力总结

- 界面相关初始化（在主线程调用）
- 返回插件唯一标识
- 返回模块的窗口组件
- 返回模块类型（包括登录类型、托盘类型、全托管登录类型、IPC 辅助登录类型、密码扩展登录类型）
- 返回加载类型（包括加载和不加载）

### 使用场景

开发登录插件或托盘插件时，作为插件基类继承。

## LoginModuleInterfaceV2

### 定位

V2 登录模块接口，位于 `dss::module_v2` 命名空间。替代已过时的 V1 接口，支持认证回调与消息通信。V2 头文件通过 `using` 声明引入以下类型：`AuthResult`、`AuthType`、`AuthState`、`AppType`、`DefaultAuthLevel` 来自 `login_module_interface.h`，`AppDataPtr`、`MessageCallbackFunc` 来自 `base_module_interface.h`。使用 V2 时需同时包含 `login_module_interface.h` 和 `base_module_interface.h`，V1 接口本身已过时，但其中定义的类型仍为 V2 所用。V2 头文件还定义了 `AuthCallbackData` 结构体（详见独立章节）和 `AuthObjectType` 枚举。`AuthObjectType` 用于标识验证对象的类型，包括 `LightDM`（lightdm 显示管理器）和 `DeepinAuthenticate`（深度认证框架）两个枚举值。

### 功能能力总结

- 设置认证回调函数
- 设置消息回调函数
- 设置登录器回调指针
- 接收登录器发送的消息并返回响应
- 返回插件图标
- 重置 UI 和验证状态

### 使用场景

需要开发登录界面认证插件并使用认证回调时。从 V1 迁移时，改用 V2 接口并实现 `setAuthCallback`、`icon`、`reset` 方法，同时可按需实现 `setMessageCallback`、`setAppData`、`message` 方法以支持消息通信。

## AuthCallbackData

### 定位

认证回调数据结构体，位于 `dss::module_v2` 命名空间，定义于 `login_module_interface_v2.h`。V2 版本使用 `QString` 字段（区别于 V1 中的 `std::string` 版本），作为认证回调函数的参数传递认证结果数据。

### 功能能力总结

- 携带认证结果（`result`，取值为 `AuthResult` 枚举值）
- 携带账户名（`account`）
- 携带令牌（`token`）
- 携带提示消息（`message`）
- 携带预留数据（`json`）

### 使用场景

在 V2 登录插件中，认证完成后需要将认证结果回传给登录器时，填充此结构体并通过 `AuthCallbackFun` 回调函数传递。

## TrayModuleInterface

### 定位

托盘模块接口，位于 `dss::module` 命名空间。定义托盘插件需要实现的接口，包括图标、项部件、提示部件和上下文菜单，以及菜单点击响应与消息通信。

### 功能能力总结

- 返回托盘插件图标
- 返回托盘项部件
- 返回托盘项提示部件
- 返回托盘项上下文菜单
- 响应菜单项点击
- 设置消息回调函数
- 设置登录器回调指针
- 接收登录器发送的消息并返回响应

### 使用场景

需要开发登录或锁屏界面中的托盘插件时。

## assist_login_interface

### 定位

C 语言辅助认证接口，面向需要以 C 函数形式实现厂商密码接收的调用者。头文件为 `assist_login_interface.h`，无命名空间，使用 `extern "C"` 声明。需链接共享库 `libassist_Login_interface.so`，与 C++ 插件接口的集成方式不同。

### 功能能力总结

- 发送账号密码进行认证
- 判断认证服务是否已开启
- 获取非对称加密公钥

### 使用场景

需要实现厂商密码接收插件并通过 C 接口与认证服务交互时。
