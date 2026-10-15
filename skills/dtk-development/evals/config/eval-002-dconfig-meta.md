# DConfig meta 文件

## 任务

为应用配置编写元数据文件，要求：
1. 应用标识为 "com.example.app"
2. 包含一个字符串配置项（用户名）
3. 包含一个布尔配置项（是否启用）

## 期望输出

代码应：
1. JSON 格式正确
2. version 字段为 1.0
3. contents 对象包含配置项定义
4. 每个配置项有 key、value、visibility 等字段
5. 未使用 QSettings 替代 DConfig
6. 配置服务不可用时未阻塞主窗口（应有 fallback）
7. 未混淆 appId 与配置 ID

## 验证要点

- [ ] JSON 格式正确
- [ ] version 字段为 1.0
- [ ] contents 对象包含配置项定义
- [ ] 每个配置项有 key、value、visibility 等字段

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
