# 核心工具总览

## 1. 概述

dtkcore 提供丰富的工具类，按模块分类：

| 模块 | 主要功能 |
|------|----------|
| `base` | DObject, DSingleton, DError |
| `filesystem` | 文件监听、标准路径、回收站 |
| `global` | 配置、桌面入口、系统信息 |
| `settings` | DSettings 框架 |
| `util` | DBus、通知、拼音、线程工具 |

## 2. 常用工具

### 2.1 DStandardPaths — 标准路径

```cpp
#include <DStandardPaths>

QString configPath = DStandardPaths::writableLocation(
    QStandardPaths::AppConfigLocation);
QString cachePath = DStandardPaths::writableLocation(
    QStandardPaths::CacheLocation);
```

### 2.2 DFileWatcher — 文件监听

```cpp
#include <DFileWatcher>

auto *watcher = new DFileWatcher("/path/to/file", this);

connect(watcher, &DFileWatcher::fileModified, [](const QUrl &url) {
    qInfo() << "File modified:" << url;
});
```

### 2.3 DNotifySender — 通知

```cpp
#include <DNotifySender>

using namespace Dtk::Core::DUtil;

DNotifySender("提示")
    .appBody("操作已完成")
    .call();
```

### 2.4 DDBusInterface — DBus 辅助

```cpp
#include <DDBusInterface>

DDBusInterface iface("org.example.Service",
                     "/org/example/Object",
                     "org.example.Interface",
                     QDBusConnection::sessionBus());

// 调用方法（继承自 QDBusAbstractInterface::call）
QDBusReply<QString> reply = iface.call("GetStatus");
```

## 3. 相关文档

- [filesystem.md](filesystem.md) - 文件系统工具
- [dbus.md](dbus.md) - DBus 辅助
- [notify.md](notify.md) - 通知系统
