# dde-tray-loader 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-tray-loader-dev |
| 版本 | 2.0.99（Dock 兼容版本 6.0.37） |
| 描述 | DDE 托盘/ Dock 插件加载器，提供 header-only 接口头文件，允许开发 Dock 托盘插件 |
| CMake target | 不适用（header-only，无编译库） |
| find_package 名 | `DdeTrayLoader` / `DdeDock` |
| 头文件安装路径 | `${CMAKE_INSTALL_INCLUDEDIR}/dde-tray-loader` |
| 仓库地址 | https://github.com/linuxdeepin/dde-tray-loader.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6widgets6 (>= 6.x)
- libdtk6core, libdtk6gui, libdtk6widget

### 开发依赖
- Qt 6 Core, Gui, Widgets, DBus (>= 6.x)
- dtkcore, dtkgui, dtkwidget
- CMake >= 3.16

## 3. CMake 集成

### find_package 用法

```cmake
# 新接口（推荐）
find_package(DdeTrayLoader REQUIRED)
target_link_libraries(your-plugin PRIVATE Dde::TrayLoader)

# 兼容旧接口
find_package(DdeDock REQUIRED)
target_link_libraries(your-plugin PRIVATE Dde::Dock)
```

### 安装的 CMake 配置文件

- `${CMAKE_INSTALL_LIBDIR}/cmake/DdeTrayLoader/DdeTrayLoaderConfig.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/DdeDock/DdeDockConfig.cmake`

## 4. pkg-config

| .pc 文件 | 内容 |
|----------|------|
| `dde-tray-loader.pc` | header-only，Cflags: -I.../dde-tray-loader（无 Libs） |
| `dde-dock.pc` | header-only，Cflags: -I.../dde-tray-loader（兼容旧接口，无 Libs） |

```bash
pkg-config --cflags dde-tray-loader
```

## 5. 命名空间

`Dock`

```cpp
#include <pluginsiteminterface.h>
// 使用 Dock 命名空间
```

## 6. 关键公共类及功能描述

| 类名 | 功能 | 关键方法 |
|------|------|----------|
| `PluginsItemInterface` | Dock 插件基础接口（V1），所有 Dock 插件必须实现 | `pluginName()`, `pluginDisplayName()`, `itemWidget()`, `init()` |
| `PluginsItemInterfaceV2` | 插件接口 V2，扩展 V1 | 增加 `itemSize()`, `itemTipsWidget()` 等 |
| `PluginsItemInterfaceV3` | 插件接口 V3，最新版 | 增加更多扩展方法和信号 |
| `PluginProxyInterface` | 插件代理接口，插件通过它与 Dock 通信 | `itemAdded()`, `itemRemoved()`, `requestWindowAutoHide()` |
| `PluginManagerInterface` | 插件管理器接口 | `loadPlugin()`, `getPlugin()` |

### PluginsItemInterface 关键方法

```cpp
class PluginsItemInterface {
    virtual const QString pluginName() const = 0;
    virtual const QString pluginDisplayName() const = 0;
    virtual void init(PluginProxyInterface *proxyInter) = 0;
    virtual QWidget *itemWidget(const QString &itemKey) = 0;
    // ...
};
```

## 7. QML 模块

不适用（Dock 插件使用 QWidget，不使用 QML）

## 8. DBus 接口

Dock 插件可通过 DBus 与系统服务通信，但 dde-tray-loader 本身不导出 DBus 接口。

常用 DBus 服务（供插件调用）：

| 服务名 | 对象路径 | 说明 |
|--------|----------|------|
| `org.deepin.dde.daemon.Dock1` | `/org/deepin/dde/daemon/Dock1` | Dock 后端服务 |
| `org.deepin.dde.Display1` | `/org/deepin/dde/Display1` | 显示设置服务 |

## 9. 插件开发

### 插件接口

继承 `PluginsItemInterface`（或 V2/V3），实现纯虚方法：

```cpp
#include <pluginsiteminterface.h>

class MyPlugin : public QObject, public PluginsItemInterface {
    Q_OBJECT
    Q_INTERFACES(PluginsItemInterface)
    Q_PLUGIN_METADATA(IID "com.deepin.dock.PluginsItemInterface" FILE "myplugin.json")

public:
    const QString pluginName() const override { return "myplugin"; }
    const QString pluginDisplayName() const override { return "My Plugin"; }
    void init(PluginProxyInterface *proxyInter) override { m_proxy = proxyInter; }
    QWidget *itemWidget(const QString &itemKey) override { return m_widget; }
    // ...

private:
    PluginProxyInterface *m_proxy = nullptr;
    QWidget *m_widget = nullptr;
};
```

### CMake 示例

```cmake
find_package(DdeTrayLoader REQUIRED)
find_package(Dtk6 REQUIRED COMPONENTS Core Gui Widget)

add_library(myplugin SHARED myplugin.cpp myplugin.h)
target_link_libraries(myplugin PRIVATE
    Dde::TrayLoader Dtk6::Core Dtk6::Gui Dtk6::Widget Qt6::Widgets
)
install(TARGETS myplugin LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}/dde-dock/plugins)
```

### 插件安装路径

- `${CMAKE_INSTALL_LIBDIR}/dde-dock/plugins/`

### 元数据文件

```json
{
    "api": "1.0",
    "name": "myplugin",
    "display": "My Plugin"
}
```
