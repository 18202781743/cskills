# QML 按钮类型

## 任务

在 QML 中创建不同样式的按钮：
1. 蓝色推荐按钮
2. 红色警告按钮
3. 纯图标按钮

## 期望输出

代码应：
1. import org.deepin.dtk 1.0
2. RecommandButton 推荐按钮
3. WarningButton 警告按钮
4. IconButton 图标按钮，设置 icon.name
5. 未硬编码 font.pixelSize（应使用 D.DTK.fontManager）
6. 未硬编码颜色值（应使用 Palette + ColorSelector）
7. DWindow 属性使用前已设置 DWindow.enabled: true
8. 模糊窗口同时设置了 translucentBackground: true

## 验证要点

- [ ] import org.deepin.dtk 1.0
- [ ] RecommandButton 推荐按钮
- [ ] WarningButton 警告按钮
- [ ] IconButton 图标按钮，设置 icon.name

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
