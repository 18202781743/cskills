# 文件系统工具

## 1. DStandardPaths

```cpp
#include <DStandardPaths>
#include <QStandardPaths>

// 获取标准路径（使用 QStandardPaths::StandardLocation 枚举）
QString config = DStandardPaths::writableLocation(QStandardPaths::AppConfigLocation);
QString data = DStandardPaths::writableLocation(QStandardPaths::AppDataLocation);
QString cache = DStandardPaths::writableLocation(QStandardPaths::CacheLocation);
QString temp = DStandardPaths::writableLocation(QStandardPaths::TempLocation);
```

## 2. DFileWatcher

```cpp
#include <DFileWatcher>

// 构造函数传入文件路径，监听单个文件
auto *watcher = new DFileWatcher("/path/to/watch", this);

// 文件修改信号
connect(watcher, &DFileWatcher::fileModified, [](const QUrl &url) {
    // 文件变化处理
});
```

## 3. DTrashManager

```cpp
#include <DTrashManager>

// 移动到回收站（实例方法，通过 instance() 获取单例）
DTrashManager::instance()->moveToTrash("/path/to/file");

// 清空回收站
DTrashManager::instance()->cleanTrash();
```

## 4. 相关文档

- [index.md](index.md) - 核心工具总览
