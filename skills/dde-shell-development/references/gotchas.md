# dde-shell 开发常见陷阱

## 1. 插件加载

- **插件编译成功但不能实例化**：每个 C++ 实现文件末尾必须有 `D_APPLET_CLASS(ClassName)` 和 `#include "<文件名>.moc"`，缺一不可。
- **插件 ID 不匹配**：插件 ID、`Plugin.Parent`、安装包目录和运行时父插件必须一致。
- **DPluginLoader 未发现插件**：检查 `pluginType` 元数据是否正确（Applet/Containment/Panel）。

## 2. 三层插件模型

- **Applet → Containment → Panel 选错**：先根据宿主和父子关系选择正确类型，不要用 Applet 做 Panel 的事。
- **混用托盘插件体系**：Applet/Containment/Panel 属于 dde-shell 插件体系，不要混用 dde-tray-loader 的 IID、flags 或消息协议。

## 3. LayerShell 窗口

- **排他区域滥用**：只有需要保留工作区的面板（如 Dock）才设置 exclusionZone，普通弹窗不要设置。
- **多屏问题**：LayerShell 必须验证目标屏幕、锚点、层级和键盘交互，并在多屏和热插拔下测试。
- **模糊效果**：Wayland 下需要确保 compositor 支持，且设置 `DWindow.translucentBackground: true`。

## 4. CMake 与元数据

- **元数据 JSON 格式错误**：`pluginType`、`pluginId`、`Plugin.Parent` 必须与实际类型匹配。
- **DTK 依赖遗漏**：需要 DConfig/DPalette/DCI 图标时添加 `find_package(Dtk6 ...)`。

## 5. 不要做的事

- 不要混用 dde-tray-loader 的 `PluginsItemInterfaceV2` 接口
- 不要把 LayerShell 排他区域加给所有窗口
- 不要忘记 `#include "<文件名>.moc"` 在文件末尾
- 不要使用 `QSettings` 替代 DConfig（详见 `$dtk-development`）
