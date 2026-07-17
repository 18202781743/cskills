# 工具类速查

DTK 工具类提供应用入口、DBus 通信、系统信息、日志等常用功能。

## 触发关键词

DApplication、DDBusSender、DSysInfo、DLog、单实例、系统版本、DBus 调用

---

## DApplication 应用入口

```cpp
#include <DApplication>

int main(int argc, char *argv[]) {
    DApplication a(argc, argv);
    a.setOrganizationName("deepin");
    a.setApplicationName("myapp");
    a.setApplicationVersion("1.0");
    a.loadTranslator();
    a.setProductIcon(QIcon(":/icon.png"));
    
    MainWindow w;
    w.show();
    return a.exec();
}
```

### 单实例模式

```cpp
a.setSingleInstance("myapp-unique-key");
connect(&a, &DApplication::newInstanceStarted, []() {
    // 已有实例启动，激活窗口
});
```

---

## DDBusSender DBus 通信

```cpp
#include <DDBusSender>

// Session Bus 调用
DDBusSender()
    .service("org.deepin.dde.Launcher1")
    .path("/org/deepin/dde/Launcher1")
    .interface("org.deepin.dde.Launcher1")
    .method("Show")
    .call();

// 发送通知
DDBusSender()
    .service("org.freedesktop.Notifications")
    .path("/org/freedesktop/Notifications")
    .interface("org.freedesktop.Notifications")
    .method("Notify")
    .arg("MyApp")
    .arg(0U)
    .arg("dialog-information")
    .arg("标题")
    .arg("内容")
    .arg(QStringList())
    .arg(QVariantMap())
    .arg(5000)
    .call();

// System Bus
DDBusSender::system()
    .service("org.freedesktop.login1")
    .path("/org/freedesktop/login1")
    .interface("org.freedesktop.login1.Manager")
    .method("PowerOff")
    .arg(false)
    .call();
```

---

## DSysInfo 系统信息

```cpp
#include <DSysInfo>

// 系统版本
QString version = DSysInfo::minorVersion();        // "23"
QString prettyName = DSysInfo::prettyProductName(); // "Deepin 23"

// 系统类型
auto type = DSysInfo::uosType();  // UosType / DeepinType / UnknownType

// 硬件信息
QString cpu = DSysInfo::cpuModelName();
qint64 mem = DSysInfo::memoryTotalSize();
```

---

## DLog 日志

```cpp
#include <DLog>

DLogManager::registerFileAppender("/var/log/myapp.log");
DLogManager::registerJournalAppender();

qInfo() << "Info message";
qWarning() << "Warning message";
```

---

## DDesktopServices 桌面服务

```cpp
#include <DDesktopServices>

// 打开文件
DDesktopServices::openFile("/path/to/file");

// 打开 URL
DDesktopServices::openUrl(QUrl("https://www.deepin.org"));

// 显示在文件管理器中
DDesktopServices::showInFileManager("/path/to/file");
```

---

## DWindowManagerHelper 窗口管理

```cpp
#include <DWindowManagerHelper>

auto *wm = DWindowManagerHelper::instance();

// 判断窗口管理器能力
bool hasComposite = wm->hasComposite();
bool hasBlur = wm->hasBlurWindow();

// 窗口管理器名称
QString name = wm->windowManagerName();  // KWin / DeepinWm / Treeland
```

---

## 单例模板 DSingleApplication

```cpp
#include <DSingleApplication>

class Manager : public DSingleApplication<Manager> {
    // 自动单例
};

Manager *instance = Manager::instance();
```

---

## 相关文档

- [theme-system.md](theme-system.md) — DGuiApplicationHelper
- [config-system.md](config-system.md) — DConfig
