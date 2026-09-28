# 导出类型介绍

dtkdeclarative 提供 DTK QML 应用的加载器、应用主窗口接口与预加载接口、QML 场景中的帧缓冲区位块传输渲染与视口裁剪渲染、DTK 窗口及其附加属性。DTK5 还提供平台主题代理和系统调色板 QML 项。

## DAppLoader

### 定位

DTK QML 应用的加载器。

### 功能能力总结

以单例方式运行，负责初始化 QML 引擎、加载 QML 主文件并创建应用主窗口。支持设置应用元数据、QML 上下文属性和翻译加载。内部管理 QML 引擎生命周期，并在窗口关闭时处理应用退出逻辑。

### 使用场景

作为 DTK QML 应用的入口点使用，通常由 DTK 应用模板自动调用，无需直接实例化。

## DQmlAppMainWindowInterface

### 定位

DTK QML 应用主窗口的 C++ 扩展接口。

### 功能能力总结

纯虚接口（使用 `Q_DECLARE_INTERFACE` 声明），定义 DTK QML 应用主窗口可供 C++ 插件扩展的行为契约。插件通过实现此接口向主窗口注入自定义功能。

### 使用场景

C++ 插件需要扩展 DTK QML 应用主窗口行为时实现此接口。

## DQmlAppPreloadInterface

### 定位

DTK QML 应用预加载的 C++ 扩展接口。

### 功能能力总结

纯虚接口（使用 `Q_DECLARE_INTERFACE` 声明），定义在 QML 引擎加载主文件前执行预加载逻辑的契约。插件通过实现此接口在应用启动早期完成资源预加载、配置初始化操作。

### 使用场景

C++ 插件需要在 QML 应用启动早期执行预加载逻辑时实现此接口。

## DQuickBlitFramebuffer

### 定位

QML 场景中的帧缓冲区位块传输渲染项。

### 功能能力总结

继承 QQuickItem，将离屏帧缓冲区内容通过位块传输（blit）方式渲染到 QML 场景中。在 DTK6 中通过 `QML_NAMED_ELEMENT(BlitFramebuffer)` 注册为 QML 类型 `BlitFramebuffer`，可在 QML 中直接使用。

### 使用场景

需要将离屏渲染的帧缓冲区内容高效地呈现到 QML 场景中时。

## DQuickItemViewport

### 定位

QML 场景中的视口裁剪渲染项。

### 功能能力总结

继承 QQuickItem，提供将指定源项的局部区域裁剪并渲染到视口的能力。在 DTK6 中通过 `QML_NAMED_ELEMENT(ItemViewport)` 注册为 QML 类型 `ItemViewport`，可在 QML 中直接使用。

### 使用场景

需要在 QML 中实现视口裁剪或局部区域渲染时。

## DQuickWindow

### 定位

DTK QML 窗口类型。

### 功能能力总结

继承 QQuickWindow，提供 DTK 窗口特有的属性和行为，包括窗口圆角、模糊效果、窗口阴影在内的平台视觉属性的 QML 接口。在 DTK6 中通过 `QML_NAMED_ELEMENT(DWindow)` 注册为 QML 类型 `DWindow`，可在 QML 中直接使用。

### 使用场景

QML 中需要使用 DTK 扩展窗口属性（圆角、模糊、阴影）时。

## DQuickWindowAttached

### 定位

DTK 窗口附加属性提供者。

### 功能能力总结

继承 QObject，通过 `QML_ATTACHED` 机制为任意 QML Item 提供 DTK 窗口附加属性。使普通 QML Item 能够访问其所属 DTK 窗口的平台属性。

### 使用场景

需要在普通 QML Item 中访问所属 DTK 窗口的平台属性时。

## DPlatformThemeProxy

### 定位

平台主题的 QML 代理接口（仅 DTK5）。

### 功能能力总结

继承 QObject，将 DPlatformTheme 的平台主题属性（主题色、字号、图标主题）暴露为 QML 可访问的属性和信号。DTK6 已移除此类型，相关功能由 QML 层直接提供。

### 使用场景

DTK5 QML 应用中需要读取或监听平台主题属性变化时。

## DQuickSystemPalette

### 定位

QML 系统调色板项（仅 DTK5，已废弃）。

### 功能能力总结

继承 QObject，将系统调色板暴露为 QML 可访问的属性，支持 Active、Inactive、Disabled 三种颜色组。已废弃，应使用 `DQMLGlobalObject::palette` 替代。DTK6 已移除此类型。

### 使用场景

已废弃，DTK5 中如需在 QML 中访问系统调色板时可使用，新代码应迁移至 `DQMLGlobalObject::palette`。
