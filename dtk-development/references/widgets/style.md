# QWidget DStyle / ChameleonStyle 控件绘制指南

## 1. 概述与适用场景

本文档详细说明 DTK QWidget 控件的绘制机制，帮助开发者理解控件外观实现，以及在自定义控件时正确复用 DTK 风格元素。

**适用场景：**
- 理解 DTK 控件绘制原理
- 自定义控件时复用 DTK 风格
- 排查控件样式问题

**相关接口：**
- `DStyle` — DTK 扩展风格类
- `DStyleHelper` — 风格辅助类
- `DPaletteHelper` — 调色板辅助类

## 3. 文档范围与源码入口

DTK QWidget 的最终外观主要由两层组成：

- `DStyle`（`dtkwidget/src/widgets/dstyle.cpp`）：定义 DTK 扩展的图元、像素度量、状态到画刷的转换和普通风格回退。
- `ChameleonStyle`（`qt5integration/styleplugins/chameleon/chameleonstyle.cpp`）：重写 Qt 标准控件的 `drawPrimitive()`、`drawControl()`、`drawComplexControl()`，实现实际绘制。

本文按应用中大致使用频率介绍 ChameleonStyle 自绘控件。它描述的是当前源码逻辑，而不是要求应用手工重画控件。未被 switch 分支处理的元素会回退到 `DStyle`，再回退到 `QCommonStyle`。

绘制入口的分工：

| 入口 | 用途 | 典型元素 |
|---|---|---|
| `drawPrimitive()` | 不可再拆的背景、边框、指示器 | 按钮背景、输入框、复选框、单选框、箭头、分支线 |
| `drawControl()` | 完整控件或控件标签 | 按钮、菜单项、标签页、进度条、表头、列表项 |
| `drawComplexControl()` | 含多个可交互子区域的控件 | 工具按钮、组合框、滑块、微调框 |
| `subElementRect()` | 普通控件内部区域布局 | 图标、文本、焦点框、指示器 |
| `subControlRect()` | 复杂控件子区域布局 | 下拉箭头、滑块手柄、微调按钮 |

> 不要硬编码本文列出的矩形尺寸。应用若需与风格对齐，应调用 `subElementRect()`、`subControlRect()`、`pixelMetric()`；尺寸随 DTK 版本、紧凑模式和 DPI 变化。


## 3. QWidget 绘制机制

`DStyle` 扩展 Qt 的图元、控件元素、像素度量、子元素、标准图标和状态标志。DTK 控件通过 `DStylePainter`、`DStyleHelper` 或 `DStyle` 静态辅助函数请求当前风格绘制；当前风格未实现 DTK 扩展时，使用公共实现和 Qt 标准绘制作为回退。

ChameleonStyle 除三个绘制入口外，还重写 `subElementRect()`、`subControlRect()`、`hitTestComplexControl()`、`sizeFromContents()`、`pixelMetric()` 和 `styleHint()`。绘制区域、布局区域与鼠标命中区域必须保持一致。

风格内部还维护菜单、进度、数值、混合和滚动条动画。`polish(QWidget *)` 为需要交互反馈的控件启用 hover，并初始化控件绘制所需属性；`unpolish()` 负责恢复属性。

## 4. 所有控件共用的状态、颜色与组合逻辑

### 3.1 状态来源

绘制不直接查询鼠标位置，而读取 `QStyleOption::state`：

| 状态 | 含义 | 常见视觉作用 |
|---|---|---|
| `State_Enabled` | 可用 | 未设置时使用 Disabled 色组/降低视觉强调 |
| `State_MouseOver` | hover | 背景或手柄增亮，DCI 图标播放 Hover 帧 |
| `State_Sunken` | pressed | 背景加深，DCI 图标播放 Pressed 帧 |
| `State_On` / `State_Off` | checked / unchecked | 选择高亮色、切换勾选图形 |
| `State_NoChange` | partially checked | 复选框绘制中间态横线 |
| `State_Selected` | 项被选中 | 项背景用 Highlight、文本用 HighlightedText |
| `State_HasFocus` | 有焦点 | 在内容外围绘制 Highlight 焦点边框 |
| `State_Active` | 活动窗口 | 决定 Active/Inactive 调色板色组 |
| `State_Horizontal` | 水平方向 | 决定滚动条、滑块和进度条的几何方向 |

