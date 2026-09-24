# dtkdeclarative 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | libdtkdeclarative-dev / libdtk6declarative-dev |
| 版本 | 6.7.50 |
| 描述 | DTK QML 声明式控件库，基于 Qt6 提供 DDE 风格的 QML 组件和 Chameleon 主题样式 |
| CMake target | `Dtk::Declarative`（DTK5）/ `Dtk6::Declarative`（DTK6） |
| find_package 名 | `DtkDeclarative`（DTK5）/ `Dtk6Declarative`（DTK6） |
| 头文件安装路径 | `${CMAKE_INSTALL_INCLUDEDIR}/dtk6/DDeclarative`（DTK6） |
| 库文件 | `libdtk6declarative.so`（DTK6） |
| 仓库地址 | https://github.com/linuxdeepin/dtkdeclarative.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6qml6, libqt6quick6 (>= 6.x)
- libdtk6core (>= 6.7.50)
- libdtk6gui (>= 6.7.50)

### 开发依赖
- Qt 6 Core, Qt 6 Gui, Qt 6 Qml, Qt 6 Quick (>= 6.x)
- dtkcore (>= 6.7.50)
- dtkgui (>= 6.7.50)
- CMake >= 3.16

## 3. CMake 集成

### find_package 用法

```cmake
find_package(Dtk6Declarative REQUIRED)
target_link_libraries(your-target PRIVATE Dtk6::Declarative)
```

### 安装的 CMake 配置文件

- `${CMAKE_INSTALL_LIBDIR}/cmake/Dtk6Declarative/Dtk6DeclarativeConfig.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/Dtk6Declarative/Dtk6DeclarativeConfigVersion.cmake`

## 4. pkg-config

| .pc 文件 | 内容 |
|----------|------|
| `dtk6declarative.pc` | Libs: -ldtk6declarative，Cflags: -I.../dtk6/DDeclarative |
| `dtkdeclarative.pc` | Libs: -ldtkdeclarative |

```bash
pkg-config --cflags --libs dtk6declarative
```

## 5. 命名空间

`Dtk::Quick`（通过 `DQUICK_USE_NAMESPACE` 宏引入）

```cpp
#include <DDeclarative>
DQUICK_USE_NAMESPACE
```

## 6. 关键公共类及功能描述

| 类名 | 功能 | 关键方法 |
|------|------|----------|
| `DAppLoader` | DTK QML 应用加载器，自动设置 DDE 主题环境 | `load()`, `loadPlugin()` |
| `DPopupWindowHandle` | 弹出窗口句柄，管理 QML 弹出窗口 | `setWindow()`, `show()` |
| `DQuickItemViewport` | 视口控件，提供圆形裁剪等效果 | `setRadius()` |
| `DPlatformThemeProxy` | 平台主题代理，QML 中访问平台主题 | `accentColor()`, `windowRadius()` |
| `DQuickDciIcon` | DCI 图标 QML 渲染 | `name`, `mode`, `theme` |
| `DQuickColorLayer` | 颜色叠加层 | `color`, `spread` |
| `DQuickOpacityMask` | 透明度遮罩 | `maskSource`, `source` |

## 7. QML 模块

### org.deepin.dtk

| 属性 | 内容 |
|------|------|
| 模块 URI | `org.deepin.dtk` |
| 版本 | 1.0 |
| 插件 | `dtkdeclarativeplugin` |

关键 QML 组件：

| 组件 | 功能 |
|------|------|
| `D.ApplicationWindow` | DTK 应用窗口 |
| `D.Button` | DTK 按钮 |
| `D.TextField` | DTK 输入框 |
| `D.CheckBox` | DTK 复选框 |
| `D.ComboBox` | DTK 下拉框 |
| `D.Slider` | DTK 滑块 |
| `D.ToolTip` | DTK 工具提示 |
| `D.Popup` | DTK 弹出窗口 |
| `D.Menu` | DTK 菜单 |
| `D.MenuItem` | DTK 菜单项 |
| `D.Spinner` | 加载动画 |
| `D.CrumbEdit` | 面包屑编辑器 |
| `D.Dialog` | DTK 对话框 |
| `D.TitleBar` | 标题栏 |
| `DciIcon` | DCI 图标组件 |

### Chameleon 样式模块

| 属性 | 内容 |
|------|------|
| 模块 | `Chameleon` |
| 类型 | QtQuick.Controls 样式插件 |
| 安装路径 | `${CMAKE_INSTALL_LIBDIR}/qt6/plugins/styles/` |

通过 `D.ApplicationWindow` 或设置 `QML import Chameleon` 自动启用。

### QML 使用示例

```qml
import org.deepin.dtk 1.0 as D

D.ApplicationWindow {
    width: 400; height: 300
    visible: true
    D.TitleBar { title: "My App" }
    D.Button {
        anchors.centerIn: parent
        text: "Hello DTK"
    }
}
```

## 8. DBus 接口

不适用（dtkdeclarative 为本地库，不提供 DBus 服务）

## 9. 插件开发

dtkdeclarative 提供样式插件机制。通过 Qt Quick Controls 2 的样式插件系统注册自定义样式：

- 样式插件安装路径：`${CMAKE_INSTALL_LIBDIR}/qt6/plugins/styles/`
- Chameleon 为 DTK 默认样式插件，可通过继承扩展

## C++ 应用启动示例

```cpp
#include <DDeclarative>
DQUICK_USE_NAMESPACE

int main(int argc, char *argv[]) {
    DAppLoader appLoader;
    appLoader.load(QUrl("qrc:/main.qml"));
    return appLoader.exec();
}
```
