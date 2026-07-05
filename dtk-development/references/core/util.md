# 工具集

## 1. 文件系统

### 1.1 DStandardPaths — 标准路径

```cpp
#include <DStandardPaths>

QString config = DStandardPaths::writableLocation(QStandardPaths::AppConfigLocation);
QString data = DStandardPaths::writableLocation(QStandardPaths::AppDataLocation);
QString cache = DStandardPaths::writableLocation(QStandardPaths::CacheLocation);
QString temp = DStandardPaths::writableLocation(QStandardPaths::TempLocation);
```

### 1.2 DFileWatcher — 文件监听

```cpp
#include <DFileWatcher>

auto *watcher = new DFileWatcher("/path/to/file", this);
connect(watcher, &DFileWatcher::fileModified, [](const QUrl &url) {
    qInfo() << "File modified:" << url;
});
```

### 1.3 DTrashManager — 回收站

```cpp
#include <DTrashManager>

DTrashManager::instance()->moveToTrash("/path/to/file");
DTrashManager::instance()->cleanTrash();
```

## 2. DBus 辅助

### 2.1 DDBusInterface — 接口代理

继承 `QDBusAbstractInterface`，核心增强：

**自动服务监听：** 构造时异步检查服务是否存在，不存在时监听 `NameOwnerChanged` 信号，服务上线后自动建立连接。

```cpp
#include <DDBusInterface>

DDBusInterface iface("org.deepin.dde.Dock1",
                     "/org/deepin/dde/Dock1",
                     "org.deepin.dde.Dock1",
                     QDBusConnection::sessionBus());

// 方法调用（继承自 QDBusAbstractInterface::call）
QDBusReply<bool> reply = iface.call("IsVisible");

// 服务有效性
bool valid = iface.serviceValid();
connect(&iface, &DDBusInterface::serviceValidChanged, [](bool valid) {
    qInfo() << "Service valid:" << valid;
});
```

**属性读写：** 通过 `org.freedesktop.DBus.Properties` 接口，自动适配类型。

```cpp
// 读取属性
QVariant v = iface.property("DisplayMode");

// 设置属性
iface.setProperty("DisplayMode", value);
```

**Suffix 机制：** 当同一个 parent 对象上连接多个 `DDBusInterface` 实例时，通过 suffix 区分同名属性。

```cpp
DDBusInterface iface1("com.example.Svc", "/", "com.example.Iface1", QDBusConnection::sessionBus(), parent);
iface1.setSuffix("-iface1");

DDBusInterface iface2("com.example.Svc", "/", "com.example.Iface2", QDBusConnection::sessionBus(), parent);
iface2.setSuffix("-iface2");
```

**自动信号转发：** 传入 `parent` 对象后，`DDBusInterface` 会内省远程接口的信号签名，自动将匹配的远程信号转发到 parent 上对应的 `Q_SIGNAL`。无需手动 `QObject::connect`。

### 2.2 DDBusSender — 链式调用

builder 模式，适合单次调用。

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

DDBusSender()
    .service("org.example.Service")
    .path("/org/example/Object")
    .interface("org.example.Interface")
    .property("DisplayMode")
    .set(1);

// 系统总线
DDBusSender::system()
    .service("org.freedesktop.login1")
    .path("/org/freedesktop/login1")
    .interface("org.freedesktop.login1.Manager")
    .method("CanReboot")
    .call();
```

## 3. 通知系统

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

## 4. 相关文档

- [index.md](index.md) — 核心工具索引
- [log.md](log.md) — 日志系统
- [singleton.md](singleton.md) — 单实例应用
