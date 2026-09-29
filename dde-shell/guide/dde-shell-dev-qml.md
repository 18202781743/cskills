# 导出类型介绍

dde-shell 的 QML 模块 `org.deepin.ds` 提供 Applet 根元素、Containment 根元素、Layer Shell 窗口属性和全局 DS 对象。

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
