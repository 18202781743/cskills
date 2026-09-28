# 集成与构建配置

dde-qtplatform-plugins 是运行期 Qt 平台插件，不提供开发包、CMake 导出目标、pkg-config 模块或 qmake 模块。使用方工程无需在编译或链接阶段引入本项目。

## 安装

平台插件由系统包管理器安装到 Qt 的平台插件目录。DTK5 对应的插件安装在 `qt5/plugins/platforms` 目录下，DTK6 对应的插件安装在 `qt6/plugins/platforms` 目录下。使用方工程无需手工指定插件路径。

## 运行时加载

Qt 应用程序在启动时根据平台名称自动加载对应的 QPA 插件。使用方可通过设置环境变量 `QT_QPA_PLATFORM` 选择平台插件。在 DDE 桌面环境中，默认安装并配置了 dde-qtplatform-plugins 的平台插件，Qt 应用程序无需额外配置即可获得 DTK 平台级视觉集成。

## 主版本选择

平台插件与 DTK 主版本对应：DTK5 环境使用 DTK5 构建的平台插件，DTK6 环境使用 DTK6 构建的平台插件。使用方工程不需要自行选择或链接平台插件，运行环境中的包管理系统负责安装与 DTK 主版本匹配的插件。

## 关联文档

- 项目导出类型说明见[导出类型介绍](modules.md)。
