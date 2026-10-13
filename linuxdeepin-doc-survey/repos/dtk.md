# DTK 开发套件类仓库文档调研

## dtkcommon

- **仓库地址：** https://github.com/linuxdeepin/dtkcommon
- **项目说明：** DTK 公共资源项目（CMake 模块、配置等）
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 11 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README 和 CHANGELOG，提供 CMake 模块和配置

## dtkcore

- **仓库地址：** https://github.com/linuxdeepin/dtkcore
- **项目说明：** Deepin Tool Kit Core，DTK 核心库，所有 C++/Qt Deepin 开发的基础工具
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（50 个文件）
  - `docs/CMakeLists.txt` — Doxygen 文档构建配置
  - `docs/MainPage.zh_CN.md` — 主页文档（中文）
  - `docs/Specification.md` — Deepin 应用规范
  - `docs/dci/` — DCI 图标文档（`ddcifile.zh_CN.dox`、`index.zh_CN.md`）
  - `docs/filesystem/` — 文件系统文档（`dbasefilewatcher`、`dcapfile`、`dfilesystemwatcher` 等 .dox 文件）
  - `docs/global/` — 全局文档（`dconfig`、`ddesktopentry`、`dlicenseinfo` 等 .dox 文件）
  - `docs/log/` — 日志文档（`Logger`、`FileAppender`、`ConsoleAppender` 等 .dox 文件）
  - `docs/settings/` — 设置文档（`dsettings`、`dsettingsgroup`、`dsettingsoption` 等 .dox 文件及 backend 子目录）
  - `docs/util/` — 工具文档（`dutil`、`ddbusender`、`ddisksizeformatter` 等 .dox 文件）
  - `docs/src/` — 文档图片资源（截图、示例图等）
- **文档构建方式：** Doxygen/CMake（`docs/CMakeLists.txt` 配置 Doxygen 构建 API 文档）
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 13 个
- **文档部署（Dev-Doc）：** ✅ `call-deploy-dev-doc.yml`（push to master 时触发）
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 文档随源码同仓库维护，`docs/` 下按模块组织 Doxygen API 文档（中文），通过 CMake/Doxygen 构建，CI 自动部署

## dtkgui

- **仓库地址：** https://github.com/linuxdeepin/dtkgui
- **项目说明：** Deepin Tool Kit Gui，DTK GUI 层，平台主题、渲染等
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（13 个文件）
  - `docs/CMakeLists.txt` — Doxygen 文档构建配置
  - `docs/kernel/` — 内核文档（`dpalette.zh_CN.dox`、`index.zh_CN.md`）
  - `docs/src/` — 源码文档（`dguiapplicationhelper`、`dimagehandler`、`dplatformtheme` 等 .dox 文件）
  - `docs/util/` — 工具文档（`ddciicon`、`ddciiconpalette`、`ddciiconplayer`、`dicontheme` 等 .dox 文件）
  - `docs/images/` — 文档图片资源
- **文档构建方式：** Doxygen/CMake
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 16 个
- **文档部署（Dev-Doc）：** ✅ `call-deploy-dev-doc.yml`
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 文档随源码同仓库维护，`docs/` 下按模块组织 Doxygen API 文档（中文），通过 CMake/Doxygen 构建，CI 自动部署

## dtkwidget

- **仓库地址：** https://github.com/linuxdeepin/dtkwidget
- **项目说明：** Deepin Tool Kit Widget，DTK Widget 控件库，提供基础 Widget 组件
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（162 个文件）
  - `docs/CMakeLists.txt` — Doxygen 文档构建配置
  - `docs/index.zh_CN.md` — 主页文档（中文）
  - `docs/widgets/` — 控件文档（60+ 个 `.dox` 文件，覆盖 DAboutDialog、DAlertDialog、DButtonBox、DComboBox、DDialog、DFileDialog、DLineEdit、DListView、DMainWindow、DProgressBar、DSearchEdit、DSettingsDialog、DSlider、DSpinBox、DStyle、DSwitchButton、DTabBar、DTextEdit、DTitleBar、DToolTip 等全部控件）
  - `docs/widgets/index.zh_CN.md` — 控件文档索引
  - `docs/images/` — 文档图片资源（100+ 张截图和示例图）
