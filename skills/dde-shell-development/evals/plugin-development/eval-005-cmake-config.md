# Eval: 配置 CMake 构建

## 任务

用户有一个 dde-shell 插件项目，需要配置 CMake 构建和翻译。

指导用户正确配置 CMakeLists.txt。

## 期望输出

回答应：
1. 展示 find_package 和 target_link_libraries
2. 展示 ds_install_package 用法
3. 展示 ds_handle_package_translation 用法
4. 说明安装路径

## 验证要点

- [ ] find_package(DDEShell REQUIRED)
- [ ] target_link_libraries(... PRIVATE Dde::Shell)
- [ ] ds_install_package(PACKAGE <id> TARGET <libname>)
- [ ] ds_handle_package_translation(PACKAGE <id>)
- [ ] 说明安装路径：/usr/share/dde-shell/<id>/ 和 /usr/lib/dde-shell/plugins/

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 未混用 dde-tray-loader 的 IID
- [ ] 元数据中 pluginType 与实际类型匹配
