# Eval: dde-shell 插件使用 DTK DConfig 存储配置

## 任务

创建一个 dde-shell Applet 插件，用于显示剪贴板历史。用户希望插件能记住一些偏好设置（如最大历史条目数），需要用到 DConfig 持久化存储。

## 期望输出

回答应：
1. 使用 dde-shell-development 指导创建 Applet 插件结构（metadata.json、main.qml、CMakeLists.txt）
2. 使用 `$dtk-development` 加载 DTK 文档，并正确引用 DConfig 配置方案
3. 展示 DConfig meta 文件（JSON schema）和 override 文件的创建
4. 在插件代码中正确使用 DConfig API 读写配置

## 验证要点

- [ ] 插件结构符合 dde-shell Applet 规范（metadata.json、main.qml、CMakeLists.txt）
- [ ] 回答中显式引用了 `$dtk-development` 或加载了 DTK DConfig 参考文档
- [ ] DConfig meta 文件包含正确的 appid、name 和 visibility
- [ ] 代码中正确使用 DConfig::setValue / DConfig::value 或 QML 绑定
- [ ] 未在 dde-shell 文件中重复描述 DConfig 通用知识（应从 DTK skill 获取）

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 同时遵循 dde-shell 和 DTK 规范，显式加载了 DTK skill，DConfig 使用正确 |
| ⚠️ **PARTIAL** | 插件结构正确但未加载 DTK skill，或 DConfig 使用有误 |
| ❌ **FAIL** | 插件结构错误，或未使用 DConfig 而是用 QSettings 等替代方案

## 反模式检查

- [ ] 未在 dde-shell skill 中内联 DConfig 的详细说明
- [ ] 未混用 dde-tray-loader 的插件接口
- [ ] DConfig appid 不为空
