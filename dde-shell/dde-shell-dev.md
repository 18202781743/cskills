# dde-shell 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-shell-dev |
| 版本 | 1.99.0 |
| 描述 | DDE Shell 框架库，提供三层插件模型（Applet → Containment → Panel）、元数据驱动的插件发现、Wayland Layer Shell 窗口管理及跨插件通信机制 |
| CMake target | `Dde::Shell` |
| find_package 名 | `DDEShell` |
| 库文件 | `libdde-shell-frame.so` |
| 头文件安装路径 | `${CMAKE_INSTALL_INCLUDEDIR}/dde-shell` |
| CMake 配置安装路径 | `${CMAKE_INSTALL_LIBDIR}/cmake/DDEShell` |
| 仓库地址 | https://github.com/linuxdeepin/dde-shell.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6quick6, libqt6dbus6, libqt6waylandclient6, libqt6waylandcompositor6 (>= 6.x)
- libdtk6core, libdtk6gui (>= 6.7.50)
- libicu74
- dde-shell (= 1.99.0)

### 开发依赖
- Qt 6 Core, Gui, Concurrent, Quick, QuickTemplates2, WaylandClient, WaylandCompositor, DBus, LinguistTools, Sql (>= 6.x)
- dtkcore, dtkgui (>= 6.7.50)
- ECM (Extra CMake Modules)
- ICU >= 74.2 (uc, i18n, io 组件)
- WaylandProtocols
- CMake >= 3.16
- dde-api (可选，提供 EventLogger)

## 3. CMake 集成

### find_package 用法

```cmake
find_package(DDEShell REQUIRED)
target_link_libraries(my-plugin PRIVATE Dde::Shell)
```

### 安装的 CMake 配置文件

- `${CMAKE_INSTALL_LIBDIR}/cmake/DDEShell/DDEShellConfig.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/DDEShell/DDEShellConfigVersion.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/DDEShell/DDEShellTargets.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/DDEShell/DDEShellPackageMacros.cmake`

### 提供的 CMake 变量

| 变量 | 说明 |
|------|------|
| `DDE_SHELL_PACKAGE_INSTALL_DIR` | 包资源安装路径（`share/dde-shell`） |
| `DDE_SHELL_PLUGIN_INSTALL_DIR` | 插件库安装路径（`lib/dde-shell`） |
| `DDE_SHELL_TRANSLATION_INSTALL_DIR` | 翻译文件安装路径 |

### 提供的 CMake 宏/函数

| 宏/函数 | 说明 |
|---------|------|
| `ds_install_package(PACKAGE <id> [TARGET <lib>])` | 安装插件包和库文件，自动设置 PREFIX/OUTPUT_NAME 和安装路径 |
| `ds_build_package(PACKAGE <id> [TARGET <lib>])` | 构建插件包（不安装），将 package/ 目录拷贝到构建目录 |
| `ds_handle_package_translation(PACKAGE <id>)` | 自动扫描 QML/C++ 文件生成翻译并安装 |

### 完整示例

```cmake
cmake_minimum_required(VERSION 3.16)
project(my-plugin)

find_package(DDEShell REQUIRED)
find_package(Dtk6 REQUIRED COMPONENTS Core Gui Widget)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD 17)

add_library(my-plugin SHARED
    myapplet.h
    myapplet.cpp
)
target_link_libraries(my-plugin PRIVATE Dde::Shell)

ds_install_package(PACKAGE org.deepin.ds.example.myapplet TARGET my-plugin)
ds_handle_package_translation(PACKAGE org.deepin.ds.example.myapplet)
```

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

- C++ 命名空间：`DS_NAMESPACE`（定义为 `ds`），使用 `DS_USE_NAMESPACE` 引入
- 宏定义：`DS_BEGIN_NAMESPACE`、`DS_END_NAMESPACE`、`DS_SHARE`

```cpp
#include <applet.h>
DS_USE_NAMESPACE

class MyPlugin : public DApplet {
    Q_OBJECT
    // ...
};
```

## 6. 关键公共类及功能描述

### DApplet

| 方法 | 功能 |
|------|------|
| `DApplet(QObject *parent)` | 构造函数 |
| `virtual bool load()` | 加载阶段：从 DConfig / appletData() 读取配置 |
| `virtual bool init()` | 初始化阶段：设置信号连接、创建 UI |
| `QString pluginId() const` | 返回插件 ID |
| `DAppletData appletData() const` | 返回插件实例数据 |
| `void setAppletData(const DAppletData &)` | 设置插件实例数据 |
| `QObject *rootObject() const` | 返回 QML 根对象（加载后可用） |
| `DPanel *panel() const` | 返回所属 Panel |

生命周期：构造 → `load()` → `init()` → `rootObjectChanged`

### DContainment

继承自 `DApplet`，容器类，管理子插件。

| 方法 | 功能 |
|------|------|
| `QList<DAppletData> groupList() const` | 返回子插件数据列表 |
| `void addApplet(DApplet *applet)` | 添加子 Applet |

### DPanel

继承自 `DContainment`，顶级面板，管理窗口。

| 方法 | 功能 |
|------|------|
| `QWindow *window() const` | 返回主窗口 |
| `QWindow *popupWindow() const` | 返回弹出窗口 |
| `QWindow *tooltipWindow() const` | 返回提示窗口 |
| `QWindow *menuWindow() const` | 返回菜单窗口 |

### DPluginLoader

单例，负责插件发现和加载。

