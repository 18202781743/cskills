# CMake Guide

## Basic CMakeLists.txt

```cmake
# SPDX-FileCopyrightText: 2024 - 2026 UnionTech Software Technology Co., Ltd.
#
# SPDX-License-Identifier: GPL-3.0-or-later

add_library(<library-name> SHARED
    <name>applet.h
    <name>applet.cpp
)

target_link_libraries(<library-name> PRIVATE
    dde-shell-frame
)

ds_install_package(PACKAGE <plugin-id> TARGET <library-name>)
```

## CMake Macros

### ds_install_package()

Installs the plugin package and library:

```cmake
ds_install_package(PACKAGE <plugin-id> TARGET <library-name>)
```

Parameters:
- `PACKAGE`: The plugin ID (e.g., `org.deepin.ds.weather`)
- `TARGET`: The CMake target name (optional for QML-only plugins)

### ds_handle_package_translation()

Sets up translation files for the plugin:

```cmake
ds_handle_package_translation(
    PACKAGE <plugin-id>
    QML_FILES ${QML_FILES_NEED_TRANSLATION}
    ${CMAKE_CURRENT_LIST_DIR}/package/main.qml
)
```

Parameters:
- `PACKAGE`: The plugin ID
- `QML_FILES`: List of QML files to extract translations from
- `SOURCE_FILES`: List of C++ source files (optional, auto-detected)

## Dependencies

### Required Dependencies

```cmake
# Qt6 Core and Quick
find_package(Qt${QT_VERSION_MAJOR} ${REQUIRED_QT_VERSION} REQUIRED COMPONENTS Core Gui Quick)

# For QWidget plugins
find_package(Qt${QT_VERSION_MAJOR} ${REQUIRED_QT_VERSION} REQUIRED COMPONENTS Widgets)
find_package(Dtk${DTK_VERSION_MAJOR} REQUIRED COMPONENTS Widget)
```

### Linking

```cmake
target_link_libraries(<target> PRIVATE
    dde-shell-frame                    # dde-shell framework
    Qt${QT_VERSION_MAJOR}::Core        # Qt Core
    Qt${QT_VERSION_MAJOR}::Quick       # Qt Quick (for QML)
    Qt${QT_VERSION_MAJOR}::Widgets     # Qt Widgets (for QWidget plugins)
    Dtk${DTK_VERSION_MAJOR}::Widget    # DTK Widget (for QWidget plugins)
)
```

## Complete Example

```cmake
# SPDX-FileCopyrightText: 2024 - 2026 UnionTech Software Technology Co., Ltd.
#
# SPDX-License-Identifier: GPL-3.0-or-later

find_package(Qt${QT_VERSION_MAJOR} ${REQUIRED_QT_VERSION} REQUIRED COMPONENTS Core Gui Quick)
find_package(Dtk${DTK_VERSION_MAJOR} REQUIRED COMPONENTS Widget)

add_library(ds-weather SHARED
    weatherapplet.h
    weatherapplet.cpp
)

target_link_libraries(ds-weather PRIVATE
    dde-shell-frame
    Qt${QT_VERSION_MAJOR}::Quick
    Dtk${DTK_VERSION_MAJOR}::Widget
)

ds_install_package(PACKAGE org.deepin.ds.weather TARGET ds-weather)

ds_handle_package_translation(
    PACKAGE org.deepin.ds.weather
    QML_FILES
        ${CMAKE_CURRENT_LIST_DIR}/package/main.qml
        ${CMAKE_CURRENT_LIST_DIR}/package/WeatherWidget.qml
)
```

## Build Commands

```bash
# Configure
cmake -B build -DQT_VERSION_MAJOR=6

# Build
cmake --build build -j8

# Install (optional)
sudo cmake --install build
```
