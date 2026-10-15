```cmake
cmake_minimum_required(VERSION 3.23)
set(PLUGIN_NAME "myplugin")

find_package(Qt6 COMPONENTS Core LinguistTools REQUIRED)
find_package(DdeControlCenter REQUIRED)

# 可选额外依赖
# find_package(Qt6 COMPONENTS DBus REQUIRED)
# find_package(Dtk6 COMPONENTS Core Gui REQUIRED)

file(GLOB_RECURSE PLUGIN_SRCS "operation/*.cpp" "operation/*.h")
add_library(${PLUGIN_NAME} MODULE ${PLUGIN_SRCS})

target_link_libraries(${PLUGIN_NAME} PRIVATE
    Dde::Control-Center
    Qt6::Core
)
# 按需添加 Qt6::DBus、Dtk6::Gui 等

dcc_install_plugin(NAME ${PLUGIN_NAME} TARGET ${PLUGIN_NAME})
dcc_handle_plugin_translation(NAME ${PLUGIN_NAME})
```

### dcc_install_plugin

`dcc_install_plugin(NAME <name> TARGET <target>)`
- `NAME` — 插件名，同时作为 QML 模块 URI
- `TARGET` — C++ target 名（无 C++ 代码则省略）
- 自动收集 `qml/` 下所有 `.qml`、`.js`、`.dci`、`.svg`、`.png`、`.jpg`、`.webp` 文件
- 验证 QML 文件名首字母大写
- 验证不允许 `main.qml`
- 设置 `AUTOMOC_MACRO_NAMES` 为 `DCC_FACTORY_CLASS`

### dcc_handle_plugin_translation

`dcc_handle_plugin_translation(NAME <name>)`
- 自动处理 20 种 locale 的 TS 文件
