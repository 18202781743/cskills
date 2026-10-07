# dtkgui-dev

dtkgui 的 DCI 图标接口提供 DCI 图标资源的加载、渲染与动画播放能力，包括图标容器、单帧图像访问、图像序列播放器、内嵌调色板和整体动画播放器。

dtkgui 的文件拖拽、字体与缩略图接口提供跨进程文件拖拽的客户端与服务端、字号与基础字体管理和文件缩略图异步生成能力。

dtkgui 的图标与 SVG 渲染接口提供 DTK 图标加载、图标主题缓存管理、SVG 渲染和图像格式处理能力。

dtkgui 的调色板与主题接口提供 DTK 扩展调色板角色、应用级主题管理、原生设置读写和平台主题属性访问能力。

dtkgui 的系统服务接口提供系统服务调用（打开文件管理器、播放系统提示音）、屏幕区域监视和任务栏进度与计数控制能力。

dtkgui 的窗口与平台接口提供窗口平台属性控制、窗口管理器功能查询、跨进程窗口分组和外部窗口引用能力。


## 开发包

当前版本使用 DTK6，开发包名为 `libdtk6gui-dev`。该开发包提供 DTK6 的公开头文件和以下构建入口：

- CMake 包 `Dtk6Gui` 与导出目标 `Dtk6::Gui`
- pkg-config 模块 `dtk6gui`
- qmake 模块 `dtkgui`

仍需维护 DTK5 工程时，使用兼容开发包 `libdtkgui-dev`。它提供 CMake 包 `DtkGui`、导出目标 `Dtk::Gui`、pkg-config 模块 `dtkgui` 和同名 qmake 模块。


## 集成

### CMake 配置

CMake 是当前推荐的集成方式。DTK6 工程在已有构建目标上查找 `Dtk6Gui` 并链接 `Dtk6::Gui`：

```cmake
find_package(Dtk6Gui REQUIRED)
target_link_libraries(your_target PRIVATE Dtk6::Gui)
```

`your_target` 替换为使用方工程中的目标名。`Dtk6::Gui` 会向该目标提供 dtkgui 的头文件搜索路径、链接信息、编译定义和传递依赖，不需要再使用 `include_directories()`、`link_directories()` 或逐项链接 dtkgui 所依赖的库。

仍使用 DTK5 的工程改为查找 `DtkGui` 并链接 `Dtk::Gui`：

```cmake
find_package(DtkGui REQUIRED)
target_link_libraries(your_target PRIVATE Dtk::Gui)
```

### 使用方式

构建目标链接 dtkgui 后，可以直接包含所需类型的公开转发头：

```cpp
#include <DPalette>
```

也可以包含对应的实际公开头文件，例如 `#include <dpalette.h>`。公开类型主要位于 `Dtk::Gui` 命名空间，可使用完整限定名，也可在合适的作用域使用 `DGUI_USE_NAMESPACE`。开发包还提供便捷头 `DtkGuis`，一次引入所有已安装的公开头文件。


---


## DCI 图标

### DDciIcon

#### 定位

DCI 图标资源的容器与渲染入口。

#### 功能能力总结

从 DCI 文件、路径或字节构造图标，按尺寸、Light 或 Dark 主题及 Normal、Disabled、Hover、Pressed 模式匹配图像，查询可用尺寸和调色板能力。支持按设备像素比生成像素图、绘制、取得可播放图像和按主题名称查找；匹配标志控制回退及边距计算。

#### 使用场景

需要加载和渲染 DCI 格式图标时；需要支持多主题、多分辨率图标显示时。


---

### DDciIconImage

#### 定位

已匹配 DCI 图像及其动画帧的访问对象。

#### 功能能力总结

持有一个已匹配的 DCI 图像，可按 DDciIconPalette 输出 QImage 或直接绘制。支持动画能力判断、遍历图像帧、查询帧数、当前帧编号与时长及循环次数，并可重置或交换。

#### 使用场景

需要对 DCI 图标的单帧图像进行自定义绘制或逐帧动画处理时。


---

### DDciIconImagePlayer

#### 定位

DCI 图标图像序列的动画播放器。

#### 功能能力总结

播放 DCI 图像序列，设置调色板和循环次数，读取当前帧或图像并管理缓存。start 接收速度及继续播放、反向、缓存与循环策略标志，支持停止和中止循环；通过 started、updated、finished 和 stateChanged 通知播放状态。

#### 使用场景

需要播放 DCI 图标中的动画序列时。


---

### DDciIconPalette

#### 定位

DCI 图标内嵌调色板。

#### 功能能力总结

保存前景、背景、高亮和高亮前景四种颜色，支持角色枚举、颜色读写、相等比较、字符串编码与解码，以及从 QPalette 构造。

#### 使用场景

需要为 DCI 图标设置自定义主题颜色时；需要序列化或反序列化 DCI 调色板时。


---

### DDciIconPlayer

#### 定位

