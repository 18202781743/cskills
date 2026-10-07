# dtkdeclarative-dev

dtkdeclarative 的应用加载接口提供 DTK QML 应用的加载器、应用主窗口接口和应用预加载扩展接口。

dtkdeclarative 的快速渲染接口提供 QML 场景中的帧缓冲区位块传输渲染和视口裁剪渲染能力。

dtkdeclarative 的 QML 窗口接口提供 DTK 窗口及其附加属性，用于在 QML 场景中控制窗口外观与行为。

dtkdeclarative 的 DTK5 主题兼容接口提供平台主题代理和系统调色板 QML 项，仅在 DTK5 中提供，DTK6 已移除。


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

也可以包含对应的实际公开头文件，例如 `#include <dapploader.h>`。公开 C++ 类型主要位于 `Dtk::Quick` 命名空间。QML 控件通过 [org.deepin.dtk](org.deepin.dtk.md) 使用，设置模型与窗口通过 [org.deepin.dtk.settings](org.deepin.dtk.settings.md) 使用。


---


## 应用加载

### DAppLoader

#### 定位

分阶段加载 DTK QML 应用插件的入口。

#### 功能能力总结

构造时指定应用名称和可选路径，可追加和查询插件搜索路径，调用 exec 创建应用并进入事件循环。它通过 DQmlAppPreloadInterface 和 DQmlAppMainWindowInterface 分阶段加载预加载窗口与主组件，加载完成发出 loadFinished；instance 返回已经创建的加载器，默认构造函数已删除。

#### 使用场景

应用由预加载插件和主组件插件构成时，在入口函数中构造加载器并调用 exec。


---

### DQmlAppMainWindowInterface

#### 定位

主组件插件的 QML 地址与引擎初始化契约。

#### 功能能力总结

主组件插件必须实现 mainComponentPath 提供 QML 主组件地址；initialize 在加载前配置 QQmlApplicationEngine，finishedLoading 在加载完成后处理引擎。通过 Qt 插件接口声明接入 DAppLoader。

#### 使用场景

实现由 DAppLoader 发现和加载的主组件插件时。


---

### DQmlAppPreloadInterface

#### 定位

DTK QML 应用预加载的 C++ 扩展接口。

#### 功能能力总结

预加载插件必须实现 preloadComponentPath，aboutToPreload 在预加载前配置引擎。可通过 creatApplication 创建应用对象、通过 graphicsApi 选择图形 API；公开方法的拼写为 creatApplication。

#### 使用场景

C++ 插件需要在 QML 应用启动早期执行预加载逻辑时实现此接口。


---


## 快速渲染

### DQuickBlitFramebuffer

#### 定位

QML 场景中的帧缓冲区位块传输渲染项。

#### 功能能力总结

继承 QQuickItem，捕获其绘制位置之前的场景帧缓冲区内容，并通过 textureProvider 提供纹理供其他 Quick 项使用；不接收调用者提供的外部帧缓冲区。

#### 使用场景

需要读取场景背景纹理供其他 Quick 项采样时。


---

### DQuickItemViewport

#### 定位

QML 场景中的视口裁剪渲染项。

#### 功能能力总结

通过 sourceItem 与 sourceRect 指定源项和区域，支持圆角、固定区域与 hideSource。DTK6 增加 compositionMode 及重置入口；属性变化发出相应通知，适用于图像复制与裁剪。

#### 使用场景

需要在 QML 中实现视口裁剪或局部区域渲染时。


---


## QML 窗口

### DQuickWindow

#### 定位

DTK QML 窗口类型。

#### 功能能力总结

继承 QQuickWindow，提供 attached 与 qmlAttachedProperties 取得 DQuickWindowAttached。QML 中注册名为 DWindow，作为附加属性入口使用，不能通过 DWindow 直接创建窗口。

#### 使用场景

QML 中需要使用 DTK 扩展窗口属性（圆角、模糊、阴影）时。


---

### DQuickWindowAttached

#### 定位

窗口与弹出控件的平台附加属性对象。

#### 功能能力总结

关联 QWindow 或 Popup 对象，提供窗口装饰、透明与模糊、系统移动和缩放、窗口类型与功能标志，以及加载覆盖层和转场。支持窗口最小化、最大化、全屏、恢复、系统菜单与分屏菜单；DTK6 增加 themeType、windowEffect 和 windowStartUpEffect。

#### 使用场景

需要为 QQuickWindow 或 Popup 调整 DTK 装饰、交互与加载状态时。


---

## DTK5 主题兼容

### DPlatformThemeProxy

#### 定位

平台主题的 QML 代理接口（仅 DTK5）。

#### 功能能力总结

仅 DTK5 安装公开头文件。代理 DPlatformTheme 的字体、主题名、图标主题、鼠标交互参数、活动颜色、调色板与 DPI，可读写属性并接收变更通知；它是平台主题对象的代理，不负责 QML 控件布局。

#### 使用场景

DTK5 QML 应用中需要读取或监听平台主题属性变化时。


---

### DQuickSystemPalette

#### 定位

QML 系统调色板项（仅 DTK5，已废弃）。

#### 功能能力总结

仅 DTK5 提供，已废弃。按 Active、Inactive、Disabled 颜色组暴露系统调色板和 DTK 语义颜色，以 paletteChanged 通知更新；新代码使用 QML DTK.palette。

#### 使用场景

已废弃，DTK5 中如需在 QML 中访问系统调色板时可使用，新代码应迁移至 `DQMLGlobalObject::palette`。
