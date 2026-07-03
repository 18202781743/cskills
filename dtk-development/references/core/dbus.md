# DBus 辅助

## 1. DDBusInterface

```cpp
#include <DDBusInterface>

DDBusInterface iface("org.deepin.dde.Dock1",
                     "/org/deepin/dde/Dock1",
                     "org.deepin.dde.Dock1",
                     QDBusConnection::sessionBus());

// 调用方法（继承自 QDBusAbstractInterface::call）
QDBusReply<bool> reply = iface.call("IsVisible");
if (reply.isValid()) {
    bool visible = reply.value();
}

// 连接服务状态变化信号
connect(&iface, &DDBusInterface::serviceValidChanged, [](bool valid) {
    qInfo() << "Service valid:" << valid;
});
```

## 2. DDBusSender

```cpp
#include <DDBusSender>

// 调用方法（通过 method() 获取 DDBusCaller，.call() 发送）
DDBusSender()
    .service("org.example.Service")
    .path("/org/example/Object")
    .interface("org.example.Interface")
    .method("MethodName")
    .call();

// 带参数的方法调用
DDBusSender()
    .service("org.example.Service")
    .path("/org/example/Object")
    .interface("org.example.Interface")
    .method("SetValue")
    .arg(value)
    .call();
```

## 3. 相关文档

- [index.md](index.md) - 核心工具总览
