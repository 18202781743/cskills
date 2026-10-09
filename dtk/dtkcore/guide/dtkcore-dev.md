# dtkcore-dev

dtkcore 的配置与设置接口提供统一的配置读写入口、配置缓存访问、配置文件直接访问、配置元信息查询，以及基于后端抽象的设置模型管理。设置模型支持分组层级结构、单项元数据与值管理，并提供系统设置后端和本地文件后端两种持久化实现。

dtkcore 的 DBus 通信接口提供链式 DBus 调用构造、方法调用参数追加与异步提交、远端属性读写、扩展接口代理（含属性缓存与批量获取）以及接口导出能力。调用方可通过链式入口依次指定总线、服务、路径和接口，再选择方法或属性操作。

dtkcore 的 DCI 与文本处理接口提供 DCI 容器的加载、节点查询、数据读取与写出，文本编码探测与字符集转换，以及安全字符串管理能力。

dtkcore 的文件与路径接口提供文件与目录监视（含抽象基类、系统文件监视器和监视管理器）、文件服务、桌面条目解析、标准路径定位、路径拼接工具、回收站操作和最近使用记录管理。监视类型向调用者报告创建、删除和修改事件。

dtkcore 的日志与通知接口提供日志管理（日志规则设置与日志文件定位）和桌面通知发送能力。

dtkcore 的系统信息与许可接口提供发行版、产品、组织、架构及主机硬件与运行状态查询，应用标识查询，以及许可信息（含组件级许可）读取能力。

dtkcore 的工具与线程接口提供单位换算与格式化（抽象基类、磁盘容量格式化、时间格式化）、线程投递（主版本 6 的线程投递类型与主版本 5 的线程调用代理）、单例基类模板、对象基类、虚函数表操作以及路径拼接工具。

## 开发包

当前版本使用 DTK6，开发包名为 `libdtk6core-dev`。该开发包提供 DTK6 的公开头文件和以下构建入口：

- CMake 包 `Dtk6Core` 与导出目标 `Dtk6::Core`
- pkg-config 模块 `dtk6core`
- qmake 模块 `dtkcore`

仍需维护 DTK5 工程时，使用兼容开发包 `libdtkcore-dev`。它提供 CMake 包 `DtkCore`、导出目标 `Dtk::Core`、pkg-config 模块 `dtkcore` 和同名 qmake 模块。

## 集成

### CMake 配置

CMake 是当前推荐的集成方式。DTK6 工程在已有构建目标上查找 `Dtk6Core` 并链接 `Dtk6::Core`：

```cmake
find_package(Dtk6Core REQUIRED)
target_link_libraries(your_target PRIVATE Dtk6::Core)
```

`your_target` 替换为使用方工程中的目标名。`Dtk6::Core` 会向该目标提供 dtkcore 的头文件搜索路径、链接信息、编译定义和传递依赖，不需要再使用 `include_directories()`、`link_directories()` 或逐项链接 dtkcore 所依赖的库。

仍使用 DTK5 的工程改为查找 `DtkCore` 并链接 `Dtk::Core`：

```cmake
find_package(DtkCore REQUIRED)
target_link_libraries(your_target PRIVATE Dtk::Core)
```

### 使用方式

构建目标链接 dtkcore 后，可以直接包含所需类型的公开转发头：

```cpp
#include <DConfig>
```

也可以包含对应的实际公开头文件，例如 `#include <dconfig.h>`。公开类型主要位于 `Dtk::Core` 命名空间，可使用完整限定名，也可在合适的作用域使用 `DCORE_USE_NAMESPACE`。


---

## 接口分类

- [配置与设置](dtkcore-dev/config-and-settings.md) — DConfig 配置读写、DConfigCache 缓存访问、DConfigFile 配置文件直接访问、DConfigMeta 配置元信息查询、DSettings 设置模型管理、DSettingsBackend 设置后端抽象、DSettingsDConfigBackend DConfig 后端实现、DSettingsGroup 分组管理、DSettingsOption 配置项管理、GSettingsBackend GSettings 后端、QSettingBackend QSetting 后端
- [DBus 通信](dtkcore-dev/dbus-communication.md) — DDBusCaller 链式调用、DDBusData 数据封装、DDBusExtendedAbstractInterface 接口代理、DDBusProperty 属性读写、DDBusSender 链式发送、DExportedInterface 接口导出
- [DCI 与文本处理](dtkcore-dev/dci-and-text-processing.md) — DDciFile DCI 容器加载与读写、DTextEncoding 文本编码探测与转换、DSecureString 安全字符串管理
- [文件与路径](dtkcore-dev/file-and-path.md) — DBaseFileWatcher 文件监视抽象基类、DFileWatcher 系统文件监视器、DFileSystemWatcher 文件系统监视器、DFileWatcherManager 监视管理器、DFileServices 文件服务、DDesktopEntry 桌面条目解析、DStandardPaths 标准路径定位、DPathBuf 路径拼接、DTrashManager 回收站操作、DRecentManager 最近使用管理、DRecentData 最近使用记录
- [日志与通知](dtkcore-dev/logging-and-notification.md) — DLogManager 日志规则设置与日志文件定位、DNotifySender 桌面通知发送
- [系统信息与许可](dtkcore-dev/system-info-and-license.md) — DSysInfo 发行版与硬件信息查询、DSGApplication 应用标识查询、DLicenseInfo 许可信息读取、DLicenseInfo::DComponentInfo 组件级许可信息
- [工具与线程](dtkcore-dev/tools-and-threading.md) — DAbstractUnitFormatter 单位格式化基类、DDiskSizeFormatter 磁盘容量格式化、DTimeUnitFormatter 时间格式化、DThreadUtils 线程投递、DThreadUtil::FunctionCallProxy 线程调用代理、DSingleton 单例基类模板、DObject 对象基类、DVtableHook 虚函数表操作
