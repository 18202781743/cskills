# 集成与构建配置

使用 deepin-pw-check 公开接口前，需要安装开发包 `libdeepin-pw-check-dev`。该开发包提供公开头文件、链接库和 pkg-config 元数据。

## 开发包

开发包名为 `libdeepin-pw-check-dev`，提供以下内容：

- 公开头文件 `deepin_pw_check.h`，安装在 `/usr/include/` 目录下。
- 动态链接库 `libdeepin_pw_check.so` 和静态链接库 `libdeepin_pw_check.a`。
- pkg-config 元数据文件 `libdeepin_pw_check.pc`，包名为 `deepin_pw_check`。

## CMake 集成（首选）

deepin-pw-check 提供 pkg-config 元数据，使用方在 CMake 工程中通过 `PkgConfig` 模块查找并链接：

```cmake
find_package(PkgConfig REQUIRED)
pkg_check_modules(DEEPIN_PW_CHECK REQUIRED deepin_pw_check)

target_link_libraries(your_target PRIVATE ${DEEPIN_PW_CHECK_LIBRARIES})
```

`your_target` 替换为使用方工程中的目标名。`pkg_check_modules` 会自动解析头文件搜索路径和链接库路径，无需额外设置 `target_include_directories`。

## 兼容方式（手动查找）

在不使用 pkg-config 的环境中，可通过 `find_path` 和 `find_library` 手动查找头文件和库：

```cmake
find_path(DEEPIN_PW_CHECK_INCLUDE_DIR deepin_pw_check.h)
find_library(DEEPIN_PW_CHECK_LIB deepin_pw_check)

target_include_directories(your_target PRIVATE ${DEEPIN_PW_CHECK_INCLUDE_DIR})
target_link_libraries(your_target PRIVATE ${DEEPIN_PW_CHECK_LIB})
```

## 引用公开接口

构建目标链接 deepin-pw-check 后，包含公开头文件即可使用全部公开接口：

```c
#include <deepin_pw_check.h>
```

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](libdeepin-pw-check-dev.md)。
