# 导出类型介绍

dde-shell 的 QML 模块 `org.deepin.ds` 提供 Applet 根元素、Containment 根元素、Panel 附加属性、Layer Shell 窗口属性、全局 DS 对象、拖拽属性、弹出窗口和列表转表格代理模型。

## org.deepin.ds

### 定位

dde-shell 的 QML 模块，URI 为 `org.deepin.ds`，导入版本 1.0。提供 Applet 插件的 QML 根元素、Containment 插件的 QML 根元素、Panel 附加属性、Layer Shell 窗口属性控制和全局 DS 对象，以及拖拽、弹出窗口和代理模型等辅助类型。

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

### Panel

#### 定位

Panel 附加属性类型，不可实例化，通过附加属性使用。提供 Panel 面板的弹出窗口、提示窗口和菜单窗口访问能力，继承 Containment 的子 Applet 项模型和 Applet 的插件 ID、根对象等属性。

#### 功能能力总结

- 获取面板的弹出窗口（popupWindow）
- 获取面板的提示窗口（toolTipWindow）
- 获取面板的菜单窗口（menuWindow）
- 继承 Containment 的 `appletItems` 子 Applet 项模型
- 继承 Applet 的插件 ID（pluginId）、实例 ID（id）和根对象（rootObject）

#### 使用场景

开发 Dock、顶栏这类 Panel 面板插件的子插件时，通过附加属性访问所属 Panel 的窗口和属性。

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

QML 全局单例对象，提供跨插件访问和窗口管理能力。

#### 功能能力总结

- 按插件 ID 获取其他插件的代理对象
- 按插件 ID 获取其他插件的代理对象列表
- 获取根 Applet 对象
- 关闭指定窗口的子窗口
- 抓取和释放键盘或鼠标
- 执行延时回调

#### 使用场景

需要在 QML 中访问其他插件实例的属性或方法，或需要管理窗口焦点和子窗口时。

### DQuickDrag

#### 定位

拖拽附加属性类型，不可实例化，通过附加属性使用。提供拖拽操作的覆盖窗口、拖拽起点和当前点追踪能力。

#### 功能能力总结

- 设置拖拽是否激活
- 设置拖拽覆盖组件
- 设置热点缩放比例
- 获取拖拽起点坐标和当前拖拽坐标
- 获取覆盖窗口
- 获取是否正在拖拽

#### 使用场景

需要在 QML 中实现自定义拖拽交互并显示拖拽覆盖层时使用。

### PopupWindow

#### 定位

弹出窗口类型，继承自 QQuickApplicationWindow，可实例化。提供设置窗口几何位置和 X11 平台下的焦点抓取转换能力。

#### 功能能力总结

- 设置瞬态父窗口
- 设置窗口几何位置
- X11 平台下焦点抓取转换状态通知
- X11 平台下焦点失去和获取通知

#### 使用场景

需要创建自定义弹出窗口并控制其几何位置和焦点行为时使用。

### DListToTableProxyModel

#### 定位

列表转表格代理模型，可实例化，继承自 KExtraColumnsProxyModel。将单列列表模型扩展为多列表格模型，按指定角色添加额外列。

#### 功能能力总结

- 设置需要添加的角色列表
- 设置源模型列

#### 使用场景

需要将单列列表模型转换为多列表格模型供表格视图使用时。
