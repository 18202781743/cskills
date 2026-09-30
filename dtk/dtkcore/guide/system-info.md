# 系统信息与许可接口

dtkcore 的系统信息与许可接口提供发行版、产品、组织、架构及主机硬件与运行状态查询，应用标识查询，以及许可信息（含组件级许可）读取能力。

## 开发包

当前版本使用 DTK6，开发包名为 `libdtk6core-dev`。该开发包提供 DTK6 的公开头文件和以下构建入口：

- CMake 包 `Dtk6Core` 与导出目标 `Dtk6::Core`
- pkg-config 模块 `dtk6core`
- qmake 模块 `dtkcore`

仍需维护 DTK5 工程时，使用兼容开发包 `libdtkcore-dev`。它提供 CMake 包 `DtkCore`、导出目标 `Dtk::Core`、pkg-config 模块 `dtkcore` 和同名 qmake 模块。

## 集成

### CMake 配置

CMake 是当前推荐的集成方式。DTK6 工程在已有构建目标上查找 `Dtk6Core` 并链接 `Dtk6::Core`：

```cmake
find_package(Dtk6Core REQUIRED)
target_link_libraries(your_target PRIVATE Dtk6::Core)
```

`your_target` 替换为使用方工程中的目标名。`Dtk6::Core` 会向该目标提供 dtkcore 的头文件搜索路径、链接信息、编译定义和传递依赖，不需要再使用 `include_directories()`、`link_directories()` 或逐项链接 dtkcore 所依赖的库。

仍使用 DTK5 的工程改为查找 `DtkCore` 并链接 `Dtk::Core`：

```cmake
find_package(DtkCore REQUIRED)
target_link_libraries(your_target PRIVATE Dtk::Core)
```

### 使用方式

构建目标链接 dtkcore 后，可以直接包含所需类型的公开转发头：

```cpp
#include <DConfig>
```

也可以包含对应的实际公开头文件，例如 `#include <dconfig.h>`。公开类型主要位于 `Dtk::Core` 命名空间，可使用完整限定名，也可在合适的作用域使用 `DCORE_USE_NAMESPACE`。

## 模块API介绍

### DSysInfo

#### 定位

系统信息的公开类型。

#### 功能能力总结

查询发行版、产品、组织、架构及主机硬件与运行状态。信息可来自系统文件或外部命令；部分结果缓存，运行时长查询会重新读取状态。

#### 使用场景

需要根据产品信息展示内容，或读取主机运行信息时。

### DSGApplication

#### 定位

应用标识的公开类型。

#### 功能能力总结

查询当前进程或指定进程的应用标识。当前进程的结果可来自启动环境、应用管理服务或本地进程信息，因此与启动方式有关。

#### 使用场景

需要将配置归属或服务请求关联到应用标识时。

### DLicenseInfo

#### 定位

授权数据的加载入口。

#### 功能能力总结

从内容或文件加载授权信息，形成组件清单。可按许可证名称取得正文，并允许设置许可证文件的搜索路径。

#### 使用场景

需要从内容或文件载入组件清单时。

### DLicenseInfo::DComponentInfo

#### 定位

单个组件信息。

#### 功能能力总结

描述单个组件的名称、版本、版权和许可证名称。调用者从授权信息对象取得组件集合后，通过该类型读取每个组件的属性。

#### 使用场景

需要展示组件名称、版本、版权和许可证名称时。
