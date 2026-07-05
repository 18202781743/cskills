# 核心工具

## 1. 日志（DLogManager）

dtkcore 通过 `DLogManager` 提供便捷的日志初始化。直接使用 Qt 的 `qDebug()`/`qInfo()`/`qWarning()`/`qCritical()` 宏输出日志即可。

```cpp
#include <DLog>

// 一行初始化
DLogManager::registerConsoleAppender();   // 输出到控制台
DLogManager::registerFileAppender();      // 输出到文件（自动路径）
DLogManager::registerJournalAppender();   // 输出到 systemd journal

// 自定义路径和格式
DLogManager::setlogFilePath("/var/log/myapp.log");
DLogManager::setLogFormat("%{time}{yyyy-MM-dd HH:mm:ss.zzz} [%{type}] %{message}");
```

CMake 依赖（DtkCore 自动引入 dtklog）：

```cmake
find_package(DtkCore REQUIRED)
target_link_libraries(your_target Dtk::Core)
```

## 2. 文件系统

### 2.1 DStandardPaths — 标准路径

```cpp
#include <DStandardPaths>

QString config = DStandardPaths::writableLocation(QStandardPaths::AppConfigLocation);
QString data = DStandardPaths::writableLocation(QStandardPaths::AppDataLocation);
QString cache = DStandardPaths::writableLocation(QStandardPaths::CacheLocation);
QString temp = DStandardPaths::writableLocation(QStandardPaths::TempLocation);
```

### 2.2 DFileWatcher — 文件监听

```cpp
#include <DFileWatcher>

auto *watcher = new DFileWatcher("/path/to/file", this);
connect(watcher, &DFileWatcher::fileModified, [](const QUrl &url) {
    qInfo() << "File modified:" << url;
});
```

### 2.3 DTrashManager — 回收站

```cpp
#include <DTrashManager>

DTrashManager::instance()->moveToTrash("/path/to/file");
DTrashManager::instance()->cleanTrash();
```

## 3. DBus 辅助

### 3.1 DDBusInterface — 接口代理

继承 `QDBusAbstractInterface`，支持方法调用、属性读写、服务有效性监听。

```cpp
#include <DDBusInterface>

DDBusInterface iface("org.deepin.dde.Dock1",
                     "/org/deepin/dde/Dock1",
                     "org.deepin.dde.Dock1",
                     QDBusConnection::sessionBus());

// 调用方法（继承自 QDBusAbstractInterface::call）
QDBusReply<bool> reply = iface.call("IsVisible");

// 读写属性
QVariant v = iface.property("DisplayMode");
iface.setProperty("DisplayMode", value);

// 监听服务状态
connect(&iface, &DDBusInterface::serviceValidChanged, [](bool valid) {
    qInfo() << "Service valid:" << valid;
});
```

### 3.2 DDBusSender — 链式调用

builder 模式，适合单次方法调用和信号发送。

```cpp
#include <DDBusSender>

// 调用方法
DDBusSender()
    .service("org.example.Service")
    .path("/org/example/Object")
    .interface("org.example.Interface")
    .method("SetValue")
    .arg(42)
    .call();

// 读写属性
DDBusSender()
    .service("org.example.Service")
    .path("/org/example/Object")
    .interface("org.example.Interface")
    .property("DisplayMode")
    .get();

// 通过系统总线
DDBusSender::system()
    .service("org.freedesktop.login1")
    .path("/org/freedesktop/login1")
    .interface("org.freedesktop.login1.Manager")
    .method("CanReboot")
    .call();
```

## 4. 通知系统

`DNotifySender` 采用链式构建器模式，位于 `DUtil` 命名空间。

```cpp
#include <DNotifySender>

using namespace Dtk::Core::DUtil;

// 简单通知
DNotifySender("下载完成")
    .appBody("文件已保存到 /home/user/Downloads")
    .call();

// 带图标和超时
DNotifySender("操作完成")
    .appIcon("dialog-ok")
    .appBody("所有文件已同步")
    .timeOut(5000)
    .call();

// 带动作按钮
DNotifySender("确认删除")
    .appBody("确定要删除此文件吗？")
    .appIcon("dialog-warning")
    .actions({"open", "打开", "cancel", "取消"})
    .call();

// 更新已有通知
DNotifySender("下载进度")
    .appBody("50%")
    .replaceId(1)
    .call();
```

| 链式方法 | 说明 |
|----------|------|
| `DNotifySender(summary)` | 构造，传入通知标题 |
| `.appName(name)` | 应用名称 |
| `.appIcon(icon)` | 图标名称 |
| `.appBody(body)` | 通知正文 |
| `.replaceId(id)` | 替换 ID（更新已有通知） |
| `.timeOut(ms)` | 超时时间（毫秒） |
| `.actions(list)` | 动作列表（成对：id, 标签） |
| `.hints(map)` | 额外提示 |
| `.call()` | 发送通知 |

## 5. 相关文档

- [config/index.md](../config/index.md) — DConfig 配置系统
