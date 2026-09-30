# QML 自定义样式

> 仅适用于 v25 DTK QML。

## 任务

在 QML 中创建自定义样式组件，要求：
1. 控件外观可配置
2. 支持状态变化（hover、pressed、disabled）
3. 颜色随主题自动切换

## 期望输出

代码应：
1. 创建 QML 组件文件
2. 使用 ColorSelector 获取状态颜色
3. 定义 style 属性或使用 FlowStyle
4. 未从鼠标位置判断状态（应使用 QStyleOption::state）
5. initFrom() 后手动设置了 checked/down/selected 状态
6. 未使用 QSS 替代 DPalette/DStyle 绘制

## 验证要点

- [ ] 创建 QML 组件文件
- [ ] 使用 ColorSelector 获取状态颜色
- [ ] 定义 style 属性或使用 FlowStyle

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未从鼠标位置判断状态（应使用 QStyleOption::state）
- [ ] initFrom() 后手动设置了 checked/down/selected 状态
- [ ] 未使用 QSS 替代 DPalette/DStyle 绘制
