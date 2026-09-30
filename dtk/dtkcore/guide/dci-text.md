# DCI 与文本处理接口

dtkcore 的 DCI 与文本处理接口提供 DCI 容器的加载、节点查询、数据读取与写出，文本编码探测与字符集转换，以及安全字符串管理能力。

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

### DDciFile

#### 定位

DCI 容器的读取、修改和写出入口。

#### 功能能力总结

从文件路径或字节内容加载 DCI 容器，并按路径查询目录、文件与符号链接节点。读取文件数据时可取得与容器内部数据共享存储的字节内容；修改先发生在内存中，可再写出到文件、设备或字节。可选的文件引擎注册使常规文件接口读取容器内内容。

#### 使用场景

需要把图标内容组织在单个 DCI 文件中，或读取其中指定路径时。

### DTextEncoding

#### 定位

编码探测与转换入口。

#### 功能能力总结

探测内存内容或文件的文本编码，并在指定字符集之间转换。转换可在内存中完成，也可写入文件；未指定源编码时可先尝试探测。

#### 使用场景

需要在不同字符集之间转换内容或文件时。

### DSecureString

#### 定位

敏感字符串的公开类型。

#### 功能能力总结

保留 Qt 字符串的构造与使用方式，在对象销毁时擦除自己持有的内容。复制品各自持有内容，也各自在销毁时执行擦除。

#### 使用场景

需要短暂持有敏感文本时。
