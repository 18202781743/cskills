# deepin-update-ui

Deepin 系统更新 UI 组件集合，提供 DDE 桌面环境下的系统更新界面和插件。

## 项目简介

deepin-update-ui 是 DDE 桌面的系统更新前端组件项目，包含控制中心更新插件、Dock 更新插件、更新主程序、备份恢复工具等子模块。项目采用 Qt6 + CMake 技术栈，与 lastore-daemon（更新后端服务）配合工作。

## 模块信息

### 核心目录结构

| 目录 | 职责 |
|------|------|
| `src/dde-update/` | 系统更新主程序 |
| `src/dcc-update-plugin/` | 控制中心更新插件 |
| `src/dock-update-plugin/` | Dock 任务栏更新插件 |
| `src/ddock-update-plugin/` | Dock 更新插件（旧版） |
| `src/dde-abrecovery/` | AB 备份恢复工具 |
| `src/private-lastore-tray/` | lastore 托盘私有组件 |
| `src/common/` | 公共组件 |
| `tests/` | 单元测试 |
| `debian/` | Debian 打包配置 |

## 功能说明

- 系统更新界面：提供系统更新检查、下载、安装的 UI 界面
- 控制中心集成：作为控制中心插件提供更新设置入口
- Dock 集成：在任务栏显示更新状态和通知
- AB 备份恢复：支持 A/B 分区备份和恢复
- lastore 集成：与 lastore-daemon 后端服务通信

## 构建方式

```bash
cmake -B build
cmake --build build
sudo make install

# 构建 Debian 包
sudo apt build-dep .
dpkg-buildpackage -uc -us -nc -b
```

## 依赖关系

### 构建依赖

- CMake >= 3.18
- Qt6（base, tools, declarative）
- DTK6（core, gui, widget）
- dde-tray-loader-dev
- dde-control-center-dev (>= 6.1.71)
- extra-cmake-modules, pkg-config

### 运行时依赖

- Qt6 运行时
- DTK6 运行时
- lastore-daemon（更新后端服务）
- dde-control-center
- dde-shell（Dock 集成）

## 文档维护说明

### 现有文档

- `README.md` / `README.zh_CN.md` — 项目说明（英文/中文）
- `LICENSE` — GPL-3.0-or-later 许可协议
- 无独立 `docs/` 目录

### 维护方式

- 项目说明在 README 中维护
- 无 GitHub Pages 或 Wiki
- 文档以 Markdown 形式在仓库内维护
