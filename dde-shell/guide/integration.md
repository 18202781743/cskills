# 集成与构建配置

使用 dde-shell 公开接口前，需要安装对应的开发包。开发包提供公开头文件、链接库和 CMake 构建信息。

## 开发包

框架开发包名为 `dde-shell-dev`，提供 CMake 包 `DDEShell` 和导出目标 `Dde::Shell`。

Dock 面板开发包名为 `dde-shell-dock-dev`，提供 CMake 包 `DDEShellDock` 和导出目标 `Dde::ShellDock`。

## CMake 集成

### 框架集成

在已有构建目标上查找 `DDEShell` 并链接 `Dde::Shell`：

```cmake
find_package(DDEShell REQUIRED)
target_link_libraries(your-plugin PRIVATE Dde::Shell)
```

`Dde::Shell` 会向该目标提供 dde-shell 的头文件搜索路径、链接信息和传递依赖，不需要再使用 `include_directories()` 或逐项链接依赖库。

### Dock 面板集成

开发 Dock 区域插件时，额外查找 `DDEShellDock` 并链接 `Dde::ShellDock`：

```cmake
find_package(DDEShellDock REQUIRED)
target_link_libraries(your-plugin PRIVATE Dde::Shell Dde::ShellDock)
```

`DDEShellDockConfig.cmake` 内部会自动 `find_dependency(DDEShell)`，因此只需查找 DDEShellDock 即可获得 Dde::Shell 的传递依赖。

### 插件包安装宏

dde-shell 提供以下 CMake 宏用于插件包管理：

- `ds_install_package(PACKAGE <id> [TARGET <lib>])` — 安装插件包和库文件，自动设置 PREFIX/OUTPUT_NAME 和安装路径
- `ds_build_package(PACKAGE <id> [TARGET <lib>])` — 构建插件包（不安装），将 package/ 目录拷贝到构建目录
- `ds_handle_package_translation(PACKAGE <id>)` — 自动扫描 QML/C++ 文件生成翻译并安装

安装路径：

- 包资源安装到 `share/dde-shell/` 目录
- 插件库安装到 `lib/dde-shell/` 目录
- 翻译文件安装到 `share/dde-shell/<plugin-id>/translations/` 目录

## 引用公开接口

构建目标链接 dde-shell 后，可以直接包含所需类型的公开头文件：

```cpp
#include <applet.h>
```

公开类型位于 `ds` 命名空间，可使用完整限定名，也可在合适的作用域使用 `DS_USE_NAMESPACE`。

C++ 插件通过 `D_APPLET_CLASS` 宏注册，该宏展开为匿名 namespace 中的 `DAppletFactory` 子类，通过 `Q_PLUGIN_METADATA` 注册 Qt Plugin。

## QML 集成

dde-shell 导出 QML 模块，URI 为 `org.deepin.ds`，导入版本 1.0。在 QML 文件中导入：

```qml
import org.deepin.ds 1.0
```

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
