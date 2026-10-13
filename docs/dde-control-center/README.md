# dde-control-center

DDE 控制中心是 Deepin 桌面环境的系统设置中心，采用插件化架构管理各项系统设置模块。

## 项目简介

dde-control-center 是 DDE 桌面的核心控制面板，负责管理系统设置界面。V25 版本采用全新的插件化架构，控制中心仅负责框架设计，具体功能全部由插件实现。界面使用 QML 实现，插件数据使用 C++ 实现，实现界面与数据的完全解耦。

## 模块信息

### 核心目录结构

| 目录 | 职责 |
|------|------|
| `src/dde-control-center/` | 控制中心主程序框架 |
| `src/plugin-*/` | 各功能插件模块 |
| `src/shared-utils/` | 共享工具库 |
| `include/` | 公共头文件 |
| `docs/` | 接口文档 |
| `examples/` | 插件开发示例 |
| `translations/` | 翻译文件 |
| `tests/` | 单元测试 |
| `debian/` | Debian 打包配置 |

### 插件模块

| 插件 | 功能 |
|------|------|
| `plugin-accounts` | 账户管理 |
| `plugin-authentication` | 认证设置 |
| `plugin-bluetooth` | 蓝牙设置 |
| `plugin-commoninfo` | 通用信息 |
| `plugin-datetime` | 日期和时间 |
| `plugin-deepinid` | Deepin ID 登录 |
| `plugin-defaultapp` | 默认应用 |
| `plugin-display` | 显示设置 |
| `plugin-dock` | 任务栏设置 |
| `plugin-keyboard` | 键盘设置 |
| `plugin-mouse` | 鼠标设置 |
| `plugin-notification` | 通知设置 |
| `plugin-personalization` | 个性化设置 |
| `plugin-power` | 电源管理 |
| `plugin-privacy` | 隐私设置 |
| `plugin-sound` | 声音设置 |
| `plugin-systeminfo` | 系统信息 |
| `plugin-touchscreen` | 触摸屏设置 |
| `plugin-wacom` | 数位板设置 |

## 功能说明

- V25 插件化架构：支持多级插件系统，插件可插入到任意位置
- 精确搜索：更方便、更精确的搜索功能
- 高度可定制：可定制插件是否显示及插件内容是否显示
- QML 界面：更灵活、更易维护的 QML 界面实现
- C++ 数据层：插件数据使用 C++ 实现，高效且与界面解耦
- 多语言支持：插件支持多语言切换
- 统一配置管理：插件显示/禁用支持统一配置，修改立即生效

## 构建方式

```bash
cmake -B build
cmake --build build
sudo make install

# 构建 Debian 包
sudo apt build-dep .
dpkg-buildpackage -uc -us -nc -b
```

构建选项：
- `BUILD_DOCS` — 是否生成 Doxygen 文档（默认 OFF）
- `BUILD_TESTING` — 是否构建单元测试（默认 OFF）
- `BUILD_EXAMPLES` — 是否构建示例（默认 OFF）

运行文件：`/usr/bin/dde-control-center`
插件路径：`${CMAKE_INSTALL_LIBDIR}/dde-control-center/plugins_v1.1/`

## 依赖关系

### 构建依赖

- CMake >= 3.18
- Qt6（base, declarative, tools, svg, wayland）
- DTK6（core, gui, widget, declarative）
- dde-control-center-dev（插件开发依赖）
- extra-cmake-modules, pkg-config

### 运行时依赖

- Qt6 运行时
- DTK6 运行时
- dde-daemon（后端服务）
- dde-appearance

## 文档维护说明

### 现有文档

- `README.md` / `README.zh_CN.md` — 项目说明（英文/中文）
- `docs/v25-dcc-interface.zh_CN.md` — V25 控制中心插件接口文档
- `docs/v23-dcc-interface.zh_CN.md` — V23 控制中心接口文档
- `docs/images/` — 文档图片资源
- `docs/CMakeLists.txt` — Doxygen 文档构建配置
- `LICENSE` — GPL-3.0-or-later 许可协议

### 维护方式

- 接口文档以 Markdown 形式存放在 `docs/` 目录，随源码维护
- 支持 Doxygen 生成 API 文档（通过 `BUILD_DOCS` 选项启用）
- 无 GitHub Pages 或 Wiki
