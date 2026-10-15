# Eval: 单实例应用

## 任务

实现单实例应用程序：
1. 设置与可执行文件一致的 applicationName
2. 检查是否已有实例运行
3. 第二个进程退出，原窗口从隐藏或最小化状态恢复并激活
4. 将第二个进程的文件或命令行参数交给原进程处理

## 期望输出

代码应：
1. `DApplication::setApplicationName()` 与可执行文件名一致
2. `DApplication::setSingleInstance("唯一应用 ID")`
3. `newInstanceStarted` 或等价新实例信号
4. `showNormal()`/`show()`、`raise()`、`activateWindow()`
5. 新实例参数未被丢弃
6. 未使用 QSS 硬编码颜色（应使用 DPalette）
7. 未使用 QApplication 替代 DApplication
8. 未手动 setFont 而不使用 DFontSizeManager::bind

## 验证要点

- [ ] `DApplication::setApplicationName()` 与可执行文件名一致
- [ ] `DApplication::setSingleInstance("唯一应用 ID")`
- [ ] `newInstanceStarted` 或等价新实例信号
- [ ] `showNormal()`/`show()`、`raise()`、`activateWindow()`
- [ ] 新实例参数未被丢弃

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
