# 导出类型介绍

dde-api 提供 C++ header-only 事件日志记录接口，命名空间为 `DDE_EventLogger`，核心类为 `EventLogger`，并公开 `EventLoggerData` 数据类型用于传递日志内容。

## EventLogger

### 定位

C++ header-only 事件日志记录接口，面向需要将事件日志发送到后端的调用者。

### 功能能力总结

采用单例模式，通过 `instance()` 获取唯一实例。调用者通过 `writeEventLog` 方法写入事件日志，传入 `EventLoggerData` 结构描述日志内容，内部将数据序列化后发送到后端服务。包含头文件即可使用，无需链接库文件。

命名空间内还提供 `shouldEnableEventLog()` 函数，用于判断当前系统版本是否启用事件日志功能。UosCommunity 版本下该函数返回 false，表示该版本禁用事件日志；其他版本返回 true。`writeEventLog` 方法内部会自动调用该函数进行判断，调用者也可在写入前自行检查以决定是否构造日志数据。

### 使用场景

需要在 C++ 程序中记录并发送事件日志时使用。当需要根据系统版本条件性地记录日志时，可先调用 `shouldEnableEventLog()` 判断是否启用。

## EventLoggerData

### 定位

事件日志数据结构，用于描述单条事件日志的内容，作为 `EventLogger` 写入日志时的参数载体。

### 功能能力总结

包含三个公开字段：`tid` 为 `qint64` 类型字段；`target` 为 `QString` 类型字段，标识事件的目标对象；`message` 为 `QJsonObject` 类型字段，承载事件的具体消息内容。

### 使用场景

在调用 `writeEventLog` 前构造该结构，填充 `tid`、`target` 和 `message` 字段，传入 `EventLogger` 实例完成日志写入。
