# 核心工具与日志

## 1. 日志系统

DTK 日志系统由 dtklog 提供底层 Logger 框架，dtkcore 通过 `DLogManager` 提供便捷初始化。

### 1.1 日志宏（dtklog）

```cpp
#include <dloggerdefs.h>

dTrace() << "代码追踪";
dDebug() << "调试信息";
dInfo() << "普通信息";
dWarning() << "警告信息";
dError() << "错误信息";
dFatal() << "致命错误";  // 会 abort
```

| 宏 | 级别 | 说明 |
|----|------|------|
| `dTrace()` | `Logger::Trace` | 代码追踪 |
| `dDebug()` | `Logger::Debug` | 调试信息 |
| `dInfo()` | `Logger::Info` | 普通信息 |
| `dWarning()` | `Logger::Warning` | 警告 |
| `dError()` | `Logger::Error` | 错误 |
| `dFatal()` | `Logger::Fatal` | 致命错误（会 abort） |

### 1.2 快速初始化（dtkcore）

大多数应用通过 `DLogManager` 一行初始化即可：

```cpp
#include <DLog>

DLogManager::registerConsoleAppender();   // 输出到控制台
DLogManager::registerFileAppender();      // 输出到文件（自动路径）
DLogManager::registerJournalAppender();   // 输出到 systemd journal

// 自定义日志文件路径
DLogManager::setlogFilePath("/var/log/myapp.log");
DLogManager::registerFileAppender();

// 自定义格式
DLogManager::setLogFormat("%{time}{yyyy-MM-dd HH:mm:ss.zzz} [%{type}] %{message}");
```

### 1.3 CMake 依赖

```cmake
find_package(DtkCore REQUIRED)
target_link_libraries(your_target Dtk::Core)
```

DtkCore 自动引入 dtklog 依赖，无需单独 `find_package(DtkLog)`。

### 1.4 高级日志配置（dtklog，按需使用）

需要自定义 Appender 或分类日志时直接使用 dtklog：

```cpp
#include <Logger.h>
#include <ConsoleAppender.h>
#include <FileAppender.h>
#include <RollingFileAppender.h>

// 注册多个 Appender
Logger::globalInstance()->registerAppender(new ConsoleAppender);
Logger::globalInstance()->registerAppender(new RollingFileAppender("/var/log/myapp.log"));

// 分类日志
Logger::globalInstance()->registerCategoryAppender("network",
    new FileAppender("/var/log/myapp-network.log"));
```

## 2. 文件系统工具

### 2.1 DStandardPaths — 标准路径

```cpp
#include <DStandardPaths>

QString configPath = DStandardPaths::writableLocation(
    QStandardPaths::AppConfigLocation);
QString cachePath = DStandardPaths::writableLocation(
    QStandardPaths::CacheLocation);
QString dataPath = DStandardPaths::writableLocation(
    QStandardPaths::AppDataLocation);
```

### 2.2 DFileWatcher — 文件监听

```cpp
#include <DFileWatcher>

auto *watcher = new DFileWatcher("/path/to/file", this);

connect(watcher, &DFileWatcher::fileModified, [](const QUrl &url) {
    qInfo() << "File modified:" << url;
});
```

## 3. DBus 辅助

### 3.1 DDBusInterface — DBus 接口调用

```cpp
#include <DDBusInterface>

DDBusInterface iface("org.example.Service",
                     "/org/example/Object",
                     "org.example.Interface",
                     QDBusConnection::sessionBus());

QDBusReply<QString> reply = iface.call("GetStatus");
```

### 3.2 DDBusSender — 发送 DBus 信号

```cpp
#include <DDBusSender>

DDBusSender()
    .service("org.example.Service")
    .path("/org/example/Object")
    .interface("org.example.Interface")
    .signal("StatusChanged")
    .arg("active")
    .publish();
```

## 4. 通知系统

```cpp
#include <DNotifySender>

DNotifySender("提示")
    .appBody("操作已完成")
    .appIcon("myapp")
    .timeOut(5000)       // 超时毫秒
    .replaceId(1)        // 替换同 ID 的通知
    .call();
```

## 5. 相关文档

- [filesystem.md](filesystem.md) — 文件系统工具（标准路径、文件监听、回收站）
- [dbus.md](dbus.md) — DBus 辅助接口详解
- [notify.md](notify.md) — 通知系统详解
