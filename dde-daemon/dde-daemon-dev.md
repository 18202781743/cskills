# dde-daemon 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-daemon |
| 版本 | （跟随仓库 master 分支） |
| 描述 | DDE 系统守护进程，使用 Go 语言编写，提供账户、音频、蓝牙、显示、输入设备、快捷键、系统信息等 DBus 服务 |
| Go 模块路径 | `github.com/linuxdeepin/dde-daemon` |
| 仓库地址 | https://github.com/linuxdeepin/dde-daemon.git |

## 2. 包依赖

### 运行时依赖
- golang (>= 1.20)
- libpulse, libbluetooth, libnl, libnss, libx11
- libnotify, libgtk-3
- dde-api, dtkcore

### 开发依赖
- Go (>= 1.20)
- pkg-config: libpulse, libbluetooth, libnl-3.0, libnss, x11
- Make

## 3. CMake 集成

不适用（纯 Go 项目，使用 Makefile 构建，无 CMake 配置）

## 4. pkg-config

不适用（不导出 .pc 文件）

## 5. 命名空间

不适用（Go 项目，使用 Go 包路径代替 C++ 命名空间）

Go 包路径示例：
- `github.com/linuxdeepin/dde-daemon/accounts1`
- `github.com/linuxdeepin/dde-daemon/audio1`
- `github.com/linuxdeepin/dde-daemon/display1`
- `github.com/linuxdeepin/dde-daemon/keybinding1`
- `github.com/linuxdeepin/dde-daemon/systeminfo1`

## 6. 关键公共类及功能描述

dde-daemon 是 Go 后端服务，无 C++ 公共类。核心模块：

| 模块 | Go 包路径 | 功能 |
|------|-----------|------|
| accounts1 | `dde-daemon/accounts1` | 用户账户管理 |
| audio1 | `dde-daemon/audio1` | 音频设备管理 |
| bluetooth1 | `dde-daemon/bluetooth1` | 蓝牙设备管理 |
| display1 | `dde-daemon/display1` | 显示器、亮度管理 |
| keybinding1 | `dde-daemon/keybinding1` | 快捷键管理 |
| systeminfo1 | `dde-daemon/systeminfo1` | 系统信息 |
| timedate1 | `dde-daemon/timedate1` | 时间日期管理 |
| inputdevices1 | `dde-daemon/inputdevices1` | 输入设备管理 |
| grub2 | `dde-daemon/grub2` | GRUB 配置 |
| sessionwatcher1 | `dde-daemon/sessionwatcher1` | 会话监控 |
| lastore1 | `dde-daemon/lastore1` | 应用商店后端 |
| search1 | `dde-daemon/search1` | 搜索服务 |
| soundeffect1 | `dde-daemon/soundeffect1` | 音效服务 |
| xeventmonitor1 | `dde-daemon/...` | X 事件监控 |
| zone1 | `dde-daemon/zone1` | 热区管理 |

## 7. QML 模块

不适用

## 8. DBus 接口

dde-daemon 提供大量 DBus 服务，以下为关键服务列表：

| DBus 服务名 | 说明 |
|-------------|------|
| `org.deepin.dde.Daemon1` | 主守护进程服务 |
| `org.deepin.dde.Accounts1` | 账户管理 |
| `org.deepin.dde.Audio1` | 音频管理 |
| `org.deepin.dde.Bluetooth1` | 蓝牙管理 |
| `org.deepin.dde.Display1` | 显示管理 |
| `org.deepin.dde.InputDevices1` | 输入设备管理 |
| `org.deepin.dde.Keybinding1` | 快捷键管理 |
| `org.deepin.dde.KeyEvent1` | 按键事件 |
| `org.deepin.dde.SystemInfo1` | 系统信息 |
| `org.deepin.dde.Timedate1` | 时间日期 |
| `org.deepin.dde.LangSelector1` | 语言选择 |
| `org.deepin.dde.Search1` | 搜索服务 |
| `org.deepin.dde.SoundEffect1` | 音效 |
| `org.deepin.dde.SessionWatcher1` | 会话监控 |
| `org.deepin.dde.LastoreSessionHelper1` | 应用商店辅助 |
| `org.deepin.dde.XEventMonitor1` | X 事件监控 |
| `org.deepin.dde.Zone1` | 热区管理 |
| `org.deepin.dde.Grub2` | GRUB 配置 |
| `org.deepin.dde.BacklightHelper1` | 背光辅助 |
| `org.deepin.dde.Greeter1` | Greeter 服务 |
| `org.deepin.dde.LockService1` | 锁屏服务 |
| `org.deepin.dde.TrayManager1` | 托盘管理 |
| `org.deepin.dde.ImageEffect1` | 图像效果 |
| `org.deepin.dde.EventLog1` | 事件日志 |
| `org.deepin.dde.Gesture1` | 手势识别 |
| `org.deepin.dde.Uadp1` | UADP 服务 |
| `org.deepin.dde.ClipboardManager1` | 剪贴板管理 |
| `org.deepin.dde.SwapSchedHelper1` | 交换调度辅助 |
| `org.deepin.dde.AirplaneMode1` | 飞行模式 |
| `org.freedesktop.ScreenSaver` | 屏幕保护（兼容 freedesktop 规范） |

### 典型用法示例

```bash
# 通过 dbus-send 调用音频服务
dbus-send --session --dest=org.deepin.dde.Audio1 \
  --type=method_call --print-reply \
  /org/deepin/dde/Audio1 org.deepin.dde.Audio1.defaultSink
```

## 9. 插件开发

不适用
