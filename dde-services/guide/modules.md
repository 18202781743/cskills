# 导出类型介绍

dde-services 提供壁纸轮播控制能力，以及通过 deepin-service-manager 插件机制开发新服务插件的能力，包括 Qt 插件和 sdbus 插件两种类型。

## org.deepin.dde.WallpaperSlideshow

### 定位

壁纸轮播控制接口，面向需要编程方式控制壁纸轮播行为的调用者。

### 功能能力总结

提供壁纸轮播控制能力。

### 使用场景

需要在程序或脚本中控制壁纸轮播时。

## plugin-qt

### 定位

Qt 服务插件类型，面向需要使用 Qt 框架开发新服务插件的调用者。

### 功能能力总结

- 以 Qt 框架实现服务逻辑
- 安装到 `deepin-service-manager/` 目录
- 通过 JSON 配置文件描述插件元数据，配置文件路径为 `share/deepin-service-manager/system/`

### 使用场景

需要开发基于 Qt 的 DDE 服务插件时。

## plugin-sdbus

### 定位

sdbus 服务插件类型，面向需要使用 sdbus 框架开发新服务插件的调用者。

### 功能能力总结

- 以 sdbus 框架与 DBus 交互
- 安装到 `deepin-service-manager/` 目录
- 通过 JSON 配置文件描述插件元数据，配置文件路径为 `share/deepin-service-manager/user/`（用户级）或 `share/deepin-service-manager/system/`（系统级）

### 使用场景

需要开发基于 sdbus 的 DDE 服务插件时。
