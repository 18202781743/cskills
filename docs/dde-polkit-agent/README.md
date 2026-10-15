# dde-polkit-agent

DDE Polkit Agent 是 polkit（PolicyKit）在 Deepin 桌面环境上的认证代理。

## 项目简介

dde-polkit-agent 是 DDE 桌面的权限认证代理组件，负责在用户执行需要提权的操作时弹出认证对话框，输入密码进行身份验证。它是 polkit 框架的前端代理，通过 polkit-qt 与 polkit 后端通信，采用 Qt6 + CMake 技术栈构建。

## 模块信息

### 核心目录结构

| 目录 | 职责 |
|------|------|
| `src/` 或根目录源码 | Polkit Agent 主程序（认证对话框、代理逻辑） |
| `dbus/` | DBus 接口定义 |
| `images/` | 图标和图片资源 |
| `translations/` | 翻译文件 |
| `tests/` | 单元测试 |
| `debian/` | Debian 打包配置 |
| `rpm/` | RPM 打包配置 |

## 功能说明

- 权限认证代理：作为 polkit 的前端代理，处理权限认证请求
- 认证对话框：提供密码输入界面，支持指纹等多种认证方式
- DBus 通信：通过 DBus 与 polkit 后端交互
- 多语言支持：支持多语言翻译
- Deepin Polkit 集成：可选启用 Deepin 定制 polkit 支持

## 构建方式

```bash
mkdir build
cd build
cmake ..
make

# 安装
sudo make install

# 构建 Debian 包
sudo apt build-dep dde-polkit-agent
dpkg-buildpackage -uc -us -nc -b
```

构建选项：
- `USE_DEEPIN_POLKIT` — 启用 Deepin 定制 polkit（默认 OFF）

## 依赖关系

### 构建依赖

- CMake >= 3.16
- Qt6（base, tools, declarative）
- DTK6（core, gui, widget）
- libpolkit-qt6-1-dev
- extra-cmake-modules, pkg-config

### 运行时依赖

- Qt6 运行时
- DTK6 运行时
- polkitd（polkit 守护进程）
- libpolkit-qt6-1

## 文档维护说明

### 现有文档

- `README.md` — 项目说明（含构建、安装、帮助信息）
- `CHANGELOG.md` — 变更日志
- `LICENSE` — GPL-3.0-or-later 许可协议
- 无独立 `docs/` 目录

### 维护方式

- 项目说明在 README 中维护
- 变更日志通过 `CHANGELOG.md` 维护
- 无 GitHub Pages 或 Wiki
