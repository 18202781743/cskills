# 核心桌面前端组件类仓库文档调研

## dde-shell

- **仓库地址：** https://github.com/linuxdeepin/dde-shell
- **项目说明：** DDE Shell 插件系统，将基于该插件系统开发的插件集成到 DDE 中
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（6 个文件）
  - `docs/plugin/API_en.md` — 插件 API 文档（英文）
  - `docs/plugin/API_zh_CN.md` — 插件 API 文档（中文）
  - `docs/plugin/README.md` — 插件开发说明（英文）
  - `docs/plugin/README_zh_CN.md` — 插件开发说明（中文）
  - `docs/plugin/tutorial_en.md` — 插件开发教程（英文）
  - `docs/plugin/tutorial_zh_CN.md` — 插件开发教程（中文）
- **文档构建方式：** Markdown（中英文双语文档，无自动化构建）
- **CHANGELOG：** ❌
- **CI/CD 工作流：** 8 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 文档随源码同仓库维护，`docs/plugin/` 下存放完整的插件开发教程和 API 文档（中英文）

## dde-tray-loader

- **仓库地址：** https://github.com/linuxdeepin/dde-tray-loader
- **项目说明：** 托盘插件集及加载器，将插件集成到任务栏
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ❌
- **CI/CD 工作流：** 8 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README，无独立文档目录

## dde-clipboard

- **仓库地址：** https://github.com/linuxdeepin/dde-clipboard
- **项目说明：** DDE 剪贴板管理组件
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ❌
- **CI/CD 工作流：** 9 个（含 cppcheck）
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README

## dde-launchpad

- **仓库地址：** https://github.com/linuxdeepin/dde-launchpad
- **项目说明：** DDE 启动器（"launcher"/"start menu" 组件）
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（2 个文件）
  - `docs/DConfig.md` — DConfig 配置说明
  - `docs/TODO.md` — 待办事项
- **文档构建方式：** Markdown
- **CHANGELOG：** ❌
- **CI/CD 工作流：** 8 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 文档随源码同仓库维护，`docs/` 下存放 DConfig 说明和 TODO

## dde-control-center

- **仓库地址：** https://github.com/linuxdeepin/dde-control-center
- **项目说明：** DDE 控制中心，Deepin 桌面环境的控制面板
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（4 个文件）
  - `docs/CMakeLists.txt` — Doxygen 文档构建配置
  - `docs/v23-dcc-interface.zh_CN.md` — v23 控制中心接口文档（中文）
  - `docs/v25-dcc-interface.zh_CN.md` — v25 控制中心接口文档（中文）
  - `docs/images/plugin-demo.gif` — 插件演示图
- **文档构建方式：** Doxygen/CMake（`docs/CMakeLists.txt` 配置 Doxygen 构建）
- **CHANGELOG：** ❌
- **CI/CD 工作流：** 10 个
- **文档部署（Dev-Doc）：** ✅ `call-deploy-dev-doc.yml`（push to master 时触发，调用 `linuxdeepin/.github/.github/workflows/deploy-dev-doc.yml@master`）
- **GitHub Pages：** ❌（已配置部署工作流，但 Pages 未实际启用）
- **GitHub Wiki：** ❌
- **.github/*.md：** ✅ `copilot-instructions.md`（AI 编码助手指令）
- **文档维护方式：** 文档随源码同仓库维护，`docs/` 下含接口文档（中文），通过 CMake/Doxygen 构建，CI 自动部署

## dde-network-core

- **仓库地址：** https://github.com/linuxdeepin/dde-network-core
- **项目说明：** DDE 网络库框架
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ❌
- **CI/CD 工作流：** 9 个（含 cppcheck）
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README

## dde-session-ui

- **仓库地址：** https://github.com/linuxdeepin/dde-session-ui
- **项目说明：** DDE 通用 UI 组件（含 dde-shutdown 等子项目）
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 9 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ✅ `SUPPORT.md`（支持与反馈指引）
- **文档维护方式：** 仅 README 和 CHANGELOG

## dde-polkit-agent

- **仓库地址：** https://github.com/linuxdeepin/dde-polkit-agent
- **项目说明：** DDE Polkit 认证代理
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 9 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README 和 CHANGELOG

## deepin-update-ui

- **仓库地址：** https://github.com/linuxdeepin/deepin-update-ui
- **项目说明：** DDE 更新 UI 组件
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ❌
- **CI/CD 工作流：** 7 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README，README 中包含开发者贡献指南链接

## deepin-screensaver

- **仓库地址：** https://github.com/linuxdeepin/deepin-screensaver
- **项目说明：** DDE 屏保服务
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 9 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README 和 CHANGELOG
