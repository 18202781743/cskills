# 插件项接口

dde-tray-loader 提供 Dock 插件项接口体系，包括基础插件接口（V1）、V2 扩展插件接口和 V3 卡片 surface 扩展插件接口。插件开发者通过继承这些接口类并实现虚函数，提供任务栏项的 UI 部件、用户交互、排序与容器管理、显示模式与位置变化响应、插件标志位声明、图标获取、消息通信以及卡片 surface 能力。接口以 header-only 形式发布，使用方包含头文件即可使用，无需链接额外的共享库。

## 开发包

使用 dde-tray-loader 公开接口前，需要安装开发包 `dde-tray-loader-dev`。该开发包以 header-only 形式提供公开头文件和构建配置信息，不提供编译库文件。

## 集成

### CMake 配置

CMake 是推荐的集成方式。查找 `DdeTrayLoader` 包后，配置脚本会自动将 `dde-dock/` 头文件目录添加到全局包含路径，无需手动设置 `include_directories()` 或 `target_link_libraries()`：

```cmake
find_package(DdeTrayLoader REQUIRED)
```

由于开发包为 header-only 形式，不提供编译库文件，也不创建任何 IMPORTED 目标，因此不需要链接步骤。`find_package` 执行后即可直接包含公开头文件。

仍受支持的旧写法查找 `DdeDock` 包，同样会自动添加头文件包含路径：

```cmake
find_package(DdeDock REQUIRED)
```

此写法为兼容方式，新工程应使用 `DdeTrayLoader` 包。

开发包同时提供 pkg-config 模块。`dde-dock` 模块的 Cflags 指向 `dde-dock/` 头文件目录，提供所有公开接口头文件的搜索路径，无链接库（Libs）。`dde-tray-loader` 模块提供 Wayland 协议描述文件的搜索路径，其 Cflags 指向 `dde-tray-loader/` 目录。如需同时引用 API 头文件和协议文件，可组合使用两个模块：

```sh
pkg-config --cflags dde-dock dde-tray-loader
```

### 构建与安装插件

dde-tray-loader 开发包不提供专用的 CMake 宏或函数用于构建插件。插件作为普通的 Qt 共享库进行构建，需在 CMake 中声明 `QT_PLUGIN` 宏，将接口头文件目录加入包含路径，并将编译产物安装到 Dock 插件目录。

插件安装路径为 `lib/dde-dock/plugins/`。

### 插件注册

插件通过 Qt Plugin 机制注册到 Dock 框架。插件类需使用 `Q_PLUGIN_METADATA` 声明插件元数据，使用 `Q_INTERFACES` 声明所实现的接口。Dock 框架通过 IID 区分不同版本的插件接口：

- V1 接口 IID 为 `com.deepin.dock.PluginsItemInterface`
- V2 接口 IID 为 `com.deepin.dock.PluginsItemInterface_V2`
- V3 接口 IID 为 `com.deepin.dock.PluginsItemInterface_V3`

插件根据所实现的最高版本接口，使用对应的 IID 进行注册。Dock 框架在启动时扫描插件目录，加载符合接口版本的插件。

API 版本号为 2.0.0，V2 接口方法标注 `@since 2.0.0`。插件可在编译期通过 `DOCK_API_VERSION` 宏和 `DOCK_API_VERSION_CHECK` 宏比对版本号，判断接口兼容性。

### 使用方式

在 C++ 源文件中通过以下方式引入公开头文件：

```cpp
#include <pluginsiteminterface.h>
#include <pluginsiteminterface_v2.h>
#include <pluginsiteminterface_v3.h>
```

常量位于 `Dock` 命名空间，枚举（`DockPart`）和接口类位于全局命名空间。`DockPart` 枚举定义在 `common.h` 中。

## 模块API介绍

### PluginsItemInterface

#### 定位

Dock 插件基础接口，所有 Dock 插件必须实现的最小接口集合。位于全局命名空间，声明 IID `com.deepin.dock.PluginsItemInterface`。插件通过继承此类并实现纯虚函数提供 Dock 项的基本能力。

#### 功能能力总结

