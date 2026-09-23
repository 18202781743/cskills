# Eval: Debian 打包

## 任务

为控制中心插件创建 Debian 打包文件：
1. debian/control 文件
2. debian/rules 文件
3. debian/install 文件

## 期望输出

代码应：
1. Section: utils
2. Depends 包含 dde-control-center
3. debian/rules 使用 dh $@ --parallel

## 验证要点

- [ ] Section: utils
- [ ] Depends 包含 dde-control-center
- [ ] debian/rules 使用 dh $@ --parallel

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 插件根 QML 未依赖 dccData
- [ ] CMake 中 DdeControlCenter 和 Dtk6 版本不混用
