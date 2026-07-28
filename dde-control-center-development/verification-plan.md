# DDE Control Center Skill 验证计划

## 目标

验证 `dde-control-center-development` skill 中每个参考文档声称的 **类名、枚举值、方法签名、QML 类型、CMake 变量、宏参数** 与 `~/dde-control-center` 源码一致。

## 验证方法

- **PASS** — 文档与源码一致
- **FAIL** — 文档与源码不一致（修正文档）
- **NOT FOUND** — 源码中未找到

## 验证范围

5 个参考文档，按功能划分为 6 个验证模块。

---

## 模块 1：架构（architecture.md）

**源码位置：** `~/dde-control-center/`

| # | 验证项 | 对应源码文件 |
|---|--------|-------------|
| 1.1 | DccPluginLoader Status 枚举含 PluginBegin/MetaDataLoad/ModuleLoad/DataBegin/MainObjLoad/PluginEnd | `dccpluginloader.h` |
| 1.2 | DccPluginLoader Type 枚举含 T_V1_0/T_V1_1 | `dccpluginloader.h` |
| 1.3 | DccPluginLoader 方法 loadMetaData/loadModule/loadData/loadMain/addMainObject | `dccpluginloader.h` |
| 1.4 | DccPluginLoader 信号 statusChanged(DccPluginLoader*, StatusFlags) | `dccpluginloader.h` |
| 1.5 | DccPluginManager 方法 loadModules(root, async, dirs, engine) | `pluginmanager.h` |
| 1.6 | DccPluginManager 信号 addObject/loadAllFinished | `pluginmanager.h` |
| 1.7 | v1.0/v1.1 格式区分（metadata.json 检测） | `dccpluginloader.cpp` |
| 1.8 | DCC_PLUGINS_VERSION = "1.1" | 根 `CMakeLists.txt` |
| 1.9 | 安装路径 DDE_CONTROL_CENTER_PLUGIN_INSTALL_DIR = ${DCC_INSTALL_DIR}/plugins_v1.1 | 根 `CMakeLists.txt` |
| 1.10 | DConfig hideModule/disableModule 配置项 | `dccmanager.cpp` |
| 1.11 | DccObject visibleToApp/enabledToApp 含义 | `dccobject.h` |
| 1.12 | DBus 接口 org.deepin.dde.ControlCenter1 | `controlcenterdbusadaptor.h` |
| 1.13 | DBus 方法 Show/Hide/Toggle/ShowPage/ShowHome/GetAllModule/Exit | `controlcenterdbusadaptor.h` |
| 1.14 | Grand Search 子接口 org.deepin.dde.ControlCenter1.GrandSearch | `controlcenterdbusadaptor.h` |
| 1.15 | DccManager 方法 toBack/showHelp/isTreeland/productType/uosEdition | `dccmanager.h` |

---

## 模块 2：插件开发（plugin-development.md）

**源码位置：** `~/dde-control-center/`