- 提供插件身份标识，包括用于框架内部区分的唯一名称和面向用户展示的显示名称
- 在插件加载阶段接收框架传递的代理对象指针并保存，建立插件与 Dock 框架之间的双向通信通道
- 为每个项标识提供主界面部件，插件通过不同的项标识可在任务栏上呈现多个独立交互入口
- 为项提供鼠标悬停时显示的提示气泡部件，支持自定义提示内容
- 为项提供点击时弹出的面板部件，支持丰富的展开式交互；框架通过拦截鼠标按下与释放事件判断用户操作意图，若插件自行过滤鼠标事件则弹出面板不会被触发
- 为项提供点击时执行的 shell 命令，适用于快捷启动外部程序场景
- 为项提供 JSON 格式的右键上下文菜单定义，并响应菜单项被点击事件，支持勾选态回调
- 支持项的排序位置管理：通过排序键指定项在任务栏左侧（正值）或右侧（-1）的显示位置，并在用户拖拽改变顺序时接收并持久化新位置
- 支持项的容器区域管理：声明项是否允许移入容器、查询项当前是否在容器内、在用户拖入或拖出容器时接收状态变更通知；项移入容器后提示和弹出面板功能将被禁用
- 支持插件的启用与禁用控制：声明插件是否允许被禁用、查询当前禁用状态、响应启用/禁用切换操作
- 感知任务栏运行环境变化：接收任务栏显示模式（时尚/高效）切换通知、任务栏位置（上/右/下/左）变化通知，并在系统图标主题变更时刷新项图标
- 接收插件设置变更通知，用于响应云端同步配置更新
- 提供运行时查询当前任务栏显示模式和位置的便捷方法，通过读取全局应用属性实现
- 支持插件尺寸策略声明，可选择跟随系统或自定义尺寸
- 提供已废弃的插件类型分类方法（Normal/Fixed），已由 V2 接口的标志位机制替代

#### 使用场景

开发 Dock 插件时，作为最小接口集合继承实现，提供插件名称、显示名称、初始化、项部件、提示部件、弹出面板、点击命令、上下文菜单、排序与容器管理、禁用控制、显示模式与位置变化响应、图标刷新和设置变化通知能力。

### PluginsItemInterfaceV2

#### 定位

Dock 插件接口 V2，继承自 PluginsItemInterface，扩展插件标志位、图标获取、子插件传递和消息通信能力。位于全局命名空间，声明 IID `com.deepin.dock.PluginsItemInterface_V2`。V2 接口方法标注 `@since 2.0.0`。

#### 功能能力总结

在 V1 基础上增加以下能力（`@since 2.0.0`）：

- 通过标志位系统声明插件的类型归属和行为属性：插件类型标志指定插件在任务栏中的显示区域（快捷插件区、工具区、系统区、托盘区、固定区）；快捷面板列数标志控制插件在快捷面板中占据的列数（单列、双列、整行）；插件属性标志描述交互行为（支持拖拽、支持前方插入其他插件、可在控制中心设置显示隐藏、强制显示在任务栏、提供卡片 surface）。默认标志组合为系统区类型加普通插件属性（可拖拽、可插入、可设置）
- 为在控制中心个性化设置中显示的插件提供图标，支持按图标类型和主题类型（亮色/暗色）返回对应图标对象，使插件图标能随系统主题切换自动适配
- 接收框架传递的子插件指针，主要用于托盘插件和快捷面板插件承载其他插件模块，普通插件无需关注
- 提供基于 JSON 消息的双向通信机制：插件可注册消息回调函数向框架发送 JSON 格式请求，框架也可向插件发送 JSON 请求获取数据或执行指令并接收 JSON 响应；此机制在不添加新虚函数、不破坏二进制兼容性的前提下扩展插件与框架之间的交互能力

#### 使用场景

需要声明插件标志位、在控制中心显示插件图标、接收子插件指针或与 Dock 框架进行 JSON 消息通信时，使用 V2 接口对应方法。

### PluginsItemInterfaceV3

#### 定位

Dock 插件接口 V3，继承自 PluginsItemInterfaceV2，扩展卡片 surface 能力。位于全局命名空间，声明 IID `com.deepin.dock.PluginsItemInterface_V3`。插件通过卡片 surface 将原生窗口导出为 Wayland surface，在 Dock 卡片区展示。

