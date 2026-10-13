# 核心后端组件类仓库文档调研

## dde-services

- **仓库地址：** https://github.com/linuxdeepin/dde-services
- **项目说明：** DDE DBus 服务管理
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
- **文档维护方式：** 仅 README

## dde-daemon

- **仓库地址：** https://github.com/linuxdeepin/dde-daemon
- **项目说明：** DDE 会话设置守护进程
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（14 个文件）
  - `docs/README.md` — 文档目录说明
  - `docs/aireplane-mode.md` — 飞行模式文档
  - `docs/auto_backlight/自动亮度功能使用指南.md` — 自动亮度使用指南
  - `docs/auto_backlight/auto_brightness_design.md` — 自动亮度设计文档
  - `docs/bluetooth_debug.md` — 蓝牙调试文档
  - `docs/bluetooth_device-known.md` — 已知蓝牙设备
  - `docs/bluetooth_FAQ.md` — 蓝牙常见问题
  - `docs/bluetooth_install-firmware.md` — 蓝牙固件安装
  - `docs/brightness-architecture.md` — 亮度架构文档
  - `docs/calendar/ifc.md` — 日历接口文档
  - `docs/calendar/job.md` — 日历任务文档
  - `docs/dde-session-daemon_debug.md` — 会话守护进程调试
  - `docs/service_trigger.md` — 服务触发器文档
  - `docs/session-power.md` — 会话电源管理
- **文档构建方式：** Markdown（纯 Markdown 文档，无自动化构建）
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 8 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 文档随源码同仓库维护，`docs/` 下按模块存放技术文档（蓝牙、亮度、日历、电源等）

## dde-api

- **仓库地址：** https://github.com/linuxdeepin/dde-api
- **项目说明：** DDE API 库，提供屏幕区域检测、缩略图生成、声音播放等 DBus 接口
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 8 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README 和 CHANGELOG

## go-dbus-factory

- **仓库地址：** https://github.com/linuxdeepin/go-dbus-factory
- **项目说明：** Go DBus 绑定代码自动生成工具
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（1 个文件）
  - `docs/config.md` — 配置说明文档
- **文档构建方式：** Markdown
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 8 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 文档随源码同仓库维护，`docs/` 下存放配置说明

## go-lib

- **仓库地址：** https://github.com/linuxdeepin/go-lib
- **项目说明：** Deepin Go 工具库，包含 glib、gettext、archive、graphic 等 Go 例程
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 7 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README 和 CHANGELOG

## dde-application-manager

- **仓库地址：** https://github.com/linuxdeepin/dde-application-manager
- **项目说明：** DDE 应用管理器（重构分支，WORK IN PROGRESS）
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（7 个文件）
  - `docs/applicationHooks.md` — 应用钩子说明
  - `docs/customVariables.md` — 自定义变量说明
  - `docs/dde-am-usage.md` — 应用管理器使用说明
  - `docs/execBehavior.md` — 执行行为说明
  - `docs/package-manager-hook.md` — 包管理器钩子（英文）
  - `docs/package-manager-hook.zh_CN.md` — 包管理器钩子（中文）
  - `docs/TODO.md` — 待办事项
- **文档构建方式：** Markdown（部分文档有中英文版本）
- **CHANGELOG：** ❌
- **CI/CD 工作流：** 8 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 文档随源码同仓库维护，`docs/` 下存放使用指南、钩子说明等（部分中英文）

## xdg-desktop-portal-dde

- **仓库地址：** https://github.com/linuxdeepin/xdg-desktop-portal-dde
- **项目说明：** xdg-desktop-portal 的 DDE 后端实现
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
- **文档维护方式：** 仅 README，README 中包含接口状态说明

## dde-app-services

- **仓库地址：** https://github.com/linuxdeepin/dde-app-services
- **项目说明：** DDE 应用服务集合（含 dconfig-center）
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ❌
- **CI/CD 工作流：** 12 个（含 call-api-check、call-debian-check、call-static-check、cppcheck 等）
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README

## dde-appearance

- **仓库地址：** https://github.com/linuxdeepin/dde-appearance
- **项目说明：** DDE 主题与外观设置后端
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
- **文档维护方式：** 仅 README
