# dde-tray-loader

dde-tray-loader 提供一套任务栏托盘插件体系及加载插件的工具，是 DDE 桌面托盘功能的核心组件。

## 项目简介

dde-tray-loader 是 DDE 桌面环境中负责加载和管理托盘插件的框架。它提供插件接口定义、插件加载器和 Wayland 集成，使第三方应用可以通过标准接口将托盘图标集成到 DDE 任务栏中。项目采用 Qt6 + Wayland 技术栈，与 dde-shell 配合工作。

## 模块信息

### 核心目录结构

| 目录 | 职责 |
|------|------|
| `src/loader/` | 插件加载器主程序（`trayplugin-loader`） |
| `src/protocol/` | Wayland 协议实现 |
| `src/tray-wayland-integration/` | Wayland 托盘集成 |
| `interfaces/` | 插件接口定义头文件 |
| `plugins/` | 内置插件实现 |
| `systemd/` | systemd 服务单元文件 |
| `cmake/` | CMake 模块 |
| `tests/` | 单元测试 |
| `debian/` | Debian 打包配置 |

### 插件接口（interfaces/）

- `pluginsiteminterface.h` — 插件项基础接口
- `pluginsiteminterface_v2.h` — 插件项接口 V2
- `pluginsiteminterface_v3.h` — 插件项接口 V3
- `pluginmanagerinterface.h` — 插件管理器接口
- `pluginproxyinterface.h` — 插件代理接口
- `common.h` / `constants.h` — 公共定义和常量

### 内置插件（plugins/）

- **application-tray** — 应用托盘插件
- **dde-dock** — Dock 集成插件
- **dde-network-display-ui** — 网络显示 UI 插件
- **libdbusmenuqt** — DBus 菜单 Qt 封装库

## 功能说明

- 插件化托盘体系：通过标准接口加载和管理托盘插件
- Wayland 集成：支持 Wayland 协议下的托盘功能
- systemd 服务管理：通过 `dde-tray-loader.target` 管理插件生命周期
- 分组加载：支持按 group 分组并行加载插件实例
- 多版本接口兼容：提供 V1/V2/V3 三个版本的插件接口

## 构建方式

```bash
cmake -B build
cmake --build build

# 安装
cmake --install build

# 构建 Debian 包
sudo apt build-dep .
dpkg-buildpackage -uc -us -nc -b
```

构建产物：`build/src/loader/trayplugin-loader`

运行方式：`trayplugin-loader -p /path/to/plugin.so`（加载单个插件）
或：`trayplugin-loader --group <group>`（按分组加载）

## 依赖关系

### 构建依赖

- CMake >= 3.16
- Qt6（base, wayland, declarative）
- DTK6（core, gui）
- extra-cmake-modules
- dde-tray-loader-dev, libdde-shell-dev
- libxcb 系列

### 运行时依赖

- Qt6 运行时
- DTK6 运行时
- dde-shell（Dock 合成器）
- systemd（服务管理）

## 文档维护说明

### 现有文档

- `README.md` — 项目说明（含托盘生命周期说明）
- `LICENSE` — GPL-3.0-or-later 许可协议
- 无独立 `docs/` 目录

### 维护方式

- 项目说明在 `README.md` 中维护，包含构建说明和托盘生命周期描述
- 插件接口文档通过头文件注释维护
- 无 GitHub Pages 或 Wiki
