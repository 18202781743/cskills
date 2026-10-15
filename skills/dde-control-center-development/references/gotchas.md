# 控制中心开发常见陷阱

## 1. 插件加载

- **插件编译成功但不显示**：检查 `{Name}.qml` 中是否依赖了 `dccData`（插件根 QML 不能依赖它）；检查 `DCC_FACTORY_CLASS` 是否正确注册；检查 `--spec` 是否指向正确路径。
- **修改框架库后不生效**：`--spec` 只替换插件路径，修改框架库或 QML 引擎时还需设置 `LD_LIBRARY_PATH` 和 QML 导入路径。
- **QML 缓存导致修改不生效**：清除 `~/.cache/dde-control-center/qmlcache/`。

## 2. CMake 与依赖

- **find_package 失败**：确保安装了 `dde-control-center-dev`，它提供 CMake 配置和 `Dde::Control-Center` target。
- **DTK 依赖遗漏**：插件需要 DConfig/DPalette/DCI 图标时，须取消注释 `find_package(Dtk6 ...)` 并添加对应链接库。详见 `$dtk-development`。
- **翻译文件未加载**：使用 `dcc_handle_plugin_translation(NAME ${PLUGIN_NAME})`，不要手动处理。

## 3. DccObject 使用

- **name 不一致**：根 DccObject 的 name 必须与 CMake 中 `PLUGIN_NAME` 完全一致。
- **dccData undefined**：数据对象在插件工厂加载后才可用，`{Name}.qml` 创建元数据时不能依赖它。
- **模块树中不显示**：检查 `hideModule`、`visible` 属性、DBus 条件是否满足。

## 4. 不要做的事

- 不要套用旧版插件基类或托盘插件接口（v25 使用 `DCC_FACTORY_CLASS`）
- 不要把 `--spec` 当成万能调试开关（框架库需要额外设置）
- 不要混用 `dde-tray-loader` 的 IID、flags 或消息协议
- 不要使用 `QSettings` 替代 DConfig（详见 `$dtk-development`）
