# Eval: 使用 DConfig 存储配置

## 任务

使用配置系统存储应用设置，要求：
1. 使用应用默认 appId
2. 读取键值 "window-width"，默认值 800
3. 写入新值 1024

## 期望输出

代码应：
1. 创建 DConfig 对象
2. 使用 value() 读取配置
3. 使用 setValue() 写入配置

## 验证要点

- [ ] #include <DConfig>
- [ ] 优先使用 `DConfig` 构造函数和 `DSGApplication::id()` 默认 appId
- [ ] 知道工程可通过 `DSG_APP_ID` 声明 appId，并保持应用身份一致
- [ ] 使用 value(key, fallback) 读取
- [ ] 使用 setValue(key, value) 写入
- [ ] 只有默认 appId 无法满足需求时才使用 `DConfig::create(appId, ...)`

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未使用 QSettings 替代 DConfig
- [ ] 配置服务不可用时未阻塞主窗口（应有 fallback）
- [ ] 未混淆 appId 与配置 ID
