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

### 4.1 注册 Appender

```cpp
#include <Logger>
#include <ConsoleAppender>

int main(int argc, char *argv[]) {
    Logger::globalInstance()->registerAppender(new ConsoleAppender);
    dInfo() << "应用启动";
}
```

### 4.2 输出到文件

```cpp
#include <Logger>
#include <RollingFileAppender>

int main(int argc, char *argv[]) {
    auto *fileAppender = new RollingFileAppender("/var/log/myapp.log");
    Logger::globalInstance()->registerAppender(fileAppender);
    dInfo() << "应用启动";
}
```

### 4.3 多输出目标

```cpp
#include <Logger>
#include <ConsoleAppender>
#include <FileAppender>

Logger::globalInstance()->registerAppender(new ConsoleAppender);
Logger::globalInstance()->registerAppender(new FileAppender("/var/log/myapp.log"));
```

### 4.4 分类 Appender

```cpp
#include <Logger>
#include <FileAppender>

// 为特定分类注册 appender
Logger::globalInstance()->registerCategoryAppender("network", 
    new FileAppender("/var/log/myapp-network.log"));
```

## 5. 日志级别

| 级别 | 枚举值 | 说明 |
|------|--------|------|
| Trace | `Logger::Trace` | 代码追踪 |
| Debug | `Logger::Debug` | 调试信息 |
| Info | `Logger::Info` | 普通信息 |
| Warning | `Logger::Warning` | 警告 |
| Error | `Logger::Error` | 错误 |
| Fatal | `Logger::Fatal` | 致命错误（会 abort） |

## 6. Logger 核心 API

```cpp
// 全局实例
Logger *Logger::globalInstance();

// 注册/注销 appender
void registerAppender(AbstractAppender *appender);
void registerCategoryAppender(const QString &category, AbstractAppender *appender);
void unregisterAppender(AbstractAppender *appender);

// 日志级别转换
static QString levelToString(LogLevel level);
static LogLevel levelFromString(const QString &str);
```

## 7. 相关文档

- [index.md](../SKILL.md) - DTK 开发指南
