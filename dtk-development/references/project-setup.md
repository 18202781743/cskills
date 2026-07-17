# 项目配置与编译

DTK 应用的 CMake 配置和编译调试方法。

## 触发关键词

CMake、find_package、DTK 项目、编译 DTK、调试 DTK 源码

---

## CMake 配置

### 最小 CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.16)
project(myapp VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

find_package(Dtk6 REQUIRED COMPONENTS Core Gui Widget)

add_executable(myapp
    main.cpp
    mainwindow.cpp
)

target_link_libraries(myapp PRIVATE
    Dtk6::Core
    Dtk6::Gui
    Dtk6::Widget
)

install(TARGETS myapp DESTINATION bin)
```

### 常用模块

| 模块 | 说明 |
|------|------|
| `Dtk6::Core` | 核心工具类、DConfig、日志 |
| `Dtk6::Gui` | 主题、图标、平台抽象 |
| `Dtk6::Widget` | QWidget 控件 |
| `Dtk6::Declarative` | QML 控件 |

---

## 编译 DTK 源码

```bash
# 克隆仓库
git clone https://github.com/linuxdeepin/dtkcore.git
git clone https://github.com/linuxdeepin/dtkgui.git
git clone https://github.com/linuxdeepin/dtkwidget.git

# 编译（以 dtkcore 为例）
cd dtkcore
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Debug ..
make -j$(nproc)
sudo make install
```

### 编译选项

| 选项 | 说明 |
|------|------|
| `-DCMAKE_BUILD_TYPE=Debug` | 调试版本 |
| `-DCMAKE_INSTALL_PREFIX=/usr` | 安装路径 |
| `-DBUILD_EXAMPLES=ON` | 编译示例 |
| `-DBUILD_TESTING=ON` | 编译测试 |

---

## 调试 DTK 应用

### 运行时调试

```bash
# 切换主题
./myapp -style fusion

# 环境变量
QT_LOGGING_RULES="dtk.debug=true" ./myapp
QT_DEBUG_PLUGINS=1 ./myapp
```

### 风格调试

```cpp
qInfo() << "Current style:" << QApplication::style()->objectName();
qInfo() << "Available styles:" << QStyleFactory::keys();
```

---

## 安装文件

```
/usr/bin/myapp
/usr/share/applications/myapp.desktop
/usr/share/icons/hicolor/.../myapp.png
/usr/share/dsg/appid/configs/myapp.json  # DConfig 元数据
```

---

## 相关文档

- [architecture.md](architecture.md) — DTK 架构
- [config-system.md](config-system.md) — DConfig 配置
