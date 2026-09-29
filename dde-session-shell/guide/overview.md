# dde-session-shell 二次开发文档 · 概览

## 项目定位

dde-session-shell 是 DDE 登录锁屏壳，提供登录界面（lightdm-deepin-greeter）和锁屏界面（dde-lock）。支持登录插件、托盘插件和 assist_login 插件扩展，允许第三方通过继承接口实现自定义登录界面和托盘功能。

## 术语与缩写

- **greeter**：登录管理器的前端界面程序。
- **登录插件**：在登录界面中提供自定义认证 UI 的插件模块。
- **托盘插件**：在登录或锁屏界面中提供托盘功能的插件模块。
- **assist_login 插件**：通过 C 接口实现的厂商密码接收插件。
- **模块类型**：区分插件加载方式的枚举，包括登录型、托盘型、全托管登录型、进程辅助登录型和密码扩展登录型。

## 导出类型

[导出类型介绍](dde-session-shell-dev.md)是本项目唯一的类型参考文档。以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 全局约定

公开头文件安装在 `dde-session-shell/` 目录下。C++ 接口类型位于 `dss::module` 和 `dss::module_v2` 命名空间。插件通过 Qt Plugin 机制加载和注册。登录插件推荐使用 V2 接口，V1 接口已过时。

## 按功能查阅

- 将 dde-session-shell 头文件引入 CMake 工程：参见[集成与构建配置](integration.md)。
- 开发登录插件：参见 [LoginModuleInterfaceV2](dde-session-shell-dev.md#loginmoduleinterfacev2) 与 [BaseModuleInterface](dde-session-shell-dev.md#basemoduleinterface)。
- 开发托盘插件：参见 [TrayModuleInterface](dde-session-shell-dev.md#traymoduleinterface) 与 [BaseModuleInterface](dde-session-shell-dev.md#basemoduleinterface)。
- 开发 assist_login 插件：参见 [assist_login_interface](dde-session-shell-dev.md#assist_login_interface)。
