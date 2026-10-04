# Eval: 消息管理器

## 任务

在窗口内显示消息提示，要求：
1. 显示成功消息 "操作成功"
2. 3 秒后自动消失

## 期望输出

代码应：
1. #include <DMessageManager>
2. sendMessage() 发送消息
3. DFloatingMessage 类型
4. 未使用 QSS 硬编码颜色（应使用 DPalette）
5. 未使用 QApplication 替代 DApplication
6. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DMessageManager>
- [ ] sendMessage() 发送消息
- [ ] DFloatingMessage 类型

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
