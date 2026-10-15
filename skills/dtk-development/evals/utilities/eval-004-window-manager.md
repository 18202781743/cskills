# Eval: 窗口管理助手

## 任务

检查窗口管理器支持的特性：
1. 检查是否支持模糊效果
2. 检查是否支持窗口圆角
3. 获取窗口管理器类型

## 期望输出

代码应：
1. #include <DWindowManagerHelper>
2. hasBlurWindow()
3. hasComposite()
4. 未直接使用 QPalette 而非 DPalette
5. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DWindowManagerHelper>
- [ ] hasBlurWindow()
- [ ] hasComposite()

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未直接使用 QPalette 而非 DPalette
- [ ] 未手动 setFont 而不使用 DFontSizeManager::bind
