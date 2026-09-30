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

辅助类型（枚举与常量）位于 `Dock` 命名空间，接口类（PluginsItemInterface、PluginsItemInterfaceV2、PluginsItemInterfaceV3）位于全局命名空间。`DockPart` 枚举定义在 `common.h` 中，位于全局命名空间。

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

需要自定义插件标志位以指定插件类型和属性时，使用 flags 方法。需要在控制中心个性化设置中显示插件图标时，使用 icon 方法。开发托盘插件或快捷面板插件需要接收子插件指针时，使用 addPlugin 方法。需要与 Dock 框架进行 JSON 消息通信以扩展功能时，使用 setMessageCallback 和 message 方法。

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

需要将插件原生窗口作为卡片在 Dock 卡片区展示时，实现 cardItemKey 和 cardWindow。需要控制卡片排列顺序时，实现 cardOrder。需要为卡片提供独立的上下文菜单和提示部件时，实现 cardContextMenu、cardTipsWidget 和 invokedCardMenuItem。
