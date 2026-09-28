# 集成与构建配置

使用 dtkcommon 的 CMake 包配置前，需要安装开发包 `libdtkcommon-dev`。该开发包提供 CMake 包配置文件和构建辅助函数，不提供链接库或公开头文件。

## 开发包

当前版本使用 DTK6，开发包名为 `libdtkcommon-dev`。该开发包提供以下构建入口：

- 伞式 CMake 包 `Dtk6`，通过组件查找 DTK6 各子模块；
- 构建辅助 CMake 包 `DtkBuildHelper`，提供 `dtk_gen_config_header` 等函数。

仍需维护 DTK5 工程时，使用同一开发包 `libdtkcommon-dev`，伞式 CMake 包名为 `Dtk`。

## CMake 集成

### 查找伞式包

DTK6 工程通过伞式包一次性引入多个 DTK 子模块：

```cmake
find_package(Dtk6 REQUIRED COMPONENTS Core Gui Widget)
```

`Dtk6` 包会依次查找每个指定的组件（对应 `Dtk6Core`、`Dtk6Gui`、`Dtk6Widget` 等），无需逐个 `find_package`。DTK5 兼容工程将包名改为 `Dtk`：

```cmake
find_package(Dtk REQUIRED COMPONENTS Core Gui Widget)
```

### 使用构建辅助函数

需要使用 dtkcommon 提供的构建辅助函数时，查找 `DtkBuildHelper`：

```cmake
find_package(DtkBuildHelper REQUIRED)
```

查找后可直接调用 `dtk_gen_config_header`、`dtk_setup_code_coverage` 和 `dtk_check_and_add_definitions` 函数。这些函数在 DTK5 和 DTK6 中均可使用。

## 主版本选择

dtkcommon 的开发包在 DTK5 和 DTK6 中同名，均为 `libdtkcommon-dev`。伞式 CMake 包名按主版本区分：DTK6 使用 `Dtk6`，DTK5 使用 `Dtk`。构建辅助包 `DtkBuildHelper` 在两个主版本中名称不变。

## 关联文档

- dtkcommon 不导出 C++ 类型，导出类型介绍见[导出类型介绍](modules.md)。
