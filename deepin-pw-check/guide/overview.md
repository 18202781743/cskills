# deepin-pw-check 二次开发文档 · 概览

## 项目定位

deepin-pw-check 是 DDE 密码强度校验 C 语言库，提供密码复杂度校验、密码强度评估、密码校验策略查询、错误信息转换、grub2 密码校验和调试控制能力。使用方在 C 或 C++ 程序中链接该库调用相关函数。项目还提供 PAM 模块和 DBus 配置服务作为系统级集成组件，但不属于二次开发直接调用的公开接口范围。

## 术语与缩写

- **密码复杂度校验**：检查密码是否满足长度、字符类型种类和最小数量、回文、单调递增、连续相同字符等要求。
- **密码强度等级**：对新密码进行的强度分级，分为错误、低、中、高四级。
- **密码校验策略**：通过配置文件定义的密码校验规则，包括最小长度、最大长度、最小字符类型数、校验策略、回文位数、单调字符数、连续相同字符数。
- **grub2 密码校验**：读取 grub2 专用配置文件进行密码校验，与普通密码校验使用不同的配置文件路径。
- **开发包**：使用方编译和链接程序所需安装的包，名为 `libdeepin-pw-check-dev`。

## 导出类型

[导出类型介绍](libdeepin-pw-check-dev.md)是本项目唯一的类型参考文档。以公开头文件 `deepin_pw_check.h` 为章节，逐一说明其中函数集的定位、功能能力和使用场景。

## 全局约定

deepin-pw-check 的密码校验策略通过配置文件 `/etc/deepin/dde.conf` 定义；grub2 密码校验对应的配置文件为 `/etc/deepin/grub2_edit_auth.conf`。项目提供 pkg-config 元数据，包名为 `deepin_pw_check`。公开头文件仅 `deepin_pw_check.h`，安装在 `/usr/include/` 目录下。

## 按功能查阅

- 将 deepin-pw-check 引入 CMake 工程：参见[集成与构建配置](integration.md)。
- 校验密码复杂度或查询密码校验策略：参见 [deepin_pw_check.h](libdeepin-pw-check-dev.md#deepin_pw_checkh)。
- 评估密码强度等级：参见 [deepin_pw_check.h](libdeepin-pw-check-dev.md#deepin_pw_checkh)。
- 将密码校验错误码转换为可读字符串：参见 [deepin_pw_check.h](libdeepin-pw-check-dev.md#deepin_pw_checkh)。
- 执行 grub2 密码校验：参见 [deepin_pw_check.h](libdeepin-pw-check-dev.md#deepin_pw_checkh)。