| # | 验证项 | 对应源码文件 |
|---|--------|-------------|
| 2.1 | dcc_install_plugin 函数存在，参数 NAME/TARGET | `DdeControlCenterPluginMacros.cmake` |
| 2.2 | dcc_handle_plugin_translation 函数存在 | `DdeControlCenterPluginMacros.cmake` |
| 2.3 | QML 文件名必须首字母大写（正则 ^[A-Z]） | `DdeControlCenterPluginMacros.cmake` |
| 2.4 | main.qml 触发 FATAL_ERROR | `DdeControlCenterPluginMacros.cmake` |
| 2.5 | NAME 只允许字母数字 | `DdeControlCenterPluginMacros.cmake` |
| 2.6 | qt_add_qml_module URI=NAME, VERSION 1.0 | `DdeControlCenterPluginMacros.cmake` |
| 2.7 | AUTOMOC_MACRO_NAMES = DCC_FACTORY_CLASS | `DdeControlCenterPluginMacros.cmake` |
| 2.8 | 翻译支持 20 种 locale | `DdeControlCenterPluginMacros.cmake` |
| 2.9 | DCC_FACTORY_CLASS 宏定义（IID、Q_PLUGIN_METADATA、create()） | `dccfactory.h` |
| 2.10 | DccFactory 虚方法 create()/dccObject() | `dccfactory.h` |
| 2.11 | IID "org.deepin.dde.dcc-factory/v1.0" | `dccfactory.h` |
| 2.12 | Example 插件 CMakeLists 含 find_package(DdeControlCenter) | `examples/plugin-example/CMakeLists.txt` |
| 2.13 | Example 插件 CMakeLists 含 dcc_install_plugin + dcc_handle_plugin_translation | `examples/plugin-example/CMakeLists.txt` |
| 2.14 | pluginexample.cpp 含 DCC_FACTORY_CLASS(PluginExample) + #include "pluginexample.moc" | `pluginexample.cpp` |
| 2.15 | pluginexample.h 含 Q_PROPERTY + Q_INVOKABLE calc(int,int) + Q_SLOTS setCalcType | `pluginexample.h` |
| 2.16 | Example.qml name:"example" + parentName:"root" | `Example.qml` |
| 2.17 | ExampleMain.qml 引用 ExamplePage1/2/3 | `ExampleMain.qml` |
| 2.18 | ExamplePage1.qml 使用 DccGroupView + DccRepeater | `ExamplePage1.qml` |
| 2.19 | 线程安全描述：子对象必须纳入 QObject 树 | — |
| 2.20 | Bluetooth 插件 DCC_FACTORY_CLASS(BluetoothInteraction) | `bluetoothinteraction.cpp` |
| 2.21 | BluetoothInteraction 构造函数创建 Model + Worker | `bluetoothinteraction.cpp` |
| 2.22 | system/device 为 QML-only（CMake 无 add_library） | `plugin-system/CMakeLists.txt` |
| 2.23 | 打包构建依赖 dde-control-center-dev | — |
| 2.24 | 运行时依赖 dde-control-center | — |

---

## 模块 3：C++ API（cpp-api.md）

**源码位置：** `~/dde-control-center/src/dde-control-center/plugin/`

| # | 验证项 | 对应源码文件 |
|---|--------|-------------|
| 3.1 | DccObject QML_ELEMENT | `dccobject.h` |
| 3.2 | name 属性 QString, setName(const QString&) | `dccobject.h` |
| 3.3 | weight 属性 quint32 | `dccobject.h` |
| 3.4 | visibleToApp/enabledToApp 只读 bool | `dccobject.h` |
| 3.5 | canSearch 属性 bool，默认 true | `dccobject.h` |
| 3.6 | pageType 属性 quint8，默认 Menu(0x40) | `dccobject.h` |
| 3.7 | PageType::Menu=0x40, MenuEditor=0x41, Editor=0x21, Item=0x22, UserType=0x80 | `dccobject.h` |
| 3.8 | BackgroundType::AutoBg=0, Normal=0x01, Hover=0x02, Clickable=0x04, Highlight=0x08, Warning=0x10 | `dccobject.h` |
| 3.9 | ClickStyle=Normal|Hover|Clickable | `dccobject.h` |
| 3.10 | 信号 active(const QString&)/deactive() | `dccobject.h` |
| 3.11 | 子对象变化信号 childAdded/childRemoved/childrenChanged | `dccobject.h` |
| 3.12 | 属性变化信号 xxxChanged | `dccobject.h` |
| 3.13 | DccApp QML 注册 qmlRegisterSingletonInstance("org.deepin.dcc", 1, 0, "DccApp", ...) | `dccmanager.cpp` |
| 3.14 | DccApp 属性 root/activeObject/sidebarWidth（默认180） | `dccapp.h` |
| 3.15 | DccApp 方法 showPage/addObject/removeObject/object/navModel/searchModel/mainWindow | `dccapp.h` |
| 3.16 | DccRepeater 属性 model/delegate/count | `dccrepeater.h` |
| 3.17 | DccRepeater 方法 resetModel()/objectAt(int) | `dccrepeater.h` |
| 3.18 | DccRepeater 信号 objAdded/objRemoved | `dccrepeater.h` |
| 3.19 | DccModel QML_ELEMENT，属性 root，方法 setRoot/getObject | `dccmodel.h` |

---

## 模块 4：QML API（qml-api.md）

**源码位置：** `~/dde-control-center/src/dde-control-center/plugin/`

