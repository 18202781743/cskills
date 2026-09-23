# Eval: CMake 配置 DTK6 依赖

## 任务

编写 CMakeLists.txt 配置 DTK6 依赖，要求：
1. 项目名 "myapp"
2. 依赖 Dtk6::Core、Dtk6::Gui、Dtk6::Widget
3. 链接到可执行目标

## 期望输出

CMakeLists.txt 应：
1. 使用 find_package 查找 DTK 组件
2. 使用 target_link_libraries 链接

## 验证要点

- [ ] find_package(Dtk6Core REQUIRED)
- [ ] find_package(Dtk6Gui REQUIRED)
- [ ] find_package(Dtk6Widget REQUIRED)
- [ ] target_link_libraries(myapp PRIVATE Dtk6::Core Dtk6::Gui Dtk6::Widget)

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，代码可编译或语法正确 |
| ⚠️ **PARTIAL** | 核心功能满足（第 1-2 项），但边缘检查项未通过 |
| ❌ **FAIL** | 核心功能未实现，或使用了禁止的模式

## 反模式检查

- [ ] 未混用 DTK5/Qt5 与 DTK6/Qt6
- [ ] CMake 中 AUTOMOC 和 AUTORCC 均已开启
