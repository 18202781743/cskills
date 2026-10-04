# QML 视觉效果

## 任务

在 QML 中使用视觉效果：
1. 阴影效果
2. 矩形阴影
3. 窗口模糊效果

## 期望输出

代码应：
1. BoxShadow 阴影效果
2. RectangularShadow 矩形阴影
3. StyledBehindWindowBlur 窗口模糊
4. 未硬编码 font.pixelSize（应使用 D.DTK.fontManager）
5. 未硬编码颜色值（应使用 Palette + ColorSelector）
6. DWindow 属性使用前已设置 DWindow.enabled: true
7. 模糊窗口同时设置了 translucentBackground: true

## 验证要点

- [ ] BoxShadow 阴影效果
- [ ] RectangularShadow 矩形阴影
- [ ] StyledBehindWindowBlur 窗口模糊

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
