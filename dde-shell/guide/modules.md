# 导出类型介绍

dde-shell 提供三层插件模型（Applet、Containment、Panel）、插件元数据与实例数据、插件发现与加载、跨插件通信桥接、子插件项模型暴露、Dock 面板插件接口与 Dock 项信息结构体，以及 QML 模块 `org.deepin.ds` 提供 Applet 根元素、Containment 根元素、Layer Shell 窗口属性和全局 DS 对象。

## DApplet

### 定位

基础功能部件插件类型，所有 Applet 插件的基类。定义插件的生命周期阶段和基本属性。

### 功能能力总结

- 加载阶段从 DConfig 或 appletData 读取配置
- 初始化阶段设置信号连接和创建 UI
- 返回插件 ID
- 返回插件实例数据
- 设置插件实例数据
- 返回 QML 根对象（加载后可用）
- 返回所属 Panel

生命周期顺序为：构造 → 加载 → 初始化 → 就绪。

### 使用场景

开发基础功能部件插件时，作为插件基类继承。

## DContainment

### 定位

容器插件类型，管理子 Applet，提供子插件数据列表和添加子 Applet 的能力。

### 功能能力总结

- 返回子插件数据列表
- 添加子 Applet

### 使用场景

开发需要包含子插件的容器插件时。

## DPanel

### 定位

顶级面板插件类型，管理窗口，提供主窗口和弹出窗口的访问能力。

### 功能能力总结

- 返回主窗口
- 返回弹出窗口
- 返回提示窗口
- 返回菜单窗口

### 使用场景

开发 Dock、顶栏这类顶级面板插件时。

## DPluginLoader

### 定位

插件发现与加载单例，负责从安装目录发现和加载插件。

### 功能能力总结

- 获取单例实例
- 获取指定父插件的子插件元数据列表（参数为父插件 ID）

### 使用场景

需要查询已安装插件的元数据信息时。

## DAppletBridge

### 定位

跨插件通信桥接类型，用于查找并访问其他插件实例。

### 功能能力总结

- 按插件 ID 构造桥接对象并查找目标插件
- 判断目标插件是否存在且已加载
- 返回目标插件实例
- 返回代理对象用于属性读写和方法调用

### 使用场景

需要在插件之间通信、读取其他插件属性或调用其他插件方法时。

## DPluginMetaData

### 定位

插件元数据类型，来自 `metadata.json` 文件，描述插件的 ID、版本、入口和父子关系。

### 功能能力总结

保存插件元数据信息，包括插件 ID、版本、QML 入口文件路径和父插件 ID。

### 使用场景

需要读取插件元数据信息时。

## DAppletData

### 定位

插件实例运行时数据类型，保存插件实例在运行时的数据。

### 功能能力总结

- 从插件元数据构造实例数据
- 设置子插件列表

### 使用场景

需要构造或修改插件实例数据时。

## DAppletItemModel

### 定位

子 Applet 项模型类型，将子 Applet 的 QML item 暴露给 QML 视图。

### 功能能力总结

- 以接口方式暴露子 Applet 的 QML item

### 使用场景

需要在 QML 中使用 Repeater 渲染子 Applet item 时。

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

## org.deepin.ds

### 定位

dde-shell 的 QML 模块，URI 为 `org.deepin.ds`，导入版本 1.0。提供 Applet 插件的 QML 根元素、Containment 插件的 QML 根元素、Layer Shell 窗口属性控制和全局 DS 对象。

### AppletItem

#### 定位

Applet 插件的 QML 根元素，提供 `Applet` 附加属性（包括 `pluginId`）。

#### 功能能力总结

- 作为 Applet 插件 QML 入口的根元素
- 通过附加属性获取插件 ID

#### 使用场景

开发 Applet 插件的 QML 界面时，作为根元素使用。

### ContainmentItem

#### 定位

Containment 插件的 QML 根元素，提供 `Containment.appletItems` 模型供 Repeater 渲染子 item。

#### 功能能力总结

- 作为 Containment 插件 QML 入口的根元素
- 通过 `Containment.appletItems` 模型访问子 Applet item

#### 使用场景

开发 Containment 插件的 QML 界面并需要渲染子 Applet 时。

### DLayerShellWindow

#### 定位

Layer Shell 附加属性类型，控制 Wayland 窗口的锚定方向、层级和边距。

#### 功能能力总结

- 设置窗口锚定方向（包括顶部、底部、左侧、右侧）
- 设置窗口层级
- 设置窗口边距

#### 使用场景

需要控制插件窗口在 Wayland Layer Shell 中的位置和层级时。

### DS

#### 定位

QML 全局对象，提供跨插件访问能力。

#### 功能能力总结

- 按插件 ID 获取其他插件的代理对象

#### 使用场景

需要在 QML 中访问其他插件实例的属性或方法时。
