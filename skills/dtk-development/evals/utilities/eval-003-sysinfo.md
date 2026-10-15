# Eval: 系统信息

## 任务

获取系统信息（如产品类型、版本等）：
1. 获取系统版本
2. 获取产品名称
3. 判断是否为社区版

## 期望输出

代码应：
1. #include <DSysInfo>
2. DSysInfo::distributionInfo()
3. DSysInfo::majorVersion()
4. 未直接使用 QPalette 而非 DPalette
5. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DSysInfo>
- [ ] DSysInfo::distributionInfo()
- [ ] DSysInfo::majorVersion()

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未直接使用 QPalette 而非 DPalette
- [ ] 未手动 setFont 而不使用 DFontSizeManager::bind
