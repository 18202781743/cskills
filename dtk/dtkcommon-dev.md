# dtkcommon 二次开发接口文档

## 1. 包信息

| 项目 | 内容 |
|------|------|
| 包名 | libdtkcommon-dev |
| 版本 | 6.7.50 |
| 描述 | DTK 公共资源模块，提供 CMake 构建辅助宏、配置文件和公共定义，不包含编译库 |
| CMake target | 不适用（仅提供 CMake 模块文件） |
| find_package 名 | `Dtk` / `Dtk6` |
| 头文件安装路径 | 不适用（无公共头文件） |
| CMake 模块安装路径 | `${CMAKE_INSTALL_LIBDIR}/cmake/Dtk`、`${CMAKE_INSTALL_LIBDIR}/cmake/Dtk6` |
| 仓库地址 | https://github.com/linuxdeepin/dtkcommon.git |

## 2. 包依赖

### 运行时依赖
- 无（纯 CMake 模块，无运行时库）

### 开发依赖
- CMake >= 3.13
- Qt 6（或 Qt 5，取决于构建配置）

## 3. CMake 集成

dtkcommon 不产出编译库，仅安装 CMake 模块文件供其他 DTK 项目使用。

### find_package 用法

```cmake
# DTK6
find_package(Dtk6 REQUIRED)
# 或 DTK5
find_package(Dtk REQUIRED)
```

### 提供的 CMake 模块

| 模块 | 说明 |
|------|------|
| `DtkBuildHelper.cmake` | 构建辅助函数，如 `dtk_gen_config_header()` 生成版本头文件 |
| `DtkCMakeConfig.cmake` | DTK CMake 基础配置 |
| `DtkToolsConfig.cmake` | DTK 工具宏（DConfig 宏、DBus 宏、设置宏等） |
| `DtkDConfigConfig.cmake` | DConfig 配置文件处理宏 |

### dtk_gen_config_header 示例

```cmake
find_package(Dtk6 REQUIRED)

# 生成包含版本信息的头文件 dtkcommon_config.h
dtk_gen_config_header(${CMAKE_CURRENT_BINARY_DIR}/dtkcommon_config.h
    DTKCOMMON_VERSION
    DTK_VERSION_MAJOR
    DTK_VERSION_MINOR
    DTK_VERSION_PATCH
)
```

### 安装的 CMake 配置文件路径

- `${CMAKE_INSTALL_LIBDIR}/cmake/Dtk/DtkConfig.cmake`
- `${CMAKE_INSTALL_LIBDIR}/cmake/Dtk6/Dtk6Config.cmake`
- `${CMAKE_INSTALL_DATAROOTDIR}/dsg/` 下的配置文件

## 4. pkg-config

不适用（无 .pc 文件）

## 5. 命名空间

不适用（无 C++ 代码）

## 6. 关键公共类及功能描述

不适用（无 C++ 库）

dtkcommon 提供的关键 CMake 宏：

| 宏/函数 | 功能 |
|---------|------|
| `dtk_gen_config_header()` | 根据项目版本生成版本头文件 |
| `dtk_add_config_meta_files()` | 注册 DConfig 元数据文件 |
| `dtk_install_dconfig()` | 安装 DConfig 配置文件 |

## 7. QML 模块

不适用

## 8. DBus 接口

不适用

## 9. 插件开发

不适用
