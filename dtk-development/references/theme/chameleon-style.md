# QWidget 变色龙风格实现

## 1. 定位与分层

DTK 的 QWidget 风格由基础实现和 Qt 风格插件两层组成：

```text
QCommonStyle
└── DStyle                         dtkwidget：DTK 扩展协议与公共实现
    └── ChameleonStyle             qt5integration：DDE 控件外观与交互实现

QStylePlugin
└── ChameleonStylePlugin
    └── create("chameleon") → ChameleonStyle
```

`DStyle` 不负责注册 Qt 插件。它扩展 `QStyle` 的元素、度量、图标和状态颜色，并为 DTK 控件提供统一绘制接口。`ChameleonStyle` 继承 `DStyle`，实现标准 QWidget 和 DTK 控件在 DDE 中的具体外观、布局、动画及平台窗口效果。

## 2. 插件注册与启用

`qt5integration/styleplugins/chameleon/main.cpp` 中的 `ChameleonStylePlugin` 继承 `QStylePlugin`，使用 Qt 的 `QStyleFactoryInterface` 插件接口。`chameleon.json` 声明键名 `chameleon`，插件仅在 `create()` 收到该键名时创建 `ChameleonStyle`。

插件通过 `dtk_add_plugin` 构建，依赖 `Dtk::Widget` 以及 Qt Core、Gui、Widgets 的私有接口，并安装到 Qt 的 `styles` 插件目录。Qt 因而可以通过 `QStyleFactory` 或 `QApplication::setStyle("chameleon")` 加载它。

Deepin 平台主题的 `QDeepinTheme::themeHint(QPlatformTheme::StyleNames)` 按 `chameleon`、`fusion` 的顺序提供候选风格。未运行在 Deepin 平台主题环境时，`DApplication` 主动设置 `chameleon`，使 DTK 应用仍使用相同的 QWidget 风格。

## 3. DStyle 基础层

### 3.1 DTK 风格协议

`DStyle` 继承 `QCommonStyle`，在 Qt 标准风格枚举之外定义 DTK 专用的：

- 绘制元素，例如项目背景、图标按钮、开关按钮和浮动控件；
- 像素度量，例如圆角、阴影和焦点边框宽度；
- 标准图标，例如窗口按钮、增减按钮和状态指示图标；
- 子元素、内容类型及控件状态标志。

DTK 控件通过 `DStylePainter`、`DStyleHelper` 或 `DStyle` 静态辅助函数请求绘制、颜色、图标和尺寸，不直接依赖 `ChameleonStyle`。例如 `DIconButton`、`DSwitchButton` 和 `DFloatingWidget` 分别请求对应的 DTK `ControlElement`，具体绘制由当前应用风格完成。

### 3.2 兼容普通 QStyle

`DStyleHelper::setStyle()` 尝试把当前风格转换为 `DStyle`：

- 当前风格是 `DStyle` 子类时，分发到该对象的虚函数；
- 当前风格是普通 `QStyle` 时，使用 `DStyle` 的静态公共实现，并把该 `QStyle` 作为标准绘制后端。

这一层隔离使 DTK 控件可以使用扩展风格能力，同时保留与其他 Qt 风格的兼容路径。

### 3.3 状态与颜色生成

`DStyle` 把 `QStyleOption::state` 转换为普通、悬停、按下等基础状态，并附加选中、勾选和焦点标志。禁用状态主要由调色板的颜色组表达；控件未启用 `WA_Hover` 时，不采用悬停状态。

颜色计算同时支持 Qt 的 `QPalette::ColorRole` 和 DTK 的 `DPalette::ColorType`。`generatedBrush()` 根据颜色组与控件状态生成最终画刷，对悬停、按下等状态进行亮度、透明度或高亮色混合处理。完整链路为：

```text
主题或应用调色板
→ QPalette / DPalette
→ QStyleOption 状态
→ DStyle::generatedBrush()
→ 风格绘制
```

## 4. ChameleonStyle 具体实现

`ChameleonStyle` 重写 `drawPrimitive()`、`drawControl()`、`drawComplexControl()`、`subElementRect()`、`subControlRect()`、`hitTestComplexControl()`、`sizeFromContents()`、`pixelMetric()`、`styleHint()`、`polish()` 和 `unpolish()`，统一处理绘制、布局、命中测试、尺寸、度量和控件初始化。

其覆盖范围包括按钮、复选框、单选框、输入框、组合框、SpinBox、滑块、滚动条、菜单、标签页、项目视图、进度条、工具按钮、表头、工具提示、日历和分组框等标准 QWidget。未专门处理的元素回落到 `DStyle`，再由 `QCommonStyle` 完成标准兜底。

`ChameleonStyle::getColor()` 根据传入角色选择颜色来源：Qt 标准角色直接读取 `QStyleOption` 的 `QPalette`；DTK 语义色通过 `DPaletteHelper` 获取控件对应的 `DPalette`。两条路径最终都交给 `DStyle` 的状态画刷生成逻辑，因此标准控件与 DTK 控件共享主题状态规则。

## 5. 动画与平台窗口效果

风格维护以控件对象为键的动画实例。菜单选中项使用 `ChameleonMovementAnimation` 在矩形位置间过渡；进度、数值、混合和滚动条效果分别由 `DProgressStyleAnimation`、`DNumberStyleAnimation`、`DBlendStyleAnimation` 和 `DScrollbarStyleAnimation` 实现。

`polish(QWidget *)` 为需要状态反馈的按钮、组合框、滚动条、SpinBox、TabBar 和项目视图视口启用悬停属性，平板环境下关闭悬停行为。它还为菜单、组合框弹出窗口和工具提示配置透明、圆角、模糊与边框等平台属性，并对日历进行专门的布局和视觉初始化。相关窗口能力通过 `DPlatformWindowHandle`、`DPlatformTheme`、`DWindowManagerHelper` 和 `DGuiApplicationHelper` 接入；`unpolish()` 负责恢复风格设置的属性。

## 6. 源码入口

| 职责 | 源码 |
|------|------|
| DTK 风格协议、公共绘制与颜色生成 | `dtkwidget/include/widgets/dstyle.h`、`dtkwidget/src/widgets/dstyle.cpp` |
| 变色龙风格声明与实现 | `qt5integration/styleplugins/chameleon/chameleonstyle.h`、`chameleonstyle.cpp` |
| 动画实现 | `qt5integration/styleplugins/chameleon/dstyleanimation.h`、`dstyleanimation.cpp` |
| 插件入口与元数据 | `qt5integration/styleplugins/chameleon/main.cpp`、`chameleon.json` |
| 插件构建安装 | `qt5integration/styleplugins/chameleon/CMakeLists.txt` |
| 平台主题风格候选 | `qt5integration/platformthemeplugin/qdeepintheme.cpp` |
| 非 Deepin 平台主题下的启用逻辑 | `dtkwidget/src/widgets/dapplication.cpp` |

## 7. 相关文档

- [style.md](style.md) - DStyle API 与控件风格用法
- [palette.md](palette.md) - DPalette 语义色与状态配色
- [../platform-abstraction.md](../platform-abstraction.md) - 窗口效果与平台抽象
