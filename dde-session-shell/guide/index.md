# dde-session-shell 二次开发文档 · 概览

## 项目定位

dde-session-shell 是 DDE 登录锁屏壳，提供登录界面（lightdm-deepin-greeter）和锁屏界面（dde-lock）。支持登录插件、托盘插件和辅助登录插件扩展，允许第三方通过继承接口实现自定义登录认证界面和托盘功能。

## 导出类型

- [插件接口（C++）](plugin-interface.md)：C++ 插件接口，包括模块基础接口、V2 登录模块接口、认证回调数据结构和托盘模块接口，用于开发登录认证插件和托盘插件。
- [辅助登录接口（C）](assist-login-interface.md)：C 语言辅助认证接口，用于通过 C 函数与认证服务交互，发送账号密码进行认证。

## 按功能查阅

- 将 dde-session-shell 公开头文件引入 CMake 工程：参见[插件接口（C++）](plugin-interface.md#集成)的 CMake 配置。
- 开发登录认证插件：参见 [LoginModuleInterfaceV2](plugin-interface.md#loginmoduleinterfacev2) 与 [BaseModuleInterface](plugin-interface.md#basemoduleinterface)。
- 传递认证结果数据：参见 [AuthCallbackData](plugin-interface.md#authcallbackdata)。
- 开发托盘插件：参见 [TrayModuleInterface](plugin-interface.md#traymoduleinterface) 与 [BaseModuleInterface](plugin-interface.md#basemoduleinterface)。
- 通过 C 接口与认证服务交互：参见 [辅助登录接口（C）](assist-login-interface.md)。