DCI 图标整体的动画播放器。

#### 功能能力总结

管理一个 DDciIcon 的主题、模式、图标尺寸、设备像素比和调色板。play 按指定模式与播放标志播放状态图像，提供当前帧、停止和中断，通过 updated、stateChanged 和 modeChanged 通知变化。

#### 使用场景

需要播放完整 DCI 图标（而非单帧序列）的动画时。


---


## 文件拖拽、字体与缩略图

### DFileDrag

#### 定位

向拖拽 MIME 数据写入跨进程会话标识的 QDrag。

#### 功能能力总结

继承 QDrag，构造时关联 DFileDragServer 与源对象，设置 MIME 数据后加入会话信息；接收方回传目标 URL 时可查询 targetUrl 并收到 targetUrlChanged。

#### 使用场景

作为拖拽源发起可回传目标信息和处理进度的文件拖拽时。


---

### DFileDragClient

#### 定位

拖拽接收方访问源进程会话的客户端。

#### 功能能力总结

从 MIME 数据建立客户端，检查 MIME 是否包含 DTK 拖拽会话，读取源进程提供的进度和 DFileDragState，并通知变化或服务对象销毁。可把任意目标数据或目标 URL 回传给源进程。

#### 使用场景

接收 DTK 文件拖拽后，需要通知目标路径或观察源端处理状态时。


---

### DFileDragServer

#### 定位

拖拽源进程对外提供的会话服务对象。

#### 功能能力总结

读取接收方回传的键值数据，并设置进度与 DFileDragState 向客户端发布状态；targetDataChanged 通知接收方修改目标数据。它与 DFileDragClient 均直接继承 QObject，不互相派生。

#### 使用场景

需要在拖拽源进程中维护一次跨进程拖拽的处理状态时。


---

### DFontManager

#### 定位

DTK 字号层级与基础字体的管理对象。

#### 功能能力总结

管理 T1 至 T11 字号和 baseFont，查询、设置字号的像素值，并基于字号与基础字体生成 QFont。基础字体与字号变化通过 fontChanged 通知；不提供字体文件安装或卸载功能。

#### 使用场景

需要生成统一规格字体或响应基础字体和字号变化时。


---

### DThumbnailProvider

#### 定位

文件缩略图异步生成器。

#### 功能能力总结

以单例 QThread 提供 Small、Normal、Large 缩略图规格，查询文件或 MIME 类型是否支持、缓存路径与文件大小限制。可直接生成或加入队列并指定回调，支持移除待处理项、读取错误及接收成功、失败和缩略图变化通知。

#### 使用场景

需要为文件生成预览缩略图时。


---


## 图标与 SVG 渲染

### DIcon

#### 定位

DTK 图标类型，扩展 Qt 图标的图标加载能力。

#### 功能能力总结

继承 QIcon，支持按目标尺寸、设备像素比、模式和状态生成像素图，提供 loadNxPixmap 加载适合设备像素比的图片。

#### 使用场景

需要加载多分辨率位图图标时。


---

### DIconTheme::Cached

#### 定位

DTK 图标主题查找的缓存管理器。

#### 功能能力总结

DIconTheme 命名空间中的缓存对象，设置最大缓存成本并清空缓存，通过图标名与 Options 查找 QIcon 或 DCI 文件。Options 可控制 Qt 回退及忽略内置图标、DCI 图标和缓存；主题搜索路径管理和图标来源判断由命名空间自由函数完成。

#### 使用场景

需要重复查找图标并控制独立缓存容量时。


---

### DSvgRenderer

#### 定位

SVG 图像渲染器。

#### 功能能力总结

从文件或字节加载 SVG，查询有效性、默认尺寸、视图区域、指定元素是否存在及其边界。支持更改视图区域、渲染全部或指定元素到 QPainter，以及生成指定尺寸的 QImage。

#### 使用场景

需要加载和渲染 SVG 图像到自定义绘制设备时。


---

### DImageHandler

#### 定位

图像格式处理工具（已废弃）。

#### 功能能力总结

已废弃。读取图像、生成缩略图、查询格式、尺寸和元数据，保存或旋转图像，报告读写能力与错误。还提供色彩滤镜、锐化、边缘检测、亮度与对比度调整及翻转；基于 FreeImage 和 LibRaw 的扩展格式支持默认关闭，新代码使用 QImageReader 与 QImageWriter。

#### 使用场景

已废弃，应使用图像读写库或其他图像库替代。


---


## 调色板与主题

### DPalette

#### 定位

DTK 扩展调色板，在 Qt 调色板基础上增加 DTK 专属颜色角色。

#### 功能能力总结

继承 QPalette，增加 ItemBackground、TextTitle、TextTips、TextWarning、TextLively、LightLively、DarkLively、FrameBorder、PlaceholderText、FrameShadowBorder、ObviousBackground 语义角色，支持按颜色组读写颜色与画刷、查询状态和序列化。

#### 使用场景

