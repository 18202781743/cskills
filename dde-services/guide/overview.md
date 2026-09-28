# dde-services 二次开发文档 · 概览

## 项目定位

dde-services 是 DDE 服务框架，通过 deepin-service-manager 管理的插件式服务，提供主题管理、壁纸缓存、壁纸轮播、X 设置、环境亮度、电源、快捷键和 IP 冲突检测功能。使用方通过 DBus 接口访问各插件服务，或通过 deepin-service-manager 的插件机制开发新服务插件。

## 术语与缩写

- **deepin-service-manager**：DDE 服务管理框架，负责加载和管理 dde-services 中的插件。
- **plugin-qt**：基于 Qt 的服务插件类型，使用 Qt 框架实现服务逻辑。
- **plugin-sdbus**：基于 sdbus 框架的服务插件类型，通过 sdbus 与 DBus 交互。
- **DBus 属性**：远端接口上的具名值，使用方可读取或监听变化。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以 DBus 接口名和插件类型为章节，逐一说明各接口的定位、功能能力和使用场景。

## 全局约定

dde-services 不安装公共开发头文件，不导出 C++ 命名空间或 CMake 库目标。使用方通过 DBus 接口访问各服务插件的功能。新服务插件通过 deepin-service-manager 的 plugin-qt 或 plugin-sdbus 机制开发，安装到 `deepin-service-manager/` 目录。

## 按功能查阅

- 通过 DBus 控制壁纸轮播：参见 [org.deepin.dde.WallpaperSlideshow](modules.md#orgdeepinddewallpaperslideshow)。
- 开发 Qt 服务插件：参见 [plugin-qt](modules.md#plugin-qt)。
- 开发 sdbus 服务插件：参见 [plugin-sdbus](modules.md#plugin-sdbus)。
- 将 dde-services 引入工程：参见[集成与构建配置](integration.md)。
