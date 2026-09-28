# 集成与构建配置

使用 deepin-pw-check 公开接口前，需要安装开发包 `libdeepin_pw_check-dev`。该开发包提供公开头文件和链接库；deepin-pw-check 不提供 CMake 配置文件或 pkg-config 元数据，使用方需手动查找头文件和库。

## 开发包

开发包名为 `libdeepin_pw_check-dev`，提供以下内容：

- 公开头文件 `deepin_pw_check.h`、`common.h`、`md5.h`，安装在 `deepin-pw-check/` 目录下。
- 动态链接库 `libdeepin_pw_check.so` 和静态链接库 `libdeepin_pw_check.a`。

## CMake 集成

deepin-pw-check 不提供 CMake 配置文件。使用方在 CMake 工程中通过 `find_path` 和 `find_library` 手动查找头文件和库：

```cmake
find_path(DEEPIN_PW_CHECK_INCLUDE_DIR deepin_pw_check.h)
find_library(DEEPIN_PW_CHECK_LIB deepin_pw_check)

target_include_directories(your_target PRIVATE ${DEEPIN_PW_CHECK_INCLUDE_DIR})
target_link_libraries(your_target PRIVATE ${DEEPIN_PW_CHECK_LIB})
```

`your_target` 替换为使用方工程中的目标名。头文件默认安装在 `deepin-pw-check/` 子目录下，`find_path` 可正确解析包含路径。

## 引用公开接口

构建目标链接 deepin-pw-check 后，可以直接包含所需头文件：

```c
#include <deepin_pw_check.h>
```

根据所需功能，还可包含 `common.h` 获取错误码和最大长度定义，或包含 `md5.h` 获取 MD5 加密函数。

## 其他受支持的构建入口

deepin-pw-check 不提供 pkg-config 元数据或 qmake 模块。

## Go 集成

项目提供 Go 绑定，通过 CGO 调用 C 库函数。Go 模块路径见项目 `go.mod` 文件。在 Go 工程中通过 Go 模块系统引入对应包路径即可使用。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
