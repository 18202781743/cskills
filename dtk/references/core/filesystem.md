# 文件系统工具

## 1. DStandardPaths

```cpp
#include <DStandardPaths>

// 获取标准路径
QString config = DStandardPaths::writableLocation(DStandardPaths::AppConfigLocation);
QString data = DStandardPaths::writableLocation(DStandardPaths::AppDataLocation);
QString cache = DStandardPaths::writableLocation(DStandardPaths::CacheLocation);
QString temp = DStandardPaths::writableLocation(DStandardPaths::TempLocation);
```

## 2. DFileWatcher

```cpp
#include <DFileWatcher>

auto *watcher = new DFileWatcher(this);
watcher->addPath("/path/to/watch");

connect(watcher, &DFileWatcher::fileChanged, [](const QString &path) {
    // 文件变化处理
});
```

## 3. DTrashManager

```cpp
#include <DTrashManager>

// 移动到回收站
DTrashManager::moveToTrash("/path/to/file");

// 清空回收站
DTrashManager::emptyTrash();
```

## 4. 相关文档

- [index.md](index.md) - 核心工具总览
