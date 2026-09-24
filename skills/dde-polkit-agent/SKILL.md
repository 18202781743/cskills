---
name: dde-polkit-agent
description: 提供 polkit 认证代理窗口 ID 设置的 D-Bus 接口和 PolicyKit 认证代理守护进程的 CLI 命令
Categories:
  - Application
---

# dde-polkit-agent

dde-polkit-agent 是 DDE 的 PolicyKit 认证代理组件，通过 Session 总线提供认证代理窗口 ID 设置的 D-Bus 接口，并提供认证代理守护进程的 CLI 命令。

## D-Bus 接口

### 认证代理

提供 polkit 认证代理窗口 ID 设置能力。

详见 [org.deepin.dde.Polkit1.AuthAgent.md](references/dbus/org.deepin.dde.Polkit1.AuthAgent.md)

dde-polkit-agent 仅在 Session 总线上注册唯一的 D-Bus 服务 `org.deepin.dde.Polkit1.AuthAgent`（对象路径 `/com/deepin/dde/Polkit1/AuthAgent`），不存在为兼容旧版接口而保留的别名或废弃接口。该接口为当前正在使用的唯一 D-Bus 接口。

## CLI 命令

### dde-polkit-agent

DDE 的 PolicyKit 认证代理，负责在用户执行需要特权的操作时弹出认证对话框。

详见 [dde-polkit-agent.md](references/cli/dde-polkit-agent.md)
