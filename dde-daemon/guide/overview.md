# dde-daemon 二次开发文档 · 概览

## 项目定位

dde-daemon 是 DDE 系统守护进程，使用 Go 语言编写，以 DBus 服务方式运行，提供账户管理、音频设备管理、蓝牙设备管理、显示器与亮度管理、输入设备管理、快捷键管理、系统信息查询、时间日期管理、GRUB 配置、会话监控、应用商店后端、搜索服务、音效服务、X 事件监控和热区管理能力。使用方通过 DBus 接口与之交互。

## 术语与缩写

- **Go 模块路径**：`github.com/linuxdeepin/dde-daemon`，Go 包以此为前缀路径组织。
- **DBus 服务**：dde-daemon 在系统总线和会话总线上注册的 DBus 服务接口，使用方通过服务名和对象路径连接。
- **DBus 属性**：远端接口上的具名值，使用方可读取或监听变化。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以 DBus 服务名为章节，逐一说明各接口的定位、功能能力和使用场景。

## 全局约定

dde-daemon 是纯 Go 项目，不安装 C++ 公共头文件，不导出 CMake 配置文件或库目标。使用方通过 DBus 接口访问其功能。Go 模块路径为 `github.com/linuxdeepin/dde-daemon`，内部按功能划分为 accounts1、audio1、bluetooth1、display1、keybinding1、systeminfo1、timedate1、inputdevices1、grub2、sessionwatcher1、lastore1、search1、soundeffect1、xeventmonitor1、zone1 等 Go 包。

## 按功能查阅

- 管理用户账户：参见 [org.deepin.dde.Accounts1](modules.md#orgdeepinddeaccounts1)。
- 管理音频设备：参见 [org.deepin.dde.Audio1](modules.md#orgdeepinddeaudio1)。
- 管理蓝牙设备：参见 [org.deepin.dde.Bluetooth1](modules.md#orgdeepinddebluetooth1)。
- 管理显示器与亮度：参见 [org.deepin.dde.Display1](modules.md#orgdeepinddedisplay1)。
- 管理输入设备：参见 [org.deepin.dde.InputDevices1](modules.md#orgdeepinddeinputdevices1)。
- 管理快捷键：参见 [org.deepin.dde.Keybinding1](modules.md#orgdeepinddekeybinding1)。
- 查询系统信息：参见 [org.deepin.dde.SystemInfo1](modules.md#orgdeepinddesysteminfo1)。
- 管理时间日期：参见 [org.deepin.dde.Timedate1](modules.md#orgdeepinddetimedate1)。
- 配置 GRUB：参见 [org.deepin.dde.Grub2](modules.md#orgdeepinddegrub2)。
- 监控会话状态：参见 [org.deepin.dde.SessionWatcher1](modules.md#orgdeepinddesessionwatcher1)。
- 管理应用商店后端：参见 [org.deepin.dde.LastoreSessionHelper1](modules.md#orgdeepinddelastoresessionhelper1)。
- 使用搜索服务：参见 [org.deepin.dde.Search1](modules.md#orgdeepinddesearch1)。
- 管理音效：参见 [org.deepin.dde.SoundEffect1](modules.md#orgdeepinddesoundeffect1)。
- 监控 X 事件：参见 [org.deepin.dde.XEventMonitor1](modules.md#orgdeepinddexeventmonitor1)。
- 管理热区：参见 [org.deepin.dde.Zone1](modules.md#orgdeepinddezone1)。
