# 导出类型介绍

dde-shell 提供 Dock 面板插件接口与 Dock 项信息结构体。

## DAppletDock

### 定位

Dock 面板插件接口类型，提供 Dock 面板的可见性控制、支持状态查询和 Dock 项信息获取能力。

### 功能能力总结

- 返回 Dock 是否可见
- 设置 Dock 可见性
- 返回 Dock 是否被支持
- 设置支持状态
- 返回 Dock 项信息
- 可见性变化通知
- 支持状态变化通知

### 使用场景

开发需要访问 Dock 面板可见性状态或 Dock 项信息的插件时。

## DockItemInfo

### 定位

Dock 项信息结构体，描述 Dock 区域插件项的名称、显示名称、标识键、设置键、图标和可见性。已注册为 Qt 元类型和 DBus 可序列化类型。

### 功能能力总结

- `name`（QString）— 插件名称
- `displayName`（QString）— 显示名称
- `itemKey`（QString）— 插件唯一标识键
- `settingKey`（QString）— 设置键
- `dccIcon`（QString）— 控制中心图标
- `visible`（bool）— 是否可见

支持 DBus 序列化和反序列化。

### 使用场景

需要在 DBus 通信中传输 Dock 项信息，或读取 Dock 插件项的显示信息时。

