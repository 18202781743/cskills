# linuxdeepin 项目文档调研数据表

本表汇总了 github.com/linuxdeepin 组织下 35 个 DDE 相关仓库的文档情况。每个仓库一行，字段含义见列头说明。

> 说明：✅ = 有 | ❌ = 无 | — = 不适用

| 仓库名称 | 仓库地址 | 分类 | README(英) | README(中) | docs/ 目录 | docs/ 文件数 | 文档构建方式 | CHANGELOG | CI/CD 工作流数 | 文档部署(Dev-Doc) | GitHub Pages | GitHub Wiki | .github/*.md | 文档维护方式 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ddm | https://github.com/linuxdeepin/ddm | 运行环境 | ✅ | ✅ | ✅ | 2 | Markdown | ❌ | 10 | ❌ | ❌ | ❌ | ✅ (copilot-instructions.md) | 文档随源码同仓库维护，docs/ 下存放架构与主题文档 |
| treeland | https://github.com/linuxdeepin/treeland | 运行环境(Treeland生态) | ✅ | ✅ | ✅ | 1 | Markdown | ❌ | 13 | ❌ | ❌ | ❌ | ✅ (copilot-instructions.md) | 文档随源码同仓库维护 |
| dde-session | https://github.com/linuxdeepin/dde-session | Session管理 | ✅ | ✅ | ✅ | 2 | Markdown | ❌ | 8 | ❌ | ❌ | ❌ | ❌ | 文档随源码同仓库维护，docs/ 下存放设计文档 |
| dde-session-shell | https://github.com/linuxdeepin/dde-session-shell | Session管理 | ✅ | ✅ | ✅ | 1 | Markdown | ❌ | 10 | ❌ | ❌ | ❌ | ❌ | 文档随源码同仓库维护，docs/ 下存放开发指南 |
| dde-shell | https://github.com/linuxdeepin/dde-shell | 前端组件 | ✅ | ✅ | ✅ | 6 | Markdown | ❌ | 8 | ❌ | ❌ | ❌ | ❌ | 文档随源码同仓库维护，docs/plugin/ 下存放插件开发教程和API文档(中英文) |
| dde-tray-loader | https://github.com/linuxdeepin/dde-tray-loader | 前端组件 | ✅ | ✅ | ❌ | 0 | 无 | ❌ | 8 | ❌ | ❌ | ❌ | ❌ | 仅README，无独立文档目录 |
| dde-clipboard | https://github.com/linuxdeepin/dde-clipboard | 前端组件 | ✅ | ✅ | ❌ | 0 | 无 | ❌ | 9 | ❌ | ❌ | ❌ | ❌ | 仅README |
| dde-launchpad | https://github.com/linuxdeepin/dde-launchpad | 前端组件 | ✅ | ✅ | ✅ | 2 | Markdown | ❌ | 8 | ❌ | ❌ | ❌ | ❌ | 文档随源码同仓库维护，docs/ 下存放DConfig说明和TODO |
| dde-control-center | https://github.com/linuxdeepin/dde-control-center | 前端组件 | ✅ | ✅ | ✅ | 4 | Doxygen/CMake | ❌ | 10 | ✅ | ❌ | ❌ | ✅ (copilot-instructions.md) | 文档随源码同仓库维护，docs/ 下含接口文档(中英文)，通过CMake/Doxygen构建，CI自动部署 |
| dde-network-core | https://github.com/linuxdeepin/dde-network-core | 前端组件 | ✅ | ✅ | ❌ | 0 | 无 | ❌ | 9 | ❌ | ❌ | ❌ | ❌ | 仅README |
| dde-session-ui | https://github.com/linuxdeepin/dde-session-ui | 前端组件 | ✅ | ✅ | ❌ | 0 | 无 | ✅ | 9 | ❌ | ❌ | ❌ | ✅ (SUPPORT.md) | 仅README和CHANGELOG |
| dde-polkit-agent | https://github.com/linuxdeepin/dde-polkit-agent | 前端组件 | ✅ | ✅ | ❌ | 0 | 无 | ✅ | 9 | ❌ | ❌ | ❌ | ❌ | 仅README和CHANGELOG |
| deepin-update-ui | https://github.com/linuxdeepin/deepin-update-ui | 前端组件 | ✅ | ✅ | ❌ | 0 | 无 | ❌ | 7 | ❌ | ❌ | ❌ | ❌ | 仅README |
| deepin-screensaver | https://github.com/linuxdeepin/deepin-screensaver | 前端组件 | ✅ | ✅ | ❌ | 0 | 无 | ✅ | 9 | ❌ | ❌ | ❌ | ❌ | 仅README和CHANGELOG |
| dde-services | https://github.com/linuxdeepin/dde-services | 后端组件 | ✅ | ✅ | ❌ | 0 | 无 | ❌ | 7 | ❌ | ❌ | ❌ | ❌ | 仅README |
| dde-daemon | https://github.com/linuxdeepin/dde-daemon | 后端组件 | ✅ | ✅ | ✅ | 14 | Markdown | ✅ | 8 | ❌ | ❌ | ❌ | ❌ | 文档随源码同仓库维护，docs/ 下存放各模块技术文档(蓝牙、亮度、日历、电源等) |
| dde-api | https://github.com/linuxdeepin/dde-api | 后端组件 | ✅ | ✅ | ❌ | 0 | 无 | ✅ | 8 | ❌ | ❌ | ❌ | ❌ | 仅README和CHANGELOG |
| go-dbus-factory | https://github.com/linuxdeepin/go-dbus-factory | 后端组件 | ✅ | ✅ | ✅ | 1 | Markdown | ✅ | 8 | ❌ | ❌ | ❌ | ❌ | 文档随源码同仓库维护，docs/ 下存放配置说明 |
| go-lib | https://github.com/linuxdeepin/go-lib | 后端组件 | ✅ | ✅ | ❌ | 0 | 无 | ✅ | 7 | ❌ | ❌ | ❌ | ❌ | 仅README和CHANGELOG |
| dde-application-manager | https://github.com/linuxdeepin/dde-application-manager | 后端组件 | ✅ | ✅ | ✅ | 7 | Markdown | ❌ | 8 | ❌ | ❌ | ❌ | ❌ | 文档随源码同仓库维护，docs/ 下存放使用指南、钩子说明等(中英文) |
| xdg-desktop-portal-dde | https://github.com/linuxdeepin/xdg-desktop-portal-dde | 后端组件 | ✅ | ✅ | ❌ | 0 | 无 | ❌ | 8 | ❌ | ❌ | ❌ | ❌ | 仅README |
| dde-app-services | https://github.com/linuxdeepin/dde-app-services | 后端组件 | ✅ | ✅ | ❌ | 0 | 无 | ❌ | 12 | ❌ | ❌ | ❌ | ❌ | 仅README |
| dde-appearance | https://github.com/linuxdeepin/dde-appearance | 后端组件 | ✅ | ✅ | ❌ | 0 | 无 | ❌ | 8 | ❌ | ❌ | ❌ | ❌ | 仅README |
| dtkcommon | https://github.com/linuxdeepin/dtkcommon | DTK套件 | ✅ | ✅ | ❌ | 0 | 无 | ✅ | 11 | ❌ | ❌ | ❌ | ❌ | 仅README和CHANGELOG，提供CMake模块和配置 |
| dtkcore | https://github.com/linuxdeepin/dtkcore | DTK套件 | ✅ | ✅ | ✅ | 50 | Doxygen/CMake | ✅ | 13 | ✅ | ❌ | ❌ | ❌ | 文档随源码同仓库维护，docs/ 下含Doxygen API文档(中文)，通过CMake构建，CI自动部署 |
| dtkgui | https://github.com/linuxdeepin/dtkgui | DTK套件 | ✅ | ✅ | ✅ | 13 | Doxygen/CMake | ✅ | 16 | ✅ | ❌ | ❌ | ❌ | 文档随源码同仓库维护，docs/ 下含Doxygen API文档(中文)，通过CMake构建，CI自动部署 |
| dtkwidget | https://github.com/linuxdeepin/dtkwidget | DTK套件 | ✅ | ✅ | ✅ | 162 | Doxygen/CMake | ✅ | 16 | ✅ | ❌ | ❌ | ❌ | 文档随源码同仓库维护，docs/ 下含大量Doxygen控件文档(中文)，通过CMake构建，CI自动部署 |
| dtkdeclarative | https://github.com/linuxdeepin/dtkdeclarative | DTK套件 | ✅ | ✅ | ✅ | 263 | Doxygen/CMake | ✅ | 13 | ✅ | ❌ | ❌ | ❌ | 文档随源码同仓库维护，docs/ 下含Doxygen QML控件文档(中文)和开发规范，通过CMake构建，CI自动部署 |
| dtklog | https://github.com/linuxdeepin/dtklog | DTK套件(已废弃) | ✅ | ✅ | ❌ | 0 | 无 | ✅ | 12 | ✅ | ❌ | ❌ | ❌ | 仅README和CHANGELOG，日志功能已合并至dtkcore，不再独立维护 |
| dtksystemsettings | https://github.com/linuxdeepin/dtksystemsettings | DTK套件 | ✅ | ✅ | ✅ | 23 | Doxygen/CMake | ✅ | 11 | ✅ | ❌ | ❌ | ❌ | 文档随源码同仓库维护，docs/ 下含Doxygen API文档(账号、登录、电源、系统时间等)，通过CMake构建，CI自动部署 |
| dde-qtintegration | https://github.com/linuxdeepin/dde-qtintegration | DTK套件 | ✅ | ✅ | ❌ | 0 | 无 | ✅ | 14 | ❌ | ❌ | ❌ | ❌ | 仅README和CHANGELOG |
| dde-qtplatform-plugins | https://github.com/linuxdeepin/dde-qtplatform-plugins | DTK套件 | ✅ | ✅ | ❌ | 0 | 无 | ✅ | 14 | ❌ | ❌ | ❌ | ❌ | 仅README和CHANGELOG |
| deepin-icon-theme | https://github.com/linuxdeepin/deepin-icon-theme | DDE资源 | ✅ | ✅ | ❌ | 0 | 无 | ✅ | 8 | ❌ | ❌ | ❌ | ❌ | 仅README和CHANGELOG |
| deepin-desktop-theme | https://github.com/linuxdeepin/deepin-desktop-theme | DDE资源 | ✅ | ✅ | ❌ | 0 | 无 | ❌ | 8 | ❌ | ❌ | ❌ | ❌ | 仅README，提供DCI主题资源 |
| dde-manual-content | https://github.com/linuxdeepin/dde-manual-content | DDE资源 | ✅ | ✅ | ❌ | 0 | 无 | ❌ | 8 | ❌ | ❌ | ❌ | ❌ | 仅README，提供帮助手册内容 |
