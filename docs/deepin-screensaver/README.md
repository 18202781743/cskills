# deepin-screensaver

Deepin 屏保是 DDE 桌面环境自主研发的屏保服务，提供屏幕保护和屏保设置功能。

## 项目简介

deepin-screensaver 是 DDE 桌面的屏幕保护程序，支持自定义屏保图片、xscreensaver 兼容、DBus 控制等功能。项目采用 Qt6 + CMake 技术栈（兼容 Qt5），提供屏保窗口、设置对话框和预览工具。

## 模块信息

### 核心目录结构

| 目录 | 职责 |
|------|------|
| `src/` | 屏保主程序源码（屏保窗口、DBus 服务、配置管理、图片提供器） |
| `src/configs/` | 配置定义 |
| `customscreensaver/` | 自定义屏保模块 |
| `xscreensaver/` | xscreensaver 兼容模块 |
| `tools/` | 工具程序（屏保预览） |
| `cmake/` | CMake 模块（翻译生成等） |
| `debian/` | Debian 打包配置 |
| `rpm/` | RPM 打包配置 |

## 功能说明

- 屏保显示：全屏显示屏保图片或动画
- 自定义屏保：支持用户自定义屏保图片
- xscreensaver 兼容：集成 xscreensaver 屏保
- DBus 服务：通过 DBus 提供屏保控制接口（`com.deepin.ScreenSaver`）
- 屏保设置：提供屏保设置对话框
- 预览工具：提供屏保预览功能
- 多语言支持：支持多语言翻译

## 构建方式

```bash
cd deepin-screensaver
mkdir Build
cd Build
cmake ..
make

# 安装
sudo make install

# 构建 Debian 包
sudo apt build-dep deepin-screensaver
dpkg-buildpackage -uc -us -nc -b
```

安装路径：
- 库文件：`${CMAKE_INSTALL_PREFIX}/lib/deepin-screensaver/`
- 模块文件：`${LIB_PATH}/modules/`
- 资源文件：`${LIB_PATH}/resources/`

## 依赖关系

### 构建依赖

- CMake >= 3.14
- Qt6（base, declarative, tools, 5compat）或 Qt5
- DTK6（core, gui, widget）或 DTK5
- xscreensaver, xscreensaver-data（运行时）
- libx11, libxss, libxext

### 运行时依赖

- Qt6 运行时
- DTK6 运行时
- xscreensaver（xscreensaver 兼容模式）
- startdde（会话启动）

## 文档维护说明

### 现有文档

- `README.md` — 项目说明（含依赖、构建、安装说明）
- `LICENSE` — GPL-3.0-or-later 许可协议
- 无独立 `docs/` 目录

### 维护方式

- 项目说明在 README 中维护
- 无 GitHub Pages 或 Wiki
- 文档以 Markdown 形式在仓库内维护
