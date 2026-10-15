# dde-session-ui

DDE 会话 UI 组件集合，包含锁屏、关机、登录界面、OSD 等多个 DDE 桌面会话相关的 UI 组件。

## 项目简介

dde-session-ui 是 DDE 桌面会话期间各类 UI 界面的集合项目，涵盖锁屏、关机、登录、OSD 提示、低电量提醒、欢迎界面等多个子项目。项目采用 Qt6 + CMake 技术栈，与 lightdm 显示管理器和 DDE 会话管理紧密配合。

## 模块信息

### 核心目录结构

| 目录 | 职责 |
|------|------|
| `dde-shutdown/` | 关机界面 |
| `dde-lock/` | 锁屏界面（在 dde-session-shell 中） |
| `dde-osd/` | 屏幕叠加显示界面（音量、亮度等提示） |
| `dde-lowpower/` | 低电量提醒界面 |
| `dde-welcome/` | 欢迎界面 |
| `dde-wm-chooser/` | 窗口管理器选择器 |
| `dde-switchtogreeter/` | 切换用户登录工具 |
| `dde-blackwidget/` | 黑屏组件 |
| `dde-bluetooth-dialog/` | 蓝牙对话框 |
| `dde-hints-dialog/` | 提示对话框 |
| `dde-license-dialog/` | 许可证对话框 |
| `dde-pixmix/` | 图片混合工具 |
| `dde-suspend-dialog/` | 挂起对话框 |
| `dde-touchscreen-dialog/` | 触摸屏对话框 |
| `dde-warning-dialog/` | 警告对话框 |
| `deepin-login-reminder/` | 登录提醒 |
| `reset-password-dialog/` | 重置密码对话框 |
| `dmemory-warning-dialog/` | 内存警告对话框 |
| `common/` | 公共组件 |
| `widgets/` | 通用 Widget 组件 |
| `global_util/` | 全局工具 |
| `translations/` | 翻译文件 |

## 功能说明

- 关机界面：提供关机、重启、休眠等操作界面
- OSD 显示：音量、亮度、键盘背光等屏幕叠加提示
- 低电量提醒：电池电量低时弹出提醒
- 登录相关：切换用户、登录提醒等
- 对话框组件：蓝牙配对、许可证、警告等多种对话框
- 欢迎界面：首次使用欢迎向导
- 通用 Widget：可复用的 UI 组件库

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
- `DISABLE_SYS_UPDATE` — 禁用系统更新功能（默认 OFF）
- `ENABLE_MIEEE` — 启用 MIPS IEEE 浮点支持

## 依赖关系

### 构建依赖

- CMake >= 3.13
- Qt6（base, svg, tools, declarative）
- DTK6（core, gui, widget）
- libxcb（ewmh, util, shape）, libx11, libxtst
- extra-cmake-modules, pkg-config

### 运行时依赖

- Qt6 运行时
- DTK6 运行时
- lightdm（登录管理器）
- dde-session-shell（锁屏）
- dde-daemon（后端服务）

## 文档维护说明

### 现有文档

- `README.md` / `README.zh_CN.md` — 项目说明（英文/中文）
- `CHANGELOG.md` — 变更日志
- `LICENSE` — GPL-3.0-or-later 许可协议
- 无独立 `docs/` 目录

### 维护方式

- 项目说明在 README 中维护，包含各子项目说明
- 变更日志通过 `CHANGELOG.md` 维护
- 无 GitHub Pages 或 Wiki
