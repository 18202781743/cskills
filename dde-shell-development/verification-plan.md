# dde-shell-development 验证计划

## 源码映射

| 文档 | 对应源码头文件 |
|------|---------------|
| api/core.md | `frame/applet.h`, `frame/containment.h`, `frame/panel.h`, `frame/appletbridge.h`, `frame/appletproxy.h`, `frame/pluginloader.h`, `frame/pluginmetadata.h`, `frame/appletdata.h`, `frame/pluginfactory.h`, `frame/dsglobal.h` |
| api/qml-api.md | `frame/appletitem.h`, `frame/containmentitem.h`, `frame/panel.h`, `frame/layershell/dlayershellwindow.h`, `frame/qml/*.qml`, `frame/plugin/qmlplugin.cpp` |
| layershell.md | `frame/layershell/dlayershellwindow.h` |
| design.md | `frame/*.h`, `cmake/DDEShellPackageMacros.cmake` |
| plugin-development.md | 示例代码引用上述头文件 |

## 验证项

### api/core.md

| # | 验证项 | 结果 |
|---|--------|------|
| 1 | DApplet 属性列表（id/pluginId/parent/rootObject）与 applet.h 一致 | PASS |
| 2 | DApplet 方法签名（load/init/createProxyMeta 等）与 applet.h 一致 | PASS |
| 3 | DApplet 信号 rootObjectChanged 存在 | PASS |
| 4 | D_APPLET_CLASS 宏描述正确 | PASS |
| 5 | DContainment 属性 appletItems 与 containment.h 一致 | PASS |
| 6 | DContainment 方法（createApplet/removeApplet/applets/applet 等）签名正确 | PASS |
| 7 | DAppletItemModel role 为 Qt::UserRole+1 | PASS |
| 8 | DPanel 属性（popupWindow/toolTipWindow/menuWindow）与 panel.h 一致 | PASS |
| 9 | DPanel 方法（window/popupWindow/toolTipWindow/menuWindow）签名正确 | PASS |
| 10 | DPanel 信号（popupWindowChanged/toolTipWindowChanged/menuWindowChanged）存在 | PASS |
| 11 | DPanel QML_DECLARE_TYPEINFO 声明存在 | PASS |
| 12 | DAppletBridge 构造函数和方法（isValid/pluginId/applets/applet）签名正确 | PASS |
| 13 | DAppletProxy 类存在 | PASS |
| 14 | DPluginLoader 方法（instance/plugins/rootPlugins/childrenPlugin 等）签名正确 | PASS |
| 15 | DPluginMetaData 方法（pluginId/pluginDir/url/value/fromJsonFile 等）签名正确 | PASS |
| 16 | DAppletData 方法（id/setId/pluginId/groupList/setGroupList/value 等）签名正确 | PASS |
| 17 | DAppletFactory 方法（registerInstance/registerApplet/create）签名正确 | PASS |

### api/qml-api.md

| # | 验证项 | 结果 |
|---|--------|------|
| 18 | AppletItem 类存在，QML 类型名正确 | PASS |
| 19 | Applet 附加属性（id/pluginId/rootObject/parent）正确 | PASS |
| 20 | ContainmentItem 类存在 | PASS |
| 21 | Containment 附加属性（appletItems）正确 | PASS |
| 22 | Panel 附加属性存在 | PASS |
| 23 | DS 单例对象注册正确 | PASS |
| 24 | DLayerShellWindow QML 类型注册正确 | PASS |
| 25 | DQuickDrag QML 类型注册正确 | PASS |
| 26 | DListToTableProxyModel QML 类型注册正确 | PASS |
| 27 | PopupWindow QML 类型注册正确 | PASS |
| 28 | PanelPopup/PanelToolTip/PanelMenu QML 文件存在 | PASS |
| 29 | PanelPopupWindow/PanelToolTipWindow/PanelMenuWindow QML 文件存在 | PASS |
| 30 | QuickDragWindow QML 文件存在 | PASS |
| 31 | PanelPopupWindow 属性（xOffset/yOffset/margins/currentItem 等）与源码一致 | PASS |
| 32 | PanelToolTipWindow 继承 PanelPopupWindow | PASS |
| 33 | PanelMenuWindow 继承 PanelPopupWindow，有 mainMenuWindow 属性 | PASS |

### layershell.md

| # | 验证项 | 结果 |
|---|--------|------|
| 34 | DLayerShellWindow 属性（anchors/layer/margins/exclusionZone 等）与 dlayershellwindow.h 一致 | PASS |
| 35 | Anchor 枚举值（None=0, Top=1, Bottom=2, Left=4, Right=8）正确 | PASS |
| 36 | Layer 枚举值（Background=0, Buttom=1, Top=2, Overlay=3）正确 | PASS |
| 37 | KeyboardInteractivity 枚举值（None=0, Exclusive=1, OnDemand=2）正确 | PASS |
| 38 | screenConfiguration/preferredWidth/preferredHeight/inputRegion/scope/closeOnDismissed 属性存在 | PASS |

### design.md

| # | 验证项 | 结果 |
|---|--------|------|
| 39 | 类层次结构（QObject→DApplet→DContainment→DPanel）正确 | PASS |
| 40 | DPluginLoader 扫描路径描述正确 | PASS |
| 41 | 生命周期描述（构造→load→init→rootObjectChanged）正确 | PASS |
| 42 | DConfig 集成方式正确 | PASS |
| 43 | 安装路径正确 | PASS |
| 44 | D_APPLET_CLASS 展开描述正确 | PASS |

### plugin-development.md

| # | 验证项 | 结果 |
|---|--------|------|
| 45 | 插件类型表正确 | PASS |
| 46 | 纯 QML Applet 的 metadata.json 格式正确 | PASS |
| 47 | C++ Applet 示例代码符合头文件 API | PASS |
| 48 | Containment 示例代码符合 API | PASS |
| 49 | Panel 示例代码符合 API | PASS |
| 50 | CMake ds_install_package/ds_handle_package_translation 宏参数正确 | PASS |
| 51 | Debian 依赖项正确 | PASS |
| 52 | 翻译配置描述正确 | PASS |
| 53 | metadata.json 字段表正确 | PASS |
| 54 | 跨插件通信示例正确 | PASS |

### SKILL.md

| # | 验证项 | 结果 |
|---|--------|------|
| 55 | 所有路由链接指向的文件存在 | PASS |
| 56 | 描述中的触发场景覆盖主要用例 | PASS |
