# DBus 辅助

## 1. DDBusInterface

```cpp
#include <DDBusInterface>

DDBusInterface iface("org.deepin.dde.Dock1",
                     "/org/deepin/dde/Dock1",
                     QDBusConnection::sessionBus());

// 调用方法
QDBusReply<bool> reply = iface.call("IsVisible");
if (reply.isValid()) {
    bool visible = reply.value();
}

// 连接信号
connect(&iface, &DDBusInterface::signal, [](const QString &name, const QVariantList &args) {
    qInfo() << "Signal:" << name << args;
});
```

## 2. DDBusSender

```cpp
#include <DDBusSender>

// 发送信号
DDBusSender()
    .service("org.example.Service")
    .path("/org/example/Object")
    .interface("org.example.Interface")
    .signal("SignalName")
    .arg(value1)
    .arg(value2)
    .publish();
```

## 3. 相关文档

- [index.md](index.md) - 核心工具总览
