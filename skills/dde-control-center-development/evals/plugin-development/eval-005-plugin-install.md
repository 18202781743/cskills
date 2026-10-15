# Eval: 插件安装路径

## 任务

配置控制中心插件的安装路径：
1. 库文件安装路径
2. 翻译文件安装路径
3. 资源文件安装路径

## 期望输出

代码应：
1. 库: lib/dde-control-center/plugins
2. 翻译: share/dde-control-center/translations
3. 资源: share/dde-control-center/resources

## 验证要点

- [ ] 库: lib/dde-control-center/plugins
- [ ] 翻译: share/dde-control-center/translations
- [ ] 资源: share/dde-control-center/resources

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 插件根 QML 未依赖 dccData
- [ ] CMake 中 DdeControlCenter 和 Dtk6 版本不混用
