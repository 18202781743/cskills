# Eval: 翻译配置

## 任务

为控制中心插件配置翻译：
1. 创建 .ts 文件
2. CMake 配置 qt_add_translations
3. 加载翻译文件

## 期望输出

代码应：
1. qt_add_translations() 添加翻译文件
2. 翻译文件命名格式: pluginname_zh_CN.ts
3. install() 安装 .qm 文件

## 验证要点

- [ ] qt_add_translations() 添加翻译文件
- [ ] 翻译文件命名格式: pluginname_zh_CN.ts
- [ ] install() 安装 .qm 文件

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 插件根 QML 未依赖 dccData
- [ ] CMake 中 DdeControlCenter 和 Dtk6 版本不混用
