# dtkwidget 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | libdtkwidget-dev / libdtk6widget-dev |
| 版本 | 6.7.50 |
| 描述 | DTK Widget 控件库，提供完整的 DDE 风格 Widget 控件集，包括窗口、按钮、输入框、对话框等 |
| CMake target | `Dtk::Widget`（DTK5）/ `Dtk6::Widget`（DTK6） |
| find_package 名 | `DtkWidget`（DTK5）/ `Dtk6Widget`（DTK6） |
| 头文件安装路径 | `${CMAKE_INSTALL_INCLUDEDIR}/dtk6/DWidget`（DTK6）/ `${CMAKE_INSTALL_INCLUDEDIR}/dtk/DWidget`（DTK5） |
| 库文件 | `libdtk6widget.so`（DTK6）/ `libdtkwidget.so`（DTK5） |
| 仓库地址 | https://github.com/linuxdeepin/dtkwidget.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6widgets6 (>= 6.x)
- libdtk6core (>= 6.7.50)
- libdtk6gui (>= 6.7.50)

### 开发依赖
- Qt 6 Core, Qt 6 Gui, Qt 6 Widgets (>= 6.x)
- dtkcore (>= 6.7.50)
- dtkgui (>= 6.7.50)
- CMake >= 3.13

## 3. CMake 集成

### find_package 用法

```cmake
find_package(Dtk6Widget REQUIRED)
target_link_libraries(your-target PRIVATE Dtk6::Widget)
```

### 安装的 CMake 配置文件

- `${CMAKE_INSTALL_LIBDIR}/cmake/Dtk6Widget/Dtk6WidgetConfig.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/Dtk6Widget/Dtk6WidgetConfigVersion.cmake`

## 4. pkg-config

| .pc 文件 | 内容 |
|----------|------|
| `dtk6widget.pc` | Libs: -ldtk6widget，Cflags: -I.../dtk6/DWidget |
| `dtkwidget.pc` | Libs: -ldtkwidget，Cflags: -I.../dtk/DWidget |

```bash
pkg-config --cflags --libs dtk6widget
```

## 5. 命名空间

`Dtk::Widget`（通过 `DWIDGET_USE_NAMESPACE` 宏引入）

```cpp
#include <DWidget>
DWIDGET_USE_NAMESPACE
```

## 6. 关键公共类及功能描述

| 类名 | 功能 | 关键方法 |
|------|------|----------|
| `DApplication` | DTK 应用基类 | `loadDXcbEventTranslator()`, `setProductIcon()`, `setApplicationVersion()` |
| `DMainWindow` | DTK 主窗口，支持圆角、无标题栏模式 | `setFrameFlags()`, `titlebar()` |
| `DPushButton` | DTK 按钮 | `setText()`, `click()` |
| `DLineEdit` | DTK 输入框 | `setText()`, `setAlert()`, `text()` |
| `DIconButton` | 图标按钮 | `setIcon()`, `setIconSize()` |
| `DFileDialog` | DTK 文件对话框 | `getOpenFileName()`, `getSaveFileName()` |
| `DToast` | Toast 提示 | `setText()`, `show()` |
| `DSpinner` | 加载动画 | `start()`, `stop()` |
| `DSwitchButton` | 开关按钮 | `setChecked()`, `checked()` |
| `DWaterProgress` | 水滴进度条 | `start()`, `stop()`, `setValue()` |
| `DCrumbEdit` | 面包屑编辑器 | `insertCrumb()`, `removeCrumb()` |
| `DAnchors` | QML 风格锚点布局 | `setLeft()`, `setFill()`, `setCenterIn()` |
| `DListView` | DTK 列表视图 | `setModel()`, `currentIndex()` |
| `DMenu` | DTK 菜单 | `addAction()`, `exec()` |
| `DMessageManager` | 消息管理器（内嵌提示） | `sendMessage()`, `instance()` |
| `DTitlebar` | 标题栏 | `setMenu()`, `addWidget()`, `setIcon()` |
| `DFrame` | DTK 框架容器 | `setFrameRoundedRadius()` |
| `DGroupBox` | DTK 分组框 | `setTitle()` |
| `DTabBar` | DTK 标签栏 | `addTab()`, `currentChanged()` |
| `DScrollBar` | DTK 滚动条 | `setValue()`, `value()` |

## 7. QML 模块

不适用（dtkwidget 为 C++ Widget 库，QML 支持由 dtkdeclarative 提供）

## 8. DBus 接口

不适用（dtkwidget 为本地库，不提供 DBus 服务）

## 9. 插件开发

不适用（dtkwidget 不提供插件开发接口）
