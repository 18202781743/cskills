# org.deepin.dde.PasswdConf1 接口参考

deepin-pw-check 是 DDE 的密码安全策略组件，负责管理系统级密码校验规则。本接口提供全局密码校验开关、密码长度限制、校验策略、校验规则数量、首字母大写要求的读写及配置管理能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.PasswdConf1` |
| Object path | `/org/deepin/dde/PasswdConf1` |
| Interface | `org.deepin.dde.PasswdConf1` |
| Bus | System |

## 兼容性接口

**关系类型：兼容**

旧版接口 `com.deepin.daemon.PasswdConf`（对象路径 `/com/deepin/daemon/PasswdConf`，接口名 `com.deepin.daemon.PasswdConf`，System 总线）为兼容历史调用方而保留，提供与 `org.deepin.dde.PasswdConf1` 完全相同的 14 个方法，功能一致但使用旧版命名规范。新代码应推荐使用 `org.deepin.dde.PasswdConf1`，因为该接口采用了符合 DDE 新版 D-Bus 命名规范的接口名称。本文档中的所有示例均使用最新接口 `org.deepin.dde.PasswdConf1`，旧接口不提供示例。

## 通用配置

### WriteConfig

写入完整配置。

- **功能**：一次性写入全部密码安全策略配置（JSON 格式）。
- **触发条件**：由调用方主动调用。
- **使用场景**：需要批量修改多个密码安全策略配置项时使用，避免逐项设置。

- **输入参数**: `data`（string, 类型 `s`）：配置 JSON
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.WriteConfig '{"min_length":8}'
```

### ReadConfig

读取完整配置。

- **功能**：读取当前全部密码安全策略配置（JSON 格式）。
- **触发条件**：由调用方主动调用。
- **使用场景**：需要查看当前全部密码安全策略配置时使用，也可用于备份前获取当前配置。

- **输入参数**: 无
- **返回值**: `s`（string）：配置 JSON

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.ReadConfig
```

### Reset

重置配置为默认值。

- **功能**：将全部密码安全策略配置恢复为出厂默认值。
- **触发条件**：由调用方主动调用。
- **使用场景**：需要将密码安全策略恢复到初始状态时使用。

- **输入参数**: 无
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.Reset
```

### Backup

备份配置。

- **功能**：备份当前密码安全策略配置。
- **触发条件**：由调用方主动调用。
- **使用场景**：在修改密码安全策略前备份当前配置，以便后续恢复。

- **输入参数**: 无
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.Backup
```

## 密码长度限制

### GetLengthLimit

获取密码长度限制范围。

- **功能**：获取当前密码最小长度和最大长度限制。
- **触发条件**：由调用方主动调用。
- **使用场景**：在用户修改密码前，查询当前密码长度限制范围。

- **输入参数**: 无
- **返回值**: `(ii)`（int32, int32）：最小长度和最大长度

```bash
gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.GetLengthLimit
```

示例输出（实际值因系统配置而异）：

```
(1, 510)
```

### SetLengthLimit

设置密码长度限制范围。

- **功能**：设置密码最小长度和最大长度限制。
- **触发条件**：由调用方主动调用。
- **使用场景**：管理员需要调整密码长度要求时使用。

- **输入参数**: `min`（int32, 类型 `i`）：最小长度；`max`（int32, 类型 `i`）：最大长度
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.SetLengthLimit 8 32
```

## 校验策略

### GetValidatePolicy

获取校验策略。

- **功能**：获取当前密码校验所使用的策略（包含允许的字符集）。
- **触发条件**：由调用方主动调用。
- **使用场景**：查询当前密码校验允许的字符集和策略配置。

- **输入参数**: 无
- **返回值**: `s`（string）：校验策略 JSON

```bash
gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.GetValidatePolicy
```

示例输出（实际值因系统配置而异）：

```
("1234567890;abcdefghijklmnopqrstuvwxyz;ABCDEFGHIJKLMNOPQRSTUVWXYZ;~`!@#$%^&*()-_+=|\\{}[]:\"'<>,.?/",)
```

### SetValidatePolicy

设置校验策略。

- **功能**：设置密码校验所使用的策略（包含允许的字符集）。
- **触发条件**：由调用方主动调用。
- **使用场景**：管理员需要修改密码校验允许的字符集和策略时使用。

- **输入参数**: `s`（string, 类型 `s`）：校验策略 JSON
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.SetValidatePolicy '{"policy":"strict"}'
```

### GetValidateRequired

获取校验规则数量。

- **功能**：获取密码必须满足的校验规则数量。
- **触发条件**：由调用方主动调用。
- **使用场景**：查询当前密码需要满足多少条校验规则才能通过校验。

- **输入参数**: 无
- **返回值**: `i`（int32）：校验规则数量

```bash
gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.GetValidateRequired
```

示例输出（实际值因系统配置而异）：

```
(1,)
```

### SetValidateRequired

设置校验规则数量。

- **功能**：设置密码必须满足的校验规则数量。
- **触发条件**：由调用方主动调用。
- **使用场景**：管理员需要调整密码必须满足的校验规则数量时使用。

- **输入参数**: `n`（int32, 类型 `i`）：校验规则数量
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.SetValidateRequired 3
```

## 功能开关

### GetEnabled

获取密码校验是否启用。

- **功能**：查询当前是否启用了密码校验功能。
- **触发条件**：由调用方主动调用。
- **使用场景**：在用户修改密码前，确认密码校验功能是否已开启。

- **输入参数**: 无
- **返回值**: `b`（bool）：是否启用

```bash
gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.GetEnabled
```

示例输出（实际值因系统配置而异）：

```
(true,)
```

### SetEnabled

设置密码校验是否启用。

- **功能**：开启或关闭密码校验功能。
- **触发条件**：由调用方主动调用。
- **使用场景**：管理员需要开启或关闭密码校验功能时使用。

- **输入参数**: `enabled`（bool, 类型 `b`）：是否启用
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.SetEnabled true
```

### GetFirstLetterUpper

获取是否要求首字母大写。

- **功能**：查询当前是否要求密码首字母大写。
- **触发条件**：由调用方主动调用。
- **使用场景**：查询当前密码是否需要首字母大写才能通过校验。

- **输入参数**: 无
- **返回值**: `b`（bool）：是否要求

```bash
gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.GetFirstLetterUpper
```

示例输出（实际值因系统配置而异）：

```
(false,)
```

### SetFirstLetterUpper

设置是否要求首字母大写。

- **功能**：开启或关闭密码首字母大写要求。
- **触发条件**：由调用方主动调用。
- **使用场景**：管理员需要开启或关闭密码首字母大写要求时使用。

- **输入参数**: `enabled`（bool, 类型 `b`）：是否要求
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.PasswdConf1 \
  --object-path /org/deepin/dde/PasswdConf1 \
  --method org.deepin.dde.PasswdConf1.SetFirstLetterUpper true
```

---