| 方法 | 功能 |
|------|------|
| `static DPluginLoader *instance()` | 获取单例 |
| `QList<DPluginMetaData> childrenPlugin(const QString &parentId)` | 获取指定父插件的子插件元数据 |

### DAppletBridge

跨插件通信桥接。

| 方法 | 功能 |
|------|------|
| `DAppletBridge(const QString &pluginId)` | 构造，查找目标插件 |
| `bool isValid() const` | 目标插件是否存在且已加载 |
| `DApplet *applet() const` | 返回目标插件实例 |
| `DAppletProxy *proxy() const` | 返回代理对象（用于属性读写/方法调用） |

### DPluginMetaData

插件元数据，来自 `metadata.json`。

### DAppletData

插件实例运行时数据。

| 方法 | 功能 |
|------|------|
| `static DAppletData fromPluginMetaData(const DPluginMetaData &)` | 从元数据构造实例数据 |
| `void setGroupList(const QList<DAppletData> &)` | 设置子插件列表 |

### DAppletItemModel

`QAbstractListModel` 子类，暴露子 Applet 的 QML item 给 QML。角色 `Qt::UserRole+1` 对应 `model.data`。

## 7. QML 模块

| 项目 | 内容 |
|------|------|
| 模块 URI | `org.deepin.ds` |
| 版本 | 1.0 |

### 关键 QML 组件

| 组件 | 说明 |
|------|------|
| `AppletItem` | Applet 插件的 QML 根元素，提供 `Applet` 附加属性（`pluginId` 等） |
| `ContainmentItem` | Containment 插件的 QML 根元素，提供 `Containment.appletItems` 模型供 Repeater 渲染子 item |
| `DLayerShellWindow` | Layer Shell 附加属性，控制 Wayland 窗口锚定（AnchorTop/Bottom/Left/Right）、层级、边距 |

### QML 全局对象

| 对象 | 说明 |
|------|------|
| `DS` | 全局对象，提供 `DS.applet(pluginId)` 获取其他插件代理 |

### 示例

```qml
import QtQuick
import org.deepin.ds 1.0

AppletItem {
    implicitWidth: 100; implicitHeight: 100
    Text { text: Applet.pluginId }
}
```

## 8. DBus 接口

不适用（dde-shell 框架本身不对外提供 DBus 接口；个别 Panel/Applet 插件可能内部使用 DBus，但不属于框架公共接口）

## 9. 插件开发

### 插件类型

| 类型 | 基类 | 场景 | 可含子插件 |
|------|------|------|-----------|
| Applet | `DApplet` | 基础功能部件 | 否 |
| Containment | `DContainment` | 容器 | 是 |
| Panel | `DPanel` | 顶级面板（Dock、顶栏等） | 是 |

### 插件注册

C++ 插件通过 `D_APPLET_CLASS` 宏注册：

```cpp
#include <pluginfactory.h>

class MyApplet : public DApplet {
    Q_OBJECT
    // ...
};

D_APPLET_CLASS(MyApplet)
#include "myapplet.moc"
```

该宏展开为匿名 namespace 中的 `DAppletFactory` 子类，通过 `Q_PLUGIN_METADATA` 注册 Qt Plugin，框架通过 `QPluginLoader` 加载 `.so`。

### 元数据文件 metadata.json

```json
{
    "Plugin": {
        "Version": "1.0",
        "Id": "org.deepin.ds.example.applet",
        "Url": "main.qml",
        "Parent": "org.deepin.ds.dock"
    }
}
```

| 字段 | 必需 | 说明 |
|------|------|------|
| `Plugin.Version` | 是 | 版本号 |
| `Plugin.Id` | 是 | 反向域名格式插件 ID |
| `Plugin.Url` | 否 | QML 入口文件（QWidget 插件不填） |
| `Plugin.Parent` | 否 | 父插件 ID |
| `Plugin.ContainmentType` | 否 | `"Panel"` 或 `"Containment"` |

### 安装路径

| 内容 | 路径 |
|------|------|
| 包资源 | `/usr/share/dde-shell/<plugin-id>/` |
| 插件库 | `/usr/lib/dde-shell/plugins/` |
| 翻译 | `/usr/share/dde-shell/<plugin-id>/translations/` |

### 纯 QML 插件（无 C++）

```cmake
ds_install_package(PACKAGE org.deepin.ds.example.applet)
```

无需 `TARGET` 参数，仅安装 package/ 目录下的 QML 和元数据。

### 跨插件通信

C++ 端：

```cpp
DAppletBridge bridge("org.deepin.ds.weather");
if (bridge.isValid() && bridge.applet()) {
    bridge.applet()->property("temperature").toString();
    connect(bridge.applet(), SIGNAL(temperatureChanged()), this, SLOT(onChanged()));
}
```

QML 端：

```qml
var weather = DS.applet("org.deepin.ds.weather")
if (weather && weather.rootObject) {
    console.log(weather.rootObject.temperature)
}
```

### DConfig 集成

```cpp
auto config = DConfig::create("org.deepin.dde.shell", PLUGIN_ID);
config->value("key", defaultValue);
```

配置元数据文件放在 `configs/<plugin-id>.json`，通过 `dtk_add_config_meta_files` 注册。

### 测试

```bash
# 列出所有插件
dde-shell --list

# 测试单个插件
dde-shell -p <plugin-id>

# 禁用指定插件
dde-shell -d <plugin-id>

# 从 build 目录加载
DDE_SHELL_PACKAGE_PATH=/path/to/packages \
DDE_SHELL_PLUGIN_PATH=/path/to/plugins \
./build/shell/dde-shell -p <plugin-id>
```
