# 日志规范

## 1. 概述

dtklog 是 DTK 的日志框架，支持多输出目标。

## 2. 头文件与依赖

```cpp
#include <Logger>
#include <FileAppender>
#include <ConsoleAppender>
#include <RollingFileAppender>

// CMake
find_package(DtkLog REQUIRED)
target_link_libraries(your_target Dtk::Log)
```

## 3. 基本 API

```cpp
#include <Logger>

// 日志级别
dDebug() << "调试信息";
dInfo() << "普通信息";
dWarning() << "警告信息";
dError() << "错误信息";
dFatal() << "致命错误";
```

## 4. 配置日志输出

### 4.1 输出到控制台

```cpp
#include <Logger>
#include <ConsoleAppender>

int main(int argc, char *argv[]) {
    DLogHelper::setGlobalAppender(new ConsoleAppender);
    dInfo() << "应用启动";
}
```

### 4.2 输出到文件

```cpp
#include <Logger>
#include <RollingFileAppender>

int main(int argc, char *argv[]) {
    auto *fileAppender = new RollingFileAppender("/var/log/myapp.log");
    fileAppender->setMaxFileSize(10 * 1024 * 1024); // 10MB
    fileAppender->setMaxBackupIndex(5); // 保留 5 个备份
    
    DLogHelper::setGlobalAppender(fileAppender);
}
```

### 4.3 多输出目标

```cpp
#include <Logger>
#include <ConsoleAppender>
#include <FileAppender>

auto *logger = DLogHelper::getLogger("myapp");
logger->addAppender(new ConsoleAppender);
logger->addAppender(new FileAppender("/var/log/myapp.log"));
```

## 5. 日志格式

```cpp
// 设置日志格式
ConsoleAppender *appender = new ConsoleAppender;
appender->setFormat("%{time yyyy-MM-dd HH:mm:ss} [%{type}] %{file}:%{line}: %{message}");
```

## 6. 日志级别控制

```cpp
// 设置最低日志级别
DLogHelper::setLogLevel(DLogHelper::Debug);
```

## 7. 相关文档

- [index.md](../SKILL.md) - DTK 开发指南
