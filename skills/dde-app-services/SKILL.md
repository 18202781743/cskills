---
name: dde-app-services
description: 提供配置管理器对象获取、配置值读写、配置更新同步的全局 DConfig 管理 D-Bus 接口，dde-dconfig-daemon 自身的日志规则设置接口，以及 dde-dconfig、dde-dconfig-daemon、dde-dconfig-editor 命令行配置管理工具
Categories:
  - Settings
---

# dde-app-services

dde-app-services 是 DDE 的 DConfig 配置管理服务组件。通过 System 总线提供全局的配置管理器对象获取、配置值读写、配置更新同步能力，以及 dde-dconfig-daemon 自身的日志规则设置能力。同时提供 dde-dconfig、dde-dconfig-daemon、dde-dconfig-editor 命令行配置管理工具。部分接口需要提权操作。

## D-Bus 接口

### 配置管理器

提供全局的配置管理器对象获取、更新、同步能力，以及 dde-dconfig-daemon 自身的日志规则设置、用户配置数据移除和配置重新加载能力。

详见 [org.desktopspec.ConfigManager.md](references/dbus/org.desktopspec.ConfigManager.md)

### 配置管理器 Manager 接口

提供全局的配置值读写、重置和元信息查询能力。

详见 [org.desktopspec.ConfigManager.Manager.md](references/dbus/org.desktopspec.ConfigManager.Manager.md)

## CLI 命令

### dde-dconfig

DDE 配置（dconfig）命令行管理工具，用于管理 DTK 提供的配置策略系统（dconfig）。

详见 [dde-dconfig.md](references/cli/dde-dconfig.md)

### dde-dconfig-daemon

DDE 配置守护进程，是 dconfig 系统的后台服务进程。

详见 [dde-dconfig-daemon.md](references/cli/dde-dconfig-daemon.md)

### dde-dconfig-editor

DDE 配置编辑器，提供图形化界面用于查看和修改 dconfig 配置项。

详见 [dde-dconfig-editor.md](references/cli/dde-dconfig-editor.md)
