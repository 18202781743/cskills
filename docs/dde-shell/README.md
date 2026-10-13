# dde-shell

DDE Shell 是 Deepin 桌面环境的 shell 框架，提供一套插件体系，将基于此体系开发的插件整合到 DDE 桌面，实现面板（Panel）和小程序（Applet）的动态加载与管理。

## 项目简介

dde-shell 是 DDE 桌面的核心 shell 组件，负责管理桌面上的面板（如任务栏 Dock、通知面板）和各类小程序（如应用启动器、关机模块、外观设置等）。项目采用 Qt6 + QML 技术栈，支持 Wayland 和 X11 两种显示协议，通过插件机制实现模块化扩展。

## 模块信息

### 核心目录结构

| 目录 | 职责 |
|------|------|
| `shell/` | Shell 主程序入口，负责加载面板和小程序配置、初始化运行环境 |
| `frame/` | 框架核心，提供 Applet、Panel、Plugin、Containment 等基础抽象类和加载机制 |
| `panels/` | 面板实现，包含 Dock（任务栏）和 Notification（通知面板） |
| `applets/` | 小程序实现，包含多个功能模块 |
| `example/` | 示例插件，用于演示插件开发 |
| `tests/` | 单元测试 |
| `docs/` | 插件开发文档（API 文档和教程） |
| `cmake/` | CMake 模块和宏定义 |
| `debian/` | Debian 打包配置 |

### 面板模块（panels/）

- **dock** — 任务栏面板，包含应用停靠、多任务视图、窗口管理等功能
- **notification** — 通知中心面板

### 小程序模块（applets/）

- **dde-am** — 应用管理小程序
- **dde-appearance** — 外观设置小程序
- **dde-apps** — 应用列表小程序，管理应用图标、分组、启动次数等
- **dde-key-notify** — 按键通知小程序
- **dde-shutdown** — 关机/重启小程序

## 功能说明

- 插件化架构：支持通过 C++ 插件和 QML 包两种方式扩展面板和小程序
- 多面板管理：Dock 任务栏和通知面板，支持位置、大小等配置
- Wayland/X11 双协议支持：通过 Layer Shell 协议在 Wayland 下实现面板窗口
- DConfig 配置管理：基于 DTK DConfig 实现面板和小程序的配置持久化
- QML 引擎集成：支持 QML 动态加载小程序 UI，提供自定义 QML 引擎
- 主题与国际化：支持 DTK 主题和多语言翻译

## 构建方式

```bash
# 标准 CMake 构建
cmake -B build
cmake --build build

# 安装
cmake --install build

# 构建 Debian 包
sudo apt build-dep .
dpkg-buildpackage -uc -us -nc -b
```

构建选项：
- `BUILD_WITH_X11` — 是否构建 X11 支持（默认 ON）
- `DS_BUILD_WITH_QT6` — 使用 Qt6 构建（默认 ON）

## 依赖关系

### 构建依赖

- CMake >= 3.16
- Qt6（Core, Gui, Concurrent, Quick, WaylandClient, WaylandCompositor, DBus, Sql, LinguistTools）
- DTK6（Core, Gui, Declarative, Widget）
- extra-cmake-modules
- dde-application-manager-api, dde-api-dev, dde-tray-loader-dev
- libxcb 系列（ewmh, icccm, res, util, shape）
- libyaml-cpp-dev, libgtest-dev, libgmock-dev

### 运行时依赖

- Qt6 运行时
- DTK6 运行时
- Wayland 合成器（如 Treeland）或 X11
- dde-application-manager

## 文档维护说明

### 现有文档

- `README.md` / `README.zh_CN.md` — 项目说明（英文/中文）
- `docs/plugin/` — 插件开发文档，包含：
  - `tutorial_zh_CN.md` / `tutorial_en.md` — 插件开发教程（中英文）
  - `API_zh_CN.md` / `API_en.md` — 插件 API 文档（中英文）
  - `README.md` / `README_zh_CN.md` — 插件文档说明
- `LICENSE` — GPL-3.0-or-later 许可协议

### 维护方式

- 插件开发文档存放在 `docs/plugin/` 目录，随源码维护
- 无 GitHub Pages 或 Wiki，文档以 Markdown 形式在仓库内维护
- 变更日志通过 Git 提交记录管理，无独立 CHANGELOG.md
