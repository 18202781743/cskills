# 集成与构建配置

使用 dde-polkit-agent 公开接口前，需要安装对应的开发包。开发包提供公开头文件，供使用方包含和继承。使用方编写的扩展插件编译为共享库，通过 Qt Plugin 机制被 dde-polkit-agent 在运行时加载，不需要链接 dde-polkit-agent 的库文件。

## 开发包

开发包名为 `dde-polkit-agent-dev`。该开发包提供安装在 `dpa/` 目录下的公开头文件：

- `agent-extension.h`
- `agent-extension-proxy.h`

## CMake 集成

dde-polkit-agent 不导出 CMake 配置文件或库目标，使用方不调用 `find_package(dde-polkit-agent)`。使用方在 CMake 工程中手动指定头文件搜索路径，并链接 Qt 插件机制所需的模块：

```cmake
find_package(Qt6 REQUIRED COMPONENTS Core Widgets)
target_include_directories(your-plugin PRIVATE /usr/include/dpa)
```

扩展插件编译为共享库（`SHARED`），由 dde-polkit-agent 通过 `QPluginLoader` 加载，不需要链接 dde-polkit-agent 的库文件。

## 插件 IID

扩展插件使用 Qt Plugin 机制接入 dde-polkit-agent。插件 IID 定义在 `agent-extension.h` 中，值为 `com.deepin.dpa.AgentExtension`，对应宏为 `AgentExtensionPluginIID`。使用方在插件类声明中使用 `Q_PLUGIN_METADATA` 宏声明此 IID，使 `QPluginLoader` 能够识别并实例化插件对象。

`agent-extension.h` 中已通过 `Q_DECLARE_INTERFACE(dpa::AgentExtension, AgentExtensionPluginIID)` 注册接口与 IID 的关联。使用方在插件类中通过 `Q_INTERFACES(dpa::AgentExtension)` 声明实现该接口，使 `qobject_cast` 能够正确进行接口转换。

## 插件元数据

`Q_PLUGIN_METADATA` 宏通过 `FILE` 参数指定一个 JSON 元数据文件。dde-polkit-agent 在加载插件时会检查元数据中的 `api_version` 字段，值必须为 `"1.0"`，否则插件不会被加载。

元数据文件示例（`plugin.json`）：

```json
{
    "api_version": "1.0"
}
```

插件类中的宏声明示例：

```cpp
class MyExtension : public QObject, public dpa::AgentExtension
{
    Q_OBJECT
    Q_PLUGIN_METADATA(IID AgentExtensionPluginIID FILE "plugin.json")
    Q_INTERFACES(dpa::AgentExtension)
    // ...
};
```

CMake 中需要将元数据文件放置在源码目录中，使 `Q_PLUGIN_METADATA` 宏的 `FILE` 参数能够找到该文件。编译产物中会自动包含元数据信息。

## 插件安装路径

扩展插件共享库（`.so`）需要安装到 dde-polkit-agent 的插件搜索路径下才能被加载。默认搜索路径为 `/usr/lib/polkit-1-dde/plugins/`。也可以通过环境变量 `DDE_POLKIT_AGENT_PLUGINS_DIRS` 指定额外的插件搜索目录，多个目录以路径分隔符分隔。

CMake 安装示例：

```cmake
install(TARGETS your-plugin LIBRARY DESTINATION /usr/lib/polkit-1-dde/plugins)
```

## 引用公开接口

包含所需类型的公开头文件：

```cpp
#include <agent-extension.h>
#include <agent-extension-proxy.h>
```

公开类型位于 `dpa` 命名空间。

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](dde-polkit-agent-dev.md)。