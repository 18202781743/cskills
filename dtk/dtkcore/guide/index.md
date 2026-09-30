# dtkcore 二次开发文档 · 概览

## 项目定位

dtkcore 是基于 Qt 的 C++ 基础库，提供配置与设置、日志、文件与目录、系统信息、DBus 通信、通知、文本处理和线程调度能力。界面控件与视觉主题由上层库提供。

## 导出类型

- [配置与设置](dtkcore-dev.md#配置与设置)：配置读写、配置缓存、配置元信息、设置模型与后端
- [DBus 通信](dtkcore-dev.md#dbus-通信)：链式 DBus 调用、方法调用、属性访问、接口代理与导出
- [文件与路径](dtkcore-dev.md#文件与路径)：文件监视、文件服务、桌面条目、标准路径、回收站与最近使用记录
- [系统信息与许可](dtkcore-dev.md#系统信息与许可)：系统信息查询、应用标识与许可信息
- [日志与通知](dtkcore-dev.md#日志与通知)：日志管理与桌面通知
- [DCI 与文本处理](dtkcore-dev.md#dci-与文本处理)：DCI 容器读写、文本编码探测与安全字符串
- [工具与线程](dtkcore-dev.md#工具与线程)：单位格式化、线程投递、单例、对象基类与虚函数表工具

## 按功能查阅

- 管理配置或设置：参见 [DConfig](dtkcore-dev.md#dconfig) 与 [DSettings](dtkcore-dev.md#dsettings)
- 发起 DBus 调用或访问远端属性：参见 [DDBusSender](dtkcore-dev.md#ddbussender) 与 [DDBusProperty](dtkcore-dev.md#ddbusproperty)
- 监视文件或查询标准路径：参见 [DFileWatcher](dtkcore-dev.md#dfilewatcher) 与 [DStandardPaths](dtkcore-dev.md#dstandardpaths)
- 查询系统信息或读取许可：参见 [DSysInfo](dtkcore-dev.md#dsysinfo) 与 [DLicenseInfo](dtkcore-dev.md#dlicenseinfo)
- 管理日志或发送通知：参见 [DLogManager](dtkcore-dev.md#dlogmanager) 与 [DNotifySender](dtkcore-dev.md#dnotifysender)
- 读取 DCI 资源或探测文本编码：参见 [DDciFile](dtkcore-dev.md#ddcifile) 与 [DTextEncoding](dtkcore-dev.md#dtextencoding)
- 线程投递或单位格式化：参见 [DThreadUtils](dtkcore-dev.md#dthreadutils) 与 [DDiskSizeFormatter](dtkcore-dev.md#ddisksizeformatter)
- 将 dtkcore 引入 CMake 工程：参见 [dtkcore-dev.md](dtkcore-dev.md) 中的 `## 开发包` 与 `## 集成` 章节
