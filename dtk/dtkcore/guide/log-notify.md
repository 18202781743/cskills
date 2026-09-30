# 日志与通知接口

dtkcore 的日志与通知接口提供日志管理（日志规则设置与日志文件定位）和桌面通知发送能力。

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

### DLogManager

#### 定位

日志输出通道的管理入口。

#### 功能能力总结

注册控制台、滚动文件及条件可用的系统日志输出通道，设置日志格式与文件位置。还可依据配置项调整进程的日志过滤规则；文件通道按天滚动并限制保留数量。

#### 使用场景

应用需要控制控制台、文件或系统日志输出时。

### DNotifySender

#### 定位

桌面通知的构造和发送入口。

#### 功能能力总结

逐步设置通知的摘要、应用名、图标、正文、替换标识、动作、提示数据和超时时间。完成后通过通知服务异步发送，并返回待完成调用对象。

#### 使用场景

需要指定标题、正文、动作或超时时间并发送通知时。
