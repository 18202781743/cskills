# dde-launchpad 二次开发文档 · 概览

## 项目定位

dde-launchpad 是 DDE 启动器，提供全屏模式和窗口模式的应用启动界面。以 dde-shell applet 插件形式部署，通过 DBus 接口向外部提供启动器显示、隐藏和切换控制能力。

## 术语与缩写

- **applet 插件**：dde-shell 框架中的功能部件插件，dde-launchpad 以此形式集成到桌面环境。
- **DBus 属性**：远端接口上的具名值，使用方可读取或监听变化。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以 DBus 接口名为章节，逐一说明各接口的定位、功能能力和使用场景。

## 全局约定

dde-launchpad 不安装公共开发头文件，不导出 C++ 命名空间或 CMake 库目标。使用方通过 DBus 接口控制启动器的显示与隐藏。dde-launchpad 作为 dde-shell 的 applet 插件运行，插件通过 dde-shell 的 `ds_install_package` 机制安装。

## 按功能查阅

- 通过 DBus 控制启动器显示、隐藏或切换：参见 [org.deepin.dde.Launcher1](modules.md#orgdeepinddelauncher1)。
- 将 dde-launchpad 引入 dde-shell 插件工程：参见[集成与构建配置](integration.md)。
