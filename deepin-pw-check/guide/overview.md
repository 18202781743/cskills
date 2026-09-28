# deepin-pw-check 二次开发文档 · 概览

## 项目定位

deepin-pw-check 是密码强度检查 C 语言库，提供密码复杂度校验、密码字典检查、密码格式检查、密码长度查询、单一字符类型判断、MD5 加密和大密码加密能力。使用方在 C 或 C++ 程序中链接该库调用相关函数。项目同时提供 Go 绑定，通过 CGO 调用 C 库函数。

## 术语与缩写

- **密码复杂度校验**：检查密码是否满足长度、字符类型种类和最小数量要求。
- **密码字典检查**：检查密码是否出现在常见密码字典中。
- **CGO**：Go 语言调用 C 代码的机制，deepin-pw-check 的 Go 绑定通过 CGO 调用 C 库函数。
- **开发包**：使用方编译和链接程序所需安装的包，名为 `libdeepin_pw_check-dev`。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以公开头文件中的函数集为章节，逐一说明各函数集的定位、功能能力和使用场景。

## 全局约定

deepin-pw-check 是 C 语言库，不提供 CMake 配置文件或 pkg-config 元数据。使用方需通过 CMake 的 `find_path` 和 `find_library` 手动查找头文件和链接库。公开头文件安装在 `deepin-pw-check/` 目录下，链接库名为 `deepin_pw_check`，同时提供动态库 `libdeepin_pw_check.so` 和静态库 `libdeepin_pw_check.a`。

## 按功能查阅

- 将 deepin-pw-check 引入 CMake 工程：参见[集成与构建配置](integration.md)。
- 校验密码强度或检查密码字典：参见 [deepin_pw_check.h](modules.md#deepin_pw_checkh)。
- 查询密码长度要求或判断单一字符类型：参见 [deepin_pw_check.h](modules.md#deepin_pw_checkh)。
- 使用密码错误码或最大长度定义：参见 [common.h](modules.md#commonh)。
- 使用 MD5 加密或大密码加密：参见 [md5.h](modules.md#md5h)。
