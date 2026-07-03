# DTK 编译与调试

## 1. DTK5/DTK6 同一套代码

DTK 各项目（dtkcore、dtkgui、dtkwidget、dtkdeclarative、dtklog）以及两个平台插件（qt5integration、qt5platform-plugins）的 DTK5 和 DTK6 是**同一套代码**，通过 CMake option `DTK5` 切换编译目标。修改代码时需**同时保证 DTK5 和 DTK6 都能编译运行**。

`dtkcommon` 是唯一的例外——它不区分 DTK5/DTK6。

### 1.1 版本号规则

除 dtkcommon 外，所有 DTK 项目的版本号**统一相同**，DTK5 和 DTK6 仅第一位不同：

| 项目 | DTK5 版本 | DTK6 版本 |
|------|----------|----------|
| dtkcore | 5.7.44 | 6.7.44 |
| dtkgui | 5.7.44 | 6.7.44 |
| dtkwidget | 5.7.44 | 6.7.44 |
| dtkdeclarative | 5.7.44 | 6.7.44 |
| dtklog | 5.7.44 | 6.7.44 |
| qt5integration | 5.7.44 | 6.7.44 |
| qt5platform-plugins | 5.7.44 | 6.7.44 |

### 1.2 CMake 编译切换

`DTK5` option 控制以下 CMake 变量，决定包名、target 名、库名和安装路径：

| 变量 | DTK5=ON | DTK5=OFF |
|------|---------|----------|
| `DTK_VERSION_MAJOR` | `5` | `6` |
| `DTK_NAME_SUFFIX` | `""`（空） | `"6"` |
| `QT_VERSION_MAJOR` | `5` | `6` |

### 1.3 区分 DTK5/DTK6 代码的方式

**方式一：预处理器宏（C++ 代码中）**

通过 `DTK_VERSION_MAJOR` 或 `QT_VERSION_MAJOR` 宏在 C++ 中条件编译：

```cpp
#if DTK_VERSION_MAJOR == 6
    // DTK6 专有代码
#else
    // DTK5 专有代码
#endif
```

**方式二：目录区分（CMake 中）**

在 CMakeLists.txt 中按版本添加不同的源文件目录。例如 dtkdeclarative 的 DTK6 QML 源码放在独立的 `qt6/src` 目录：

```cmake
if(NOT DTK5)
    add_subdirectory(qt6)
endif()
```

### 1.4 命名对照表

| 维度 | DTK5 | DTK6 |
|------|------|------|
| Qt 版本 | Qt 5 | Qt 6 |
| CMake 包名 | `DtkCore`, `DtkGui`, `DtkWidget` | `Dtk6Core`, `Dtk6Gui`, `Dtk6Widget` |
| CMake target | `Dtk::Core`, `Dtk::Gui`, `Dtk::Widget` | `Dtk6::Core`, `Dtk6::Gui`, `Dtk6::Widget` |
| 库文件名 | `libdtkcore.so.5` | `libdtk6core.so.6` |
| 头文件路径 | `/usr/include/dtk5/DCore/` | `/usr/include/dtk6/DCore/` |
| pkg-config | `dtkcore` | `dtk6core` |

### 1.5 DTK5 与 DTK6 API 差异

DTK6 中已移除的 API（DTK5 仍可用）：`DApplicationHelper`、`DApplicationSettings`、`DThemeManager`、`DImageButton`、`DSegmentedControl`、`DToast`、`DArrowLineExpand`、`DExpandGroup`。

DTK6 移除了 `gsettings-qt` 和 `libxdg` 依赖。

### 1.6 开发原则

- **除了 dtkdeclarative 的 QML 部分只维护 DTK6（DTK5 仅需保证编译通过和运行），其余项目（dtkcore、dtkgui、dtkwidget、dtklog）的 DTK5 和 DTK6 都需要完整支持**
- 新需求/Bug 修复优先保证 DTK6，同时确保 DTK5 也能编译运行并保持功能一致

---

## 2. 安装编译依赖

DTK 项目通过 `debian/control` 声明编译依赖，使用 `apt build-dep` 自动安装，无需手动列出包名。

### 2.1 安装编译依赖

```bash
# 进入目标项目目录
cd <dtk-project-path>

# 自动安装 debian/control 中声明的所有编译依赖
sudo apt build-dep .
```

### 2.2 构建 Profile

DTK 项目通过 debian build profile 控制 DTK5/DTK6 构建：

