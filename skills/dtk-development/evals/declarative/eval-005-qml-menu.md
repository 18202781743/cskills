# QML 菜单

## 任务

在 QML 中创建右键菜单，要求：
1. 包含 3 个菜单项
2. 包含分隔线
3. 支持子菜单

## 期望输出

代码应：
1. Menu 组件
2. MenuItem 组件
3. MenuSeparator 分隔线
4. 嵌套 Menu 创建子菜单
5. 未硬编码 font.pixelSize（应使用 D.DTK.fontManager）
6. 未硬编码颜色值（应使用 Palette + ColorSelector）
7. DWindow 属性使用前已设置 DWindow.enabled: true
8. 模糊窗口同时设置了 translucentBackground: true

## 验证要点

- [ ] Menu 组件
- [ ] MenuItem 组件
- [ ] MenuSeparator 分隔线
- [ ] 嵌套 Menu 创建子菜单

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
