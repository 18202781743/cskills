# Eval: 浮动按钮

## 任务

创建一个浮动操作按钮，要求：
1. 显示增加图标（加号）
2. 点击时执行添加操作

## 期望输出

代码应：
1. #include <DFloatingButton>
2. 构造函数传入 DStyle::SP_IncreaseElement
3. 连接 clicked 信号
4. 未使用 QSS 硬编码颜色（应使用 DPalette）
5. 未使用 QApplication 替代 DApplication
6. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DFloatingButton>
- [ ] 构造函数传入 DStyle::SP_IncreaseElement
- [ ] 连接 clicked 信号

## 参考

参见 [按钮控件](../../references/widgets/button.md) 了解 DFloatingButton 的用法。

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未使用 QSS 硬编码颜色（应使用 DPalette）
- [ ] 未使用 QApplication 替代 DApplication
- [ ] 未手动 setFont 而不使用 DFontSizeManager::bind
