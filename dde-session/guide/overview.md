# dde-session 二次开发文档 · 概览

## 项目定位

dde-session 是 DDE 会话管理组件，负责会话启动、会话状态管理和会话控制工具。提供会话管理器主程序和多个辅助工具，通过 DBus 接口向外部提供会话管理能力。

## 术语与缩写

- **会话**：用户登录后的桌面会话实例。
- **OOM 评分**：内核 OOM（Out-Of-Memory）killer 使用的进程评分，影响进程被杀死的优先级。
- **DBus 属性**：远端接口上的具名值，使用方可读取或监听变化。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以 DBus 接口名和组件名为章节，逐一说明各接口和组件的定位、功能能力和使用场景。

## 全局约定

dde-session 不安装公共开发头文件，不导出 C++ 命名空间或 CMake 库目标。使用方通过 DBus 接口或命令行工具访问会话管理功能。dde-session 内部引用 freedesktop.login1 和 systemd1 等 DBus 接口。

## 按功能查阅

- 通过 DBus 访问会话管理服务：参见 [org.deepin.dde.Session1](modules.md#orgdeepinddesession1)。
- 了解各命令行工具用途：参见 [dde-session-ctl](modules.md#dde-session-ctl)、[dde-version-checker](modules.md#dde-version-checker)、[dde-oom-score-adj](modules.md#dde-oom-score-adj)、[dde-quick-login](modules.md#dde-quick-login)、[dde-keyring-checker](modules.md#dde-keyring-checker)、[dde-xsettings-checker](modules.md#dde-xsettings-checker)。
- 将 dde-session 引入工程：参见[集成与构建配置](integration.md)。
