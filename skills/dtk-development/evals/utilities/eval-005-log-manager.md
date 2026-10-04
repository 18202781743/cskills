# Eval: 日志管理

## 任务

配置应用日志系统：
1. 注册控制台输出
2. 注册文件输出
3. 在实际使用日志的源文件声明 category

## 期望输出

代码应：
1. #include <DLog>
2. registerConsoleAppender()
3. registerFileAppender()
4. 使用 `DLogManager::registerConsoleAppender()` 和 `DLogManager::registerFileAppender()`
5. 未设置固定日志路径或日志格式
6. 使用处包含 `Q_LOGGING_CATEGORY`
7. 未直接使用 QPalette 而非 DPalette
8. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] #include <DLog>
- [ ] registerConsoleAppender()
- [ ] registerFileAppender()
- [ ] 使用 `DLogManager::registerConsoleAppender()` 和 `DLogManager::registerFileAppender()`
- [ ] 未设置固定日志路径或日志格式
- [ ] 使用处包含 `Q_LOGGING_CATEGORY`

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未直接使用 QPalette 而非 DPalette
- [ ] 未手动 setFont 而不使用 DFontSizeManager::bind
