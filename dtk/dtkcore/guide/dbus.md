# DBus 通信接口

dtkcore 的 DBus 通信接口提供链式 DBus 调用构造、方法调用参数追加与异步提交、远端属性读写、扩展接口代理（含属性缓存与批量获取）以及接口导出能力。调用方可通过链式入口依次指定总线、服务、路径和接口，再选择方法或属性操作。

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

### DDBusCaller

#### 定位

一次方法调用及其参数的载体。

#### 功能能力总结

在已选定远端方法后，追加调用参数并发起异步请求。提交后返回待完成调用对象，调用方可据此取得远端结果。

#### 使用场景

需要追加调用参数并异步提交方法时。

### DDBusData

#### 定位

一次调用使用的连接与定位信息。

#### 功能能力总结

保存一次远端操作所需的服务名、对象路径、接口名和总线连接。链式发送器、方法调用与属性访问对象共用这些定位信息。

#### 使用场景

需要在链式调用中共享服务与路径信息时。

### DDBusExtendedAbstractInterface

#### 定位

扩展的远端接口代理。

#### 功能能力总结

在远端接口代理上提供同步和异步属性访问、属性缓存及批量获取。还支持服务状态感知、属性变化通知和启动远端服务。

#### 使用场景

需要异步属性访问、缓存或批量读取时。

### DDBusProperty

#### 定位

远端属性访问的载体。

#### 功能能力总结

针对已选定的远端属性发起读取或写入。操作以异步方式提交，并返回待完成调用对象。

#### 使用场景

需要读取或写入已定位的 DBus 属性时。

### DDBusSender

#### 定位

链式 DBus 调用的构造入口。

#### 功能能力总结

依次指定总线连接、服务、对象路径和接口，再选择方法或属性操作。方法操作交给调用对象追加参数，属性操作交给属性对象完成读写。

#### 使用场景

需要拼装服务、路径、接口和方法调用时。

### DExportedInterface

#### 定位

向会话总线导出动作的类型。

#### 功能能力总结

登记动作名称、描述与处理函数，并把调用入口注册到会话总线。远端进程可按动作名触发处理；类型也提供动作说明供外部发现。

#### 使用场景

需要让其他进程发现并触发应用动作时。
