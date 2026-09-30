# dtkgui 二次开发文档 · 概览

## 项目定位

dtkgui 是基于 Qt GUI 模块的 C++ 库，提供 DTK 图形界面层面的能力，包括 DCI 图标渲染与播放、调色板管理、窗口装饰与平台主题、文件拖拽、字体管理、缩略图生成、SVG 渲染、区域监视和任务栏控制。控件级别的功能由上层 dtkwidget 提供。

## 导出类型

- [DCI 图标接口](modules.md)：DCI 图标资源容器、单帧图像访问、图像序列播放、内嵌调色板与整体动画播放
- [调色板与主题接口](modules.md)：DTK 扩展调色板、应用级主题管理、原生设置读写与平台主题属性
- [窗口与平台接口](modules.md)：窗口平台属性控制、窗口管理器功能查询、跨进程窗口分组与外部窗口引用
- [图标与 SVG 渲染接口](modules.md)：DTK 图标加载、图标主题缓存管理、SVG 渲染与图像格式处理
- [文件拖拽、字体与缩略图接口](modules.md)：跨进程文件拖拽、字体安装与管理与文件缩略图异步生成
- [系统服务接口](modules.md)：系统服务调用、屏幕区域监视与任务栏进度计数控制

## 按功能查阅

- 加载和渲染 DCI 图标：参见 [DDciIcon](modules.md#ddciicon) 与 [DDciIconPlayer](modules.md#ddciiconplayer)
- 管理调色板与应用主题：参见 [DPalette](modules.md#dpalette) 与 [DGuiApplicationHelper](modules.md#dguiapplicationhelper)
- 控制窗口装饰与平台属性：参见 [DPlatformHandle](modules.md#dplatformhandle) 与 [DWindowManagerHelper](modules.md#dwindowmanagerhelper)
- 加载图标与渲染 SVG：参见 [DIcon](modules.md#dicon) 与 [DSvgRenderer](modules.md#dsvgrenderer)
- 跨进程文件拖拽与字体管理：参见 [DFileDragClient](modules.md#dfiledragclient) 与 [DFontManager](modules.md#dfontmanager)
- 调用系统服务与监视屏幕区域：参见 [DDesktopServices](modules.md#ddesktopservices) 与 [DRegionMonitor](modules.md#dregionmonitor)
- 将 dtkgui 引入 CMake 工程：参见 [modules.md](modules.md) 中的 `## 开发包` 与 `## 集成` 章节