#### 功能能力总结

在 V2 基础上增加以下能力：

- 声明需要导出为卡片 surface 的项标识，框架以插件名称与项标识组合作为稳定的 surface 标识，使每个卡片在合成器层面可独立寻址
- 提供卡片项的原生窗口，框架将此窗口导出为 Wayland surface 在卡片区展示；窗口所有权归插件，QML 或 QWidget 界面的创建与渲染由插件自行处理
- 控制卡片在卡片区中的排列顺序，框架按排序值升序排列，值最小的卡片显示在最前，值相同的卡片按 surface 创建顺序排列；默认排序值将卡片排在所有指定了排序值的卡片之后；框架不解释具体数值含义也不感知插件标识，因此独立发布的插件也能参与统一排序
- 为卡片 surface 提供独立的右键上下文菜单，采用与项上下文菜单相同的 JSON 格式，默认复用项的上下文菜单实现以保持向后兼容
- 为卡片 surface 提供独立的鼠标悬停提示部件，默认复用项的提示部件，两者均未提供时框架回退到插件显示名称
- 响应卡片 surface 上下文菜单项的点击事件，默认转发到项的菜单项点击处理以保持向后兼容

#### 使用场景

需要将插件原生窗口作为卡片在 Dock 卡片区展示并控制卡片排列顺序、独立上下文菜单和提示部件时，使用 V3 接口。

### Common

#### 定位

定义任务栏部件位置枚举 `DockPart`，用于标识插件项在任务栏不同区域和控制中心中的归属位置。位于全局命名空间，声明在 `common.h` 中。

#### 功能能力总结

- 定义快捷插件显示区域 `QuickShow`（值为 0），标识插件在任务栏快捷插件区显示
- 定义快捷面板区域 `QuickPanel`，标识插件在快捷面板区域显示
- 定义系统插件显示区域 `SystemPanel`，标识插件在系统插件区显示
- 定义控制中心设置位置 `DCCSetting`，标识插件在控制中心个性化设置中显示图标

#### 使用场景

插件根据 `DockPart` 枚举值判断自身所处的任务栏部件位置，据此调整布局和交互行为。

### Constants

#### 定位

`Dock` 命名空间下的公开常量集合，定义任务栏显示模式、隐藏模式、位置、隐藏状态、插件标志位、图标类型、主题类型枚举，API 版本宏，消息通信常量和尺寸常量。位于 `Dock` 命名空间，声明在 `constants.h` 中。

#### 功能能力总结

