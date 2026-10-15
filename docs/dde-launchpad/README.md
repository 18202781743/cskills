# dde-launchpad

DDE 启动器是 Deepin 桌面环境的"启动器"（开始菜单）组件，提供应用搜索、分类浏览和启动功能。

## 项目简介

dde-launchpad 是 DDE 桌面的应用启动器，支持全屏和窗口两种模式，提供应用搜索、分类管理、文件夹管理等功能。项目采用 Qt6 + QML 技术栈，通过 AppStreamQt 获取应用信息，支持 DDE Shell 插件集成和 Treeland Wayland 集成。

## 模块信息

### 核心目录结构

| 目录 | 职责 |
|------|------|
| `src/` | C++ 源码，包含模型、工具、集成模块 |
| `src/models/` | 数据模型（应用列表、文件夹等） |
| `src/ddeintegration/` | DDE 集成模块 |
| `src/treelandintegration/` | Treeland Wayland 集成 |
| `src/gioutils/` | GIO 工具库 |
| `src/quick/` | QML 快速组件 |
| `qml/` | QML 界面文件 |
| `shell-launcher-applet/` | DDE Shell 小程序封装 |
| `dbus/` | DBus 接口定义 |
| `docs/` | 项目文档 |
| `systemd/` | systemd 服务文件 |
| `translations/` | 翻译文件 |
| `tests/` | 单元测试 |

## 功能说明

- 全屏/窗口双模式：支持全屏启动器和窗口式启动器
- 应用搜索：支持按名称、分类搜索应用
- 文件夹管理：支持创建和管理应用文件夹
- AppStream 集成：通过 AppStreamQt 获取应用元数据
- DConfig 配置：基于 DTK DConfig 管理可配置项
- DDE Shell 集成：作为 dde-shell 的 applet 运行
- Treeland 集成：支持 Treeland Wayland 合成器
- 多语言支持：支持多语言翻译

## 构建方式

```bash
mkdir build && cd build
cmake ..
cmake --build .

# 安装
cmake --build . --target install

# 构建 Debian 包
sudo apt build-dep .
dpkg-buildpackage -uc -us -nc -b

# 更新翻译
cmake --build . --target update_translations
```

## 依赖关系

### 构建依赖

- CMake >= 3.10
- Qt6（Core, Gui, Concurrent, DBus, Qml, Svg, Quick, QuickControls2, LinguistTools）
- DTK6（Core, Gui）
- AppStreamQt >= 1.0
- DDEShell
- extra-cmake-modules

### 运行时依赖

- Qt6 运行时
- DTK6 运行时
- dde-shell
- dde-app-services（DConfig 服务）
- AppStream

## 文档维护说明

### 现有文档

- `README.md` — 项目说明（含构建和翻译说明）
- `docs/DConfig.md` — DConfig 配置使用说明
- `docs/TODO.md` — 待办事项
- `LICENSE` — GPL-3.0-or-later 许可协议

### 维护方式

- 项目文档存放在 `docs/` 目录
- DConfig 配置文档详细说明了配置文件的使用方式
- 无 GitHub Pages 或 Wiki
