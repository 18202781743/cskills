# dtkgui 二次开发文档 · 概览

## 项目定位

dtkgui 是基于 Qt GUI 模块的 C++ 库，提供 DTK 图形界面层面的能力，包括 DCI 图标渲染与播放、调色板管理、窗口装饰与平台主题、文件拖拽、字体管理、缩略图生成、SVG 渲染、区域监视和任务栏控制。控件级别的功能由上层 dtkwidget 提供。

## 术语与缩写

- **DTK**：Deepin Tool Kit。
- **DTK5 / DTK6**：分别与 Qt5 / Qt6 配套的主版本。
- **DGui**：公开头文件安装目录名，也是主要 C++ 命名空间的一部分。
- **DCI**：将多份图标数据组织在单个文件中的格式，支持多主题、多分辨率、多状态。
- **转发头**：以公开类型名命名的无后缀头文件，转而引入实际声明所在的头文件。
- **平台主题**：窗口装饰、圆角、模糊效果这些平台级视觉属性的集合。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。它以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 全局约定

公开头文件安装在按主版本区分的 DGui 目录。主要公开符号位于 `Dtk::Gui` 命名空间，可使用 `DGUI_USE_NAMESPACE` 引入。版本判断和跨主版本构建方式见[集成与构建配置](integration.md)。

公开类型多以 `D` 开头。DCI 相关类型以 `DDci` 为前缀。枚举项通常用英文描述状态或属性。具体名称以公开声明为准。

## 按功能查阅

- 将 dtkgui 引入 CMake、pkg-config 或 qmake 工程：参见[集成与构建配置](integration.md)。
- 使用 DCI 图标：参见 [DDciIcon](modules.md#ddciicon)、[DDciIconImage](modules.md#ddciiconimage)、[DDciIconPalette](modules.md#ddciiconpalette)、[DDciIconPlayer](modules.md#ddciiconplayer) 与 [DDciIconImagePlayer](modules.md#ddciiconimageplayer)。
- 管理调色板与主题：参见 [DPalette](modules.md#dpalette) 与 [DGuiApplicationHelper](modules.md#dguiapplicationhelper)。
- 控制窗口装饰与平台属性：参见 [DPlatformHandle](modules.md#dplatformhandle)、[DPlatformTheme](modules.md#dplatformtheme) 与 [DWindowManagerHelper](modules.md#dwindowmanagerhelper)。
- 图标与 SVG 渲染：参见 [DIcon](modules.md#dicon)、[DIconTheme](modules.md#diconthemecached) 与 [DSvgRenderer](modules.md#dsvgrenderer)。
- 文件拖拽、字体管理与缩略图：参见 [DFileDrag](modules.md#dfiledrag)、[DFileDragClient](modules.md#dfiledragclient)、[DFileDragServer](modules.md#dfiledragserver)、[DFontManager](modules.md#dfontmanager) 与 [DThumbnailProvider](modules.md#dthumbnailprovider)。
- 系统服务、区域监视与任务栏控制：参见 [DDesktopServices](modules.md#ddesktopservices)、[DRegionMonitor](modules.md#dregionmonitor) 与 [DTaskbarControl](modules.md#dtaskbarcontrol)。
- 在 DTK5 与 DTK6 之间迁移构建配置：参见[集成与构建配置](integration.md)；迁移公开类型：参见对应的[导出类型介绍](modules.md)。
