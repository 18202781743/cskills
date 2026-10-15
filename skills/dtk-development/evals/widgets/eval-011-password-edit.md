# Eval: 密码输入框

## 任务

创建一个密码输入框，要求：
1. 默认隐藏密码
2. 包含显示/隐藏切换按钮

## 期望输出

代码应：
1. #include <DPasswordEdit>
2. setEchoMode(QLineEdit::Password)
3. 内置显示/隐藏按钮
4. 未使用 QSS 硬编码颜色（应使用 DPalette）
5. 未使用 QApplication 替代 DApplication
6. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DPasswordEdit>
- [ ] setEchoMode(QLineEdit::Password)
- [ ] 内置显示/隐藏按钮

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
