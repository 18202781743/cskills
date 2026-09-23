# Eval: 托盘插件使用 DTK DPalette 适配主题

## 任务

创建一个系统托盘插件，显示网络流量速度。要求插件图标和文字颜色能跟随系统亮暗主题自动切换，需要使用 DPalette 或 DGuiApplicationHelper 实现主题适配。

## 期望输出

回答应：
1. 使用 dde-tray-development 指导创建托盘插件（PluginsItemInterfaceV2、metadata.json、CMakeLists.txt）
2. 使用 `$dtk-development` 加载 DTK 文档，并正确引用 DGuiApplicationHelper 或 DPalette 主题方案
3. 在插件中正确实现主题切换回调（监听 themeTypeChanged 信号）
4. 根据当前主题选择正确的图标或颜色

## 验证要点

- [ ] 插件实现 PluginsItemInterfaceV2 接口，使用正确的 IID 和 PluginFlags
- [ ] 回答中显式引用了 `$dtk-development` 或加载了 DTK 主题参考文档
- [ ] 代码中正确使用 DGuiApplicationHelper::themeTypeChanged 或 DPalette
- [ ] 图标/颜色在亮暗主题下均有正确处理
- [ ] 未在 dde-tray 文件中重复描述 DPalette 通用知识

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 同时遵循托盘和 DTK 规范，显式加载了 DTK skill，主题适配正确 |
| ⚠️ **PARTIAL** | 托盘结构正确但未加载 DTK skill，或主题切换实现有误 |
| ❌ **FAIL** | 托盘接口实现错误，或未实现主题适配

## 反模式检查

- [ ] 未在 dde-tray skill 中内联 DPalette 的详细说明
- [ ] 未混用 dde-shell 的 DApplet 接口
- [ ] 未硬编码颜色值