- 定义任务栏显示模式 `DisplayMode`：时尚模式 `Fashion`（值为 0）和高效模式 `Efficient`（值为 1），通过全局属性 `PROP_DISPLAY_MODE` 读取当前模式
- 定义任务栏隐藏模式 `HideMode`：一直显示 `KeepShowing`（值为 0）、一直隐藏 `KeepHidden`（值为 1）、智能隐藏 `SmartHide`（值为 3），通过全局属性 `PROP_HIDE_MODE` 读取
- 定义任务栏位置 `Position`：顶部 `Top`（值为 0）、右侧 `Right`（值为 1）、底部 `Bottom`（值为 2）、左侧 `Left`（值为 3），任务栏始终位于主屏幕边缘，通过全局属性 `PROP_POSITION` 读取
- 定义任务栏隐藏状态 `HideState`：未知 `Unknown`（值为 0）、显示 `Show`（值为 1）、隐藏 `Hide`（值为 2），仅在隐藏模式为智能隐藏时生效，通过全局属性 `PROP_HIDE_STATE` 读取
- 定义插件标志位枚举 `PluginFlag` 及对应的 `QFlags` 类型 `PluginFlags`，支持位运算组合：插件类型标志（`Type_Quick` 快捷插件区、`Type_Tool` 工具插件、`Type_System` 系统插件、`Type_Tray` 托盘区、`Type_Fixed` 固定区域）指定插件显示区域，快捷面板列数标志（`Quick_Panel_Single` 单列、`Quick_Panel_Multi` 双列、`Quick_Panel_Full` 整行）控制插件在快捷面板中占据的列数，插件属性标志（`Attribute_CanDrag` 支持拖拽、`Attribute_CanInsert` 支持前方插入、`Attribute_CanSetting` 可在控制中心设置、`Attribute_ForceDock` 强制显示、`Attribute_HasCard` 提供卡片 surface）描述交互行为，`Attribute_Normal` 为可拖拽、可插入、可设置的默认组合
- 定义图标类型 `IconType`：`IconType_None`（值为 0），当前为默认值无实际意义
- 定义主题类型 `ThemeType`：`ThemeType_None`（不涉及）、`ThemeType_Light`（亮色）、`ThemeType_Dark`（暗色），与 DTK 标志位对应
- 提供 API 版本宏：主版本 `DOCK_API_VERSION_MAJOR`、次版本 `DOCK_API_VERSION_MINOR`、补丁版本 `DOCK_API_VERSION_PATCH`（当前为 2.0.0），版本编码宏 `DOCK_API_VERSION_CHECK(major, minor, patch)` 将版本号编码为整数用于编译期比对，`DOCK_API_VERSION` 为当前版本编码值，插件可在编译期通过 `#if (DOCK_API_VERSION >= DOCK_API_VERSION_CHECK(2, 0, 0))` 判断接口兼容性，运行时可通过 `qApp->property(DOCK_API_VERSION_PROPERTY)` 获取版本号
- 提供消息通信字段名常量 `MSG_TYPE`（消息类型）和 `MSG_DATA`（消息数据），用于在插件 `message` 和 `MessageCallbackFunc` 方法中解析 JSON 格式数据
- 提供插件功能可用性消息常量：`MSG_GET_SUPPORT_FLAG` 查询插件功能是否可用、`MSG_SUPPORT_FLAG` 返回可用状态、`MSG_SUPPORT_FLAG_CHANGED` 通知状态变更，插件功能不可用时任务栏将插件图标从控制中心移除
- 提供任务栏溢出状态消息 `MSG_UPDATE_OVERFLOW_STATE`，对应溢出状态常量 `OVERFLOW_STATE_NOT_EXIST`（无溢出区）、`OVERFLOW_STATE_EXIST`（有溢出区）、`OVERFLOW_STATE_ALL`（所有应用在溢出区）
- 提供最小弹窗高度消息 `MSG_SET_APPLET_MIN_HEIGHT`，任务栏根据快捷面板高度动态向快捷插件发送
- 提供插件加载意愿消息 `MSG_WHETHER_WANT_TO_BE_LOADED`，插件自行决定是否被任务栏加载，不发送则默认被加载
- 提供弹窗容器位置消息 `MSG_APPLET_CONTAINER`，标识弹窗在任务栏（`APPLET_CONTAINER_DOCK`，值为 0）或快捷面板二级页面（`APPLET_CONTAINER_QUICK_PANEL`，值为 1）显示
- 提供插件图标激活状态消息 `MSG_ITEM_ACTIVE_STATE`，插件状态变化时主动发送给任务栏
- 提供卡片排序消息 `MSG_CARD_ORDER`，插件在卡片 surface 创建后主动上报排序值，任务栏按该值升序排列卡片
- 提供提示气泡更新消息 `MSG_UPDATE_TOOLTIPS_VISIBLE`，插件请求任务栏更新提示气泡，任务栏收到后调用 `itemTips()` 方法
- 提供面板尺寸变化消息 `MSG_DOCK_PANEL_SIZE_CHANGED`，任务栏面板尺寸变化时通知插件
- 提供时尚模式消息 `MSG_DOCK_FASHION_MODE`，surface 创建时和模式变化时任务栏主动发送，插件据此调整布局
- 提供插件属性消息 `MSG_PLUGIN_PROPERTY`，任务栏获取插件属性（如变色龙效果），返回 `QMap<QString, QVariant>`，对应属性常量 `PLUGIN_PROP_NEED_CHAMELEON`（是否需要变色龙效果）和 `PLUGIN_PROP_CHAMELEON_MARGIN`（变色龙边距）
- 提供快捷面板尺寸常量：`QUICK_ITEM_HEIGHT`（60）快捷面板插件高度、`QUICK_ITEM_SINGLE_WIDTH`（70）单格宽度、`QUICK_ITEM_MULTI_WIDTH`（150）双格宽度、`QUICK_ITEM_FULL_WIDTH`（310）整行宽度
- 提供插件固定尺寸常量：`DOCK_PLUGIN_ITEM_FIXED_WIDTH`（16）和 `DOCK_PLUGIN_ITEM_FIXED_HEIGHT`（16）及组合 `DOCK_PLUGIN_ITEM_FIXED_SIZE`，用于任务栏插件；`TRAY_PLUGIN_ITEM_FIXED_WIDTH`（16）和 `TRAY_PLUGIN_ITEM_FIXED_HEIGHT`（16）及组合 `TRAY_PLUGIN_ITEM_FIXED_SIZE`，用于托盘插件；`DOCK_POPUP_WIDGET_WIDTH`（330）任务栏弹窗宽度
- 提供快捷面板标识常量：`QUICK_TOP_ACTION` 标识快捷面板子页面右上角控件，`QUICK_ITEM_KEY` 标识快捷面板详情页面 itemWidget 对应的 itemKey
- 提供其他常量：`DOCK_PLUGIN_MIME`（Dock 插件 MIME 类型 `dock/plugin`）、`PLUGIN_ITEM_WIDTH`（300）插件项宽度、`DOCK_MAX_SIZE`（100）Dock 最大尺寸、`PLUGIN_MIN_ICON_NAME`（`-dark`，图标采用深色的最小尺寸后缀）、`IS_TOUCH_STATE`（触摸状态属性名）、`dockMenuItemId` 和 `unDockMenuItemId`（右键菜单驻留/移除驻留选项标识）、`REQUEST_SHUTDOWN` 和 `SHUTDOWN_MENU_FLAG`（电源插件请求调出电源管理标识）

