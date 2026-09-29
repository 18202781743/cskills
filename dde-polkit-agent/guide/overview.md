# dde-polkit-agent 二次开发文档 · 概览

## 项目定位

dde-polkit-agent 是 DDE Polkit 认证代理，为需要提权的操作提供图形化认证对话框。项目安装认证代理扩展接口头文件，允许第三方通过继承扩展接口自定义认证行为。

## 术语与缩写

- **Polkit**：Linux 系统的授权管理框架。
- **认证动作**：Polkit 中需要授权的操作，以动作 ID 标识。
- **扩展接口**：允许第三方扩展认证代理行为的 C++ 抽象接口。
- **扩展插件**：第三方编译的共享库（`.so`），实现扩展接口后被 dde-polkit-agent 加载执行。

## 导出类型

[导出类型介绍](dde-polkit-agent-dev.md)是本项目唯一的类型参考文档。以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 全局约定

公开头文件安装在 `dpa/` 目录下。公开类型位于 `dpa` 命名空间。扩展插件通过继承扩展接口并实现其纯虚方法接入认证代理。

dde-polkit-agent 采用 Qt Plugin 机制加载扩展插件。插件编译为共享库（`.so`），在运行时由 `QPluginLoader` 扫描并加载。插件元数据中必须声明 `api_version: "1.0"`，否则不会被加载。插件搜索路径为环境变量 `DDE_POLKIT_AGENT_PLUGINS_DIRS` 指定的目录，或默认路径 `/usr/lib/polkit-1-dde/plugins/`。

## 按功能查阅

- 将 dde-polkit-agent 扩展头文件引入 CMake 工程并配置插件构建：参见[集成与构建配置](integration.md)。
- 开发认证代理扩展插件：参见 [AgentExtension](dde-polkit-agent-dev.md#agentextension) 与 [AgentExtensionProxy](dde-polkit-agent-dev.md#agentextensionproxy)。