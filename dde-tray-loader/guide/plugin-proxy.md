# 插件代理接口

dde-tray-loader 提供插件代理接口，作为插件与 Dock 框架之间双向通信的中间层。插件在初始化阶段接收框架传递的代理对象指针并保存，后续通过该代理对象向框架通知项的生命周期变化、请求窗口行为控制以及持久化插件配置数据。接口以 header-only 形式发布，使用方包含头文件即可使用。

## 开发包

使用 dde-tray-loader 公开接口前，需要安装开发包 `dde-tray-loader-dev`。该开发包以 header-only 形式提供公开头文件和构建配置信息，不提供编译库文件。

## 集成

### CMake 配置

CMake 是推荐的集成方式。查找 `DdeTrayLoader` 包后，配置脚本会自动将 `dde-dock/` 头文件目录添加到全局包含路径，无需手动设置 `include_directories()` 或 `target_link_libraries()`：

```cmake
find_package(DdeTrayLoader REQUIRED)
```

由于开发包为 header-only 形式，不提供编译库文件，也不创建任何 IMPORTED 目标，因此不需要链接步骤。仍受支持的旧写法可查找 `DdeDock` 包，同样会自动添加头文件包含路径，此写法为兼容方式，新工程应使用 `DdeTrayLoader` 包。

开发包同时提供 pkg-config 模块 `dde-dock`，其 Cflags 指向 `dde-dock/` 头文件目录，提供所有公开接口头文件的搜索路径，无链接库（Libs）。

### 使用方式

在 C++ 源文件中通过以下方式引入公开头文件：

```cpp
#include <pluginproxyinterface.h>
```

PluginProxyInterface 位于全局命名空间。插件在 PluginsItemInterface 的初始化方法中接收代理对象指针并保存到成员变量中，后续通过该指针调用代理接口方法与框架通信。

## 模块API介绍

### PluginProxyInterface

#### 定位

插件代理接口，插件通过此接口与 Dock 框架通信。位于全局命名空间。插件在初始化时接收代理对象指针并保存，后续通过代理对象通知框架项变化、请求窗口行为和持久化配置。

#### 功能能力总结

- 向框架通知项的生命周期事件：新增项（需保证同一插件下所有项标识互不重复，否则新项被忽略）、更新项（触发重绘）、移除项（框架不删除插件的对象，内存由插件自行管理）
- 请求框架控制窗口行为：设置指定项的窗口自动隐藏行为、刷新窗口可见性、控制指定项弹出面板的显示与隐藏
- 持久化插件配置数据：以插件名称为分组，将键值对保存到 dde-dock 配置文件中；支持按键读取配置值并提供默认值兜底；支持按键列表批量移除配置项，键列表为空时移除该插件的所有配置

#### 使用场景

插件需要向 Dock 框架通知项的添加、更新或移除时，使用 itemAdded、itemUpdate 和 itemRemoved。插件需要请求窗口自动隐藏、刷新窗口可见性或控制弹出面板可见性时，使用 requestWindowAutoHide、requestRefreshWindowVisible 和 requestSetAppletVisible。插件需要持久化配置数据时，使用 saveValue、getValue 和 removeValue。
