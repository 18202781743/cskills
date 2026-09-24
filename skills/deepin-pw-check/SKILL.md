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
