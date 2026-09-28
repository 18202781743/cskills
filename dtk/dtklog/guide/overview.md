# dtklog 二次开发文档 · 概览

## 项目定位

dtklog 是基于 Qt 的线程安全日志库，提供多级别日志输出、多种日志输出目标（控制台、文件、滚动文件、系统日志）和便捷日志宏。它独立于其他 DTK 模块，仅依赖 Qt Core。

> **弃用说明**：在 DTK6 中 dtklog 已废弃，日志功能已合并至 dtkcore，不再独立维护。DTK6 项目应直接使用 dtkcore 提供的日志功能，不要集成 `libdtk6log-dev`。dtklog 仓库仍独立维护 DTK5 版本，以下文档仅适用于 DTK5 场景。

## 术语与缩写

- **DTK**：Deepin Tool Kit。
- **DTK5 / DTK6**：分别与 Qt5 / Qt6 配套的主版本。
- **DLog**：公开头文件安装目录名。
- **Appender**：日志输出目标，将日志消息写入控制台、文件或其他后端。
- **日志级别**：从 Trace 到 Fatal 的优先级体系，低于设定级别的消息被丢弃。
- **滚动文件**：按时间周期自动轮转的日志文件输出方式。
- **公开接口载体**：本库对外发布、供调用者引入的头文件。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。它以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 全局约定

公开头文件安装在按主版本区分的 DLog 目录。公开符号位于 `Dtk` 命名空间，另有 `Dtk::Core` 命名空间用于部分内部组织。版本判断和跨主版本构建方式见[集成与构建配置](integration.md)。

日志宏 `dDebug`、`dInfo`、`dWarning`、`dError`、`dFatal` 以全局宏形式提供，按类别输出的 `dCDebug`、`dCInfo`、`dCWarning`、`dCError`、`dCFatal` 需指定日志类别。计时宏 `dTraceTime`、`dDebugTime`、`dInfoTime` 用于记录代码执行耗时。断言宏 `dAssert` 和 `dAssertX` 用于条件检查。

## 按功能查阅

- 将 dtklog 引入 CMake、qmake 或 pkg-config 工程：参见[集成与构建配置](integration.md)。
- 管理日志级别和全局日志实例：参见 [Logger](modules.md#logger)。
- 实现自定义日志输出目标：参见 [AbstractAppender](modules.md#abstractappender) 与 [AbstractStringAppender](modules.md#abstractstringappender)。
- 输出日志到控制台、文件或滚动文件：参见 [ConsoleAppender](modules.md#consoleappender)、[FileAppender](modules.md#fileappender) 与 [RollingFileAppender](modules.md#rollingfileappender)。
- 在 Qt 应用中集成日志：参见 [DLogHelper](modules.md#dloghelper)。
- 在 DTK5 与 DTK6 之间迁移构建配置：参见[集成与构建配置](integration.md)。
