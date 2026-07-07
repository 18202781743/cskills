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

## 4. 系统信息

`DSysInfo` 提供操作系统类型、版本、硬件信息等静态查询接口。

### 头文件

```cpp
#include <DSysInfo>
```

### 实际分析的文件

`DSysInfo` 从以下系统文件读取信息：

- `/etc/os-release` — 发行版标识、版本号、产品类型
- `/etc/deepin-version` — Deepin/UOS 版本详情（edition、major/minor/build version）
- `/etc/uos-version` — UOS 专用版本信息
- `/proc/cpuinfo` — CPU 型号
- `/proc/meminfo` — 内存信息
- `/proc/stat` — 启动时间
- `/etc/hostname` — 主机名

### 常用接口

**产品类型判断：**

```cpp
#include <DSysInfo>

DSysInfo::ProductType type = DSysInfo::productType();
bool isDeepin = DSysInfo::isDeepin();
bool isDDE = DSysInfo::isDDE();
bool isCommunity = DSysInfo::isCommunityEdition();

QString osName = DSysInfo::operatingSystemName();
QString version = DSysInfo::productVersion();
```

**Deepin/UOS 版本信息：**

```cpp
DSysInfo::DeepinType dt = DSysInfo::deepinType(); // 桌面版/专业版/服务器版
QString version = DSysInfo::deepinVersion();
QString edition = DSysInfo::deepinEdition();

DSysInfo::UosType ut = DSysInfo::uosType();          // 桌面/服务器/设备/智能终端
DSysInfo::UosEdition ue = DSysInfo::uosEditionType(); // 专业版/家庭版/社区版/教育版/...
QString productName = DSysInfo::uosProductTypeName();
QString systemName = DSysInfo::uosSystemName();

QString sp = DSysInfo::spVersion();     // 补丁版本
QString major = DSysInfo::majorVersion();
QString minor = DSysInfo::minorVersion();
```

**发行版组织信息：**

```cpp
QString orgName = DSysInfo::distributionOrgName(
    DSysInfo::Distribution, QLocale::system());
QString vendor = DSysInfo::distributionOrgName(
    DSysInfo::Distributor, QLocale::system());
QString logo = DSysInfo::distributionOrgLogo(
    DSysInfo::Distribution, DSysInfo::Normal, ":/logo.svg");
```

**硬件与运行信息：**

```cpp
QString hostname = DSysInfo::computerName();
QString cpu = DSysInfo::cpuModelName();
qint64 memSize = DSysInfo::memoryInstalledSize();
qint64 diskSize = DSysInfo::systemDiskSize();
qint64 uptime = DSysInfo::uptime(); // 秒
DSysInfo::Arch arch = DSysInfo::arch(); // X86_64 / ARM64 / LOONGARCH64 / ...
```

### 枚举速查

| 枚举 | 常用值 |
|------|--------|
| `ProductType` | `Deepin`, `Uos`, `Ubuntu`, `Debian`, `Fedora`, `ArchLinux`, `CentOS`, `openSUSE`, `NixOS` 等 |
| `DeepinType` | `DeepinDesktop`, `DeepinProfessional`, `DeepinServer`, `DeepinPersonal`, `DeepinMilitary` |
| `UosType` | `UosDesktop`, `UosServer`, `UosDevice`, `UosSmart` |
| `UosEdition` | `UosProfessional`, `UosHome`, `UosCommunity`, `UosEnterprise`, `UosEducation`, `UosMilitary`, `UosEuler` 等 |
| `Arch` | `X86_64`, `ARM64`, `LOONGARCH64`, `MIPS64`, `SW_64`, `RISCV64` 等 |
| `OrgType` | `Distribution`（发行版）, `Distributor`（发行商）, `Manufacturer`（制造商） |
| `LogoType` | `Normal`, `Light`, `Symbolic`, `Transparent` |

## 5. 拼音转换

拼音功能为 dtkcore 中的自由函数，位于 `Dtk::Core` 命名空间。

### 头文件

```cpp
#include <dpinyin.h>
```

### 基本用法

```cpp
// 无多音字支持，返回单个字符串
QString pinyin = Dtk::Core::Chinese2Pinyin("中国");  // "zhongguo"

// 多音字支持，返回所有组合
QStringList list = Dtk::Core::pinyin("重庆");  // [ "chongqing", "zhongqing" ]

// 首字母
QStringList fl = Dtk::Core::firstLetters("中国");  // [ "zg" ]
```

### 声调控制

`ToneStyle` 枚举控制输出格式：

| 值 | 示例输出 |
|----|----------|
| `TS_NoneTone` | `"zhongguo"` |
| `TS_Tone`（默认） | `"zhōngguó"` |
| `TS_ToneNum` | `"zhong1guo2"` |

```cpp
Dtk::Core::pinyin("中国", Dtk::Core::TS_Tone);
Dtk::Core::firstLetters("中国", Dtk::Core::TS_Tone);
```

## 6. 相关文档

- [index.md](index.md) — 工具类索引
- [log.md](log.md) — 日志系统
- [singleton.md](singleton.md) — 单实例应用
