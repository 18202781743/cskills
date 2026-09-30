# deepin-pw-check 二次开发文档 · 概览

## 项目定位

deepin-pw-check 是 DDE 密码强度校验 C 语言库，提供密码复杂度校验、密码强度等级评估、密码校验策略查询、错误码到可读信息转换和调试日志控制能力。使用方在 C 或 C++ 程序中链接该库即可调用相关接口，普通版接口读取 `/etc/deepin/dde.conf` 配置文件，grub2 版接口读取 `/etc/deepin/grub2_edit_auth.conf` 配置文件。

## 导出类型

- [密码校验接口](password-check.md)：以公开头文件 `deepin_pw_check.h` 为入口，涵盖密码复杂度校验、密码强度等级评估、密码校验策略查询、错误码到可读信息转换和调试控制能力的全部公开接口。

## 按功能查阅

- 将 deepin-pw-check 引入 CMake 工程并链接库：参见 [CMake 配置](password-check.md#cmake-配置)。
- 校验密码是否满足复杂度要求：参见 [deepin_pw_check.h](password-check.md#deepin_pw_checkh)。
- 评估密码强度等级：参见 [deepin_pw_check.h](password-check.md#deepin_pw_checkh)。
- 查询当前密码校验策略参数：参见 [deepin_pw_check.h](password-check.md#deepin_pw_checkh)。
- 将密码校验错误码转换为可读提示字符串：参见 [deepin_pw_check.h](password-check.md#deepin_pw_checkh)。
- 控制 debug 日志输出：参见 [deepin_pw_check.h](password-check.md#deepin_pw_checkh)。
