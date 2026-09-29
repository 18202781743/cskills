# 集成与构建配置

使用 dde-session-shell 公开接口前，需要安装对应的开发包。开发包提供公开头文件，供使用方包含和继承。

## 开发期依赖

开发包名为 `dde-session-shell-dev`。该开发包提供安装在 `dde-session-shell/` 目录下的公开头文件：

- `base_module_interface.h`
- `login_module_interface.h`
- `login_module_interface_v2.h`
- `tray_module_interface.h`
- `assist_login_interface.h`

## C++ 插件接口集成

dde-session-shell 提供 CMake 配置文件 `DdeSessionShellConfig.cmake`，安装到 `lib/cmake/DdeSessionShell` 目录。该配置文件设置 `DDESESSIONSHELL_INCLUDE_DIR` 变量并调用 `include_directories`，不导出库目标。使用方可通过 `find_package` 引入：

```cmake
find_package(DdeSessionShell REQUIRED)
```

作为兼容写法，使用方也可手动指定头文件搜索路径：

```cmake
target_include_directories(your-plugin PRIVATE /usr/include/dde-session-shell)
```

C++ 插件接口（`BaseModuleInterface`、`LoginModuleInterfaceV2`、`TrayModuleInterface`）仅包含头文件，不需要链接 dde-session-shell 的库文件。使用方编写的插件编译为共享库，通过 Qt Plugin 机制加载。

使用 V2 登录接口时，需同时包含 V1 头文件，因为 V2 通过 `using` 声明引入 V1 中的类型定义：

```cpp
#include <base_module_interface.h>
#include <login_module_interface.h>
#include <login_module_interface_v2.h>
```

C++ 接口类型位于 `dss::module` 和 `dss::module_v2` 命名空间。

## assist_login C 接口集成

assist_login 接口为 C 语言接口（`extern "C"`），无命名空间，与 C++ 插件接口的集成方式不同。该接口的头文件 `assist_login_interface.h` 对应的源码通过 `plugins/assist_login/interface/CMakeLists.txt` 构建为共享库 `libassist_Login_interface.so`，安装到 `lib/dde-session-shell/modules` 目录。

使用 assist_login C 接口时，不仅需要包含头文件，还需要链接该共享库：

```cmake
target_link_libraries(your-plugin PRIVATE /usr/lib/dde-session-shell/modules/libassist_Login_interface.so)
```

包含头文件：

```cpp
#include <assist_login_interface.h>
```

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](dde-session-shell-dev.md)。
