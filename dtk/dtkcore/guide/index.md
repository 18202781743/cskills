# dtkcore 二次开发文档 · 概览

## 项目定位

dtkcore 是基于 Qt 的 C++ 基础库，提供配置与设置、日志、文件与目录、系统信息、DBus 通信、通知、文本处理和线程调度能力。界面控件与视觉主题由上层库提供。

## 导出类型

- [配置与设置接口](config-settings.md)：配置读写、配置缓存、配置元信息、设置模型与后端
- [DBus 通信接口](dbus.md)：链式 DBus 调用、方法调用、属性访问、接口代理与导出
- [文件与路径接口](file-path.md)：文件监视、文件服务、桌面条目、标准路径、回收站与最近使用记录
- [系统信息与许可接口](system-info.md)：系统信息查询、应用标识与许可信息
- [日志与通知接口](log-notify.md)：日志管理与桌面通知
- [DCI 与文本处理接口](dci-text.md)：DCI 容器读写、文本编码探测与安全字符串
- [工具与线程接口](utility.md)：单位格式化、线程投递、单例、对象基类与虚函数表工具

## 按功能查阅

- 管理配置或设置：参见 [DConfig](config-settings.md#dconfig) 与 [DSettings](config-settings.md#dsettings)
- 发起 DBus 调用或访问远端属性：参见 [DDBusSender](dbus.md#ddbussender) 与 [DDBusProperty](dbus.md#ddbusproperty)
- 监视文件或查询标准路径：参见 [DFileWatcher](file-path.md#dfilewatcher) 与 [DStandardPaths](file-path.md#dstandardpaths)
- 查询系统信息或读取许可：参见 [DSysInfo](system-info.md#dsysinfo) 与 [DLicenseInfo](system-info.md#dlicenseinfo)
- 管理日志或发送通知：参见 [DLogManager](log-notify.md#dlogmanager) 与 [DNotifySender](log-notify.md#dnotifysender)
- 读取 DCI 资源或探测文本编码：参见 [DDciFile](dci-text.md#ddcifile) 与 [DTextEncoding](dci-text.md#dtextencoding)
- 线程投递或单位格式化：参见 [DThreadUtils](utility.md#dthreadutils) 与 [DDiskSizeFormatter](utility.md#ddisksizeformatter)
- 将 dtkcore 引入 CMake 工程：参见各导出类型文件中的 `## 开发包` 与 `## 集成` 章节