组合时不是简单的互斥枚举。源码通常按以下优先级处理：

1. `!Enabled` 先决定 Disabled 色组；
2. `Sunken` 覆盖 `MouseOver`；
3. `On/Selected` 决定是否采用 Highlight；
4. `HasFocus` 作为独立的最外层描边叠加；
5. 水平/垂直、LTR/RTL 再决定区域方向。

因此 checked 控件仍可 hover，selected 项仍可 focus，最终外观是多层效果的组合。

### 3.2 颜色不是常量

ChameleonStyle 的两个 `getColor()` 重载分别读取 `QPalette::ColorRole` 和 `DPalette::ColorType`，随后交给 `DStyle::generatedBrush()` 根据当前状态生成画刷。常用语义为：

- 背景：`QPalette::Window`、`Button`、`Base`、`Highlight`，以及 `DPalette::ItemBackground`、`ObviousBackground`；
- 前景：`WindowText`、`ButtonText`、`Text`、`HighlightedText`；
- 边框：`DPalette::FrameBorder`；
- 提示与警告：`DPalette::TextTips`、`TextWarning`；
- 焦点/选中：`DPalette::Highlight` 或 `QPalette::Highlight`。

应用自定义 palette 后，这些颜色会随 palette 改变；不要把文中“白色/黑色”理解成所有分支都固定使用纯色。

### 3.3 应用如何定制颜色、字体和图标

ChameleonStyle 从传入控件的 `QStyleOption::palette` 取标准角色，并通过 `DPaletteHelper` 取得 DTK 扩展角色。因此应用定制应优先修改应用或控件 palette，而不是覆盖 `paintEvent()`。

常用角色与影响范围：

| 角色 | 主要影响 |
|---|---|
| `QPalette::Button` | 普通按钮、工具按钮等可点击面的基础背景 |
| `QPalette::ButtonText` | 按钮和工具按钮前景文字 |
| `QPalette::Base` | 输入框、列表视图等内容区背景 |
| `QPalette::Text` / `WindowText` | 输入文字、标签、复选框/单选框文字和部分指示器 |
| `QPalette::Highlight` | 推荐按钮、选中项、checked 状态、进度和焦点强调 |
| `QPalette::HighlightedText` | 高亮背景上的文字或图标前景 |
| `DPalette::FrameBorder` | 输入框、面板和部分控件边框 |
| `DPalette::ItemBackground` | hover item、flat 控件等弱背景反馈 |
| `DPalette::ObviousBackground` | 进度槽等需要可辨识但不抢眼的背景 |
| `DPalette::TextWarning` | 警告按钮或警告文本 |

应用级 palette 会影响所有未设置局部 palette 的控件；单控件 palette 则通过 `DPaletteHelper` 设置。应从当前 palette 开始修改，并按需要补齐 `Active`、`Inactive`、`Disabled` 色组。应用级 palette 示例见 [调色板规范](../theme/palette.md)。

各类控件定制时优先修改的入口如下；后续控件章节解释这些角色对应的绘制区域：

| 控件 | 背景/槽 | 前景/文本 | 图标或指示器 | 字体入口 |
|---|---|---|---|---|
| PushButton/ToolButton | `Button`、强调态 `Highlight` | `ButtonText`、`HighlightedText`、`TextWarning` | `setIcon()`、`setIconSize()` | `setFont()` |
| LineEdit/ComboBox/SpinBox | `Base`/`Window`，边框 `FrameBorder` | `Text`、placeholder | ComboBox 当前 icon、SpinBox 风格箭头 | 编辑器 `setFont()` |
| CheckBox/RadioButton | indicator 使用 `Highlight`/`WindowText` | `WindowText` | DCI checked/unchecked 资源由风格选择 | `setFont()` |
| Item View | `Base`、`ItemBackground`、`Highlight` | `Text`、`HighlightedText` | model 的 `DecorationRole`/`CheckStateRole` | view font 或 model `FontRole` |
| Menu/Tab | `Window`、`ItemBackground`、`Highlight` | `WindowText`、`HighlightedText` | `QAction::setIcon()`、tab icon | menu/tab font |
| Slider/ProgressBar | groove 的 `ObviousBackground`，contents 的 `Highlight` | 进度文字 `ButtonText`/`HighlightedText` | handle/indicator 由风格绘制 | progress font |

