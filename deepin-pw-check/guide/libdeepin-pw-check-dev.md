# 导出类型介绍

deepin-pw-check 提供密码复杂度校验、密码强度评估、密码校验策略查询、错误信息转换、grub2 密码校验和调试控制能力。公开头文件为 `deepin_pw_check.h`。

## deepin_pw_check.h

### 定位

密码校验核心接口，面向需要在 C 或 C++ 程序中执行密码复杂度校验、强度评估、策略查询和错误信息转换的调用者。接口分为普通版和 grub2 版两组，普通版读取 `/etc/deepin/dde.conf` 配置，grub2 版读取 `/etc/deepin/grub2_edit_auth.conf` 配置。

### 功能能力总结

- **类型定义**：`PW_ERROR_TYPE` 枚举，包含 15 个密码校验错误码（`PW_NO_ERR`、`PW_ERR_PASSWORD_EMPTY`、`PW_ERR_LENGTH_SHORT`、`PW_ERR_LENGTH_LONG`、`PW_ERR_CHARACTER_INVALID`、`PW_ERR_PALINDROME`、`PW_ERR_WORD`、`PW_ERR_PW_REPEAT`、`PW_ERR_PW_MONOTONE`、`PW_ERR_PW_CONSECUTIVE_SAME`、`PW_ERR_PW_FIRST_UPPERM`、`PW_ERR_PARA`、`PW_ERR_INTERNAL`、`PW_ERR_USER`、`PW_ERR_CHARACTER_TYPE_TOO_FEW`、`PW_ERR_SAME_AS_USERNAME`）。
- **类型定义**：`PASSWORD_LEVEL_TYPE` 枚举，包含 4 个密码强度等级（`PASSWORD_STRENGTH_LEVEL_ERROR`、`PASSWORD_STRENGTH_LEVEL_LOW`、`PASSWORD_STRENGTH_LEVEL_MIDDLE`、`PASSWORD_STRENGTH_LEVEL_HIGH`）。
- **宏定义**：`LEVEL_STANDARD_CHECK`（标准校验，检查长度和字符）、`LEVEL_STRICT_CHECK`（严格校验，检查长度、字典词、回文和字符有效性）。
- `deepin_pw_check`：密码复杂度校验，校验密码是否满足策略要求，返回错误码。
- `deepin_pw_check_grub2`：grub2 密码复杂度校验，读取 grub2 配置文件校验密码，返回错误码。
- `get_new_passwd_strength_level`：评估新密码的强度等级，返回 `PASSWORD_LEVEL_TYPE`。
- `get_new_passwd_strength_level_grub2`：评估新密码的 grub2 强度等级，返回 `PASSWORD_LEVEL_TYPE`。
- `err_to_string`：将 `PW_ERROR_TYPE` 错误码转换为可读字符串。
- `err_to_string_grub2`：将 `PW_ERROR_TYPE` 错误码转换为可读字符串（grub2 版）。
- `get_pw_min_length`：获取密码最小长度要求。
- `get_pw_min_length_grub2`：获取 grub2 密码最小长度要求。
- `get_pw_max_length`：获取密码最大长度要求。
- `get_pw_max_length_grub2`：获取 grub2 密码最大长度要求。
- `get_pw_min_character_type`：获取密码最小字符类型数要求。
- `get_pw_min_character_type_grub2`：获取 grub2 密码最小字符类型数要求。
- `get_pw_validate_policy`：获取密码校验策略，由配置文件 `Password:VALIDATE_POLICY` 指定。
- `get_pw_validate_policy_grub2`：获取 grub2 密码校验策略，由 grub2 配置文件 `Password:VALIDATE_POLICY` 指定。
- `get_pw_palimdrome_num`：获取密码回文检查位数。
- `get_pw_palimdrome_num_grub2`：获取 grub2 密码回文检查位数。
- `get_pw_monotone_character_num`：获取密码单调递增字符检查位数。
- `get_pw_monotone_character_num_grub2`：获取 grub2 密码单调递增字符检查位数。
- `get_pw_consecutive_same_character_num`：获取密码连续相同字符检查位数。
- `get_pw_consecutive_same_character_num_grub2`：获取 grub2 密码连续相同字符检查位数。
- `set_debug_flag`：设置调试标志，控制调试输出。

`deepin_pw_check` 和 `deepin_pw_check_grub2` 的 `level` 参数以及 `get_pw_*` 系列函数的 `level` 参数均已标注 Deprecated，使用方无需关注该校验级别参数。

### 使用场景

需要在 C 或 C++ 程序中校验密码复杂度、评估密码强度等级、查询密码校验策略配置、将错误码转换为可读信息、执行 grub2 密码校验或控制调试输出时。
