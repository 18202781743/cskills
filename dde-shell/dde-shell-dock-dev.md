# dde-shell-dock 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-shell-dock-dev |
| 版本 | 1.99.0 |
| 描述 | DDE Shell Dock 面板开发库，提供 Dock 面板插件的 C++ 接口和 CMake 集成，允许第三方开发 Dock 区域的 Applet 插件 |
| CMake target | `Dde::ShellDock` |
| find_package 名 | `DDEShellDock` |
| 库文件 | `libdde-shell-dock.so` |
| 头文件安装路径 | `${CMAKE_INSTALL_INCLUDEDIR}/dde-shell/dock` |
| CMake 配置安装路径 | `${CMAKE_INSTALL_LIBDIR}/cmake/DDEShellDock` |
| 仓库地址 | https://github.com/linuxdeepin/dde-shell.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6quick6 (>= 6.x)
- libdde-shell-frame (>= 1.99.0)
- dde-shell (= 1.99.0)

### 开发依赖
- Qt 6 Core, Gui, Quick (>= 6.x)
- dde-shell-dev (>= 1.99.0)
- CMake >= 3.16

## 3. CMake 集成

### find_package 用法

```cmake
find_package(DDEShellDock REQUIRED)
target_link_libraries(my-dock-plugin PRIVATE Dde::ShellDock)
```

### 安装的 CMake 配置文件

- `${CMAKE_INSTALL_LIBDIR}/cmake/DDEShellDock/DDEShellDockConfig.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/DDEShellDock/DDEShellDockConfigVersion.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/DDEShellDock/DDEShellDockTargets.cmake`

### 依赖关系

`DDEShellDockConfig.cmake` 内部会自动 `find_dependency(DDEShell)`，因此只需 find DDEShellDock 即可获得 Dde::Shell 的传递依赖。

### 完整示例

```cmake
cmake_minimum_required(VERSION 3.16)
project(my-dock-applet)

find_package(DDEShell REQUIRED)
find_package(DDEShellDock REQUIRED)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD 17)

add_library(my-dock-applet SHARED
    mydockapplet.h
    mydockapplet.cpp
)
target_link_libraries(my-dock-applet PRIVATE Dde::Shell Dde::ShellDock)

ds_install_package(PACKAGE org.deepin.ds.dock.myapplet TARGET my-dock-applet)
```

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

- C++ 命名空间：`DS_NAMESPACE`（定义为 `ds`），使用 `DS_USE_NAMESPACE` 引入
- 与 dde-shell 框架共用同一命名空间

## 6. 关键公共类及功能描述

### DAppletDock

继承自 `DApplet`，Dock 面板的 C++ 后端类。

| 方法/属性 | 功能 |
|-----------|------|
| `bool visible() const` | 返回 Dock 是否可见 |
| `void setVisible(bool visible)` | 设置 Dock 可见性 |
| `bool isSupported() const` | 返回 Dock 是否被支持 |
| `void setSupported(bool supported)` | 设置支持状态 |
| `virtual DockItemInfo dockItemInfo()` | 返回 Dock 项信息 |

信号：
- `visibleChanged()`
- `supportedChanged()`

### DockItemInfo

结构体，描述 Dock 区域的插件项信息。

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | `QString` | 插件名称 |
| `displayName` | `QString` | 显示名称 |
| `itemKey` | `QString` | 插件唯一标识键 |
| `settingKey` | `QString` | 设置键 |
| `dccIcon` | `QString` | 控制中心图标 |
| `visible` | `bool` | 是否可见 |

已注册为 Qt 元类型：`Q_DECLARE_METATYPE(DockItemInfo)` 和 `Q_DECLARE_METATYPE(DockItemInfos)`。

### 辅助函数

| 函数 | 说明 |
|------|------|
| `void registerPluginInfoMetaType()` | 注册 DockItemInfo / DockItemInfos 元类型，用于 DBus 传输 |
| `QDBusArgument &operator<<(...)` | DBus 序列化 DockItemInfo |
| `const QDBusArgument &operator>>(...)` | DBus 反序列化 DockItemInfo |

## 7. QML 模块

| 项目 | 内容 |
|------|------|
| 模块 URI | `org.deepin.ds` |
| 版本 | 1.0 |

### Dock 相关 QML 组件

| 组件 | 说明 |
|------|------|
| `AppletItem` | Dock Applet 的 QML 根元素，通过 `Applet.pluginId` 获取插件 ID |
| `ContainmentItem` | Dock 面板容器，通过 `Containment.appletItems` 模型渲染子 Applet |
| `DLayerShellWindow` | 控制 Dock 窗口的 Layer Shell 锚定（通常锚定屏幕底部） |

### Dock Applet QML 示例

```qml
import QtQuick
import QtQuick.Controls
import org.deepin.ds 1.0

AppletItem {
    implicitWidth: 48; implicitHeight: 48

    // 通过 Applet 附加属性获取上下文
    Text {
        anchors.centerIn: parent
        text: Applet.pluginId
    }
}
```

metadata.json 中设置 `Parent` 为 `org.deepin.ds.dock` 即可将插件挂载到 Dock：

```json
{
    "Plugin": {
        "Version": "1.0",
        "Id": "org.deepin.ds.dock.myapplet",
        "Url": "main.qml",
        "Parent": "org.deepin.ds.dock"
    }
}
```

## 8. DBus 接口

DockItemInfo / DockItemInfos 结构体已注册 DBus 序列化支持（`QDBusArgument` 运算符重载），可用于在 DBus 通信中传输 Dock 项信息。具体 DBus 服务由 Dock 面板插件运行时提供，非本开发库直接暴露。

## 9. 插件开发

### Dock Applet 插件

Dock Applet 是挂载到 Dock Panel（`org.deepin.ds.dock`）下的子插件。开发流程：

1. 继承 `DApplet`（或 `DAppletDock` 如需 Dock 特定接口）
2. 在 metadata.json 中设置 `Parent: "org.deepin.ds.dock"`
3. 提供 QML 入口文件（`Plugin.Url`）
4. 使用 `D_APPLET_CLASS` 宏注册
5. 用 `ds_install_package` 安装

### 纯 QML Dock Applet

```cmake
find_package(DDEShell REQUIRED)
ds_install_package(PACKAGE org.deepin.ds.dock.myapplet)
```

### 带 C++ 后端的 Dock Applet

```cpp
#include <applet.h>
#include <dappletdock.h>
#include <pluginfactory.h>

DS_USE_NAMESPACE

class MyDockApplet : public DApplet {
    Q_OBJECT
public:
    explicit MyDockApplet(QObject *parent = nullptr) : DApplet(parent) {}
    bool load() override { return DApplet::load(); }
    bool init() override {
        DApplet::init();
        // 可通过 panel() 获取 Dock 面板
        return true;
    }
};

D_APPLET_CLASS(MyDockApplet)
#include "mydockapplet.moc"
```

### 安装路径

| 内容 | 路径 |
|------|------|
| 包资源 | `/usr/share/dde-shell/<plugin-id>/` |
| 插件库 | `/usr/lib/dde-shell/plugins/` |
| 翻译 | `/usr/share/dde-shell/<plugin-id>/translations/` |

### Debian 打包依赖

```
Build-Depends: libdde-shell-dev (>= 0.0.10), libdde-shell-dock-dev
Depends: dde-shell (>= 2.0)
```

`.install` 文件：
```
usr/lib/dde-shell/plugins/*
usr/share/dde-shell/*
```
