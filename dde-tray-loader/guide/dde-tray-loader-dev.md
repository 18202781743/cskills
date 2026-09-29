# 导出类型介绍

dde-tray-loader 提供 Dock 插件接口体系，包括基础插件接口、V2 扩展插件接口、V3 扩展插件接口、插件代理接口和插件管理器接口，支持插件名称与显示名称、初始化、项部件、项提示部件、项弹出面板、项命令、项上下文菜单、项排序与容器、插件禁用、显示模式与位置变化通知、图标刷新、插件设置变化通知、插件标志位、图标获取、子插件传递、消息回调与消息通信、卡片 surface、项增删与更新、窗口自动隐藏与可见性刷新、弹出面板可见性控制、配置持久化、插件加载与查询。

辅助类型 `Dock::DisplayMode`（Fashion、Efficient）、`Dock::Position`（Top、Right、Bottom、Left）、`Dock::HideMode`（KeepShowing、KeepHidden、SmartHide）、`Dock::HideState`（Unknown、Show、Hide）、`Dock::PluginFlag`/`Dock::PluginFlags`、`Dock::IconType`、`Dock::ThemeType`（None、Light、Dark）和 `DockPart`（QuickShow、QuickPanel、SystemPanel、DCCSetting）定义在 `constants.h` 和 `common.h` 中，作为接口方法的参数或返回值类型使用，不单独建章节。

## PluginsItemInterface

### 定位

Dock 插件基础接口，所有 Dock 插件必须实现的最小接口集合。位于 `Dock` 命名空间，声明 IID `com.deepin.dock.PluginsItemInterface`。插件通过继承此类并实现纯虚函数提供 Dock 项的基本能力。

### 功能能力总结

- 返回插件唯一名称（pluginName）
- 返回插件显示名称（pluginDisplayName）
- 使用代理对象初始化插件，插件应保存代理指针供后续通信使用（init）
- 返回指定 itemKey 对应的项部件（itemWidget）
- 返回指定 itemKey 对应的提示部件，在鼠标悬停时显示（itemTipsWidget）
- 返回指定 itemKey 对应的弹出面板部件，在用户点击时显示（itemPopupApplet）
- 返回指定 itemKey 对应的点击命令字符串（itemCommand）
- 返回指定 itemKey 对应的上下文菜单 JSON 字符串（itemContextMenu）
- 响应上下文菜单项被点击（invokedMenuItem）
- 返回指定 itemKey 的排序位置，0 表示左侧、-1 表示右侧（itemSortKey）
- 保存指定 itemKey 的新排序位置，在用户拖拽改变顺序时调用（setSortKey）
- 返回指定 itemKey 是否允许移入容器区域（itemAllowContainer）
- 返回指定 itemKey 当前是否在容器区域内（itemIsInContainer）
- 保存指定 itemKey 的容器状态，在用户拖入或拖出容器时调用（setItemIsInContainer）
- 返回插件是否允许被禁用（pluginIsAllowDisable）
- 返回插件当前是否已禁用（pluginIsDisable）
- 切换插件的启用与禁用状态（pluginStateSwitched）
- 接收 Dock 显示模式变化通知，显示模式为 `Dock::DisplayMode`（Fashion 或 Efficient）（displayModeChanged）
- 接收 Dock 位置变化通知，位置为 `Dock::Position`（Top、Right、Bottom 或 Left）（positionChanged）
- 刷新指定 itemKey 的图标，在系统图标主题变化时触发（refreshIcon）
- 接收插件设置变化通知（pluginSettingsChanged）
- 获取当前 Dock 显示模式，通过读取 qApp 属性实现（displayMode）
- 获取当前 Dock 位置，通过读取 qApp 属性实现（position）
- 返回插件尺寸策略，值为 System（跟随系统）或 Custom（自定义）（pluginSizePolicy）
- 返回插件类型，值为 Normal 或 Fixed；此方法已废弃，应使用 V2 接口的 flags 方法替代（type）

### 使用场景

开发 Dock 插件时，作为最小接口集合继承实现，提供插件名称、显示名称、初始化、项部件、提示部件、弹出面板、点击命令、上下文菜单、排序与容器管理、禁用控制、显示模式与位置变化响应、图标刷新和设置变化通知能力。

## PluginsItemInterfaceV2

### 定位

Dock 插件接口 V2，继承自 PluginsItemInterface，扩展插件标志位、图标获取、子插件传递和消息通信能力。位于 `Dock` 命名空间，声明 IID `com.deepin.dock.PluginsItemInterface_V2`。V2 接口方法标注 `@since 2.0.0`。

### 功能能力总结

在 V1 基础上增加以下能力（`@since 2.0.0`）：

- 返回插件标志位，类型为 `Dock::PluginFlags`，包含插件类型标志（Type_Quick、Type_Tool、Type_System、Type_Tray、Type_Fixed）、快捷面板列数标志（Quick_Panel_Single、Quick_Panel_Multi、Quick_Panel_Full）和插件属性标志（Attribute_CanDrag、Attribute_CanInsert、Attribute_CanSetting、Attribute_ForceDock、Attribute_HasCard），默认值为 Type_System 与 Attribute_Normal（flags）
- 按图标类型和主题类型返回图标对象，图标类型为 `Dock::IconType`，主题类型为 `Dock::ThemeType`（None、Light、Dark）；设置了 Attribute_CanSetting 属性的插件需实现此方法，返回在控制中心个性化设置中显示的图标（icon）
- 接收 Dock 框架传递的子插件指针，主要供托盘插件和快捷面板插件使用，普通插件无需关注（addPlugin）
- 设置消息回调函数，插件可通过回调函数向 Dock 框架发送 JSON 格式请求，用于在不破坏二进制兼容性的前提下扩展功能（setMessageCallback）
- 接收 Dock 框架发送的 JSON 格式请求，用于获取数据或执行指令，返回 JSON 格式响应（message）

