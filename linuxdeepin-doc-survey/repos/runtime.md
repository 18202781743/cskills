# 运行环境类仓库文档调研

## ddm

- **仓库地址：** https://github.com/linuxdeepin/ddm
- **项目说明：** DDE 显示管理器，基于 SDDM fork，使用 Treeland 作为 greeter
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（2 个文件）
  - `docs/ARCHITECTURE.md` — 架构说明文档
  - `docs/THEMING.md` — 主题开发文档
- **文档构建方式：** Markdown（纯 Markdown 文档，无自动化构建）
- **CHANGELOG：** ❌
- **CI/CD 工作流：** 10 个（含 backup-to-gitlab、call-auto-tag、call-build-distribution、call-chatOps、call-clacheck、call-commitlint、call-license-check、call-update-changelog 等）
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ✅ `copilot-instructions.md`（AI 编码助手指令）
- **文档维护方式：** 文档随源码同仓库维护，`docs/` 下存放架构与主题文档

## treeland

- **仓库地址：** https://github.com/linuxdeepin/treeland
- **项目说明：** Wayland 合成器，基于 wlroots 和 QtQuick（**Treeland 生态，非 DDE 项目范围**）
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（1 个文件）
  - `docs/liquid-glass-dispersion.md` — 液态玻璃分散效果文档
- **文档构建方式：** Markdown
- **CHANGELOG：** ❌
- **CI/CD 工作流：** 13 个（含 treeland-archlinux-build、treeland-deepin-build、waylib 系列构建工作流等）
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ✅ `copilot-instructions.md`
- **文档维护方式：** 文档随源码同仓库维护

> **注：** treeland 属于 Treeland 生态项目，非 DDE 项目范围，但应用户要求纳入调研。
