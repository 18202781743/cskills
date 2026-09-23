# DDE 托盘插件开发常见陷阱

## 1. 插件类型

- **Type_Tray 与 Type_Quick 混用**：两者互斥，快捷面板插件必须选择一个 `Quick_Panel_*` 布局标志。
- **基础托盘插件附加无关能力**：不要给 `Type_Tray` 插件加强加 `PluginFlags` 中的快捷面板或拖拽能力。

## 2. PluginProxyInterface

- **释放问题**：`PluginProxyInterface` 由 loader 管理，插件只保存指针，不负责释放。
- **快捷面板宽度**：由布局标志决定，控件只固定框架规定的高度，不要手动设置。

## 3. 消息协议

- **MSG_GET_SUPPORT_FLAG 未处理**：插件必须响应此消息，返回正确的支持标志。
- **MSG_ITEM_ACTIVE_STATE 未发送**：快捷面板子项激活状态变化时需主动发送此消息。

## 4. 图标与资源

- **Attribute_CanSetting 未实现图标接口**：使用此属性时必须实现控制中心图标接口并安装对应资源。
- **亮暗主题图标**：托盘图标须提供亮色和暗色两套，通过 `DciIcon` 或 `DIconTheme` 动态切换。

## 5. 不要做的事

- 不要把 `Type_Tray` 和 `Type_Quick` 同时使用
- 不要给基础托盘插件强加 `Attribute_CanSetting`、拖拽或快捷面板能力
- 不要释放 `PluginProxyInterface` 指针
- 不要使用 `QSystemTrayIcon`（不属于 DDE 托盘插件体系）
- 不要使用 `QSettings` 替代 DConfig（详见 `$dtk-development`）