字体由控件的 `font()` / `QApplication::font()` 进入 `QStyleOption`，改变字号或字重后应让布局重新计算。图标应优先使用 `DIconTheme`、`DStyle::standardIcon()` 或 DCI 图标，使各交互状态和亮暗主题可由风格选择。

具体示例按控件放置：

- [button.md](button.md)：普通/强调按钮、复选框选中色、字体和主题图标；
- [input.md](input.md)：输入区背景、文字、placeholder 和边框；
- [view.md](view.md)：列表底色、hover、选中背景/文字和 model role；
- [progress.md](progress.md)：进度槽、contents 和跨区域文字。

使用 `setStyleSheet()` 可能接管控件的部分或全部绘制，使 palette 状态生成、圆角度量、DCI 动画和暗色适配失效。需要保持 DTK 风格行为时，应优先使用 palette、font 和 icon。各控件的实际定制代码放在对应的控件文档中。

如果局部 palette 修改没有效果，可保持 palette 代码不变，用 `-style fusion` 临时替换 Chameleon 进行对比。仅在 Fusion 生效时，应检查 Chameleon 对应绘制分支实际读取的 role；两种风格都不生效时，则优先检查内部控件、delegate、Style Sheet 和颜色组。完整步骤见 [Chameleon 动态指定与对比调试](../theme/chameleon-style.md#34-修改-palette-不生效时的对比方法)。

### 3.4 亮色与暗色

主题由 `DGuiApplicationHelper::themeType()` 判定。大部分控件不写 `if (dark)`，而通过标准 palette 和 `DPalette` 间接适配。只有少量绘制细节显式分支：

- DCI 复选框/单选框给 `DDciIconPlayer` 设置 `DDciIcon::Light` 或 `Dark`；
- 非动画单选框的内圈在亮色使用白色，在暗色使用黑色；未选中暗色内圈还叠加半透明黑；
- 标签页等个别背景使用 `adjustColor()`，亮暗主题采用不同明度偏移。

这意味着“暗色”不是把亮色 RGB 取反，而是选择另一套语义 palette，再叠加少量控件特化。

### 3.5 通用绘制顺序

多数控件遵循：**背景/槽 → 边框 → 状态覆盖层 → 图标/指示器 → 文本 → 焦点框**。`QPainter::save()/restore()` 用于限制抗锯齿、裁剪、透明度和坐标变换的影响范围。

## 5. 按钮（最高频）

### 4.1 QPushButton 与 DTK 按钮派生类

`CE_PushButton` 将完整按钮拆成：

1. `CE_PushButtonBevel`：按钮背景和边框；
2. `SE_PushButtonContents`：图标、文本所在内容区；
3. `CE_PushButtonLabel`：实际前景；
4. `SE_PushButtonFocusRect`：焦点区域。

`PE_PanelButtonCommand` 绘制圆角背景。普通按钮使用 Button 语义色；hover、pressed、checked 由生成画刷叠加状态。flat 按钮在普通状态不强调面板，hover/pressed/on 时才显示反馈。默认按钮还会使用 `PM_ButtonDefaultIndicator` 留出默认态区域。

`CE_PushButtonLabel`：

- 文本颜色通常取 `ButtonText`；checked 时按分支可使用 `HighlightedText`；
- 警告按钮使用 `TextWarning`，推荐/高亮按钮使用 `HighlightedText`；
- 图标与文本共同存在时先计算二者总宽度并居中，再分别绘制图标区和文本区；
- 菜单按钮在右侧（RTL 时相反）预留 `PM_MenuButtonIndicator`，由 `drawButtonDownArrow()` 绘制下拉箭头；
- pressed/on 不通过移动业务布局实现，而主要依靠背景和前景色状态表现。

焦点不是按钮填充的一部分：`State_HasFocus` 时在 `SE_PushButtonFocusRect` 额外绘制边框，宽度和间距来自 `PM_FocusBorderWidth`、`PM_FocusBorderSpacing`。

应用定制按钮时，最关键的角色是 `Button`（普通背景）、`ButtonText`（普通前景）、`Highlight`（推荐/选中/强调背景）、`HighlightedText`（强调背景上的前景）和 `TextWarning`（警告前景）。hover 与 pressed 不是独立 palette role，而是 ChameleonStyle 基于这些基础色生成的状态色；因此只要基础色配置完整，交互态会自动派生。按钮字体来自 `QStyleOptionButton::fontMetrics`，图标来自 `QStyleOptionButton::icon` 和 `iconSize`。

### 4.2 QToolButton / DToolButton

`CC_ToolButton` 包含 `SC_ToolButton` 主按钮区与 `SC_ToolButtonMenu` 菜单区。背景在普通状态可以透明；hover 或 pressed 时才绘制圆角反馈。`State_On` 的图标/文本采用 Highlight，普通态采用 ButtonText。

`CE_ToolButtonLabel` 根据 `toolButtonStyle` 划分区域：

- `ToolButtonIconOnly`：图标居中；
- `ToolButtonTextOnly`：文本居中；
- `ToolButtonTextBesideIcon`：图标与文本水平组合；
- `ToolButtonTextUnderIcon`：上方图标、下方文本。

带菜单时，内容区减去箭头宽度。`MenuButtonPopup` 的主区和箭头区可分别 hover/pressed；`HasMenu` 则在统一按钮区内绘制箭头。焦点边框仍在内容之外叠加。

## 6. 输入控件

### 5.1 QLineEdit / DLineEdit

输入框由两个图元组成：

- `PE_PanelLineEdit`：填充内部背景；
- `PE_FrameLineEdit`：边框，实际委托 `drawBorder()`。

绘制区域是 option 的 `rect`，边框半径取 `PM_FrameRadius`。背景通常来自 Base/Window 类语义色，边框来自 `FrameBorder`。hover 可改变边框/背景生成色，focus 使用 Highlight 强调边框，disabled 使用禁用色组。文本、选择区、placeholder 仍由 Qt/控件自身按 `Text`、`HighlightedText`、`PlaceholderText` 绘制。

DLineEdit 可能在外层组合图标、清除按钮或提示区；这些是控件布局层，不应与 ChameleonStyle 的基础输入框矩形混为一谈。

### 5.2 QComboBox

`CC_ComboBox` 分为：

- `SC_ComboBoxFrame`：圆角背景和边框；
- `SC_ComboBoxEditField`：当前文本/图标区域；
- `SC_ComboBoxArrow`：下拉箭头区域。

`CE_ComboBoxLabel` 在 edit field 中绘制当前图标和文本；editable 组合框需避免覆盖内部 `QLineEdit`。箭头区位于尾端，RTL 自动镜像。hover/pressed 可以作用于整体或当前 active sub-control；disabled 同时改变背景、箭头和文字。焦点态以 Highlight 边框叠加，不改变内容区划分。

### 5.3 QSpinBox

`CC_SpinBox` 使用 `SC_SpinBoxFrame`、`SC_SpinBoxEditField`、`SC_SpinBoxUp`、`SC_SpinBoxDown`。上下按钮位于尾端并上下分割；`spinboxIndicatorRect()` 在按钮矩形中取短边形成居中的正方形箭头区。

`updateSpinBoxButtonState()` 分别把 active、enabled、hover、sunken 状态传给上/下按钮，避免按下一个按钮时另一个按钮也呈 pressed。按钮区域绘制背景后，再用 `PE_IndicatorArrowUp/Down` 绘制前景箭头。

## 7. 选择控件

### 6.1 QCheckBox

完整复选框按 `CE_CheckBox` 拆成 indicator、label、focus rect：

- `SE_CheckBoxIndicator`：方形勾选指示器；
- `SE_CheckBoxContents`：文本/图标；
- `SE_CheckBoxFocusRect`：包含可见内容的焦点框。

启用动画时，指示器使用 `checkbox_checked` / `checkbox_unchecked` DCI：checked 决定图标文件，hover/pressed 决定 `DDciIcon::Hover/Pressed` 播放模式，Light/Dark 决定资源主题，palette 由控件 palette 转为 `DDciIconPalette`。

关闭动画时：

- `State_Off`：绘制 WindowText/FrameBorder 语义边框；
- `State_On`：Highlight 背景上绘制勾线；
- `State_NoChange`：绘制边框和中间横线；
- disabled、hover、pressed 再通过状态生成色调整上述前景和背景。

`CE_CheckBoxLabel` 使用 WindowText 绘制文本；有图标时先分配图标区。`HasFocus` 最后在 focus rect 绘制 Highlight 圆角边框。

### 6.2 QRadioButton

区域结构与复选框相同，只是 indicator 为圆形。动画路径使用 `radio_checked` / `radio_unchecked` DCI。

非动画路径：

- `State_On`：外环填充 Highlight；内圈按主题填充亮色白/暗色黑；
- `State_Off`：用 WindowText 描圆边，内部亮色透明、暗色半透明黑；
- hover/pressed/disabled 继续影响语义色；
- focus 在 indicator/label 外绘制 Highlight 椭圆焦点框。

## 8. 列表、树和表格

### 7.1 Item 背景与完整项

`PE_PanelItemViewItem`/`PE_PanelItemViewRow` 先绘制行或项背景，`CE_ItemViewItem` 再绘制内容。典型分层为：

1. `backgroundBrush`（模型通过 `Qt::BackgroundRole` 提供）优先；
2. `State_Selected` 使用 Highlight；
3. hover 使用 ItemBackground 的 hover 状态；
4. disabled 使用禁用色组；
5. 根据 view 特性绘制分隔线；
6. check indicator、decoration icon、display text；
7. `State_HasFocus` 绘制 `SE_ItemViewItemFocusRect`。

文本颜色在 selected 时为 HighlightedText，否则为 Text；disabled/Inactive 选择相应 `QPalette::ColorGroup`。内容矩形由 `viewItemLayout`/`subElementRect` 拆分为 check、decoration、text，不能假设图标永远在左侧（RTL 会镜像）。

### 7.2 树分支

`PE_IndicatorBranch` 在 branch rect 中绘制树形连接线和展开/折叠箭头。是否有 children、是否 open 由 `State_Children`、`State_Open` 等 item-view 状态决定；横竖连接线由 sibling/item 状态组合决定。箭头复用 `PE_IndicatorArrowRight/Down`，RTL 时方向镜像。

### 7.3 表头

`CE_Header` 组合：

- `CE_HeaderSection`：section 背景和分隔边框；
- `SE_HeaderLabel`：图标与文字；
- `SE_HeaderArrow`：排序箭头。

pressed/hover 影响 section 背景，文字使用 WindowText；排序状态由 `QStyleOptionHeader::sortIndicator` 决定。源码遵循常见 UI 语义：SortUp 绘制向下图标、SortDown 绘制向上图标。水平/垂直表头及首尾 section 会影响边框绘制边。

## 9. 菜单与菜单栏

`PE_PanelMenu` 绘制菜单面板，`CE_MenuEmptyArea` 填充空白区域。`CE_MenuItem` 的实际布局由菜单辅助逻辑拆成：

1. 左侧 check/icon 区；
2. 主文本区；
3. shortcut 区（宽度来自 `reservedShortcutWidth`，Qt 5 对应 `tabWidth`）；
4. submenu arrow 区；
5. 可选红点提示区。

separator 只绘制分隔线/标题，不走普通 action 路径。普通项在 selected（菜单 hover）时绘制高亮背景并使用 HighlightedText；disabled 使用禁用色组；checkable + checked 绘制勾选标志；有 icon 时按 icon mode/state 绘制。submenu 在尾端画右箭头，RTL 画左箭头。

菜单栏 `CE_MenuBarItem` 在 active/selected 时绘制状态背景，再绘制文字/图标；`CE_MenuBarEmptyArea` 使用 Window 背景。菜单移动动画会更新旧、新 item 矩形的并集，动画期间还会调整文字 opacity。

## 10. 标签页

`CE_TabBarTab` 依次绘制 `CE_TabBarTabShape` 和 `CE_TabBarTabLabel`。区域包括 icon、text、左右按钮（常见为 close button）；`tabLayout()` 根据 tab shape、方向和按钮尺寸计算 icon/text rect。

- `State_Selected` 转换为按钮的 `State_On`，背景采用选中/Highlight 语义；
- hover 绘制 ItemBackground 类反馈；
- 未选中背景在亮暗主题分别通过 `adjustColor()` 调整；
- 文本和图标在 label rect 内组合；
- `PE_IndicatorTabClose` 绘制关闭图标；
- north/south/east/west shape 决定背景边界、分隔线以及文字旋转。

`PE_FrameTabWidget` 绘制内容页框，`PE_FrameTabBarBase` 被 ChameleonStyle 留空，避免重复底边。

## 11. 滚动条

滚动条最主要的自绘区域是 `CE_ScrollBarSlider`（滑块/handle）。水平与垂直分别计算圆角矩形：

- 非 hover 时 handle 较细并居中于 scrollbar；
- hover 时扩展到较宽区域；
- pressed 在 hover 基础上进一步调整颜色；
- 颜色与边缘描线由 palette 状态生成；
- 圆角半径取实际 handle 短边的一半。

源码会检查滚动区域父控件及 transient scrollbar 属性，以决定显示和动画行为。add-line/sub-line/page 区域主要负责交互，视觉上可保持透明；因此不要把整个 scrollbar rect 当成始终可见的轨道。

## 12. 滑块

`CC_Slider` 使用：

- `SC_SliderGroove`：轨道；
- `SC_SliderHandle`：手柄；
- `SC_SliderTickmarks`：刻度（存在时）。

groove 沿中心线绘制，Highlight 表示已走过区间，普通背景表示剩余区间；`upsideDown`、orientation 和 RTL 共同决定高亮从哪一端开始。`drawSliderHandle()` 画圆形/圆角手柄，hover/pressed 改变尺寸或颜色；`drawSliderHandleFocus()` 在 `State_HasFocus` 时额外画焦点环。active sub-control 只影响 handle，而不应把整个 groove 画成 pressed。

## 13. 进度条

`CE_ProgressBar` 组合 groove、contents、label：

- `CE_ProgressBarGroove`：圆角轨道背景；
- `CE_ProgressBarContents`：按 `(progress-minimum)/(maximum-minimum)` 计算填充区域；
- `CE_ProgressBarLabel`：绘制百分比/自定义文本。

当前实现中，水平 contents 从左向右增长，垂直 contents 从下向上增长；绘制宽度/高度按 `progress / (maximum - minimum)` 计算。使用前应保证范围有效，当前分支没有专门处理 `maximum == minimum` 的 busy 模式。contents 使用 Highlight 填充并按轨道半径绘制圆角。label 跨越已填充和未填充区域时，源码构造线性渐变画笔：填充侧使用 HighlightedText，未填充侧使用 ButtonText，以保证两侧对比度。

## 14. 其他自绘元素

- **箭头**：`PE_IndicatorArrowUp/Down/Left/Right` 调用 `DDrawUtils`，前景通常为 WindowText；控件应传入正确的局部 rect。
- **焦点框**：`PE_FrameFocusRect` 使用 Highlight、`PM_FocusBorderWidth` 和 spacing，item/button/check 等会提供各自 focus rect。
- **提示框**：`PE_PanelTipLabel`/相关 frame 使用 ToolTipBase/ToolTipText 与圆角边框。
- **GroupBox/Frame**：`PE_FrameGroupBox`、`PE_Frame` 根据 Sunken/Raised 决定边框明暗顺序；内容和标题由 Qt 的 group-box 子控件布局。
- **RubberBand**：`CE_RubberBand` 使用半透明 Highlight 填充并描边。
- **SizeGrip**：`CE_SizeGrip` 在角落区域绘制多条短线/点阵，并根据 corner 与 RTL 调整方向。
- **StatusBar**：panel 使用 Window 背景；`PE_FrameStatusBarItem` 不额外绘制，避免每个 item 出现边框。

## 15. 自定义控件如何复用这套绘制

本节适用于**创建全新的自定义控件**。如果只是需要自定义列表项的外观，应优先使用 `DStyledItemDelegate` 和 `DStandardItem` 提供的属性接口：

| 需求 | 正确做法 |
|------|---------|
| 列表项圆角背景 | `delegate->setBackgroundType(RoundedBackground)` |
| 自定义项背景色 | `item->setBackgroundRole(DPalette::ColorType)` |
| 自定义项文字颜色 | `item->setTextColorRole(DPalette::ColorType)` |
| 添加操作按钮 | `item->setActionList(Qt::Edge, {actions})` |
| 嵌入自定义控件 | `action->setWidget(widget)` |

详见 [item-delegate.md](item-delegate.md)。

优先构造标准 `QStyleOption` 并调用当前 style，而不是复制 ChameleonStyle 源码：

```cpp
void MyButton::paintEvent(QPaintEvent *)
{
    QStyleOptionButton option;
    option.initFrom(this);               // 自动带入 enabled/hover/focus 等状态
    option.rect = rect();
    option.text = text();
    option.icon = icon();
    option.features = isDefault()
            ? QStyleOptionButton::DefaultButton
            : QStyleOptionButton::None;

    if (isDown())
        option.state |= QStyle::State_Sunken;
    if (isChecked())
        option.state |= QStyle::State_On;

    QPainter painter(this);
    style()->drawControl(QStyle::CE_PushButton, &option, &painter, this);
}
```

若只需要 DTK 自定义图元，可使用 `DStyleHelper`：

```cpp
DStyleHelper helper(style());
QColor text = helper.getColor(&option, DPalette::TextTitle);
helper.drawPrimitive(DStyle::PE_ItemBackground, &option, &painter, this);
```

注意事项：

1. `initFrom()` 不会自动提供每种派生控件特有状态，checked/down/selected 仍需按控件语义补齐；
2. 始终传入 `this`，否则 palette、DPI、属性和控件类型特化可能失效；
3. 图标 mode 应由 enabled/selected/active 推导，不要固定为 `QIcon::Normal`；
4. RTL 使用 `visualRect()` 或 style 的布局结果，不要自行假设箭头在右；
5. 焦点框应最后绘制，并使用 pixel metric，而不是写死 1 px；
6. 自绘区域必须与 `hitTestComplexControl()`/`subControlRect()` 一致，否则视觉区域与点击区域会错位。

## 16. 标准图标与像素度量

```cpp
#include <DStyle>

QIcon closeIcon = DStyle::standardIcon(style(), DStyle::SP_CloseButton);
int radius = DStyle::pixelMetric(style(), DStyle::PM_FrameRadius);
int focusWidth = DStyle::pixelMetric(style(), DStyle::PM_FocusBorderWidth);
int focusSpacing = DStyle::pixelMetric(style(), DStyle::PM_FocusBorderSpacing);
```

## 17. 相关文档

- [主题层 Chameleon 概览](../theme/chameleon-style.md) — 风格插件架构、加载与回退关系
- [palette.md](../theme/palette.md) — `DPalette` 语义色与状态画刷
- [theme-switch.md](../theme/theme-switch.md) — 主题切换和 palette 更新
- [dci.md](../theme/dci.md) — DCI 图标的主题、模式和 palette
