# Chameleon 风格机制

## 任务

分别处理一个 QWidget 风格问题和一个 v25 QML 风格问题，要求：
1. 先判定当前 UI 技术栈，只加载对应的 Chameleon 专篇
2. 说明控件如何获取状态颜色
3. 说明调色板如何影响控件外观
4. 需要比较两套实现时分别读取两个专篇

## 期望输出

代码应：
1. 理解 ChameleonStyle 是 QStyle 插件
2. 理解 DStyleHelper 状态颜色计算
3. 理解 DPalette 与 Chameleon 的关系
4. 未使用 QSS 替代 DPalette
5. 未使用绝对路径查找 DCI 图标
6. 未滥用 setDciThemeSearchPaths()

## 验证要点

- [ ] 理解 ChameleonStyle 是 QStyle 插件
- [ ] 理解 DStyleHelper 状态颜色计算
- [ ] 理解 DPalette 与 Chameleon 的关系

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未使用 QSS 替代 DPalette
- [ ] 未使用绝对路径查找 DCI 图标
- [ ] 未滥用 setDciThemeSearchPaths()
