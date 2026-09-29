# dde-polkit-agent 二次开发文档 · 概览

## 项目定位

dde-polkit-agent 是 DDE Polkit 认证代理，为需要提权的操作提供图形化认证对话框。项目安装认证代理扩展接口头文件，允许第三方通过继承扩展接口自定义认证行为。

## 术语与缩写

- **Polkit**：Linux 系统的授权管理框架。
- **认证动作**：Polkit 中需要授权的操作，以动作 ID 标识。
- **扩展接口**：允许第三方扩展认证代理行为的 C++ 抽象接口。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 全局约定

公开头文件安装在 `dpa/` 目录下。公开类型位于 `dpa` 命名空间。扩展插件通过继承扩展接口并实现其纯虚方法接入认证代理。

## 按功能查阅

- 将 dde-polkit-agent 扩展头文件引入 CMake 工程：参见[集成与构建配置](integration.md)。
- 开发认证代理扩展插件：参见 [AgentExtension](modules.md#agentextension) 与 [AgentExtensionProxy](modules.md#agentextensionproxy)。
