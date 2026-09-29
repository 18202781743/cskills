# 集成与构建配置

使用 dde-polkit-agent 公开接口前，需要安装对应的开发包。开发包提供公开头文件，供使用方包含和继承。

## 开发包

开发包名为 `dde-polkit-agent-dev`。该开发包提供安装在 `dpa/` 目录下的公开头文件：

- `agent-extension.h`
- `agent-extension-proxy.h`

## CMake 集成

dde-polkit-agent 不导出 CMake 配置文件或库目标。使用方在 CMake 工程中手动指定头文件搜索路径并链接 Qt 插件机制所需模块：

```cmake
find_package(Qt6 REQUIRED COMPONENTS Core)
target_include_directories(your-plugin PRIVATE /usr/include/dpa)
```

使用方编写的扩展插件编译为共享库，通过 Qt Plugin 机制加载，不需要链接 dde-polkit-agent 的库文件。

## 引用公开接口

包含所需类型的公开头文件：

```cpp
#include <agent-extension.h>
#include <agent-extension-proxy.h>
```

公开类型位于 `dpa` 命名空间。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](dde-polkit-agent-dev.md)。
