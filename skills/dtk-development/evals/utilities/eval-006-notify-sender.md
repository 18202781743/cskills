# Eval: 系统通知

## 任务

发送系统桌面通知：
1. 发送简单通知
2. 发送带图标的通知
3. 处理通知点击

## 期望输出

代码应：
1. #include <DNotifySender>
2. DNotifySender(appName).title("标题").body("内容").call()
3. 未直接使用 QPalette 而非 DPalette
4. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DNotifySender>
- [ ] DNotifySender(appName).title("标题").body("内容").call()

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未直接使用 QPalette 而非 DPalette
- [ ] 未手动 setFont 而不使用 DFontSizeManager::bind
