# Eval: 输入框验证

## 任务

创建一个带验证的输入框，要求：
1. 验证邮箱格式
2. 格式错误时显示警告消息
3. 格式正确时清除警告

## 期望输出

代码应：
1. 使用 DLineEdit
2. 使用 setAlert() 控制警告状态
3. 使用 showAlertMessage() 显示错误提示

## 验证要点

- [ ] #include <DLineEdit>
- [ ] edit->setAlert(true) 显示警告
- [ ] edit->showAlertMessage("邮箱格式不正确")
- [ ] edit->setAlert(false) 清除警告

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
