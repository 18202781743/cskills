# Eval: 输入框警告状态

## 任务

创建一个邮箱输入框，要求：
1. 验证邮箱格式
2. 格式错误时显示警告边框和提示消息
3. 格式正确时清除警告

## 期望输出

代码应：
1. #include <DLineEdit>
2. setAlert(true) 显示警告状态
3. showAlertMessage() 显示提示消息
4. setAlert(false) 清除警告
5. 未使用 QSS 硬编码颜色（应使用 DPalette）
6. 未使用 QApplication 替代 DApplication
7. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DLineEdit>
- [ ] setAlert(true) 显示警告状态
- [ ] showAlertMessage() 显示提示消息
- [ ] setAlert(false) 清除警告

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