#### 使用场景

插件在实现接口方法、处理消息通信、声明标志位或读取任务栏运行状态时，引用 `Dock` 命名空间下的对应枚举值和常量。

### PluginProxyInterface

#### 定位

框架传给插件的代理接口，插件通过 `PluginsItemInterface::init()` 接收框架传递的代理对象指针，调用代理方法向框架发送请求。位于全局命名空间，声明在 `pluginproxyinterface.h` 中。

#### 功能能力总结

- 向任务栏添加新的 Dock 项，通过插件接口指针和项标识指定要添加的项；若项标识已存在则新项将被忽略，插件需确保同一插件的多个项标识各不相同
- 请求更新（重绘）指定 Dock 项，通过插件接口指针和项标识定位目标项
- 请求移除指定 Dock 项，通过插件接口指针和项标识定位目标项；框架不删除插件对象，内存由插件自行管理
- 请求设置 Dock 项所在窗口的自动隐藏行为，控制任务栏窗口是否自动隐藏
- 请求刷新 Dock 项所在窗口的可见性状态
- 请求设置 Dock 项弹出面板（Applet）的可见性，控制弹出面板的显示或隐藏
- 将插件配置键值对持久化保存到配置文件 `~/.config/deepin/dde-dock.conf`，所有插件的配置按 `pluginName()` 返回值分组存储
- 从配置文件读取插件配置值，支持传入默认值作为键不存在时的回退返回
- 从配置文件移除插件配置，传入键列表移除指定键值对，传入空列表移除该插件的所有配置

#### 使用场景

插件在运行时通过代理对象向框架添加、更新、移除 Dock 项，控制窗口隐藏和弹出面板可见性，以及持久化读写插件配置。

### PluginManagerInterface

#### 定位

插件管理器接口，提供查询已加载插件列表、项标识和元数据的能力。继承自 `QObject`，位于全局命名空间，声明在 `pluginmanagerinterface.h` 中。

#### 功能能力总结

- 查询所有已加载的插件接口指针列表
- 查询在控制中心个性化设置中显示的插件接口指针列表
- 查询当前已加载的插件接口指针列表
- 根据插件接口指针查询对应的项标识
- 根据插件接口指针查询插件的元数据（`QJsonObject` 格式）
- 提供插件加载完成信号 `pluginLoadFinished`，在所有插件加载完毕时发出

#### 使用场景

插件或外部模块需要查询已加载插件信息或等待插件加载完成时，通过管理器接口获取插件列表和元数据。