```bash
# 仅编译 DTK5（跳过 DTK6 包）
dpkg-buildpackage -b -Pnodtk6

# 仅编译 DTK6（跳过 DTK5 包）
dpkg-buildpackage -b -Pnodtk5

# 跳过文档包，加速编译
dpkg-buildpackage -b -Pnodoc

# 组合使用：仅 DTK5 + 跳过文档
dpkg-buildpackage -b -Pnodtk6,nodoc
```

如果只是本地 cmake 编译调试，直接用 `-DDTK5=ON` 或 `-DDTK5=OFF` 即可（见第 4 节）。

---

## 3. 项目 CMake 配置

### 3.1 标准 CMakeLists.txt 模板

#### DTK5

```cmake
cmake_minimum_required(VERSION 3.13)
project(myapp VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Qt5 REQUIRED COMPONENTS Core Widgets)
find_package(DtkCore REQUIRED)
find_package(DtkGui REQUIRED)
find_package(DtkWidget REQUIRED)

add_executable(myapp
    main.cpp
    mainwindow.cpp
)

target_link_libraries(myapp PRIVATE
    Qt5::Core
    Qt5::Widgets
    Dtk::Core
    Dtk::Gui
    Dtk::Widget
)
```

#### DTK6

```cmake
cmake_minimum_required(VERSION 3.13)
project(myapp VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Qt6 REQUIRED COMPONENTS Core Widgets)
find_package(Dtk6Core REQUIRED)
find_package(Dtk6Gui REQUIRED)
find_package(Dtk6Widget REQUIRED)

add_executable(myapp
    main.cpp
    mainwindow.cpp
)

target_link_libraries(myapp PRIVATE
    Qt6::Core
    Qt6::Widgets
    Dtk6::Core
    Dtk6::Gui
    Dtk6::Widget
)
```

### 3.2 同时兼容 DTK5 和 DTK6

```cmake
cmake_minimum_required(VERSION 3.13)
project(myapp VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# 自动检测 Qt 版本
find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Core)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Core Widgets)

# 根据 Qt 版本决定 DTK 后缀
if(QT_VERSION_MAJOR EQUAL 6)
    set(DTK_SUFFIX 6)
else()
    set(DTK_SUFFIX "")
endif()

find_package(Dtk${DTK_SUFFIX}Core REQUIRED)
find_package(Dtk${DTK_SUFFIX}Gui REQUIRED)
find_package(Dtk${DTK_SUFFIX}Widget REQUIRED)

add_executable(myapp
    main.cpp
    mainwindow.cpp
)

target_link_libraries(myapp PRIVATE
    Qt${QT_VERSION_MAJOR}::Core
    Qt${QT_VERSION_MAJOR}::Widgets
    Dtk${DTK_SUFFIX}::Core
    Dtk${DTK_SUFFIX}::Gui
    Dtk${DTK_SUFFIX}::Widget
)
```

### 3.3 使用元包简写

如果已安装 dtkcommon 提供的 `DtkConfig.cmake` 或 `Dtk6Config.cmake`，可用元包一次性引用所有模块：

```cmake
# DTK5 元包
find_package(Dtk REQUIRED COMPONENTS Core Gui Widget)

# DTK6 元包
find_package(Dtk6 REQUIRED COMPONENTS Core Gui Widget)
```

### 3.4 CMake 编译依赖（模块级）

| 使用场景 | DTK5 CMake 依赖 | DTK6 CMake 依赖 |
|----------|----------------|----------------|
| 图标系统 (DDciIcon/DIconTheme) | `Dtk::Gui` | `Dtk6::Gui` |
| 主题/调色板 (DPalette/DGuiApplicationHelper) | `Dtk::Gui` | `Dtk6::Gui` |
| QWidget 控件 (DDialog/DMainWindow) | `Dtk::Widget` | `Dtk6::Widget` |
| 配置系统 (DConfig/DSettings) | `Dtk::Core` | `Dtk6::Core` |
| 日志系统 (Logger) | `Dtk::Log` | `Dtk6::Log` |
| QML 控件 | `Dtk::Declarative` | `Dtk6::Declarative` |
| 文件操作/DBus/DNotify | `Dtk::Core` | `Dtk6::Core` |

---

## 4. 编译命令

### 4.1 DTK 项目编译

```bash
mkdir -p build && cd build

# 编译 DTK5
cmake .. -DDTK5=ON -DCMAKE_BUILD_TYPE=Debug -DCMAKE_INSTALL_PREFIX=/usr
make -j$(nproc)

# 编译 DTK6
cmake .. -DDTK5=OFF -DCMAKE_BUILD_TYPE=Debug -DCMAKE_INSTALL_PREFIX=/usr
make -j$(nproc)
```

