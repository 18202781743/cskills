# Eval: 控制中心插件使用 DTK DBlurEffectWidget 实现模糊背景

## 任务

创建一个控制中心插件，用于管理蓝牙设备。插件的主页面需要毛玻璃模糊背景效果，使用 DBlurEffectWidget 实现。

## 期望输出

回答应：
1. 使用 dde-control-center-development 指导创建控制中心插件（DCC_FACTORY_CLASS、DccObject、CMakeLists.txt、QML 元数据）
2. 使用 `$dtk-development` 加载 DTK 文档，并正确引用 DBlurEffectWidget 或窗口模糊效果方案
3. 在插件 QML 或 C++ 中正确使用模糊效果组件
4. 确认模糊效果在 X11 和 Wayland 下的兼容性

## 验证要点

- [ ] 插件使用 DCC_FACTORY_CLASS 注册，CMake 使用 dde-control-center 宏
- [ ] 回答中显式引用了 `$dtk-development` 或加载了 DTK 窗口效果参考文档
- [ ] 模糊效果实现正确（DBlurEffectWidget 或 QML WindowBlur）
- [ ] 插件根 QML 不依赖 dccData
- [ ] 未在控制中心文件中重复描述模糊效果的通用知识

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 同时遵循控制中心和 DTK 规范，显式加载了 DTK skill，模糊效果正确 |
| ⚠️ **PARTIAL** | 控制中心结构正确但未加载 DTK skill，或模糊效果实现有误 |
| ❌ **FAIL** | 控制中心接口实现错误，或未使用 DTK 模糊效果

## 反模式检查

- [ ] 未在控制中心 skill 中内联 DBlurEffectWidget 的详细说明
- [ ] 未混用托盘插件的接口
- [ ] 未忽略 Wayland 兼容性