- **文档构建方式：** Doxygen/CMake
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 16 个（含 `call-doc-check.yml` — Doxygen 文档检查工作流）
- **文档部署（Dev-Doc）：** ✅ `call-deploy-dev-doc.yml`
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 文档随源码同仓库维护，`docs/widgets/` 下含大量 Doxygen 控件文档（中文），通过 CMake/Doxygen 构建，CI 自动部署，另有文档检查工作流

## dtkdeclarative

- **仓库地址：** https://github.com/linuxdeepin/dtkdeclarative
- **项目说明：** DTK QML 声明式控件库，基于 QtQuick/QtQml，是 dtkwidget 的全新替代
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（263 个文件）
  - `docs/CMakeLists.txt` — Doxygen 文档构建配置
  - `docs/DevSpecification.zh_CN.md` — 开发规范文档（中文）
  - `docs/index.zh_CN.md` — 主页文档（中文）
  - `docs/images/` — 文档图片资源（240+ 张截图和示例图，覆盖所有 QML 控件）
  - `docs/changelog/` — 变更日志目录
- **文档构建方式：** Doxygen/CMake
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 13 个
- **文档部署（Dev-Doc）：** ✅ `call-deploy-dev-doc.yml`
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 文档随源码同仓库维护，`docs/` 下含 Doxygen QML 控件文档（中文）和开发规范，通过 CMake/Doxygen 构建，CI 自动部署

## dtklog

- **仓库地址：** https://github.com/linuxdeepin/dtklog
- **项目说明：** DTK 日志库（**已废弃**，日志功能已合并至 dtkcore，不再独立维护）
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 12 个
- **文档部署（Dev-Doc）：** ✅ `call-deploy-dev-doc.yml`（仍保留部署工作流，但仓库已废弃）
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README 和 CHANGELOG，仓库已废弃，日志功能已合并至 dtkcore

## dtksystemsettings

- **仓库地址：** https://github.com/linuxdeepin/dtksystemsettings
- **项目说明：** DTK 系统设置库，基于 Qt 的系统设置开发库
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ✅（23 个文件）
  - `docs/CMakeLists.txt` — Doxygen 文档构建配置
  - `docs/index.zh_CN.md` — 主页文档（中文）
  - `docs/accounts/` — 账号管理文档（`daccountsmanager`、`daccountstypes`、`daccountsuser` 等 .dox 文件）
  - `docs/login/` — 登录管理文档（`dloginmanager`、`dloginseat`、`dloginsession`、`dloginuser` 等 .dox 文件）
  - `docs/power/` — 电源管理文档（`dpowerdevice`、`dpowermanager`、`dpowersettings`、`dkbdbacklight` 等 .dox 文件）
  - `docs/rfmanager/` — 射频管理文档（`drfmanager.zh_CN.dox`）
  - `docs/systemtime/` — 系统时间文档（`dsystemtime`、`dsystimetypes` 等 .dox 文件）
- **文档构建方式：** Doxygen/CMake
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 11 个
- **文档部署（Dev-Doc）：** ✅ `call-deploy-dev-doc.yml`
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 文档随源码同仓库维护，`docs/` 下按模块组织 Doxygen API 文档（中文），通过 CMake/Doxygen 构建，CI 自动部署

## dde-qtintegration

- **仓库地址：** https://github.com/linuxdeepin/dde-qtintegration
- **项目说明：** DTK 风格集成插件（qt5integration），使 DDE 对 Qt 应用更友好
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 14 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README 和 CHANGELOG

## dde-qtplatform-plugins

- **仓库地址：** https://github.com/linuxdeepin/dde-qtplatform-plugins
- **项目说明：** DTK Qt 平台插件（QPA，qt5platform-plugins）
- **README（英文）：** ✅ `README.md`
- **README（中文）：** ✅ `README.zh_CN.md`
- **docs/ 目录：** ❌
- **文档构建方式：** 无
- **CHANGELOG：** ✅ `CHANGELOG.md`
- **CI/CD 工作流：** 14 个
- **文档部署（Dev-Doc）：** ❌
- **GitHub Pages：** ❌
- **GitHub Wiki：** ❌
- **.github/*.md：** ❌
- **文档维护方式：** 仅 README 和 CHANGELOG
