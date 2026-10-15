# Eval: 窗口动效设置

## 任务

为窗口设置平台特效（如圆角、模糊）：
1. 禁用启动动效
2. 禁用关闭动效
3. 设置启动动效为从鼠标位置展开

## 期望输出

代码应：
1. 使用 EffectScene 枚举禁用动效
2. 使用 EffectType 枚举设置动效类型

## 验证要点

- [ ] handle->setEffectScene(DPlatformHandle::EffectNoStart)
- [ ] handle->setEffectScene(DPlatformHandle::EffectNoClose)
- [ ] handle->setEffectType(DPlatformHandle::EffectCursor)
- [ ] 了解 EffectScene 和 EffectType 枚举值

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未忽略 Wayland 与 X11 的平台差异
- [ ] 窗口属性设置考虑了当前显示后端
