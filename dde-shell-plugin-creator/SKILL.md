---
name: dde-shell-plugin-creator
description: |
  Use this skill when the user wants to create a dde-shell plugin for Deepin Desktop Environment. Triggers include:
  - "创建 dde-shell 插件" / "创建 ds 插件"
  - "开发 dde-shell 插件" / "开发 ds 插件"
  - "dde-shell plugin" / "ds plugin"
  - "dde-shell applet" / "dde-shell containment" / "dde-shell panel"
  - Any request to create a plugin for the Deepin desktop shell framework
---

# dde-shell Plugin Creator / dde-shell 插件创建器

This skill guides you through creating dde-shell plugins for Deepin Desktop Environment.
本技能指导您为深度桌面环境创建 dde-shell 插件。

## Overview / 概述

dde-shell is the plugin framework for Deepin Desktop Environment (DDE). It supports three plugin types:
dde-shell 是深度桌面环境（DDE）的插件框架，支持三种插件类型：

- **Applet**: Basic plugin widget (e.g., weather, system monitor) / 基础插件部件（如天气、系统监控）
- **Containment**: Container that holds multiple applets / 容器，可包含多个 applet
- **Panel**: Top-level panel like the dock / 顶级面板，如 dock

## Workflow / 工作流程

When a user requests a dde-shell plugin, follow these steps:
当用户请求创建 dde-shell 插件时，请按以下步骤操作：

### Step 1: Gather Requirements / 第一步：收集需求

Ask the user / 询问用户：
1. **Plugin name / 插件名称**: What should the plugin be called? (e.g., `org.deepin.ds.weather`)
2. **Plugin type / 插件类型**: Applet, Containment, or Panel?
3. **UI technology / UI 技术**: QWidget (embedded in panel), QQuick (standalone window), or both?
4. **Configuration / 配置**: Does the plugin need DConfig for user settings?
5. **Cross-plugin access / 跨插件访问**: Does it need to access data from other plugins via DAppletBridge?

### Step 2: Generate Project Structure / 第二步：生成项目结构

Based on the requirements, generate the following files:
根据需求，生成以下文件：

```
<plugin-name>/
├── CMakeLists.txt                    # Build configuration / 构建配置
├── <name>applet.h                    # DApplet subclass header / DApplet 子类头文件
├── <name>applet.cpp                  # DApplet subclass implementation / DApplet 子类实现
├── package/
│   ├── metadata.json                 # Plugin metadata / 插件元数据
│   ├── main.qml                      # QML entry point / QML 入口文件
│   └── control/                      # Custom QML controls (optional) / 自定义 QML 控件（可选）
└── translations/                     # Translation files / 翻译文件
    ├── <plugin-id>.ts
    ├── <plugin-id>_zh_CN.ts
    └── ... (23 languages / 23 种语言)
```

### Step 3: Generate Files / 第三步：生成文件

For each file, use the templates in the `templates/` directory and the reference documentation in `references/`.
使用 `templates/` 目录中的模板和 `references/` 目录中的参考文档生成各文件。

Key points / 要点：
- **metadata.json**: Must include `Plugin.Id`, `Plugin.Version`, `Plugin.Url`, and optionally `Plugin.Parent`
- **CMakeLists.txt**: Use `ds_install_package()` and `ds_handle_package_translation()` macros
- **C++ class**: Inherit from `DApplet`, `DContainment`, or `DPanel`, use `D_APPLET_CLASS()` macro
- **QML**: Use `AppletItem` as root element, import `org.deepin.ds 1.0`

### Step 4: Explain Each File / 第四步：说明各文件

After generating files, explain:
生成文件后，说明：
- Purpose of each file / 每个文件的作用
- How to build and test / 如何构建和测试
- How to install and debug / 如何安装和调试

## Plugin Type Templates / 插件类型模板

Based on the plugin type selected by the user, use the corresponding template:
根据用户选择的插件类型，使用对应的模板：

### Applet Templates / Applet 模板
- `templates/applet/applet.h.template` - Applet header / Applet 头文件
- `templates/applet/applet.cpp.template` - Applet implementation / Applet 实现
- `templates/applet/metadata.json.template` - Applet metadata / Applet 元数据
- `templates/applet/main.qml.template` - Applet QML / Applet QML 文件

### Containment Templates / Containment 模板
- `templates/containment/containment.h.template` - Containment header / Containment 头文件
- `templates/containment/containment.cpp.template` - Containment implementation / Containment 实现
- `templates/containment/metadata.json.template` - Containment metadata / Containment 元数据
- `templates/containment/main.qml.template` - Containment QML / Containment QML 文件

### Panel Templates / Panel 模板
- `templates/panel/panel.h.template` - Panel header / Panel 头文件
- `templates/panel/panel.cpp.template` - Panel implementation / Panel 实现
- `templates/panel/metadata.json.template` - Panel metadata / Panel 元数据
- `templates/panel/main.qml.template` - Panel QML / Panel QML 文件

## Plugin ID Convention / 插件 ID 命名规范

Use reverse domain notation: `org.deepin.ds.<name>`
使用反向域名表示法：`org.deepin.ds.<name>`

## Building and Testing / 构建和测试

```bash
# Build / 构建
cmake -B build
cmake --build build -j8

# Test single plugin / 测试单个插件
dde-shell -p <plugin-id>
```

## Reference Documentation / 参考文档

Read the relevant reference files based on the plugin type:
根据插件类型阅读相关参考文件：

- `references/plugin-structure.md` - Directory structure details / 目录结构详情
- `references/cmake-guide.md` - CMake configuration guide / CMake 配置指南
- `references/metadata-spec.md` - metadata.json specification / metadata.json 规范
- `references/applet-types.md` - Plugin type comparison / 插件类型对比
- `references/cpp-api.md` - C++ API reference / C++ API 参考
- `references/qml-api.md` - QML API reference / QML API 参考
- `references/translation-guide.md` - Translation setup / 翻译设置
- `references/dapplet-bridge.md` - Cross-plugin communication / 跨插件通信
- `references/debian-packaging.md` - Debian packaging guide / Debian 打包指南
