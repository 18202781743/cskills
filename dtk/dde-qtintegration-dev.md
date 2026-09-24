# dde-qtintegration 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | dde-qtintegration |
| 版本 | 6.7.50 |
| 描述 | DTK 风格集成插件，提供 DDE 主题、QStyle 样式、图标引擎、图片格式等 Qt 插件集成 |
| CMake target | 不适用（安装 Qt 插件，不导出 CMake target） |
| find_package 名 | 不适用 |
| 头文件安装路径 | 不适用（不安装公共头文件） |
| 仓库地址 | https://github.com/linuxdeepin/dde-qtintegration.git |

## 2. 包依赖

### 运行时依赖
- libc6
- libqt6core6, libqt6gui6, libqt6widgets6 (>= 6.x)
- libdtk6core, libdtk6gui, libdtk6widget

### 开发依赖
- Qt 6 Core, Qt 6 Gui, Qt 6 Widgets, Qt 6 WidgetsPrivate (>= 6.x)
- dtkcore, dtkgui, dtkwidget
- CMake >= 3.16

## 3. CMake 集成

不适用（dde-qtintegration 安装 Qt 插件，不提供 CMake 配置文件或导出 target。应用通过 Qt 插件加载机制自动使用）

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（不安装公共头文件）

## 6. 关键公共类及功能描述

dde-qtintegration 不提供公共 API 类，通过 Qt 插件机制为 Qt 应用提供 DDE 风格集成：

| 子目录 | 插件类型 | 功能 |
|--------|----------|------|
| `platformthemeplugin` | Platform Theme | DDE 平台主题插件，提供 DDE 主题、字体、图标等 |
| `styleplugins/chameleon` | Style | Chameleon QStyle，DDE 风格控件绘制 |
| `iconengineplugins/diconengine` | Icon Engine | DCI 图标引擎，支持 DCI 格式图标 |
| `imageformatplugins/dci` | Image Format | DCI 图片格式支持 |

插件安装路径：

| 插件类型 | 安装路径 |
|----------|----------|
| 平台主题 | `${CMAKE_INSTALL_LIBDIR}/qt6/plugins/platformthemes/` |
| 样式 | `${CMAKE_INSTALL_LIBDIR}/qt6/plugins/styles/` |
| 图标引擎 | `${CMAKE_INSTALL_LIBDIR}/qt6/plugins/iconengines/` |
| 图片格式 | `${CMAKE_INSTALL_LIBDIR}/qt6/plugins/imageformats/` |

## 7. QML 模块

不适用（QML 样式由 dtkdeclarative 的 Chameleon 模块提供）

## 8. DBus 接口

不适用

## 9. 插件开发

dde-qtintegration 本身是 Qt 插件集合，不提供二次开发插件接口。如需自定义风格行为，需直接修改源码并重新编译。

### 使用方式

Qt 应用在 DDE 环境下自动加载这些插件，无需额外配置。如需强制指定样式：

```bash
# 设置 QStyle
QT_STYLE_OVERRIDE=chameleon

# 或通过平台主题
QT_QPA_PLATFORMTHEME=deepin
```
