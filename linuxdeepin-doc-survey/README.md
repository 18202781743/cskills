# linuxdeepin 项目文档调研报告

## 一、调研概述

本报告对 github.com/linuxdeepin 组织下 35 个 DDE（Deepin Desktop Environment）相关仓库的文档情况进行了系统性调研。每个仓库均通过实际 checkout 源码确认其文档结构，确保数据准确性。

## 二、调研方法

1. **仓库范围：** 覆盖 DDE 桌面环境相关核心仓库共 35 个，按功能分为 6 大类
2. **数据采集方式：** 逐个 `git clone --depth 1` 获取仓库源码，检查以下文档要素：
   - README 文件（英文 / 中文）
   - `docs/` 目录及其内容
   - 文档构建方式（Doxygen/CMake、Markdown、无）
   - CHANGELOG 变更日志
   - CI/CD 工作流配置（`.github/workflows/`）
   - 文档部署工作流（`call-deploy-dev-doc.yml`）
   - GitHub Pages / Wiki 启用情况
   - `.github/` 下的其他 Markdown 文件
3. **调研时间：** 2026 年 10 月

## 三、统计摘要

| 指标 | 数量 | 占比 |
|---|---|---|
| 调研仓库总数 | 35 | 100% |
| 有 README（英文） | 35 | 100% |
| 有 README（中文） | 35 | 100% |
| 有 docs/ 目录 | 15 | 42.9% |
| 有 Doxygen/CMake 文档构建 | 7 | 20.0% |
| 有 CHANGELOG | 16 | 45.7% |
| 有 CI/CD 工作流 | 35 | 100% |
| 有文档部署工作流（Dev-Doc） | 7 | 20.0% |
| 启用 GitHub Pages | 0 | 0% |
| 启用 GitHub Wiki | 0 | 0% |
| 有 .github/*.md 文件 | 4 | 11.4% |

### 文档构建方式分布

| 构建方式 | 仓库数 | 仓库列表 |
|---|---|---|
| Doxygen/CMake | 7 | dde-control-center、dtkcore、dtkgui、dtkwidget、dtkdeclarative、dtksystemsettings、dtklog(仅部署) |
| Markdown | 8 | ddm、treeland、dde-session、dde-session-shell、dde-shell、dde-launchpad、dde-daemon、dde-application-manager、go-dbus-factory |
| 无（仅 README） | 20 | 其余仓库 |

### 文档部署（Dev-Doc）情况

以下 7 个仓库配置了 `call-deploy-dev-doc.yml` 工作流，在 push 到 master 时通过 GitHub Actions 自动构建并部署文档：

| 仓库 | 文档构建方式 | 部署触发 |
|---|---|---|
| dde-control-center | Doxygen/CMake | push to master / workflow_dispatch |
| dtkcore | Doxygen/CMake | push to master / workflow_dispatch |
| dtkgui | Doxygen/CMake | push to master / workflow_dispatch |
| dtkwidget | Doxygen/CMake | push to master / workflow_dispatch |
| dtkdeclarative | Doxygen/CMake | push to master / workflow_dispatch |
| dtksystemsettings | Doxygen/CMake | push to master / workflow_dispatch |
| dtklog | 无(仅部署) | push to master / workflow_dispatch |

> 注：部署工作流调用 `linuxdeepin/.github/.github/workflows/deploy-dev-doc.yml@master`，具备 `pages: write` 和 `id-token: write` 权限，但当前仓库均未在 GitHub Settings 中启用 Pages。

## 四、分类索引

### 1. 运行环境（2 个仓库）
- [ddm](https://github.com/linuxdeepin/ddm) — DDE 显示管理器（SDDM fork）
- [treeland](https://github.com/linuxdeepin/treeland) — Wayland 合成器（Treeland 生态，非 DDE 项目范围）

### 2. Session 管理（2 个仓库）
- [dde-session](https://github.com/linuxdeepin/dde-session) — DDE 会话启动管理
- [dde-session-shell](https://github.com/linuxdeepin/dde-session-shell) — DDE 锁屏与登录界面

### 3. 核心桌面前端组件（10 个仓库）
- [dde-shell](https://github.com/linuxdeepin/dde-shell) — DDE Shell 插件系统
- [dde-tray-loader](https://github.com/linuxdeepin/dde-tray-loader) — 托盘插件加载器
- [dde-clipboard](https://github.com/linuxdeepin/dde-clipboard) — 剪贴板管理组件
- [dde-launchpad](https://github.com/linuxdeepin/dde-launchpad) — 启动器
- [dde-control-center](https://github.com/linuxdeepin/dde-control-center) — 控制中心
- [dde-network-core](https://github.com/linuxdeepin/dde-network-core) — 网络库框架
- [dde-session-ui](https://github.com/linuxdeepin/dde-session-ui) — 通用 UI 组件
- [dde-polkit-agent](https://github.com/linuxdeepin/dde-polkit-agent) — Polkit 认证代理
- [deepin-update-ui](https://github.com/linuxdeepin/deepin-update-ui) — 更新 UI 组件
- [deepin-screensaver](https://github.com/linuxdeepin/deepin-screensaver) — 屏保服务

### 4. 核心后端组件（9 个仓库）
- [dde-services](https://github.com/linuxdeepin/dde-services) — DBus 服务管理
- [dde-daemon](https://github.com/linuxdeepin/dde-daemon) — DDE 会话设置守护进程
- [dde-api](https://github.com/linuxdeepin/dde-api) — DDE DBus 接口库
- [go-dbus-factory](https://github.com/linuxdeepin/go-dbus-factory) — Go DBus 绑定生成
- [go-lib](https://github.com/linuxdeepin/go-lib) — Go 工具库
- [dde-application-manager](https://github.com/linuxdeepin/dde-application-manager) — 应用管理器
- [xdg-desktop-portal-dde](https://github.com/linuxdeepin/xdg-desktop-portal-dde) — XDG Portal DDE 后端
- [dde-app-services](https://github.com/linuxdeepin/dde-app-services) — 应用服务集合（含 dconfig-center）
- [dde-appearance](https://github.com/linuxdeepin/dde-appearance) — 主题与外观设置后端

### 5. DTK 开发套件（9 个仓库）
- [dtkcommon](https://github.com/linuxdeepin/dtkcommon) — DTK 公共资源（CMake 模块、配置）
- [dtkcore](https://github.com/linuxdeepin/dtkcore) — DTK 核心库
- [dtkgui](https://github.com/linuxdeepin/dtkgui) — DTK GUI 层
- [dtkwidget](https://github.com/linuxdeepin/dtkwidget) — DTK Widget 控件库
- [dtkdeclarative](https://github.com/linuxdeepin/dtkdeclarative) — DTK QML 声明式控件库
- [dtklog](https://github.com/linuxdeepin/dtklog) — DTK 日志库（已废弃，功能合并至 dtkcore）
- [dtksystemsettings](https://github.com/linuxdeepin/dtksystemsettings) — DTK 系统设置库
- [dde-qtintegration](https://github.com/linuxdeepin/dde-qtintegration) — DTK 风格集成插件
- [dde-qtplatform-plugins](https://github.com/linuxdeepin/dde-qtplatform-plugins) — DTK Qt 平台插件（QPA）

### 6. DDE 资源（3 个仓库）
- [deepin-icon-theme](https://github.com/linuxdeepin/deepin-icon-theme) — 图标主题
- [deepin-desktop-theme](https://github.com/linuxdeepin/deepin-desktop-theme) — DCI 桌面主题
- [dde-manual-content](https://github.com/linuxdeepin/dde-manual-content) — 帮助手册内容

> 注：uos-license-content 仓库在 github.com/linuxdeepin 上未找到（可能仅存在于 Gerrit），未纳入本次调研。

## 五、文档维护方式总结

所有 35 个仓库的文档均采用**随源码同仓库维护**的方式，无独立文档仓库。具体模式如下：

1. **README 驱动型（20 个仓库）：** 仅维护 README.md（英文）和 README.zh_CN.md（中文），无独立 docs/ 目录
2. **docs/ 目录型（8 个仓库）：** 在仓库根目录下维护 `docs/` 目录，存放 Markdown 格式的技术文档，无自动化构建
3. **Doxygen/CMake 型（7 个仓库）：** 在 `docs/` 下维护 Doxygen 格式（`.dox`）的 API 文档，通过 `docs/CMakeLists.txt` 配置 CMake + Doxygen 构建，部分仓库配置了 CI 自动部署工作流

## 六、产物结构

```
linuxdeepin-doc-survey/
├── README.md              # 本文件 — 总览、调研说明、统计摘要、分类索引
├── survey-data.md         # 结构化表格（每仓库一行）
└── repos/                 # 按分类的详细文档
    ├── runtime.md         # 运行环境（ddm、treeland）
    ├── session.md         # Session 管理（dde-session、dde-session-shell）
    ├── frontend.md        # 前端组件（10 个仓库）
    ├── backend.md         # 后端组件（9 个仓库）
    ├── dtk.md             # DTK 套件（9 个仓库）
    └── resources.md       # DDE 资源（3 个仓库）
```

## 七、关键发现

1. **README 覆盖率 100%：** 所有仓库均有中英文 README，文档基础良好
2. **Doxygen 文档集中在 DTK 套件：** 7 个使用 Doxygen/CMake 构建的仓库中，6 个属于 DTK 套件，1 个为 dde-control-center
3. **GitHub Pages/Wiki 均未启用：** 虽然有 7 个仓库配置了文档部署工作流，但 GitHub Pages 和 Wiki 功能均未实际启用
4. **CHANGELOG 覆盖率约 46%：** 约一半仓库维护 CHANGELOG，主要集中在 DTK 套件和后端组件
5. **CI/CD 覆盖率 100%：** 所有仓库均配置了 GitHub Actions 工作流，但工作流内容以构建、检查、备份为主
6. **文档构建工具单一：** 仅使用 Doxygen + CMake 作为文档构建工具，无 Sphinx、MkDocs 等其他文档工具
7. **dtklog 已废弃：** 日志功能已合并至 dtkcore，dtklog 不再独立维护，但仍保留文档部署工作流
