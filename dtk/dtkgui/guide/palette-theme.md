# 调色板与主题接口

dtkgui 的调色板与主题接口提供 DTK 扩展调色板角色、应用级主题管理、原生设置读写和平台主题属性访问能力。

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

## 模块API介绍

### DPalette

#### 定位

DTK 扩展调色板，在 Qt 调色板基础上增加 DTK 专属颜色角色。

#### 功能能力总结

在 Qt 调色板基础上扩展 DTK 专属颜色角色，涵盖控件背景、标题文字、摘要文字、警告文字、活跃式文字、活跃式按钮亮色与暗色、控件边框、占位文字、阴影边框、明显背景这些界面元素的专用颜色。支持设置和获取各扩展角色的颜色。

#### 使用场景

需要使用 DTK 专属调色板角色设置控件颜色时。

### DGuiApplicationHelper

#### 定位

GUI 层面的全局辅助工具与应用级主题管理。

#### 功能能力总结

提供浅色和深色主题类型、系统级与用户级作用域、普通与紧凑尺寸模式的查询与设置。管理应用调色板、字号、主题色和窗口半径在内的全局外观属性，并发出主题变化信号。提供系统字体、鼠标按下修饰键的辅助查询。

#### 使用场景

需要读取或修改应用级主题外观（亮色/暗色、主题色、字号）时；需要响应主题变化信号时。

### DNativeSettings

#### 定位

原生设置读写接口，作为 DTK 平台主题的基类。

#### 功能能力总结

通过 DBus 或文件后端读写命名空间的设置属性，支持属性变更信号通知。设置作用域（系统级或用户级）和属性同步机制。

#### 使用场景

作为 DTK 平台主题的基类使用；需要直接读写原生设置属性时。

### DPlatformTheme

#### 定位

平台主题属性接口。

#### 功能能力总结

在 DNativeSettings 基础上提供 DTK 平台主题属性的读写，包括主题色、字号、图标主题、光标主题、窗口圆角半径。支持属性变更信号和主题重载。DTK6 中标记为待移除。

#### 使用场景

需要读取或修改 DTK 平台主题属性时。
