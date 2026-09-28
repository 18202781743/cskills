# dde-application-manager 二次开发文档 · 概览

## 项目定位

dde-application-manager 是 DDE 应用管理器，以 DBus 服务方式运行，提供应用生命周期管理、应用实例管理、异步操作跟踪和应用对象管理能力。使用方通过 DBus 接口与之交互，启动、停止、查询应用状态并管理应用对象。

## 术语与缩写

- **Job**：异步操作的跟踪句柄，用于跟踪应用启动这类耗时操作的状态。
- **ObjectManager**：DBus 标准对象管理接口，管理应用对象的创建和删除。
- **App ID**：应用的唯一标识，对应 desktop file 中的应用标识。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以 DBus 接口名为章节，逐一说明各接口的定位、功能能力和使用场景。

## 全局约定

dde-application-manager 不安装公共开发头文件，不导出 C++ 命名空间或库目标。使用方通过 DBus 调用访问其功能。应用以 App ID 标识，应用对象路径为 `/org/desktopspec/ApplicationManager1/{app-id}`。

## 按功能查阅

- 启动、停止、查询应用状态：参见 [org.desktopspec.ApplicationManager1](modules.md#orgdesktopspecapplicationmanager1)。
- 查询单个应用的属性和状态：参见 [org.desktopspec.ApplicationManager1.Application](modules.md#orgdesktopspecapplicationmanager1application)。
- 跟踪异步操作状态：参见 [org.desktopspec.JobManager1.Job](modules.md#orgdesktopspecjobmanager1job)。
- 管理应用对象列表：参见 [org.desktopspec.ObjectManager1](modules.md#orgdesktopspecobjectmanager1)。
