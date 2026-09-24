---
name: dde-launchpad
description: 提供启动器显示隐藏切换和模式控制的 D-Bus 接口，以及仅作用于启动器自身的应用列表排序、应用显示过滤、图标缩放比例、按桌面条目 ID 搜索的 DConfig 配置项
Categories:
  - Application
---

# dde-launchpad

dde-launchpad 是 DDE 启动器组件，通过 Session 总线提供启动器的显示、隐藏、切换和模式控制能力，并通过 DConfig 管理启动器自身的应用列表排序、应用显示过滤、图标缩放比例和按桌面条目 ID 搜索行为。dde-launchpad 以 dde-shell applet 形式运行，其 DConfig 配置仅作用于 dde-launchpad 自身应用行为，不影响系统全局配置。

## D-Bus 接口

### 启动器控制

提供启动器的显示、隐藏、切换和模式控制能力。

详见 [org.deepin.dde.Launcher1.md](references/dbus/org.deepin.dde.Launcher1.md)

### 兼容性说明

dde-launchpad 仅导出 `org.deepin.dde.Launcher1` 一个 D-Bus 服务接口，不存在旧版别名或废弃接口。Dock 相关的历史别名接口属于 dde-shell（见 dde-shell skill），不在 dde-launchpad 中。

## DConfig 配置项

dde-launchpad 通过 DConfig 暴露启动器自身应用行为配置，配置资源挂载在 appId `org.deepin.dde.shell` 下。

### 启动器应用配置

控制启动器的应用列表排序类别、核心必要应用列表、应用排除列表、常用应用列表、按桌面条目 ID 搜索开关和全屏模式图标缩放比例。

详见 [org.deepin.ds.launchpad.md](references/config/org.deepin.ds.launchpad.md)
