# 应用加载接口

dtkdeclarative 的应用加载接口提供 DTK QML 应用的加载器、应用主窗口接口和应用预加载扩展接口。

## 开发包

当前版本使用 DTK6，开发包名为 `libdtk6declarative-dev`。该开发包提供 DTK6 的公开头文件和以下构建入口：

- CMake 包 `Dtk6Declarative` 与导出目标 `Dtk6::Declarative`
- pkg-config 模块 `dtk6declarative`
- qmake 模块 `dtkdeclarative`

仍需维护 DTK5 工程时，使用兼容开发包 `libdtkdeclarative-dev`。它提供 CMake 包 `DtkDeclarative`、导出目标 `Dtk::Declarative`、pkg-config 模块 `dtkdeclarative` 和同名 qmake 模块。

## 集成

### CMake 配置

CMake 是当前推荐的集成方式。DTK6 工程在已有构建目标上查找 `Dtk6Declarative` 并链接 `Dtk6::Declarative`：

```cmake
find_package(Dtk6Declarative REQUIRED)
target_link_libraries(your_target PRIVATE Dtk6::Declarative)
```

`your_target` 替换为使用方工程中的目标名。`Dtk6::Declarative` 会向该目标提供 dtkdeclarative 的头文件搜索路径、链接信息、编译定义和传递依赖，不需要再使用 `include_directories()`、`link_directories()` 或逐项链接 dtkdeclarative 所依赖的库。

仍使用 DTK5 的工程改为查找 `DtkDeclarative` 并链接 `Dtk::Declarative`：

```cmake
find_package(DtkDeclarative REQUIRED)
target_link_libraries(your_target PRIVATE Dtk::Declarative)
```

### 使用方式

构建目标链接 dtkdeclarative 后，可以直接包含所需类型的公开转发头：

```cpp
#include <DAppLoader>
```

也可以包含对应的实际公开头文件，例如 `#include <dapploader.h>`。公开 C++ 类型主要位于 `Dtk::Quick` 命名空间。QML 控件通过 `org.deepin.dtk` QML 模块使用，无需在 C++ 中包含头文件。

## 模块API介绍

### DAppLoader

#### 定位

DTK QML 应用的加载器。

#### 功能能力总结

以单例方式运行，负责初始化 QML 引擎、加载 QML 主文件并创建应用主窗口。支持设置应用元数据、QML 上下文属性和翻译加载。内部管理 QML 引擎生命周期，并在窗口关闭时处理应用退出逻辑。

#### 使用场景

作为 DTK QML 应用的入口点使用，通常由 DTK 应用模板自动调用，无需直接实例化。

### DQmlAppMainWindowInterface

#### 定位

DTK QML 应用主窗口的 C++ 扩展接口。

#### 功能能力总结

纯虚接口，定义 DTK QML 应用主窗口可供 C++ 插件扩展的行为契约。插件通过实现此接口向主窗口注入自定义功能。

#### 使用场景

C++ 插件需要扩展 DTK QML 应用主窗口行为时实现此接口。

### DQmlAppPreloadInterface

#### 定位

DTK QML 应用预加载的 C++ 扩展接口。

#### 功能能力总结

纯虚接口，定义在 QML 引擎加载主文件前执行预加载逻辑的契约。插件通过实现此接口在应用启动早期完成资源预加载、配置初始化操作。

#### 使用场景

C++ 插件需要在 QML 应用启动早期执行预加载逻辑时实现此接口。
