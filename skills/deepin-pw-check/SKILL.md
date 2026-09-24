---
name: deepin-pw-check
description: 提供密码校验开关、密码长度限制、校验策略、校验规则数量、首字母大写要求的系统级密码安全策略读写及配置管理接口
Categories:
  - Settings
---

# deepin-pw-check

deepin-pw-check 是 DDE 的密码安全策略组件，通过 System 总线提供系统级密码校验开关、密码长度限制、校验策略、校验规则数量、首字母大写要求的读写及配置管理能力。该接口需要提权操作。

## D-Bus 接口

### 密码安全策略

提供系统级密码安全策略的读写和管理能力，包括密码校验开关、密码长度限制、校验策略、校验规则数量和首字母大写要求。

详见 [org.deepin.dde.PasswdConf1.md](references/dbus/org.deepin.dde.PasswdConf1.md)

### 兼容性说明

deepin-pw-check 当前推荐使用 D-Bus 服务接口 `org.deepin.dde.PasswdConf1`（对象路径 `/org/deepin/dde/PasswdConf1`，System 总线）。

旧版兼容接口 `com.deepin.daemon.PasswdConf`（对象路径 `/com/deepin/daemon/PasswdConf`，接口名 `com.deepin.daemon.PasswdConf`，System 总线）仍可访问，提供与 `org.deepin.dde.PasswdConf1` 相同的 14 个方法，用于兼容旧版调用方。文档中的所有示例均使用最新接口 `org.deepin.dde.PasswdConf1`，旧接口仅在此做功能概述说明。