| # | 验证项 | 对应源码文件 |
|---|--------|-------------|
| 4.1 | DccGroupView.qml 存在，属性 isGroup(bool,默认true) | `DccGroupView.qml` |
| 4.2 | DccGroupView.qml 方法 navigateToItem(forward) | `DccGroupView.qml` |
| 4.3 | DccSettingsView.qml 存在，属性 isGroup/scrollBarVisible | `DccSettingsView.qml` |
| 4.4 | DccSettingsObject.qml 存在，属性 bodyUrl/footerUrl（只读string） | `DccSettingsObject.qml` |
| 4.5 | DccRowView.qml 存在，根元素 RowLayout | `DccRowView.qml` |
| 4.6 | DccRightView.qml 存在 | `DccRightView.qml` |
| 4.7 | DccLoader.qml 存在，属性 dccObj/dccObjItem | `DccLoader.qml` |
| 4.8 | DccTitleObject.qml 存在，继承 DccObject | `DccTitleObject.qml` |
| 4.9 | DccLabel.qml 存在，属性 hovered | `DccLabel.qml` |
| 4.10 | DccCheckIcon.qml 存在，属性 size(默认16) | `DccCheckIcon.qml` |
| 4.11 | DccTimeRange.qml 存在，属性 hour/minute/timeString，信号 timeChanged | `DccTimeRange.qml` |
| 4.12 | DccItemBackground.qml 存在 | `DccItemBackground.qml` |
| 4.13 | DccQuickRepeater QML_NAMED_ELEMENT(Repeater) | `dccquickrepeater.h` |
| 4.14 | DccQuickDBusInterface QML_NAMED_ELEMENT(DccDBusInterface) | `dccquickdbusinterface.h` |
| 4.15 | DccDBusInterface 属性 service/path/inter/connection/suffix | `dccquickdbusinterface.h` |
| 4.16 | DccDBusInterface BusType: SessionBus=0/SystemBus=1 | `dccquickdbusinterface.h` |
| 4.17 | DccDBusInterface 方法 callWithCallback | `dccquickdbusinterface.h` |
| 4.18 | Crumb.qml 存在 | `Crumb.qml` |
| 4.19 | SearchBar.qml 存在 | `SearchBar.qml` |
| 4.20 | DccWindow.qml 存在，枚举 PageIndex | `DccWindow.qml` |
| 4.21 | HomePage.qml 存在 | `HomePage.qml` |
| 4.22 | SecondPage.qml 存在 | `SecondPage.qml` |
| 4.23 | DccUtils.js 存在，函数 copyFont/getMargin | `DccUtils.js` |

---

## 模块 5：调试（debugging.md）

| # | 验证项 | 对应源码文件 |
|---|--------|-------------|
| 5.1 | --spec 参数在 main.cpp 中处理 | `main.cpp` |
| 5.2 | 线程安全描述与源码行为一致 | `dccpluginloader.cpp` |
| 5.3 | --spec 路径歧义说明：文档区分了不同工作目录下的路径写法 | `main.cpp` (parser.values(pluginDir)) |
| 5.4 | --spec 只替换插件搜索路径，不影响框架库加载 | `main.cpp` (loadModules vs defaultpath) |
| 5.5 | 修改框架时需设置 LD_LIBRARY_PATH 指向构建目录 lib/ | `CMakeLists.txt` (CMAKE_LIBRARY_OUTPUT_DIRECTORY) |
| 5.6 | 修改框架时需设置 QT_PLUGIN_PATH 和 QML2_IMPORT_PATH | `plugin/CMakeLists.txt` (qt_add_qml_module) |
| 5.7 | killall 先关闭单实例的说明 | `main.cpp` (setSingleInstance) |
| 5.8 | 清除 QML 缓存命令与 refreshQmlCache 行为一致 | `main.cpp` (refreshQmlCache) |
| 5.9 | 验证加载路径的 ldd/proc maps 方法正确 | — |

---

## 模块 6：跨文档一致性

| # | 验证项 |
|---|--------|
| 6.1 | SKILL.md 路由表链接可达 |
| 6.2 | 所有 references/ 文档交叉引用路径正确 |
| 6.3 | 20 种 locale 数量一致 |
| 6.4 | CMake 变量名在 architecture.md 和 plugin-development.md 中一致 |
| 6.5 | DccDBusInterface 属性在 qml-api.md 中与源码一致 |

---

## 执行策略

| 执行组 | 包含模块 | 预估项数 |
|--------|----------|---------|
| Group A | 模块 1（架构） | 15 |
| Group B | 模块 2（插件开发） | 24 |
| Group C | 模块 3（C++ API） | 19 |
| Group D | 模块 4（QML API） | 23 |
| Group E | 模块 5+6（调试+一致性） | 14 |
