# dde-api 二次开发文档 · 概览

## 项目定位

dde-api 是 DDE 的 API 库，提供 header-only C++ 事件日志记录接口。调用者通过该接口将事件日志序列化后发送到后端库，由后端完成实际的日志写入。

## 导出类型

- [事件日志接口](event-logger.md)：涵盖 `EventLogger` 类和 `EventLoggerData` 数据结构，提供事件日志的组装、序列化与写入能力。

## 按功能查阅

- 将 dde-api 引入 CMake 工程：参见 [CMake 配置](event-logger.md#cmake-配置)
- 包含头文件并使用命名空间：参见 [使用方式](event-logger.md#使用方式)
- 记录事件日志：参见 [EventLogger](event-logger.md#eventlogger)
- 组装日志数据：参见 [EventLoggerData](event-logger.md#eventloggerdata)
