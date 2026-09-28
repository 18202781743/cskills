# 集成与构建配置

使用 dde-session-shell 公开接口前，需要安装对应的开发包。开发包提供公开头文件，供使用方包含和继承。

## 开发包

开发包名为 `dde-session-shell-dev`。该开发包提供安装在 `dde-session-shell/` 目录下的公开头文件：

- `base_module_interface.h`
- `login_module_interface.h`
- `login_module_interface_v2.h`
- `tray_module_interface.h`
- `assist_login_interface.h`

## CMake 集成

dde-session-shell 不导出 CMake 配置文件或库目标。使用方在 CMake 工程中手动指定头文件搜索路径：

```cmake
target_include_directories(your-plugin PRIVATE /usr/include/dde-session-shell)
```

使用方编写的插件编译为共享库，通过 Qt Plugin 机制加载，不需要链接 dde-session-shell 的库文件。

## 引用公开接口

包含所需类型的公开头文件：

```cpp
#include <base_module_interface.h>
#include <login_module_interface_v2.h>
```

C++ 接口类型位于 `dss::module` 和 `dss::module_v2` 命名空间。assist_login 接口为 C 函数，无命名空间。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
