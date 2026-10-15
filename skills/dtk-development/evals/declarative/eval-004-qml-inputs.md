# QML 输入控件

## 任务

在 QML 中创建各种输入控件：
1. 普通文本输入框
2. 搜索框（带清除按钮）
3. 密码输入框（带显示/隐藏切换）
4. 数值调节框

## 期望输出

代码应：
1. LineEdit 文本输入
2. SearchEdit 搜索框
3. PasswordEdit 密码输入
4. SpinBox 数值输入
5. 未硬编码 font.pixelSize（应使用 D.DTK.fontManager）
6. 未硬编码颜色值（应使用 Palette + ColorSelector）
7. DWindow 属性使用前已设置 DWindow.enabled: true
8. 模糊窗口同时设置了 translucentBackground: true

## 验证要点

- [ ] LineEdit 文本输入
- [ ] SearchEdit 搜索框
- [ ] PasswordEdit 密码输入
- [ ] SpinBox 数值输入

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
