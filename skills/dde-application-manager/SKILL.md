---
name: dde-application-manager
description: 提供应用启动、应用属性管理、任务跟踪、MIME 类型管理、应用更新通知的 D-Bus 接口，应用启动次数记录与环境变量配置的 DConfig 配置项，应用启动与身份识别的 CLI 命令
Categories:
  - Application
---

# dde-application-manager

dde-application-manager 是 DDE 应用管理器组件，通过 Session 总线提供应用启动、应用属性管理、任务跟踪、MIME 类型管理和应用更新通知能力，并通过 DConfig 暴露自身配置、通过 CLI 工具提供命令行操作入口。

## D-Bus 接口

### 应用管理

提供应用列表查询、应用识别、用户应用增删和应用执行能力。

详见 [org.desktopspec.ApplicationManager1.md](references/dbus/org.desktopspec.ApplicationManager1.md)

### 应用属性

提供应用启动、桌面操作和应用属性查询能力。

详见 [org.desktopspec.ApplicationManager1.Application.md](references/dbus/org.desktopspec.ApplicationManager1.Application.md)

### 任务管理

提供应用启动任务跟踪能力。

详见 [org.desktopspec.JobManager1.md](references/dbus/org.desktopspec.JobManager1.md)

### MIME 类型管理

系统级 MIME 类型管理，管理所有应用的 MIME 关联，提供默认应用 MIME 类型设置能力。

详见 [org.desktopspec.MimeManager1.md](references/dbus/org.desktopspec.MimeManager1.md)

### 应用更新通知

提供应用更新完成通知能力。

详见 [org.desktopspec.ApplicationUpdateNotifier1.md](references/dbus/org.desktopspec.ApplicationUpdateNotifier1.md)

### 兼容性说明

dde-application-manager 的所有 D-Bus 接口均遵循 desktopspec 规范，为当前正在使用的正式接口，不存在为兼容旧版历史接口而保留的别名或废弃接口。所有接口名称、对象路径和接口名均与源码中注册的接口一致。

## DConfig 配置项

以下 DConfig 配置项仅作用于 dde-application-manager 自身，用于配置 dde-application-manager 的应用启动次数记录和应用环境变量管理行为，而非系统全局配置。

### 应用启动次数配置

应用启动次数记录配置。

详见 [org.deepin.dde.am](references/config/org.deepin.dde.am.md)

### 应用管理器配置

应用环境变量黑名单和额外环境变量配置。

详见 [org.deepin.dde.application-manager](references/config/org.deepin.dde.application-manager.md)

## CLI 命令

### dde-am

DDE 应用管理器客户端命令行工具，用于启动应用、执行命令、列出已安装应用。

详见 [dde-am.md](references/cli/dde-am.md)

### app-identifier

应用身份识别工具，用于识别指定进程以何种身份（应用 ID）运行。

详见 [app-identifier.md](references/cli/app-identifier.md)
