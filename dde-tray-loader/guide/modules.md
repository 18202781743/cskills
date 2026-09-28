# 导出类型介绍

dde-tray-loader 提供 Dock 插件接口体系，包括基础插件接口（V1）、扩展插件接口（V2、V3）、插件代理接口和插件管理器接口，支持插件名称、显示名称、初始化、项部件、项尺寸、项提示部件、项上下文菜单、插件添加与移除通知、窗口自动隐藏请求和插件加载与获取。

## PluginsItemInterface

### 定位

Dock 插件基础接口（V1），所有 Dock 插件必须实现的最小接口集合。位于 `Dock` 命名空间。

### 功能能力总结

提供以下能力：

- 返回插件名称（`pluginName` 方法）
- 返回插件显示名称（`pluginDisplayName` 方法）
- 使用代理对象初始化插件（`init` 方法，参数为 `PluginProxyInterface *proxyInter`）
- 返回指定 itemKey 对应的项部件（`itemWidget` 方法）

### 使用场景

开发 Dock 插件时，作为最小接口集合继承实现。

## PluginsItemInterfaceV2

### 定位

Dock 插件接口 V2，扩展 V1 接口。位于 `Dock` 命名空间。

### 功能能力总结

在 V1 基础上增加以下能力：

- 返回项尺寸（`itemSize` 方法）
- 返回项提示部件（`itemTipsWidget` 方法）

### 使用场景

需要自定义插件项尺寸或提供提示部件时。

## PluginsItemInterfaceV3

### 定位

Dock 插件接口 V3，最新版接口。位于 `Dock` 命名空间。

### 功能能力总结

在 V2 基础上增加更多扩展方法和信号。

### 使用场景

需要使用最新版 Dock 插件接口的全部扩展能力时。

## PluginProxyInterface

### 定位

插件代理接口，插件通过此接口与 Dock 框架通信。位于 `Dock` 命名空间。

### 功能能力总结

提供以下能力：

- 通知框架项已添加（`itemAdded` 方法）
- 通知框架项已移除（`itemRemoved` 方法）
- 请求窗口自动隐藏（`requestWindowAutoHide` 方法）

### 使用场景

插件需要向 Dock 框架通知项变化或请求窗口行为时。

## PluginManagerInterface

### 定位

插件管理器接口，提供插件加载和获取能力。位于 `Dock` 命名空间。

### 功能能力总结

提供以下能力：

- 加载插件（`loadPlugin` 方法）
- 获取已加载的插件（`getPlugin` 方法）

### 使用场景

需要编程方式加载或查询 Dock 插件时。
