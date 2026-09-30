---
name: dtk
description: DTK（Deepin Tool Kit）是 Deepin 桌面环境的开发套件，提供 CLI 工具、D-Bus 接口和 DConfig 公共配置能力。本 skill 提供 DCI 图标打包解包查看、DCI 图标主题构建与查找、X11 窗口属性读写、KWin 调试信息输出、DConfig 配置 C++ 代码生成、D-Bus 接口 C++ 代码生成、DTK 设置翻译代码与 GSettings schema 生成、中文转拼音、系统信息查询、SVG 转 PNG 的 CLI 命令，DTK 应用间跨进程文件拖拽 D-Bus 接口，DTK 应用偏好 DConfig 配置（作用范围为 DTK 应用）和系统区域格式 DConfig 配置（作用范围为系统全局）
Categories:
  - Develop
---

# dtk

DTK（Deepin Tool Kit）是 Deepin 桌面环境的开发套件。本 skill 描述 DTK 对外提供的 CLI 命令、D-Bus 接口和 DConfig 公共配置能力。

## CLI 命令

### dci

DCI 文件打包/解包工具，用于将符合 DCI 目录规范的图标目录打包为 `.dci` 文件，或将 `.dci` 文件导出为目录结构，还支持以树形结构查看 DCI 文件内容。

详见 [dci.md](references/cli/dci.md)

### dci-icon-theme

DCI 图标主题构建工具，用于将普通的图标目录结构转换为 DCI 图标主题文件。

详见 [dci-icon-theme.md](references/cli/dci-icon-theme.md)

### dci-iconfinder

DCI 图标查找工具，用于在已安装的 DCI 图标主题中搜索指定名称的图标文件。

详见 [dci-iconfinder.md](references/cli/dci-iconfinder.md)

### deepin-gui-settings

DTK GUI 设置工具，用于读写 X11 窗口属性设置。

详见 [deepin-gui-settings.md](references/cli/deepin-gui-settings.md)

### dde-kwin-bug

DDE KWin 调试工具，用于输出 KWin 窗口管理器的调试信息。

详见 [dde-kwin-bug.md](references/cli/dde-kwin-bug.md)

### dtk-settings

DTK 设置工具，用于从 DTK 设置 JSON 配置文件生成翻译代码（C++）和 GSettings schema（XML）。

详见 [dtk-settings.md](references/cli/dtk-settings.md)

### ch2py

中文转拼音工具，将输入的中文字符串转换为拼音。

详见 [ch2py.md](references/cli/ch2py.md)

### deepin-os-release

系统信息查询工具，用于输出 deepin/UOS 操作系统的各项信息。

详见 [deepin-os-release.md](references/cli/deepin-os-release.md)

### dconfig2cpp

DConfig 转 C++ 代码生成器，从 DConfig JSON 配置文件生成 C++ 头文件，将 DConfig 配置项封装为类型安全的 C++ 类。

详见 [dconfig2cpp.md](references/cli/dconfig2cpp.md)

### qdbusxml2cpp-fix

D-Bus XML 转 C++ 代码生成器，是 Qt 自带 `qdbusxml2cpp` 的增强版本。

详见 [qdbusxml2cpp-fix.md](references/cli/qdbusxml2cpp-fix.md)

### dtk6-svgc

SVG 转 PNG 转换工具，将 SVG 矢量图渲染为 PNG 位图。

详见 [dtk6-svgc.md](references/cli/dtk6-svgc.md)


## D-Bus 接口

### 文件拖拽服务

提供跨进程文件拖拽交互能力。拖拽源进程在 Session 总线上注册此接口对象，文件接收方通过 D-Bus 与拖拽源通信，实现拖拽状态查询、进度同步和数据回传。接口使用动态 baseService（拖拽源进程的唯一连接名），接收方从拖拽 MIME 数据中获取 service 名称和会话 UUID 后调用。

详见 [com.deepin.dtk.FileDrag](references/dbus/com.deepin.dtk.FileDrag.md)

## DConfig 配置项

DTK 通过 DConfig 暴露两组公共配置资源（appId 为空，所有 DTK 应用共享）。两组配置的作用范围不同：DTK 应用偏好配置仅作用于 DTK 应用，区域格式配置作用于系统全局。

### DTK 应用偏好配置

控制 DTK 应用的外观与行为：主题、动画、滚动条、标题栏、新特性展示、菜单搜索、日志规则。作用范围为 DTK 应用。

详见 [org.deepin.dtk.preference](references/config/org.deepin.dtk.preference.md)

### 区域格式配置

控制系统的区域格式：语言、日期、时间、数字、货币、纸张。作用范围为系统全局。

详见 [org.deepin.region-format](references/config/org.deepin.region-format.md)

## 开发接口

### dtkcore

dtkcore 是基于 Qt 的 C++ 基础库，提供配置与设置、日志、文件与目录、系统信息、DBus 通信、通知、文本处理和线程调度能力。界面控件与视觉主题由上层库提供。

详见 [dtkcore-dev.md](interface/dtkcore/dtkcore-dev.md)

### dtkdeclarative

dtkdeclarative 是基于 Qt Quick 的 C++ 库，为 DTK QML 声明式控件提供底层支撑。它提供 DTK 应用的 QML 加载器、应用主窗口与预加载接口、QML 场景中的帧缓冲区位块传输与视口裁剪渲染、DTK 窗口附加属性以及平台主题代理。QML 控件本身以 `org.deepin.dtk` QML 模块的形式发布，设置控件以 `org.deepin.dtk.settings` QML 模块的形式发布。

详见 [dtkdeclarative-dev.md](interface/dtkdeclarative/dtkdeclarative-dev.md)

详见 [org.deepin.dtk.md](interface/dtkdeclarative/org.deepin.dtk.md)

详见 [org.deepin.dtk.settings.md](interface/dtkdeclarative/org.deepin.dtk.settings.md)

### dtkgui

dtkgui 是基于 Qt GUI 模块的 C++ 库，提供 DTK 图形界面层面的能力，包括 DCI 图标渲染与播放、调色板管理、窗口装饰与平台主题、文件拖拽、字体管理、缩略图生成、SVG 渲染、区域监视和任务栏控制。控件级别的功能由上层 dtkwidget 提供。

详见 [dtkgui-dev.md](interface/dtkgui/dtkgui-dev.md)

### dtkwidget

dtkwidget 是基于 Qt Widgets 模块的 C++ 控件库，提供 DTK 风格的对话框、窗口、按钮、输入框、列表、视图、样式、动画效果、打印预览、设置界面和辅助工具这些控件级别的功能。图形界面层面的非控件能力（调色板、DCI 图标、窗口装饰）由下层 dtkgui 提供。

详见 [dtkwidget-dev.md](interface/dtkwidget/dtkwidget-dev.md)