### 使用场景

需要自定义插件标志位以指定插件类型和属性时，使用 flags 方法。需要在控制中心个性化设置中显示插件图标时，使用 icon 方法。开发托盘插件或快捷面板插件需要接收子插件指针时，使用 addPlugin 方法。需要与 Dock 框架进行 JSON 消息通信以扩展功能时，使用 setMessageCallback 和 message 方法。

## PluginsItemInterfaceV3

### 定位

Dock 插件接口 V3，继承自 PluginsItemInterfaceV2，扩展卡片 surface 能力。位于 `Dock` 命名空间，声明 IID `com.deepin.dock.PluginsItemInterface_V3`。插件通过卡片 surface 将原生窗口导出为 Wayland surface，在 Dock 卡片区展示。

### 功能能力总结

在 V2 基础上增加以下能力：

- 返回作为卡片 surface 导出的 itemKey，Dock 框架使用 pluginName 与 itemKey 组合作为稳定的 surface 标识（cardItemKey）
- 返回卡片项的原生窗口，Dock 框架将此窗口导出为 Wayland surface；插件保留窗口所有权，QML 或 QWidget 界面由插件自行处理（cardWindow）
- 返回卡片 surface 的排序值，Dock 框架按升序排列，值最小的卡片显示在第一个，值相同则保持创建顺序；默认值将卡片排在所有指定了排序值的卡片之后（cardOrder）
- 返回卡片 surface 的上下文菜单 JSON 字符串，格式与 itemContextMenu 一致；默认实现复用 itemContextMenu 的返回值（cardContextMenu）
- 返回卡片 surface 的提示部件，在鼠标悬停时显示；默认实现复用 itemTipsWidget 的返回值，两者均未提供时 Dock 框架回退到 pluginDisplayName（cardTipsWidget）
- 响应卡片 surface 上下文菜单项被点击；默认实现转发到 invokedMenuItem（invokedCardMenuItem）

### 使用场景

需要将插件原生窗口作为卡片在 Dock 卡片区展示时，实现 cardItemKey 和 cardWindow。需要控制卡片排列顺序时，实现 cardOrder。需要为卡片提供独立的上下文菜单和提示部件时，实现 cardContextMenu、cardTipsWidget 和 invokedCardMenuItem。

## PluginProxyInterface

### 定位

插件代理接口，插件通过此接口与 Dock 框架通信。位于 `Dock` 命名空间。插件在 init 方法中接收代理对象指针并保存，后续通过代理对象通知框架项变化、请求窗口行为和持久化配置。

### 功能能力总结

- 通知 Dock 框架新增一个项，需确保同一插件下所有 itemKey 互不相同（itemAdded）
- 通知 Dock 框架更新（重绘）指定项（itemUpdate）
- 通知 Dock 框架移除指定项，框架不会删除插件的对象，内存由插件自行管理（itemRemoved）
- 请求 Dock 框架设置指定项的窗口自动隐藏行为（requestWindowAutoHide）
- 请求 Dock 框架刷新窗口可见性（requestRefreshWindowVisible）
- 请求 Dock 框架设置指定项弹出面板的可见性（requestSetAppletVisible）
- 保存配置键值对到 dde-dock 配置文件，以 pluginName 作为分组（saveValue）
- 从 dde-dock 配置文件读取指定键的值，支持提供默认值（getValue）
- 从 dde-dock 配置文件移除指定键列表的值，键列表为空时移除该插件的所有值（removeValue）

### 使用场景

插件需要向 Dock 框架通知项的添加、更新或移除时，使用 itemAdded、itemUpdate 和 itemRemoved。插件需要请求窗口自动隐藏、刷新窗口可见性或控制弹出面板可见性时，使用 requestWindowAutoHide、requestRefreshWindowVisible 和 requestSetAppletVisible。插件需要持久化配置数据时，使用 saveValue、getValue 和 removeValue。

## PluginManagerInterface

### 定位

插件管理器接口，提供插件加载和查询能力。位于 `Dock` 命名空间，继承自 QObject。

### 功能能力总结

- 获取所有已加载的插件列表（plugins）
- 获取设置中显示的插件列表（pluginsInSetting）
- 获取当前正在使用的插件列表（currentPlugins）
- 获取指定插件接口对象对应的 itemKey（itemKey）
- 获取指定插件接口对象的元数据，返回 JSON 对象（metaData）
- 发出插件加载完成信号（pluginLoadFinished）

### 使用场景

需要以编程方式查询已加载的插件、设置中的插件或当前使用的插件时，使用 plugins、pluginsInSetting 和 currentPlugins。需要获取插件的 itemKey 或元数据时，使用 itemKey 和 metaData。需要在插件加载完成后执行后续操作时，连接 pluginLoadFinished 信号。
