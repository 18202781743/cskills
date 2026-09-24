---
name: dde-tray-loader
description: dde-tray-loader 是 DDE 托盘加载器组件，负责加载和管理系统托盘区域的插件。提供全局的键盘布局切换与托盘图标管理 Session D-Bus 接口，以及仅作用于 dde-tray-loader 自身的托盘插件加载命令行工具和任务栏插件 DConfig 配置项（涵盖默认驻留列表、插件排序、关机菜单、通知状态、音量调节、充电保护阈值）
Categories:
  - Application
---

# dde-tray-loader

dde-tray-loader 是 DDE 托盘加载器组件，负责加载和管理系统托盘区域的插件。该 skill 提供以下能力：

- **全局 Session D-Bus 接口**：键盘布局切换和状态查询（Keyboard1）、托盘图标管理和通知控制（TrayManager1），对整个桌面会话生效
- **自身 CLI 工具**：`trayplugin-loader`，仅作用于 dde-tray-loader 自身的插件加载，由 dde-shell 在会话启动时自动拉起
- **自身 DConfig 配置项**：任务栏插件的默认驻留列表、插件排序、关机按钮右键菜单、通知未读状态、音量调节、充电保护阈值，仅作用于 dde-tray-loader 自身

## CLI 命令

### trayplugin-loader

dde-tray-loader 自身的托盘插件加载器，负责加载和管理系统托盘区域的插件。

详见 [trayplugin-loader.md](references/cli/trayplugin-loader.md)


## D-Bus 接口

### 键盘布局

提供全局的键盘布局切换和状态查询 Session D-Bus 接口。

详见 [org.deepin.dde.Keyboard1.md](references/dbus/org.deepin.dde.Keyboard1.md)

### 托盘管理

提供全局的托盘图标管理和通知控制 Session D-Bus 接口。

详见 [org.deepin.dde.TrayManager1.md](references/dbus/org.deepin.dde.TrayManager1.md)

### 兼容性说明

dde-tray-loader 的 D-Bus 接口（Keyboard1、TrayManager1）服务名稳定，无历史别名或兼容性接口。

## DConfig 配置项

dde-tray-loader 自身插件的 DConfig 配置资源，仅作用于 dde-tray-loader 自身。

### 任务栏插件通用配置

默认驻留任务栏插件列表和插件排序配置。

详见 [org.deepin.dde.dock.plugin.common](references/config/org.deepin.dde.dock.plugin.common.md)

### 关机按钮配置

关机按钮右键菜单内容配置。

详见 [org.deepin.dde.dock.plugin.shutdown](references/config/org.deepin.dde.dock.plugin.shutdown.md)

### 通知插件配置

通知未读状态配置。

详见 [org.deepin.dde.dock.plugin.notification](references/config/org.deepin.dde.dock.plugin.notification.md)

### 音量插件配置

音量滑动条和无输出端口时音量调节配置。

详见 [org.deepin.dde.dock.plugin.sound](references/config/org.deepin.dde.dock.plugin.sound.md)

### 电源插件配置

充电保护电量阈值和电池时间信息显示配置。

详见 [org.deepin.dde.dock.plugin.power](references/config/org.deepin.dde.dock.plugin.power.md)