需要使用 DTK 专属调色板角色设置控件颜色时。


---

### DGuiApplicationHelper

#### 定位

GUI 层面的全局辅助工具与应用级主题管理。

#### 功能能力总结

以单例方式管理应用主题、调色板、字体与尺寸模式，提供颜色调整、混合、标准调色板及状态颜色生成。可查询平台与环境能力、控制属性、加载翻译、设置单实例及打开帮助；通过主题、字体、调色板、尺寸模式和新实例信号通知变化。

#### 使用场景

需要读取或修改应用级主题外观（亮色/暗色、主题色、字号）时；需要响应主题变化信号时。


---

### DNativeSettings

#### 定位

关联平台窗口标识与设置域的属性读写对象。

#### 功能能力总结

构造时传入窗口标识和可选 domain，查询 isValid 与 allKeys，按名称读写 QVariant 设置值，并通过 propertyChanged、allKeysChanged 接收变化。实际存储和同步由平台设置后端提供。

#### 使用场景

需要直接访问平台设置域，或实现 DPlatformTheme 同类代理时。


---

### DPlatformTheme

#### 定位

平台主题与交互参数的访问对象。

#### 功能能力总结

继承 DNativeSettings，支持父主题回退、调色板读取与合成、主题名、图标和声音主题、字体、活动颜色、光标闪烁及鼠标交互参数、DPI 和窗口圆角。提供尺寸模式与滚动条策略读取和属性变化通知；DTK5 保留逐颜色角色访问，DTK6 通过 DPalette 获取。

#### 使用场景

需要读取平台主题或为应用生成跟随系统的字体和颜色时。


---

## 系统服务

### DDesktopServices

#### 定位

DTK 系统服务调用入口，提供静态方法集合。

#### 功能能力总结

以本地路径或 URL 请求文件管理器打开目录、定位文件、显示文件属性或移入回收站，支持单项与批量操作。提供系统音效播放、预听与音效名称转换，并通过 errorMessage 取得错误说明。

#### 使用场景

需要在应用中调用文件管理器打开文件或播放系统提示音时。


---

### DRegionMonitor

#### 定位

指定屏幕区域的输入事件监视器。

#### 功能能力总结

设置 watchedRegion、注册事件标志与 ScaleRatio 或 Original 坐标模式，注册、注销并查询注册状态；报告鼠标按下、释放、移动、进入、离开和键盘按下、释放。

#### 使用场景

需要在指定全局屏幕区域接收输入事件通知时。


---

### DTaskbarControl

#### 定位

任务栏进度与计数控制接口。

#### 功能能力总结

控制任务栏入口的进度与可见性、计数与可见性和紧急状态，查询计数状态并通知相关变化。

#### 使用场景

需要在任务栏上显示应用操作进度或消息计数时。


---


## 窗口与平台

### DPlatformHandle

#### 定位

窗口平台属性控制接口。

#### 功能能力总结

关联 QWindow，读写圆角、边框、阴影、透明背景、系统移动与缩放、模糊和裁剪参数，并设置窗口场景及启动效果。提供 DXcb 与无标题栏控制、模糊区域、壁纸参数、真实窗口标识和属性通知。当前仍是公开类型，源码只有未来移除的注释，没有 D_DECL_DEPRECATED 标记。

#### 使用场景

需要控制 DTK 窗口的圆角、模糊、阴影这些平台视觉效果时。


---

### DWindowManagerHelper

#### 定位

窗口管理器能力查询与窗口标志控制的单例。

#### 功能能力总结

查询模糊、合成、无标题栏和壁纸支持，以及窗口管理器名称、窗口列表和坐标处的窗口。读写窗口功能、装饰与类型标志，设置窗口类名或弹出系统窗口菜单；通过能力、列表和标志变化信号通知结果。

#### 使用场景

需要按窗口管理器能力选择效果、设置窗口按钮权限或访问工作区窗口时。


---

### DWindowGroupLeader

#### 定位

窗口组标识与成员的管理对象。

#### 功能能力总结

构造时指定或创建分组标识，读取 groupLeaderId 与 clientLeaderId，添加或移除 QWindow 成员。

#### 使用场景

需要将多个窗口关联到同一窗口组时。


---

### DForeignWindow

#### 定位

基于窗口标识访问外部窗口信息的 QWindow。

#### 功能能力总结

通过 fromWinId 引用已有窗口，读取 wmClass 与 pid，并接收对应属性变化通知；一般窗口属性使用 QWindow 接口。

#### 使用场景

需要读取外部窗口的进程标识或窗口类名时。


---

### DPlatformHandle::WMBlurArea

#### 定位

窗口模糊矩形的数据结构。

#### 功能能力总结

保存 x、y、width、height、xRadius 与 yRaduis，描述模糊区域位置、大小和圆角；最后一个字段按公开声明拼写为 yRaduis。

#### 使用场景

需要向 DPlatformHandle 提交多个模糊区域时。


---
