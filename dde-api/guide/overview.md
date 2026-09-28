# dde-api 二次开发文档 · 概览

## 项目定位

dde-api 是 DDE 的 API 库，提供 header-only C++ 接口和一组 Go 工具程序。C++ 部分提供事件日志记录能力；Go 工具部分提供图片模糊处理、显示器配置（RandR）、输入设备配置、声音主题播放、光标设置、窗口管理器兼容性检查、Status Notifier Item 代理、区域设置辅助、主题设置、音效设置和 X 事件监视能力。

## 术语与缩写

- **header-only**：仅含头文件、无需链接的 C++ 接口形式。
- **RandR**：X Window 系统的显示器配置扩展协议。
- **SNI**：Status Notifier Item，状态通知项协议。
- **Go 工具**：以独立可执行程序形式发布的 Go 程序，通过命令行调用或 DBus 交互。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。C++ 部分以命名空间为章节逐一说明 header-only 接口的定位、功能能力和使用场景；Go 工具部分以工具名为章节说明各工具的定位、功能能力和使用场景。

## 全局约定

C++ header-only 头文件安装在 `dde-api/` 目录下，主要符号位于 `DDE_EventLogger` 命名空间。Go 工具的包路径为 `github.com/linuxdeepin/dde-api/<tool>`，各工具独立编译为可执行程序。

## 按功能查阅

- 将 dde-api 引入 CMake 或 pkg-config 工程：参见[集成与构建配置](integration.md)。
- 记录事件日志：参见 [DDE_EventLogger](modules.md#dde_eventlogger)。
- 进行图片模糊、显示器配置、输入设备配置或声音主题播放：参见 [blurimage](modules.md#blurimage)、[drandr](modules.md#drandr)、[dxinput](modules.md#dxinput) 和 [sound-theme-player](modules.md#sound-theme-player)。
- 设置光标、检查窗口管理器兼容性或代理 Status Notifier Item：参见 [cursor](modules.md#cursor)、[wmcompatible](modules.md#wmcompatible) 和 [sni_stub](modules.md#sni_stub)。
- 辅助区域设置、设置主题或音效、监视 X 事件：参见 [localehelper](modules.md#localehelper)、[theme](modules.md#theme)、[soundeffect](modules.md#soundeffect) 和 [xevent_monitor](modules.md#xevent_monitor)。
