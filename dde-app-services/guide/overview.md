# dde-app-services 二次开发文档 · 概览

## 项目定位

dde-app-services 是 DDE 配置中心服务，核心为 DConfig 配置管理系统，提供配置管理守护进程、命令行配置工具和图形配置编辑器。使用方通过 DBus 接口或命令行工具读写配置项，实现应用配置的统一管理。

## 术语与缩写

- **DConfig**：DDE 配置中心，统一的配置读写机制。
- **appid**：配置所属的应用标识，用于定位配置项。
- **配置项**：以键值对形式存储的单个配置条目，具有默认值、数据类型和权限属性。
- **DBus 属性**：远端接口上的具名值，使用方可读取或监听变化。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以 DBus 接口名和命令行工具名为章节，逐一说明各接口的定位、功能能力和使用场景。

## 全局约定

dde-app-services 不安装公共开发头文件，不导出 C++ 命名空间或库目标。使用方通过 DBus 接口或命令行工具 `dde-dconfig` 访问配置管理功能。配置项以 appid 和 key 为参数进行定位。

## 按功能查阅

- 通过 DBus 读取或修改配置项：参见 [org.desktopspec.ConfigManager](modules.md#orgdesktopspecconfigmanager)。
- 通过命令行工具读写配置：参见 [dde-dconfig](modules.md#dde-dconfig)。
- 管理配置资源：参见 [org.desktopspec.ConfigManager.Manager](modules.md#orgdesktopspecconfigmanagermanager)。
