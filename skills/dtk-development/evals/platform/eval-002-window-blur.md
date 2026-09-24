# Eval: 窗口模糊效果

## 任务

为窗口启用模糊背景效果：
1. 启用窗口背景模糊
2. 设置半透明背景
3. 设置模糊区域

## 期望输出

代码应：
1. 设置 enableBlurWindow 属性
2. 设置 translucentBackground 属性
3. 正确处理模糊区域

## 验证要点

- [ ] handle->setEnableBlurWindow(true)
- [ ] handle->setTranslucentBackground(true)
- [ ] 了解模糊效果的平台差异（X11/Wayland）

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未忽略 Wayland 与 X11 的平台差异
- [ ] 窗口属性设置考虑了当前显示后端
