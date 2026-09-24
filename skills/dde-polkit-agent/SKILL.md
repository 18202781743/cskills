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

dde-polkit-agent 在 Session 总线上注册 D-Bus 服务 `org.deepin.dde.Polkit1.AuthAgent`（对象路径 `/com/deepin/dde/Polkit1/AuthAgent`），这是 V23 接口改造后启用的当前唯一 D-Bus 接口。旧版接口使用服务名 `com.deepin.Polkit1AuthAgent`（对象路径 `/com/deepin/Polkit1AuthAgent`），已在 V23 改造中替换，当前不再注册，仅作历史记录。

## CLI 命令

### dde-polkit-agent

DDE 的 PolicyKit 认证代理，负责在用户执行需要特权的操作时弹出认证对话框。

详见 [dde-polkit-agent.md](references/cli/dde-polkit-agent.md)
