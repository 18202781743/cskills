# dde-polkit-agent 二次开发文档 · 概览

## 项目定位

dde-polkit-agent 是 DDE 桌面环境的 Polkit 认证代理，为需要提权的操作提供图形化认证对话框。项目通过安装公开头文件，允许第三方继承扩展接口并编译为共享库插件，由认证代理在运行时加载，从而自定义认证行为。

## 导出类型

- [认证代理扩展接口](agent-extension.md)：介绍 `AgentExtension` 和 `AgentExtensionProxy` 两个公开 C++ 抽象接口的定位、功能能力和使用场景，以及扩展插件的集成与构建方式。

## 按功能查阅

- 将扩展头文件引入 CMake 工程并配置插件构建：参见 [CMake 配置](agent-extension.md#cmake-配置)
- 安装扩展插件共享库到认证代理的插件搜索路径：参见 [构建与安装插件](agent-extension.md#构建与安装插件)
- 通过 Qt Plugin 宏注册扩展插件：参见 [插件注册](agent-extension.md#插件注册)
- 在源文件中包含公开头文件：参见 [使用方式](agent-extension.md#使用方式)
- 了解 `AgentExtension` 接口提供的能力：参见 [AgentExtension](agent-extension.md#agentextension)
- 了解 `AgentExtensionProxy` 接口提供的能力：参见 [AgentExtensionProxy](agent-extension.md#agentextensionproxy)
