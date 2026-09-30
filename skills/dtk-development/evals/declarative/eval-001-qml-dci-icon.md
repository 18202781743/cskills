# QML 中使用 dci 图标

## 任务

在 QML 中显示一个矢量图标，要求：
1. 图标尺寸为 32x32
2. 自动跟随系统主题（亮/暗色）
3. 图标来源为应用资源文件

## 期望输出

代码应：
1. import org.deepin.dtk 1.0
2. 使用 DciIcon 组件
3. 设置 name 或 source 属性
4. 设置 sourceSize 属性
5. 未硬编码 font.pixelSize（应使用 D.DTK.fontManager）
6. 未硬编码颜色值（应使用 Palette + ColorSelector）
7. DWindow 属性使用前已设置 DWindow.enabled: true
8. 模糊窗口同时设置了 translucentBackground: true

## 验证要点

- [ ] import org.deepin.dtk 1.0
- [ ] 使用 DciIcon 组件
- [ ] 设置 name 或 source 属性
- [ ] 设置 sourceSize 属性

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
