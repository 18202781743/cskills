---
name: dde-tray-loader
description: 提供键盘布局切换与托盘图标管理的 Session D-Bus 接口，以及 dde-tray-loader 自身的托盘插件加载命令行工具、任务栏插件默认驻留列表与电源插件充电保护阈值的 DConfig 配置项
Categories:
  - Application
---

# dde-tray-loader

dde-tray-loader 是 DDE 托盘加载器组件。通过 Session 总线提供键盘布局切换和托盘图标管理能力；同时提供 dde-tray-loader 自身的托盘插件加载命令行工具和任务栏插件 DConfig 配置项。

## CLI 命令

### trayplugin-loader

dde-tray-loader 自身的托盘插件加载器，负责加载和管理系统托盘区域的插件。

详见 [trayplugin-loader.md](references/cli/trayplugin-loader.md)


## D-Bus 接口

### 键盘布局

提供键盘布局切换和状态查询的 Session D-Bus 接口。

详见 [org.deepin.dde.Keyboard1.md](references/dbus/org.deepin.dde.Keyboard1.md)

### 托盘管理

提供托盘图标管理和通知控制的 Session D-Bus 接口。

详见 [org.deepin.dde.TrayManager1.md](references/dbus/org.deepin.dde.TrayManager1.md)

### 兼容性说明

dde-tray-loader 的 D-Bus 接口（Keyboard1、TrayManager1）服务名稳定，无历史别名或兼容性接口。仓库中 `plugins/dde-dock/dbus/xml/` 目录下的 XML 文件为调用其他服务的客户端代理定义，非本仓库导出的接口；FDO Selection Manager 使用 X11 selection 机制（`_NET_SYSTEM_TRAY`），不属于 D-Bus 接口。

## DConfig 配置项

dde-tray-loader 自身插件的 DConfig 配置资源，管理任务栏插件默认驻留列表和电源插件充电保护阈值。

### 任务栏插件通用配置

默认驻留任务栏插件列表配置。

详见 [org.deepin.dde.dock.plugin.common](references/config/org.deepin.dde.dock.plugin.common.md)

### 电源插件配置

充电保护电量阈值、显示电池时间信息配置。

详见 [org.deepin.dde.dock.plugin.power](references/config/org.deepin.dde.dock.plugin.power.md)
