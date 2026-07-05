# 单实例应用

## 1. 概述

DTK 提供基于 `QLocalServer`/`QLocalSocket` 的单实例机制，确保同一应用只运行一个进程。第二个实例启动时会通知第一个实例，并传递启动参数。

## 2. 基本用法

在 `main()` 中调用 `DGuiApplicationHelper::setSingleInstance()`：

```cpp
#include <DGuiApplicationHelper>
#include <QApplication>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    if (!DGuiApplicationHelper::setSingleInstance("myapp")) {
        qInfo() << "另一实例已在运行，退出";
        return 0;
    }

    // 监听新实例启动
    QObject::connect(DGuiApplicationHelper::instance(),
                     &DGuiApplicationHelper::newProcessInstance,
                     [](qint64 pid, const QStringList &args) {
        qInfo() << "新实例启动:" << pid << args;
    });

    return app.exec();
}
```

使用 `DApplication`（dtkwidget）时更简洁，自动处理窗口激活：

```cpp
#include <DApplication>

int main(int argc, char *argv[]) {
    DApplication app(argc, argv);

    if (!app.setSingleInstance("myapp")) {
        return 0;
    }

    // DApplication 自动将 newProcessInstance 信号转发为 newInstanceStarted
    QObject::connect(&app, &DApplication::newInstanceStarted, []() {
        qInfo() << "新实例已启动";
    });

    return app.exec();
}
```

## 3. 原理

### 3.1 QLocalServer 竞争机制

```
第一个进程
  → QLockFile("_d_dtk_single_instance_<uid>_<key>.lock").tryLock() 成功
  → QLocalServer.listen("_d_dtk_single_instance_<uid>_<key>")
  → 进入事件循环，等待新连接

第二个进程
  → QLockFile.tryLock() 失败
  → QLocalSocket 连接到第一个进程的 QLocalServer
  → 接收第一个进程的信息（pid, args）
  → 发送自己的信息（pid, args）
  → 退出
```

### 3.2 进程间传递的数据

通过 `QDataStream` 序列化传递：

1. **协议版本号** (`qint8`) — 未来扩展用
2. **进程 PID** (`qint64`)
3. **启动参数** (`QStringList`) — `QApplication::arguments()`

### 3.3 SingleScope 作用域

| 枚举 | 说明 |
|------|------|
| `UserScope` | 同一用户下唯一（默认） |
| `GroupScope` | 同一用户组下唯一 |
| `WorldScope` | 全局唯一 |

```cpp
DGuiApplicationHelper::setSingleInstance("myapp", DGuiApplicationHelper::GroupScope);
```

## 4. 窗口激活

### 4.1 DApplication 自动激活

使用 `DApplication` + `DMainWindow` 时，设置 `autoActivateWindows` 后，新实例启动时自动找到第一个 `DMainWindow` 并激活：

```cpp
DApplication app(argc, argv);
app.setAutoActivateWindows(true);
```

### 4.2 手动激活

```cpp
QObject::connect(&app, &DApplication::newInstanceStarted, []() {
    for (QWidget *w : qApp->topLevelWidgets()) {
        if (auto *mainWin = qobject_cast<QMainWindow*>(w)) {
            if (mainWin->isMinimized() || mainWin->isHidden())
                mainWin->showNormal();
            mainWin->activateWindow();
            break;
        }
    }
});
```

## 5. 沙箱环境（Flatpak）

沙箱环境中的 DBus 方案（需编译时启用 `DTK_DBUS_SINGLEINSTANCE` 宏）：通过注册 DBus 服务名 `com.deepin.SingleInstance.<key>` 判断唯一性。无法注册说明已有实例。

## 6. 注意事项

- `setSingleInstanceInterval(ms)` 必须在 `setSingleInstance()` 之前调用，控制新实例等待第一个实例响应的超时时间（默认 3000ms）
- Linux 下 socket key 包含 uid 和 pid namespace，确保不同用户和容器隔离
- `DGuiApplicationHelper::newProcessInstance` 信号携带 pid 和 arguments
- 窗口激活部分仅对 `DMainWindow` 类型生效，普通 `QMainWindow` 需手动处理

## 7. 相关文档

- [index.md](index.md) — 工具类索引
- [log.md](log.md) — 日志系统
