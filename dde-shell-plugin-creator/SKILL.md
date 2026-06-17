---
name: dde-shell-plugin-creator
description: |
  Use this skill when the user wants to create a dde-shell plugin for Deepin Desktop Environment. Triggers include:
  - "创建 dde-shell 插件" / "创建 ds 插件"
  - "开发 dde-shell 插件" / "开发 ds 插件"
  - "dde-shell plugin" / "ds plugin"
  - "创建 dock 插件" / "开发 dock 小部件"
  - "dde-shell applet" / "dde-shell containment" / "dde-shell panel"
  - Any request to create a plugin for the Deepin desktop shell framework
---

# dde-shell Plugin Creator

This skill guides you through creating dde-shell plugins for Deepin Desktop Environment.

## Overview

dde-shell is the plugin framework for Deepin Desktop Environment (DDE). It supports three plugin types:
- **Applet**: Basic plugin widget (e.g., weather, system monitor)
- **Containment**: Container that holds multiple applets
- **Panel**: Top-level panel like the dock

## Workflow

When a user requests a dde-shell plugin, follow these steps:

### Step 1: Gather Requirements

Ask the user:
1. **Plugin name**: What should the plugin be called? (e.g., `org.deepin.ds.weather`)
2. **Plugin type**: Applet, Containment, or Panel?
3. **UI technology**: QWidget (embedded in dock), QQuick (standalone window), or both?
4. **Configuration**: Does the plugin need DConfig for user settings?
5. **Cross-plugin access**: Does it need to access data from other plugins via DAppletBridge?

### Step 2: Generate Project Structure

Based on the requirements, generate the following files:

```
<plugin-name>/
├── CMakeLists.txt                    # Build configuration
├── <name>applet.h                    # DApplet subclass header
├── <name>applet.cpp                  # DApplet subclass implementation
├── package/
│   ├── metadata.json                 # Plugin metadata
│   ├── main.qml                      # QML entry point
│   └── control/                      # Custom QML controls (optional)
├── configs/
│   └── <plugin-id>.json              # DConfig metadata (if needed)
└── translations/                     # Translation files
    ├── <plugin-id>.ts
    ├── <plugin-id>_zh_CN.ts
    └── ... (23 languages)
```

### Step 3: Generate Files

For each file, use the templates in the `templates/` directory and the reference documentation in `references/`.

Key points:
- **metadata.json**: Must include `Plugin.Id`, `Plugin.Version`, `Plugin.Url`, and optionally `Plugin.Parent`
- **CMakeLists.txt**: Use `ds_install_package()` and `ds_handle_package_translation()` macros
- **C++ class**: Inherit from `DApplet`, `DContainment`, or `DPanel`, use `D_APPLET_CLASS()` macro
- **QML**: Use `AppletItem` as root element, import `org.deepin.ds 1.0`

### Step 4: Explain Each File

After generating files, explain:
- Purpose of each file
- How to build and test
- How to install and debug

## Plugin ID Convention

Use reverse domain notation: `org.deepin.ds.<name>`
- For dock plugins: `org.deepin.ds.dock.<name>`
- For examples: `org.deepin.ds.example.<name>`

## Building and Testing

```bash
# Build
cmake -B build -DQT_VERSION_MAJOR=6
cmake --build build -j8

# Test single plugin
dde-shell -p <plugin-id>
```

## Reference Documentation

Read the relevant reference files based on the plugin type:
- `references/plugin-structure.md` - Directory structure details
- `references/cmake-guide.md` - CMake configuration guide
- `references/metadata-spec.md` - metadata.json specification
- `references/applet-types.md` - Plugin type comparison
- `references/cpp-api.md` - C++ API reference
- `references/qml-api.md` - QML API reference
- `references/dconfig-guide.md` - DConfig configuration
- `references/translation-guide.md` - Translation setup
- `references/dapplet-bridge.md` - Cross-plugin communication
- `references/debian-packaging.md` - Debian packaging guide

## Templates

Use templates from the `templates/` directory:
- `templates/CMakeLists.txt.template` - CMake template
- `templates/metadata.json.template` - Metadata template
- `templates/applet.h.template` - Header template
- `templates/applet.cpp.template` - Implementation template
- `templates/main.qml.template` - QML template
- `templates/dconfig.json.template` - DConfig template
- `templates/debian-control.template` - Debian control template
