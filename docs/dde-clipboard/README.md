# dde-clipboard

dde-clipboard 是 DDE 桌面环境的剪贴板管理组件，提供剪贴板历史记录管理和剪贴板内容展示功能。

## 项目简介

dde-clipboard 是一个设计精美、简洁的剪贴板管理组件，为 DDE 桌面提供剪贴板内容的记录、管理和快速访问功能。项目包含剪贴板前端 UI、后台守护进程和 Dock 插件三部分，采用 Qt6 + CMake 技术栈构建。

## 模块信息

### 核心目录结构

| 目录 | 职责 |
|------|------|
| `dde-clipboard/` | 剪贴板前端 UI 组件 |
| `dde-clipboard-daemon/` | 剪贴板后台守护进程 |
| `dock-clipboard-plugin/` | Dock 任务栏剪贴板插件 |
| `dbus/` | DBus 接口定义 |
| `misc/` | 杂项资源文件 |
| `translations/` | 翻译文件 |
| `tests/` | 单元测试 |
| `debian/` | Debian 打包配置 |

## 功能说明

- 剪贴板历史记录：记录用户复制的文本、图片等内容
- 快速访问：通过 Dock 插件快速查看和选择历史剪贴板内容
- 后台守护进程：持续监控剪贴板变化
- DBus 通信：前端 UI 与守护进程通过 DBus 通信
- 多语言支持：支持多语言翻译

## 构建方式

```bash
mkdir build
cd build
cmake ..
make

# 安装
sudo make install

# 构建 Debian 包
sudo apt build-dep .
dpkg-buildpackage -uc -us -nc -b
```

## 依赖关系

### 构建依赖

- CMake
- Qt6（base, declarative, tools）
- DTK6（core, gui, widget）
- extra-cmake-modules, pkg-config

### 运行时依赖

- Qt6 运行时
- DTK6 运行时
- dde-shell（Dock 集成）

## 文档维护说明

### 现有文档

- `README.md` — 项目说明（含构建和安装说明）
- `LICENSE` — GPL-3.0-or-later 许可协议
- 无独立 `docs/` 目录

### 维护方式

- 项目说明在 `README.md` 中维护
- 无 GitHub Pages 或 Wiki
- 文档以 Markdown 形式在仓库内维护
