---
name: dde-tray-development
description: DDE 托盘插件开发指南，面向任务栏托盘与快捷面板插件的开发和维护，覆盖插件接口、界面与交互、消息与菜单、工程构建及问题排查，并支持插件类型与实现方式选择和加载、显示问题定位。
---

# dde-tray-development

为任务栏开发托盘（Tray）插件。

## 概述

托盘插件是遵循 Qt 插件标准的共享库（`.so`），安装路径为 `lib/dde-dock/plugins`，通过实现 `PluginsItemInterfaceV2` 接口与任务栏交互。

## 前置条件

- Qt 6 + C++17 开发环境
- DTK 开发库（Dtk6::Widget, Dtk6::Gui）
- dde-tray-loader-dev 开发库（提供接口头文件和 CMake 配置）

## 快速开始

### 插件类型选择

| 插件类型 | flags 设置 | 说明 |
|----------|-----------|------|
| **纯托盘插件** | `Type_Tray \| Attribute_CanSetting` | 仅在托盘区显示图标，可选控制中心显隐 |
| **快捷面板插件** | `Type_Quick \| Quick_Panel_*` | 同时显示托盘图标和快捷面板控件 |

> **重要**：`Type_Tray` 和 `Type_Quick` 是互斥的。快捷面板插件详见 [references/quick-panel-guide.md](references/quick-panel-guide.md)。

### 必须实现的接口

| 接口 | 说明 |
|------|------|
| `pluginName()` | 返回插件唯一标识名 |
| `init(PluginProxyInterface *)` | 初始化入口，保存 proxy 到 `m_proxyInter` |
| `itemWidget(itemKey)` | 返回托盘区显示的主控件 |
| `flags()` | 返回插件类型标志（V2 接口） |

### 插件类结构

```cpp
class MyPlugin : public QObject, public PluginsItemInterfaceV2
{
    Q_OBJECT
    Q_INTERFACES(PluginsItemInterfaceV2)
    Q_PLUGIN_METADATA(IID ModuleInterface_iid_V2 FILE "myplugin.json")

public:
    const QString pluginName() const override { return "myplugin"; }
    const QString pluginDisplayName() const override { return tr("My Plugin"); }
    
    void init(PluginProxyInterface *proxyInter) override;
    QWidget *itemWidget(const QString &itemKey) override;
    Dock::PluginFlags flags() const override;
    
    // 可选：点击交互
    const QString itemCommand(const QString &itemKey) override;
    QWidget *itemPopupApplet(const QString &itemKey) override;
    
protected:
    PluginProxyInterface *m_proxyInter = nullptr;
};
```

### 托盘图标控件实现

```cpp
class MyTrayIcon : public QWidget
{
public:
    MyTrayIcon(QWidget *parent = nullptr) : QWidget(parent)
    {
        setMinimumSize(Dock::TRAY_PLUGIN_ITEM_FIXED_SIZE);
    }
};
```

> **尺寸设置**：使用 `setMinimumSize(Dock::TRAY_PLUGIN_ITEM_FIXED_SIZE)` 而非 `setFixedSize()`，让任务栏控制大小。自定义尺寸需覆写 `pluginSizePolicy()` 返回 `PluginSizePolicy::Custom`。

> **新插件默认隐藏**：使用 `Attribute_CanSetting` 的新插件默认是隐藏的，需要在「控制中心 → 个性化 → 任务栏 → 插件区域」中手动启用。

### 插件初始化

```cpp
#define MYPLUGIN_KEY "myplugin-item-key"

void MyPlugin::init(PluginProxyInterface *proxyInter)
{
    m_proxyInter = proxyInter;
    
    // 加载翻译文件（必须在创建控件前调用）
    loadTranslator();
    
    // 创建托盘图标控件
    m_trayIcon.reset(new MyTrayIcon);
    
    // 注册插件（使用自定义 key，而非 pluginName()）
    m_proxyInter->itemAdded(this, MYPLUGIN_KEY);
}

Dock::PluginFlags MyPlugin::flags() const override
{
    return Dock::PluginFlag::Type_Tray | Dock::PluginFlag::Attribute_CanSetting;
}

QWidget *MyPlugin::itemWidget(const QString &itemKey)
{
    if (itemKey == MYPLUGIN_KEY) {
        return m_trayIcon.data();
    }
    return nullptr;
}
```

## 控件尺寸规范

| 控件类型 | 尺寸 | 设置方式 |
|----------|------|----------|
| 托盘图标（系统尺寸） | 16x16 | `setMinimumSize(Dock::TRAY_PLUGIN_ITEM_FIXED_SIZE)` |
| 托盘图标（自定义尺寸） | 自定义 | 覆写 `pluginSizePolicy()` 返回 `Custom`，使用 `setFixedSize()` |
| 快捷面板控件 | 按 `Quick_Panel_*` 标志 | 只使用 `setFixedHeight(Dock::QUICK_ITEM_HEIGHT)` |

## itemPopupApplet 与 Tooltip

**框架逻辑**：鼠标 hover 托盘图标时，框架检查 `itemPopupApplet` 返回值。如果返回控件，并且面板显示，则认为有弹出面板，**不显示 tooltip**。

| 场景 | `itemPopupApplet` 返回值 |
|------|---------------------------|
| 有弹出面板（如音量滑块） | 返回弹出面板控件 |
| 无弹出面板 | 返回 `nullptr` |
| 有快捷面板 | 返回 `nullptr`（快捷面板通过 `itemWidget(QUICK_ITEM_KEY)` 提供） |

## 托盘图标点击交互

托盘图标点击有三种交互方式：

