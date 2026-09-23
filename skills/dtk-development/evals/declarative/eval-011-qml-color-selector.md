# QML 颜色选择器

## 任务

在 QML 中使用颜色选择器，要求：
1. 根据控件状态自动选择颜色
2. 使用语义化颜色定义

## 期望输出

代码应：
1. ColorSelector 组件
2. Palette 颜色定义
3. controlState 属性获取状态
4. 未硬编码 font.pixelSize（应使用 D.DTK.fontManager）
5. 未硬编码颜色值（应使用 Palette + ColorSelector）
6. DWindow 属性使用前已设置 DWindow.enabled: true
7. 模糊窗口同时设置了 translucentBackground: true

## 验证要点

- [ ] ColorSelector 组件
- [ ] Palette 颜色定义
- [ ] controlState 属性获取状态

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未硬编码 font.pixelSize（应使用 D.DTK.fontManager）
- [ ] 未硬编码颜色值（应使用 Palette + ColorSelector）
- [ ] DWindow 属性使用前已设置 DWindow.enabled: true
- [ ] 模糊窗口同时设置了 translucentBackground: true
