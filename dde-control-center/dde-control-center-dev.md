# dde-control-center 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-control-center-dev |
| 版本 | 6.0.44 |
| 描述 | DDE 控制中心，提供系统设置界面框架和插件机制，允许第三方开发设置模块插件 |
| CMake target | `Dde::ControlCenter` |
| find_package 名 | `DdeControlCenter` |
| 头文件安装路径 | `${CMAKE_INSTALL_INCLUDEDIR}/dde-control-center` |
| 库文件 | `libdde-control-center_frame.so` |
| 插件版本 | v1.1 |
| 仓库地址 | https://github.com/linuxdeepin/dde-control-center.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6quick6, libqt6dbus6 (>= 6.x)
- libdtk6core, libdtk6gui (>= 6.7.50)
- dde-control-center (= 6.0.44)

### 开发依赖
- Qt 6 Core, Quick, Gui, Network, DBus, Concurrent, Multimedia (>= 6.x)
- dtkcore, dtkgui (>= 6.7.50)
- CMake >= 3.18
- dde-api (可选)

## 3. CMake 集成

### find_package 用法

```cmake
find_package(DdeControlCenter REQUIRED)
target_link_libraries(your-plugin PRIVATE Dde::ControlCenter)
```

### 安装的 CMake 配置文件

- `${CMAKE_INSTALL_LIBDIR}/cmake/DdeControlCenter/DdeControlCenterConfig.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/DdeControlCenter/DdeControlCenterTargets.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/DdeControlCenter/DdeControlCenterPluginMacros.cmake`

### 提供的 CMake 变量

| 变量 | 说明 |
|------|------|
| `DDE_CONTROL_CENTER_PLUGIN_VERSION` | 插件版本（1.1） |
| `DDE_CONTROL_CENTER_PLUGIN_DIR` | 插件目录名（plugins_v1.1） |
| `DDE_CONTROL_CENTER_PLUGIN_INSTALL_DIR` | 插件安装完整路径 |
| `DDE_CONTROL_CENTER_TRANSLATION_INSTALL_DIR` | 翻译文件安装路径 |

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

`dccV25`

```cpp
using namespace dccV25;
```

## 6. 关键公共类及功能描述

| 类名 | 功能 | 关键方法 |
|------|------|----------|
| `DccFactory` | 插件工厂接口，所有插件需继承 | `create()`, `metaData()` |
| `DccObject` | 控制中心配置对象，描述设置项层级结构 | `appendChild()`, `displayName()`, `icon()` |
| `DccApp` | 控制中心应用单例 | `instance()`, `rootObject()` |
| `ModuleObject` | 模块对象，旧版插件接口 | `active()`, `deactive()` |

## 7. QML 模块

控制中心插件使用 QML 渲染 UI，通过 `qt_add_qml_module` 注册 QML 模块，URI 为插件名。

## 8. DBus 接口

dde-control-center 通过 DBus 与系统服务通信，但不直接导出 DBus 服务接口。

## 9. 插件开发

### 插件接口

控制中心插件通过 `DCC_FACTORY_CLASS` 宏注册：

```cpp
#include <dccfactory.h>

class MySetting : public QObject {
    Q_OBJECT
    Q_PLUGIN_METADATA(IID "org.deepin.dde.dcc-factory/v1.0" FILE "mysetting.json")
    // ...
};

DCC_FACTORY_CLASS(MySetting)
```

### CMake 宏

| 宏 | 功能 |
|----|------|
| `dcc_build_plugin(NAME <name> TARGET <target> ...)` | 构建插件，自动处理 QML 资源 |
| `dcc_install_plugin(...)` | 安装插件到控制中心插件目录 |
| `dcc_handle_plugin_translation(PACKAGE <name>)` | 处理插件翻译 |

### 插件开发示例

```cmake
find_package(DdeControlCenter REQUIRED)
find_package(Dtk6 REQUIRED COMPONENTS Core Gui)

# 构建插件
dcc_build_plugin(
    NAME mysetting
    TARGET dcc-mysetting
    QML_FILES qml/MySettingMain.qml
)

target_link_libraries(dcc-mysetting PRIVATE Dde::ControlCenter Dtk6::Core Dtk6::Gui)

# 安装插件
dcc_install_plugin(TARGET dcc-mysetting)
```

### 插件安装路径

- 插件库：`${CMAKE_INSTALL_LIBDIR}/dde-control-center/plugins_v1.1/<plugin-name>/`
- 翻译文件：`${CMAKE_INSTALL_DATAROOTDIR}/dde-control-center/translations/v1.1/`

### 元数据文件

插件通过 Q_PLUGIN_METADATA 的 JSON 文件描述：

```json
{
    "ID": "org.deepin.dde.control-center.mysetting",
    "DisplayName": "My Setting",
    "Icon": "mysetting-icon",
    "Order": 10
}
```