| 方式 | 实现接口 | 说明 |
|------|----------|------|
| 执行命令 | `itemCommand(itemKey)` | 返回要执行的命令字符串，如打开控制中心 |
| 弹出面板 | `itemPopupApplet(itemKey)` | 返回弹出控件，如音量滑块 |
| 快捷面板子页面 | `requestSetAppletVisible()` | 快捷面板插件点击后显示详情页 |

### itemCommand 示例

```cpp
const QString MyPlugin::itemCommand(const QString &itemKey)
{
    if (itemKey == MYPLUGIN_KEY) {
        return "dde-am org.deepin.dde.control-center -- mymodule";
    }
    return QString();
}
```

### 弹出面板示例

```cpp
QWidget *MyPlugin::itemPopupApplet(const QString &itemKey)
{
    if (itemKey == MYPLUGIN_KEY) {
        if (!m_appletWidget) {
            m_appletWidget.reset(new MyAppletWidget);
        }
        return m_appletWidget.data();
    }
    return nullptr;
}
```

> **弹出面板与快捷面板的区别**：弹出面板是点击托盘图标后弹出的控件；快捷面板是展开快捷面板区域后显示的控件。两者通过不同的接口返回。

## 推荐实现的接口

| 接口 | 说明 |
|------|------|
| `pluginDisplayName()` | 插件显示名称 |
| `icon(IconType, ThemeType)` | 控制中心插件图标（`Attribute_CanSetting` 时必须实现） |
| `itemTipsWidget(itemKey)` | 鼠标悬浮提示 |
| `itemContextMenu(itemKey)` | 右键菜单 JSON 数据 |
| `invokedMenuItem(...)` | 右键菜单项点击回调 |

## 翻译加载

dde-tray-loader **不会自动加载第三方插件的翻译文件**，插件必须在 `init()` 中主动加载。翻译加载遵循 Qt 标准，使用 DTK 时遵循 DTK 翻译规范。

## JSON 元数据

```json
{
    "api": "2.0.0"
}
```

## CMakeLists.txt 模板

```cmake
cmake_minimum_required(VERSION 3.16)
project(myplugin VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)

find_package(DdeTrayLoader REQUIRED)
find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets LinguistTools)
find_package(Dtk6 REQUIRED COMPONENTS Widget Gui)

add_library(myplugin SHARED
    myplugin.cpp
    mytrayicon.cpp
)

target_link_libraries(myplugin PRIVATE
    Qt6::Core
    Qt6::Gui
    Qt6::Widgets
    Dtk6::Widget
    Dtk6::Gui
)

set(TS_FILES translations/${PROJECT_NAME}_zh_CN.ts)
qt_add_translations(myplugin TS_FILES ${TS_FILES} QM_FILES_OUTPUT_VARIABLE QM_FILES)

install(TARGETS myplugin LIBRARY DESTINATION lib/dde-dock/plugins)
install(FILES ${QM_FILES} DESTINATION share/dde-dock/translations)
```

## 构建与调试

```bash
cmake -B build -DCMAKE_INSTALL_PREFIX=/usr
cmake --build build -j$(nproc)
sudo cmake --install build
```

> 安装后重启 dde-shell 使插件生效：`systemctl --user restart dde-shell@DDE`

## 典型项目结构

```
my-plugin/
├── CMakeLists.txt
├── myplugin.h
├── myplugin.cpp
├── mytrayicon.h
├── mytrayicon.cpp
├── myplugin.json
├── myplugin.qrc
└── icons/
    ├── myplugin.svg
    └── myplugin-dark.svg
```

## 常见问题

### 托盘图标不显示

- 检查控件尺寸：必须设置 `setMinimumSize(16, 16)`
- 检查 `paintEvent` 实现：确保正确绘制图标
- 检查图标路径：使用正确的资源路径（如 `:/icons/myplugin.svg`）

### Tooltip 不显示

- 检查 `itemPopupApplet` 返回值：无弹出面板应返回 `nullptr`
- 检查 `itemTipsWidget` 是否正确处理 `itemKey`

### flags 设置错误

- `Type_Tray` 和 `Type_Quick` 不应同时使用
- 需要 `Attribute_CanSetting` 时必须实现 `icon()` 方法

## 开发流程

1. 确定插件类型（纯托盘或快捷面板）
2. 创建插件类，继承 `QObject` + `PluginsItemInterfaceV2`
3. 实现 `flags()`、`pluginName()`、`init()`、`itemWidget()`
4. 加载翻译文件（调用 `loadTranslator()`）
5. 实现控件尺寸设置和绘制逻辑
6. 实现交互功能（tooltip / context menu）
7. 编写 JSON 元数据和 CMakeLists.txt
8. 构建、安装、重启 dde-shell

## References 加载指引

按需加载以下参考文档：

1. **`references/tray-plugin-spec.md`** — 托盘插件接口规范（V1/V2 + flags + proxy 合并文档）。**首次开发时必须阅读。**
2. **`references/quick-panel-guide.md`** — 快捷面板插件开发指南。仅开发快捷面板插件时阅读。
3. **`references/message-protocol.md`** — 消息协议。当插件需要与任务栏进行消息通信时阅读。
4. **`references/context-menu.md`** — 右键菜单协议。当插件需要实现右键菜单时阅读。

## 相关代码仓库

当需要查找任务栏或托盘相关实现代码时，应优先查找以下仓库：

- **dde-tray-loader**: https://github.com/linuxdeepin/dde-tray-loader — 托盘加载器和接口定义
- **dde-shell**: https://github.com/linuxdeepin/dde-shell — 任务栏 shell 实现

> 注意：不要在 dde-dock 仓库中查找，那是旧版本任务栏实现。新版本任务栏相关代码在 dde-shell 和 dde-tray-loader 中。