# dde-appearance 二次开发文档 · 概览

## 项目定位

dde-appearance 是 DDE 外观管理服务，以 DBus 服务方式运行，负责主题、图标、光标、字体、字号、壁纸、缩放比例的外观设置管理。使用方通过 DBus 接口与之交互，读取和修改外观配置。

## 术语与缩写

- **外观项**：可设置的外观属性类型，包括 theme（主题）、icon（图标主题）、cursor（光标主题）、font（字体）、fontSize（字号）、wallpaper（壁纸）。
- **DBus 属性**：远端接口上的具名值，使用方可读取或监听变化。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以 DBus 接口名为章节，逐一说明各接口的定位、功能能力和使用场景。

## 全局约定

dde-appearance 不安装公共开发头文件，不导出 C++ 命名空间或库目标。使用方通过 DBus 调用访问其功能。外观项以类型字符串标识（theme、icon、cursor、font、fontSize、wallpaper），设置和获取操作均以类型字符串为参数。

## 按功能查阅

- 通过 DBus 设置或获取外观项：参见 [org.deepin.dde.Appearance1](modules.md#orgdeepinddeappearance1)。
- 管理壁纸轮播和缩放比例：参见 [org.deepin.dde.Appearance1](modules.md#orgdeepinddeappearance1)。
- 通过窗口管理器代理获取外观相关属性：参见 [com.deepin.wm](modules.md#comdeepinwm)。
