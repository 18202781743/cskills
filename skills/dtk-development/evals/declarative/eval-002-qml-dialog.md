# QML 对话框

## 任务

在 QML 中创建一个确认对话框，要求：
1. 标题为 "确认操作"
2. 包含 "确定" 和 "取消" 按钮
3. 点击确定时执行操作

## 期望输出

代码应：
1. import org.deepin.dtk 1.0
2. 使用 DialogWindow 作为根组件
3. 使用 ButtonBox 组织按钮
4. 处理按钮点击信号
5. 未硬编码 font.pixelSize（应使用 D.DTK.fontManager）
6. 未硬编码颜色值（应使用 Palette + ColorSelector）
7. DWindow 属性使用前已设置 DWindow.enabled: true
8. 模糊窗口同时设置了 translucentBackground: true

## 验证要点

- [ ] import org.deepin.dtk 1.0
- [ ] 使用 DialogWindow 作为根组件
- [ ] 使用 ButtonBox 组织按钮
- [ ] 处理按钮点击信号

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
