# Eval: CMake 配置

## 任务

编写控制中心插件的 CMakeLists.txt：
1. 项目名 "myplugin"
2. 依赖 Dtk6::Core、Dtk6::Widget
3. 安装到正确路径

## 期望输出

代码应：
1. cmake_minimum_required(VERSION 3.16)
2. find_package(Dtk6 REQUIRED COMPONENTS Core Widget)
3. install(TARGETS myplugin LIBRARY DESTINATION lib/dde-control-center/plugins)

## 验证要点

- [ ] cmake_minimum_required(VERSION 3.16)
- [ ] find_package(Dtk6 REQUIRED COMPONENTS Core Widget)
- [ ] install(TARGETS myplugin LIBRARY DESTINATION lib/dde-control-center/plugins)

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查
- [ ] 插件根 QML 未依赖 dccData
- [ ] CMake 中 DdeControlCenter 和 Dtk6 版本不混用
