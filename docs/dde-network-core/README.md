# dde-network-core

DDE 网络核心框架是 DDE/UOS 桌面环境的网络连接框架，提供网络管理 UI、插件和后端服务。

## 项目简介

dde-network-core 是 DDE 桌面的网络管理核心组件，基于 NetworkManager（libnm）实现网络连接管理。项目包含控制中心网络模块、Dock 网络插件、网络对话框、热点管理等多个子模块，采用 Qt6 + CMake 技术栈，通过 DBus 与 NetworkManager 交互。

## 模块信息

### 核心目录结构

| 目录 | 职责 |
|------|------|
| `src/` | 网络核心库源码（网络控制器、设备管理、连接管理等） |
| `src/dbus/` | DBus 接口定义 |
| `src/impl/` | 平台实现 |
| `dcc-network/` | 控制中心网络模块（QML 界面） |
| `dcc-network-plugin/` | 控制中心网络插件 |
| `dock-network-plugin/` | Dock 任务栏网络插件 |
| `dock-hotspot-plugin/` | Dock 热点插件 |
| `common-plugin/` | 公共插件（网络对话框、密钥代理等） |
| `network-service-plugin/` | 网络服务插件 |
| `dss-network-plugin/` | DSS 网络插件 |
| `net-view/` | 网络查看器 |
| `src-old/` | 旧版网络核心代码 |
| `tests/` | 单元测试 |
| `debian/` | Debian 打包配置 |

## 功能说明

- 网络连接管理：有线、无线、VPN 等网络连接的配置和管理
- 网络设备管理：网卡设备的状态监控和管理
- 热点功能：WiFi 热点创建和管理
- 控制中心集成：为控制中心提供网络设置界面
- Dock 集成：为任务栏提供网络状态显示和快捷操作
- 网络对话框：密码输入、网络选择等对话框
- 密钥代理：NetworkManager 密钥代理服务
- 多插件架构：支持控制中心、Dock、DSS 等多个宿主的插件

## 构建方式

```bash
cd dde-network-core
mkdir Build
cd Build
cmake ..
make

# 安装
sudo make install

# 构建 Debian 包
sudo apt build-dep .
dpkg-buildpackage -uc -us -nc -b
```

构建选项：
- `BUILD_TESTS` — 是否构建单元测试（默认 OFF）
- `BUILD_EXAMPLE` — 是否构建示例（默认 OFF）

可执行文件：`/usr/bin/dde-network-dialog`

## 依赖关系

### 构建依赖

- CMake >= 3.23
- Qt6（base, declarative, wayland）
- DTK6（core, gui, widget）
- extra-cmake-modules
- libnm（NetworkManager 开发库）
- glib-2.0, gio-2.0
- WaylandProtocols
- libgtest-dev

### 运行时依赖

- Qt6 运行时
- DTK6 运行时
- NetworkManager
- dde-shell（Dock 集成）
- dde-control-center（控制中心集成）

## 文档维护说明

### 现有文档

- `README.md` / `README.zh_CN.md` — 项目说明（英文/中文）
- `LICENSE` — GPL-3.0-or-later 许可协议
- 无独立 `docs/` 目录

### 维护方式

- 项目说明在 README 中维护，包含构建和安装说明
- 无 GitHub Pages 或 Wiki
- 文档以 Markdown 形式在仓库内维护