### 4.2 编译选项

| 选项 | 说明 |
|------|------|
| `-DDTK5=ON` / `-DDTK5=OFF` | 切换 DTK5/DTK6 编译目标 |
| `-DCMAKE_BUILD_TYPE=Debug` | Debug 构建，带调试符号，使用 `-O0 -g -fno-omit-frame-pointer` |
| `-DCMAKE_BUILD_TYPE=Release` | Release 构建，DTK 使用 `-Ofast` 替代 `-O3` |
| `-DCMAKE_INSTALL_PREFIX=/usr` | 安装路径，DTK 项目编译时建议指定 |
| `-DENABLE_TESTING=ON` | 启用单元测试编译 |

### 4.3 平台插件

qt5integration 和 qt5platform-plugins 建议直接安装到系统中测试：

```bash
cmake .. -DDTK5=OFF -DCMAKE_BUILD_TYPE=Debug -DCMAKE_INSTALL_PREFIX=/usr
make -j$(nproc)
sudo make install
```

---

## 5. 调试

### 5.1 使用本地编译的库调试

当本地编译了 DTK 项目后，在没有安装到系统的情况下，通过环境变量指向本地 build 目录来调试：

```bash
# 本地编译了 dtkwidget 和 dtkdeclarative，运行使用了它们的应用
LD_LIBRARY_PATH=/path/to/dtkwidget/build6/src \
LD_LIBRARY_PATH=/path/to/dtkdeclarative/build6/qt6/src:$LD_LIBRARY_PATH \
./build6/examples/collections/collections

# 本地编译了 dtkdeclarative，运行 dde-control-center 测试 QML 效果
LD_LIBRARY_PATH=/path/to/dtkdeclarative/build6/qt6/src \
QML_IMPORT_PATH=/path/to/dtkdeclarative/build6/plugins \
dde-control-center -s
```

| 环境变量 | 作用 | 示例值 |
|----------|------|--------|
| `LD_LIBRARY_PATH` | 运行时库搜索路径 | `/path/to/dtkdeclarative/build6/qt6/src` |
| `QML_IMPORT_PATH` | QML 模块搜索路径 | `/path/to/dtkdeclarative/build6/plugins` |

### 5.2 QT 调试变量

| 环境变量 | 作用 | 示例值 |
|----------|------|--------|
| `QT_QPA_PLATFORM` | 指定平台插件 | `dxcb`（X11 深度集成）, `offscreen`（无头测试）, `wayland` |
| `QT_QPA_PLATFORM_PLUGIN_PATH` | 自定义平台插件搜索路径 | `./plugins/platforms` |
| `QT_LOGGING_RULES` | Qt 日志分类过滤 | `qt.qpa.*=true`, `*.debug=false` |

### 5.3 DTK 专用调试变量

| 环境变量 | 作用 | 示例值 |
|----------|------|--------|
| `DTK_DISABLED_LOGGING_RULES` | 禁用 DTK 自动日志规则 | `1`（任意非空值） |
| `DTK_LOGGING_FALLBACK_APPID` | 日志框架回退应用 ID | `myapp` |
| `DTK_FORCE_CONSOLE_LOGGING` | 强制输出日志到控制台 | `1` |
| `DTK_FORCE_RASTER_WIDGETS` | 强制光栅渲染模式 | `1` |
| `DTK_DISABLED_SPECIAL_EFFECTS` | 禁用 DTK 特效 | `1` |
| `D_DTK_DISABLE_ANIMATIONS` | 禁用 DTK 动画 | `1`（任意非空值） |
| `D_DTK_SIZEMODE` | 覆盖 DConfig 尺寸模式设置 | `compact` |
| `DXCB_FAKE_PLATFORM_NAME_XCB` | 使用 DXCB 时设置为 `true` | `true` |
| `DTK_USE_SEMAPHORE_SINGLEINSTANCE` | 用信号量实现单实例（替代 DBus） | `1` |
| `DTK_DBUS_SINGLEINSTANCE` | Flatpak 环境 DBus 单实例兼容 | `1` |
| `DDE_SESSION_PROCESS_COOKIE_ID` | DDE 会话 cookie | DDE 内部使用 |

### 5.4 调试工具变量

| 环境变量 | 作用 | 示例值 |
|----------|------|--------|
| `ASAN_OPTIONS` | AddressSanitizer 选项 | `halt_on_error=0:new_delete_type_mismatch=0` |

