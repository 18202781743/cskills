# deepin-pw-check 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | libdeepin_pw_check |
| 版本 | 见源码 VERSION 文件 |
| 描述 | 密码强度检查 C 库，提供密码复杂度校验、密码字典检查、密码加密比较等功能 |
| CMake target | 不适用（使用 Makefile 构建，非 CMake） |
| find_package 名 | 不适用 |
| 头文件安装路径 | `${CMAKE_INSTALL_INCLUDEDIR}/deepin-pw-check/`（手动安装） |
| 库文件 | `libdeepin_pw_check.so` / `libdeepin_pw_check.a` |
| 仓库地址 | https://github.com/linuxdeepin/deepin-pw-check.git |

## 2. 包依赖

### 运行时依赖
- libc6

### 开发依赖
- GCC / Clang（C 编译器）
- Make
- Go (>= 1.20)（项目包含 Go 模块，可选）

## 3. CMake 集成

不适用（deepin-pw-check 使用 Makefile 构建，不提供 CMake 配置文件）

### Makefile 集成方式

项目通过 `Makefile` 构建，使用 `make` 命令：

```bash
make
sudo make install
```

### 在第三方项目中链接

由于没有 .pc 文件和 CMake config，需要手动指定路径：

```cmake
# 手动查找头文件和库
find_path(DEEPIN_PW_CHECK_INCLUDE_DIR deepin_pw_check.h)
find_library(DEEPIN_PW_CHECK_LIB deepin_pw_check)

target_include_directories(your-target PRIVATE ${DEEPIN_PW_CHECK_INCLUDE_DIR})
target_link_libraries(your-target PRIVATE ${DEEPIN_PW_CHECK_LIB})
```

或直接指定：

```cmake
target_include_directories(your-target PRIVATE /usr/include/deepin-pw-check)
target_link_libraries(your-target PRIVATE deepin_pw_check)
```

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（C 语言库，无命名空间）

## 6. 关键公共类及功能描述

deepin-pw-check 为 C 语言库，提供以下公共函数（定义在头文件中）：

### deepin_pw_check.h

| 函数 | 功能 |
|------|------|
| `pw_check()` | 密码强度检查，返回密码是否满足复杂度要求 |
| `pw_dict_check()` | 密码字典检查，检查密码是否在常见密码字典中 |
| `pw_format_check()` | 密码格式检查 |
| `get_pw_str_len()` | 获取密码长度要求 |
| `is_mono_case()` | 检查密码是否为单一字符类型 |

### common.h

通用定义和工具函数：

| 函数/宏 | 功能 |
|---------|------|
| `MAX_LEN` | 最大密码长度定义 |
| `PW_ERR_*` | 密码错误码定义 |

### md5.h

MD5 加密相关函数：

| 函数 | 功能 |
|------|------|
| `md5_crypt()` | MD5 加密 |
| `bigcrypt()` | 大密码加密 |

### debug.h

调试辅助函数

## 7. QML 模块

不适用

## 8. DBus 接口

不适用（C 语言库，不提供 DBus 接口）

## 9. 插件开发

不适用

## Go 模块说明

项目包含 `go.mod`，提供 Go 绑定：

- Go 模块路径：见 `go.mod`
- Go 绑定通过 CGO 调用 C 库函数

## 使用示例

```c
#include <deepin_pw_check.h>

int result = pw_check("userpassword", 12, 3);
if (result == 0) {
    // 密码符合要求
} else {
    // 密码不符合要求，根据错误码提示
}
```
