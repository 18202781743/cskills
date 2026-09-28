# 导出类型介绍

dtkcommon 提供 CMake 包配置和构建辅助函数，不构建 C++ 库，不安装公开头文件，因此没有对外导出的 C++ 类、结构体或类模板。

dtkcommon 提供的构建辅助函数 `dtk_gen_config_header` 可根据版本号生成版本配置头文件；`dtk_setup_code_coverage` 用于为目标设置代码覆盖率编译选项；`dtk_check_and_add_definitions` 用于检查并添加编译定义。这些函数由 CMake 模块提供，不是 C++ 导出类型，不在本篇逐条展开。