### 5.5 调试启动示例

```bash
# 在 X11 下使用本地编译的库调试
LD_LIBRARY_PATH=./build6/src \
QT_QPA_PLATFORM=dxcb \
QT_LOGGING_RULES="*.debug=true" \
D_DTK_DISABLE_ANIMATIONS=1 \
./myapp

# 无图形界面的调试（off-screen）
QT_QPA_PLATFORM=offscreen \
DTK_DISABLED_SPECIAL_EFFECTS=1 \
./myapp

# 使用 ASan 调试
ASAN_OPTIONS="halt_on_error=0:new_delete_type_mismatch=0" \
QT_QPA_PLATFORM=dxcb \
./myapp
```

---

## 6. 头文件引用

### 6.1 标准引用方式

DTK 的公共头文件使用无 `.h` 后缀的转发头，与 CMake target 对应：

```cpp
// 核心模块
#include <DConfig>          // Dtk::Core / Dtk6::Core
#include <DSettings>        // Dtk::Core / Dtk6::Core
#include <DStandardPaths>   // Dtk::Core / Dtk6::Core
#include <DDBusInterface>   // Dtk::Core / Dtk6::Core
#include <DNotifySender>    // Dtk::Core / Dtk6::Core

// GUI 模块
#include <DDciIcon>         // Dtk::Gui  / Dtk6::Gui
#include <DIconTheme>       // Dtk::Gui  / Dtk6::Gui
#include <DPalette>         // Dtk::Gui  / Dtk6::Gui
#include <DGuiApplicationHelper>  // Dtk::Gui / Dtk6::Gui

// Widget 模块
#include <DApplication>     // Dtk::Widget / Dtk6::Widget
#include <DDialog>          // Dtk::Widget / Dtk6::Widget
#include <DMainWindow>      // Dtk::Widget / Dtk6::Widget
#include <DTitlebar>        // Dtk::Widget / Dtk6::Widget
#include <DIconButton>      // Dtk::Widget / Dtk6::Widget
```

### 6.2 日志规范

DTK 应用使用 Qt 自带的日志宏（`qDebug` / `qCInfo` / `qCWarning` 等），不使用 dtklog 的 `dDebug` 宏。dtkcore 提供 `DLogManager` 注册 Appender，应用不需要直接依赖 dtklog。

```cpp
#include <DLogManager>

int main(int argc, char *argv[])
{
    QCoreApplication app(argc, argv);

    // 通过 dtkcore 的 DLogManager 注册日志输出
    DLogManager::instance()->registerConsoleAppender();
    DLogManager::instance()->registerFileAppender("/var/log/myapp.log");

    // 使用 Qt 原生日志
    qInfo() << "应用启动";
    qWarning() << "配置未找到，使用默认值";
    qDebug() << "调试信息";
}
```

CMake 依赖：`Dtk::Core`（DTK5）或 `Dtk6::Core`（DTK6），**不需要** `Dtk::Log`。

---

## 7. 最小可运行示例

### 7.1 日志示例

```cpp
#include <QCoreApplication>
#include <DLogManager>

int main(int argc, char *argv[])
{
    QCoreApplication app(argc, argv);

    DLogManager::instance()->registerConsoleAppender();

    qInfo() << "DTK application started";
    return 0;
}
```

CMake 依赖：`Dtk::Core`（DTK5）或 `Dtk6::Core`（DTK6）。

### 7.2 带图标的窗口双版本

```cpp
#include <DApplication>
#include <DMainWindow>
#include <DTitlebar>
#include <DIconTheme>

int main(int argc, char *argv[])
{
    DApplication app(argc, argv);

    DMainWindow w;
    w.setMinimumSize(800, 600);
    w.titlebar()->setTitle("My DTK App");
    w.titlebar()->setIcon(DIconTheme::findQIcon("deepin"));
    w.show();

    return app.exec();
}
```

CMake 依赖：`Dtk::Gui + Dtk::Widget`（DTK5）或 `Dtk6::Gui + Dtk6::Widget`（DTK6）。

---

## 8. 开发环境初始化检查清单

```bash
# 1. 确认项目源码目录存在
ls <dtk-project-path>

# 2. 安装编译依赖
sudo apt build-dep <dtk-project-path>

# 3. 确认 CMake 能找到 DTK
cmake --find-package -DNAME=DtkCore -DCOMPILER_ID=GNU -DLANGUAGE=C -DMODE=EXIST 2>&1
```
