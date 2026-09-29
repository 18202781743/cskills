# dde-api 二次开发文档 · 概览

## 项目定位

dde-api 是 DDE 的 API 库，提供 header-only C++ 接口。C++ 部分提供事件日志记录能力。

## 术语与缩写

- **header-only**：仅含头文件、无需链接的 C++ 接口形式。

## 导出类型

[导出类型介绍](dde-api-dev.md)是本项目唯一的类型参考文档。以类型为章节，逐一说明 header-only 接口的定位、功能能力和使用场景。文档涵盖 `EventLogger` 类和 `EventLoggerData` 数据类型。

## 全局约定

C++ header-only 头文件安装在 `dde-api/` 目录下，主要符号位于 `DDE_EventLogger` 命名空间。

## 按功能查阅

- 将 dde-api 引入 CMake 工程：参见[集成与构建配置](integration.md)。
- 记录事件日志：参见 [EventLogger](dde-api-dev.md#eventlogger)。
