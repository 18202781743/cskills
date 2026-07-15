# DTK Skill 验证计划

## 目标

验证 `dtk-development` skill 中每个参考文档声称的 **类名、枚举值、方法签名、QML 类型、CMake 指令** 与 `~/dtk` 源码一致，并验证技能描述能够覆盖未明确提及 DTK/API 的桌面应用功能需求，确保 skill 能真正指导 DTK 应用开发。

## 验证范围

Skill 覆盖 8 个 DTK 项目，按参考文档结构划分为主题、控件、QML、配置、工具类、日志、平台集成、跨文档一致性、核心类和技能触发覆盖等验证模块。

## 验证方法

对每个文档声称的 API 标识符，在对应 dtk 项目的头文件中搜索确认：

- **类是否存在**：头文件中是否有 `class X` 声明
- **枚举值是否存在**：头文件中是否有对应 `enum` 及其值
- **方法签名是否匹配**：函数名、参数数量、返回类型
- **QML 类型是否注册**：`qmlRegisterType` 或 `QML_NAMED_ELEMENT` 或 `qmldir` 文件
- **CMake target 名称是否正确**：`Dtk::Core` 等
- **弃用标注是否准确**：`Q_DECL_DEPRECATED` 或注释

每个验证项输出三态结果：
- **PASS** — 文档声称与源码一致
- **FAIL** — 文档声称与源码不一致（注明差异）
- **NOT FOUND** — 源码中未找到对应 API（可能已移除或重命名）

技能触发覆盖项不直接验证 API，而是检查 `SKILL.md` 的 frontmatter 描述、“文档路由”和“高频跨域场景”是否覆盖对应功能；结果同样记录为 PASS/FAIL。

---

## 模块 0：技能触发条件与功能点覆盖

**参考文档：** `SKILL.md`、`references/widgets/index.md`、`references/declarative/index.md`、`references/examples.md`、`references/theme/index.md`、`references/platform-abstraction.md`、`references/config/index.md`、`references/utilities/index.md`、`references/app-dev-with-dtk.md`、`references/dtksrc-compile-debug.md`

**验证目标：** 检查 `SKILL.md` 是否以陈述句概括 DTK 应用开发的功能范围和适用场景，覆盖界面、视觉、配置、系统集成、工程构建与问题排查，并为未被“文档路由”直接覆盖的高频场景提供快捷入口。

| # | 验证项 | 验证方法 | 通过标准 |
|---|--------|----------|----------|
| 0.1 | 功能范围与适用场景 | 检查 frontmatter 是否以陈述句概括 DTK 应用开发功能，并覆盖 Deepin/UOS/DDE 应用的界面、视觉、配置、系统集成、工程构建与问题排查 | PASS：描述完整且不依赖具体 API 或命令式触发语句 |
| 0.2 | 控件与交互功能覆盖 | 检查“文档路由”表是否分别提供 QWidget、QML 和可运行示例入口 | PASS：三个入口均存在且指向对应索引文档 |
| 0.3 | 视觉与平台功能覆盖 | 检查“文档路由”表是否覆盖主题、配色、图标、字体、控件风格、窗口装饰、模糊效果和平台兼容 | PASS：能路由到主题、字体和平台抽象文档 |
| 0.4 | 配置与系统能力覆盖 | 检查“文档路由”表是否覆盖 DConfig、应用入口、日志、DBus、通知、单实例和系统服务 | PASS：能路由到 config、application 和 utilities 文档 |
| 0.5 | 工程与问题排查覆盖 | 检查“文档路由”表是否覆盖应用创建、CMake 与依赖、DTK 源码编译调试、架构和跨应用共性问题 | PASS：能路由到应用开发、架构和 DTK 源码文档 |
| 0.6 | 高频跨域场景 | 检查高频场景是否提供主题与调色板、QML 能力、常用控件及系统工具的直接文档入口，并排除“文档路由”已有条目 | PASS：保留高频直接入口且不重复顶层文档路由 |
| 0.7 | 参考链接有效 | 检查“文档路由”和“高频跨域场景”中的每个链接均指向现有文件 | PASS：所有链接存在且与功能点对应 |

---

## 模块 1：theme（主题系统）— 来源 dtkgui/dtkwidget

**参考文档：** `references/theme/index.md`, `references/theme/palette.md`, `references/theme/style.md`, `references/theme/theme-switch.md`, `references/theme/dci.md`, `references/theme/builtin.md`, `references/theme/icontheme.md`

**源码位置：** `~/dtk/dtkgui/include/kernel/` + `~/dtk/dtkgui/include/util/` + `~/dtk/dtkwidget/include/widgets/`

### 1.1 图标（来源 dtkgui）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 1.1.1 | `DDciIcon` 类存在，构造函数 `DDciIcon(QString path)` 和 `DDciIcon(QByteArray)` | grep `class DDciIcon` + 构造函数声明 | `ddciicon.h` |
| 1.1.2 | `DDciIcon::Theme` 枚举有 `Light`/`Dark` | grep `enum.*Theme` | `ddciicon.h` |
| 1.1.3 | `DDciIcon::Mode` 枚举有 `Normal`/`Disabled`/`Hover`/`Pressed` | grep `enum.*Mode` | `ddciicon.h` |
| 1.1.4 | `DDciIcon::HasPalette` 属性枚举存在 | grep `HasPalette` | `ddciicon.h` |
| 1.1.5 | `DDciIcon::fromTheme()` 静态方法（1 参和 2 参重载） | grep `fromTheme` | `ddciicon.h` |
| 1.1.6 | `pixmap()`、`paint()`、`availableSizes()`、`isNull()` 方法签名 | 逐个核对 | `ddciicon.h` |
| 1.1.7 | `DDciIconPlayer` 类存在，方法 `setIcon`/`setIconSize`/`setTheme`/`play`/`currentImage`，信号 `updated` | grep class + 方法 | `ddciiconplayer.h` |
| 1.1.8 | `DDciIconPalette` 类存在，4 色构造函数，`fromQPalette`/`convertToString`/`convertFromString` 静态方法，getter/setter（foreground/background/highlight/highlightForeground） | 逐个核对 | `ddciiconpalette.h` |
| 1.1.9 | `DIconTheme` 类存在，静态方法 `findQIcon`（3 个重载）、`isBuiltinIcon`、`isXdgIcon`、`createIconEngine`、`findDciIconFile`（2 个重载）、`dciThemeSearchPaths`/`setDciThemeSearchPaths`、`cached` | 逐个核对 | `dicontheme.h` |
| 1.1.10 | `DIconTheme::Options` 枚举有 `DontFallbackToQIconFromTheme`/`IgnoreBuiltinIcons`/`IgnoreDciIcons`/`IgnoreIconCache` | grep `enum.*Options` | `dicontheme.h` |
| 1.1.11 | `DIconTheme::Cached` 内部类有 `findQIcon`/`findDciIconFile`/`setMaxCost`/`clear` 方法 | grep `class Cached` | `dicontheme.h` |
| 1.1.12 | **参数顺序差异验证**：顶层 `findQIcon(iconName, fallback, options)` vs `Cached::findQIcon(iconName, options, fallback)` — 确认文档所述参数顺序是否正确 | 核对函数签名 | `dicontheme.h` |
| 1.1.13 | builtin 图标资源路径 `:/icons/deepin/builtin/light/` 和 `:/icons/deepin/builtin/dark/` 存在 | 搜索 `.qrc` 文件或资源目录 | `dtkgui/src/util/icons/` 或 `dtkwidget/src/widgets/assets/` |
| 1.1.14 | builtin 图标名列表（如 `dialog-ok`、`window-close_round_30px`、`icon_ok_32px` 等）在资源中存在 | glob 搜索资源文件 | 同上 |
| 1.1.15 | CMake `find_package(DtkGui)` + `Dtk::Gui` target | 检查 cmake 配置文件 | `dtkgui/dtkgui.cmake` |

### 1.2 调色板与样式（来源 dtkgui/dtkwidget）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 1.2.1 | `DPalette` 类继承 `QPalette`，`ColorType` 枚举有全部 11 个值：`ItemBackground`/`TextTitle`/`TextTips`/`TextWarning`/`TextLively`/`LightLively`/`DarkLively`/`FrameBorder`/`PlaceholderText`/`FrameShadowBorder`/`ObviousBackground` | grep `enum.*ColorType` + 逐个值 | `dtkgui/include/kernel/dpalette.h` |
| 1.2.2 | `DPalette` 方法：`color(ColorType)`、`textTitle()`/`textTips()`/`textWarning()`/`itemBackground()` getter、`setColor`/`setBrush` setter | 逐个核对 | 同上 |
| 1.2.3 | `DGuiApplicationHelper` 类存在，`ColorType` 枚举有 `LightType`/`DarkType` | grep class + enum | `dtkgui/include/kernel/dguiapplicationhelper.h` |
| 1.2.4 | `DGuiApplicationHelper` 静态方法：`standardPalette(ColorType)`、`generatePaletteColor`、`generatePalette`、`adjustColor`、`blendColor`、`toColorType`、`fetchPalette` | 逐个核对签名 | 同上 |
| 1.2.5 | `DGuiApplicationHelper` 实例方法：`themeType()`、`applicationPalette()`（含重载）、`applicationTheme()`、`setApplicationPalette()`、`setPaletteType()` | 逐个核对 | 同上 |
| 1.2.6 | 信号：`themeTypeChanged(ColorType)`、`applicationPaletteChanged` | grep `Q_SIGNALS`/`signals` | 同上 |
| 1.2.7 | `DStyle` 类存在，继承 `QCommonStyle` | grep `class DStyle` | `dtkwidget/include/widgets/dstyle.h` |
| 1.2.8 | `DStyle::StandardPixmap` 枚举有 `SP_CloseButton`/`SP_IncreaseElement`/`SP_DecreaseElement`/`SP_MarkElement`/`SP_DeleteButton`/`SP_AddButton`/`SP_ArrowEnter`/`SP_ArrowLeave` | grep enum + 逐个值 | 同上 |
| 1.2.9 | `DStyle::PixelMetric` 枚举有 `PM_FrameRadius`/`PM_ShadowRadius`/`PM_FocusBorderWidth` | grep enum | 同上 |
| 1.2.10 | `DStyle::PE_ItemBackground` 原始元素存在 | grep `PE_ItemBackground` | 同上 |
| 1.2.11 | `DStyle` 静态方法：`standardIcon(style, SP)`、`pixelMetric(style, PM)` | 核对签名 | 同上 |
| 1.2.12 | `DStyleHelper` 类存在，方法 `getColor`/`generatedBrush`/`drawPrimitive` | grep class + 方法 | 同上 |
| 1.2.13 | `DStyle::SS_HoverState`/`SS_FocusFlag` 状态标志存在 | grep `SS_HoverState` | 同上 |
| 1.2.14 | `DPlatformTheme` 类存在（`fetchPalette` 参数类型） | grep `class DPlatformTheme` | `dtkgui/include/kernel/dplatformtheme.h` |

---

## 模块 2：widgets（QWidget 控件）— 来源 dtkwidget

**参考文档：** `references/widgets/index.md` + 9 个子文档（`button.md`/`container.md`/`dialog.md`/`input.md`/`message.md`/`navigation.md`/`progress.md`/`view.md`/`window.md`）

**源码位置：** `~/dtk/dtkwidget/include/widgets/` + `~/dtk/dtkwidget/include/DWidget/`（转发头文件）

### 2.1 按钮类（button.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 2.1.1 | 按钮类全部存在：`DSuggestButton`/`DWarningButton`/`DIconButton`/`DToolButton`/`DSwitchButton`/`DButtonBox`/`DFloatingButton` | glob 头文件名 | `include/DWidget/` |
| 2.1.2 | `DIconButton` 构造函数：`(DStyle::StandardPixmap, parent)`、`(DDciIcon, parent)`、`(parent)` 三种重载 | 核对构造函数 | `diconbutton.h` |
| 2.1.3 | `DIconButton` 方法：`setIcon(QIcon)`/`setIcon(DStyle::StandardPixmap)`/`setIcon(DDciIcon)`/`setFlat`/`setEnabledCircle`/`dciIcon` | 逐个核对 | 同上 |
| 2.1.4 | `DSwitchButton` 方法 `setChecked` + 信号 `checkedChanged(bool)` | grep signal | `dswitchbutton.h` |
| 2.1.5 | `DButtonBox` 方法 `setButtonList(QList, bool)` | 核对签名 | `dbuttonbox.h` |
| 2.1.6 | `DFloatingButton` 构造函数 `(DStyle::StandardPixmap, parent)` + 信号 `clicked` | 核对 | `dfloatingbutton.h` |
| 2.1.7 | `DImageButton` 弃用标注（deprecated -> use `DIconButton`） | grep `deprecated`/`Q_DECL_DEPRECATED` | `dimagebutton.h` |

### 2.2 对话框类（dialog.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 2.2.1 | 对话框类全部存在：`DDialog`/`DInputDialog`/`DFileDialog`/`DAboutDialog`/`DAbstractDialog` | glob 头文件 | `include/DWidget/` |
| 2.2.2 | `DDialog` 构造函数 `(parent)` 和 `(title, message, parent)` 两种 | 核对构造函数 | `ddialog.h` |
| 2.2.3 | `DDialog` 方法：`setTitle`/`setMessage`/`setIcon`/`addButton(text,bool,ButtonType)`/`insertButton`/`addContent`/`setOnButtonClickedClose`/`exec` | 逐个核对 | 同上 |
| 2.2.4 | `DDialog::ButtonType` 枚举 `ButtonNormal`/`ButtonWarning`/`ButtonRecommend` | grep enum | 同上 |
| 2.2.5 | `DDialog` 信号 `buttonClicked(int, QString)` 和 `closed` | grep signals | 同上 |
| 2.2.6 | `DDialog::setIconPixmap` 和 `setIcon(QIcon,QSize)` 弃用标注 | grep deprecated | 同上 |
| 2.2.7 | `DInputDialog` 静态方法 `getText`/`getInt` 签名 | 核对 | `dinputdialog.h` |
| 2.2.8 | `DFileDialog` 静态方法 `getOpenFileName`/`getOpenFileNames`/`getExistingDirectory`/`getSaveFileName` | 核对 | `dfiledialog.h` |
| 2.2.9 | `DAbstractDialog::DisplayPosition` 枚举 `Center`/`TopRight` + `setDisplayPosition` 方法 | grep enum + method | `dabstractdialog.h` |

### 2.3 输入类（input.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 2.3.1 | 输入类全部存在：`DLineEdit`/`DSearchEdit`/`DPasswordEdit`/`DTextEdit`/`DSpinBox`/`DDoubleSpinBox`/`DComboBox`/`DKeySequenceEdit` | glob 头文件 | `include/DWidget/` |
| 2.3.2 | `DLineEdit` 方法：`setPlaceholderText`/`setAlert`/`isAlert`/`showAlertMessage`/`hideAlertMessage`/`setLeftWidgets`/`setRightWidgets`/`setClearButtonEnabled`/`lineEdit`/`setSpeechToTextEnabled`/`setTextToSpeechEnabled`/`setTextToTranslateEnabled`/`text` | 逐个核对 | `dlineedit.h` |
| 2.3.3 | `DSearchEdit` 信号 `textChanged(const QString &)` | grep signal | `dsearchedit.h` |
| 2.3.4 | `DPasswordEdit` 信号 `textChanged(const QString &)` | grep signal | `dpasswordedit.h` |
| 2.3.5 | `DSpinBox` 方法 `setRange`/`setValue`/`setSingleStep` + 信号 `valueChanged(int)` | 核对 | `dspinbox.h` |
| 2.3.6 | `DComboBox` 方法 `addItems` + 信号 `currentIndexChanged(int)` | 核对 | `dcombobox.h` |
| 2.3.7 | `DKeySequenceEdit` 信号 `keySequenceChanged(const QKeySequence &)` | grep signal | `dkeysequenceedit.h` |
| 2.3.8 | `DShortcutEdit` 弃用标注（-> use `DKeySequenceEdit`） | grep deprecated | `dshortcutedit.h` |

### 2.4 消息类（message.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 2.4.1 | 消息类全部存在：`DMessageManager`/`DFloatingMessage`/`DFloatingWidget`/`DToolTip` | glob 头文件 | `include/DWidget/` |
| 2.4.2 | `DMessageManager` 静态方法 `instance()`/`sendMessage`（3 个重载：QIcon 版、DFloatingMessage 版、DDciIcon 版）/`setContentMargens` | 逐个核对 | `dmessagemanager.h` |
| 2.4.3 | `DFloatingMessage::MessageType` 枚举 `TransientType`/`ResidentType` + 构造函数 + `setMessage`/`setIcon`(2 重载)/`setWidget`/`setDuration`/`messageType` + 信号 `closeButtonClicked` | 逐个核对 | `dfloatingmessage.h` |
| 2.4.4 | `DToolTip` 静态方法 `setToolTipTextFormat`/`toolTipTextFormat` | 核对 | `dtooltip.h` |
| 2.4.5 | `DToast` 弃用标注（-> use `DMessageManager`） | grep deprecated | `dtoast.h` |

### 2.5 导航类（navigation.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 2.5.1 | 导航类全部存在：`DTabBar`/`DDrawer`/`DDrawerGroup`/`DStackWidget` | glob 头文件 | `include/DWidget/` |
| 2.5.2 | `DTabBar` 方法 `addTab` + 信号 `currentChanged(int)` | 核对 | `dtabbar.h` |
| 2.5.3 | `DDrawer` 方法 `setHeader`/`setContent`/`setExpand` + 信号 `expandChange(bool)` | 核对 | `ddrawer.h` |
| 2.5.4 | `DDrawerGroup` 方法 `addDrawer` + 信号 `drawerClicked(int)` | 核对 | `ddrawergroup.h` |
| 2.5.5 | `DBaseExpand`/`DExpandGroup` 弃用标注 | grep deprecated | 对应头文件 |

### 2.6 进度类（progress.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 2.6.1 | 进度类全部存在：`DProgressBar`/`DColoredProgressBar`/`DIndeterminateProgressBar`/`DCircleProgress`/`DWaterProgress`/`DSpinner`/`DLoadingIndicator` | glob 头文件 | `include/DWidget/` |
| 2.6.2 | `DProgressBar` 方法 `setRange`/`setValue`/`setOrientation` | 核对 | `dprogressbar.h` |
| 2.6.3 | `DIndeterminateProgressBar` 方法 `start`/`stop` | 核对 | `dindeterminateprogressbar.h` |
| 2.6.4 | `DSpinner` 方法 `start`/`stop` | 核对 | `dspinner.h` |
| 2.6.5 | `DCircleProgress` 方法 `setValue`（0-100） | 核对 | `dcircleprogress.h` |
| 2.6.6 | `DWaterProgress` 方法 `setValue`（0-100）/`start`/`stop` | 核对 | `dwaterprogress.h` |
| 2.6.7 | `DCircleProgress` 弃用标注 | grep deprecated | 同上 |

### 2.7 视图类（view.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 2.7.1 | 视图类全部存在：`DListView`/`DSimpleListView`/`DStyledItemDelegate`/`DSimpleListItem` | glob 头文件 | `include/DWidget/` |
| 2.7.2 | `DListView` 方法 `setModel`/`setItemDelegate` | 核对 | `dlistview.h` |
| 2.7.3 | `DStyledItemDelegate` 构造函数 `(parent)` | 核对 | `dstyleditemdelegate.h` |

### 2.8 窗口类（window.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 2.8.1 | 窗口类全部存在：`DMainWindow`/`DTitlebar`/`DApplication`/`DPlatformWindowHandle` | glob 头文件 | `include/DWidget/` |
| 2.8.2 | `DMainWindow` 方法：`titlebar()`/`setCentralWidget`/`setSidebarWidget`/`setSidebarWidth`/`setSidebarVisible`/`setSidebarExpanded`/`sidebarVisible`/`setWindowRadius`/`setBorderWidth`/`setBorderColor`/`setShadowRadius`/`setShadowOffset`/`setShadowColor`/`setTranslucentBackground`/`setEnableBlurWindow`/`sendMessage`(2 重载)/`isDXcbWindow` | 逐个核对 | `dmainwindow.h` |
| 2.8.3 | `DTitlebar` 方法：`setTitle`/`setIcon`/`setMenu`/`setMenuVisible`/`setSwitchThemeMenuVisible`/`addWidget`/`setCustomWidget`/`setDisableFlags`/`setFullScreenButtonVisible`/`setSplitScreenEnabled` | 逐个核对 | `dtitlebar.h` |
| 2.8.4 | `DApplication` 构造函数 `(argc, argv)` | 核对 | `dapplication.h` |

### 2.9 容器类（container.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 2.9.1 | 容器类全部存在：`DFrame`/`DBackgroundGroup`/`DHeaderLine`/`DLine`/`DHorizontalLine`/`DVerticalLine` | glob 头文件 | `include/DWidget/` |
| 2.9.2 | `DFrame` 方法 `setFrameRounded`/`setBackgroundRole` | 核对 | `dframe.h` |
| 2.9.3 | `DBackgroundGroup` 方法 `setBackgroundRole` | 核对 | `dbackgroundgroup.h` |
| 2.9.4 | `DHeaderLine` 方法 `setTitle` | 核对 | `dheaderline.h` |
| 2.9.5 | `DLine` 方法 `setOrientation` | 核对 | `dline.h` |

### 2.10 CMake 验证

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 2.10.1 | CMake `find_package(DtkWidget)` + `Dtk::Widget` target | 检查 cmake | `dtkwidget/dtkwidget.cmake` |

---

## 模块 3：declarative（QML 控件）— 来源 dtkdeclarative

**参考文档：** `references/declarative/index.md`, `references/declarative/buttons.md`, `references/declarative/inputs.md`, `references/declarative/menus.md`, `references/declarative/dialogs.md`, `references/declarative/panels.md`, `references/declarative/lists.md`, `references/declarative/progress.md`, `references/declarative/color-selector.md`, `references/declarative/dci-icon.md`, `references/declarative/effects.md`

**源码位置：** `~/dtk/dtkdeclarative/qmlplugin/`（Qt5）+ `~/dtk/dtkdeclarative/qt6/`（Qt6）+ `~/dtk/dtkdeclarative/src/qml/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 3.1 | QML 模块 URI `org.deepin.dtk` 正确 | 检查 `qmldir` 文件 | `qmlplugin/qmldir` |
| 3.2 | 按钮类控件 QML 文件存在：`Button`/`RecommandButton`/`WarningButton`/`ToolButton`/`IconButton`/`ActionButton`/`FloatingButton`/`DelayButton`/`RadioButton`/`CheckBox`/`Switch` | 在 `src/qml/` 中确认 | `src/qml/` |
| 3.3 | 输入类控件 QML 文件存在：`TextField`/`LineEdit`/`SearchEdit`/`PasswordEdit`/`SpinBox`/`PlusMinusSpinBox`/`IpV4LineEdit`/`KeySequenceEdit`/`ComboBox` | 在 `src/qml/` 中确认 | `src/qml/` |
| 3.4 | 菜单类控件 QML 文件存在：`Menu`/`MenuItem`/`MenuSeparator`/`ThemeMenu` | 在 `src/qml/` 中确认 | `src/qml/` |
| 3.5 | 对话框/窗口类控件 QML 文件存在：`ApplicationWindow`/`DialogWindow`/`DialogTitleBar`/`AboutDialog`/`TitleBar`/`WindowButtonGroup`/`Popup`/`ArrowShapePopup`/`FloatingMessage`/`AlertToolTip` | 在 `src/qml/` 中确认 | `src/qml/` |
| 3.6 | 面板/视觉类控件 QML 文件存在：`BoxPanel`/`ButtonPanel`/`ButtonBox`/`FloatingPanel`/`HighlightPanel`/`BoxShadow`/`BoxInsetShadow`/`InsideBoxBorder`/`OutsideBoxBorder`/`FocusBoxBorder`/`CicleSpreadAnimation` | 在 `src/qml/` 中确认 | `src/qml/` |
| 3.7 | 列表类控件 QML 文件存在：`ItemDelegate`/`CheckDelegate`/`ArrowListView` | 在 `src/qml/` 中确认 | `src/qml/` |
| 3.8 | 进度/滑动类控件 QML 文件存在：`ProgressBar`/`EmbeddedProgressBar`/`WaterProgressBar`/`BusyIndicator`/`ScrollBar`/`Slider`/`TipsSlider` | 在 `src/qml/` 中确认 | `src/qml/` |
| 3.9 | CMake `find_package(DtkDeclarative)` + `Dtk::Declarative` | 检查 cmake | `dtkdeclarative/cmake/` |
| 3.10 | `ColorSelector` 类型为附加属性（`QML_ATTACHED` + `QML_UNCREATABLE`） | grep `ColorSelector` | `src/private/dquickcontrolpalette_p.h` |
| 3.11 | `ColorSelector` 属性 `control`/`controlTheme`/`controlState`/`family`/`hovered`/`pressed`/`disabled`/`inactived` 存在 | 核对 Q_PROPERTY | `dquickcontrolpalette_p.h` |
| 3.12 | `ColorSelector::controlState` 枚举值 `NormalState`/`HoveredState`/`PressedState`/`DisabledState`/`InactiveState` | grep `ControlState` | `dqmlglobalobject_p.h` |
| 3.13 | `Palette` 类型可创建，属性 `enabled`/`normal`/`normalDark`/`hovered`/`hoveredDark`/`pressed`/`pressedDark`/`disabled`/`disabledDark` 存在 | 核对 Q_PROPERTY | `dquickcontrolpalette_p.h` |
| 3.14 | `Palette::ColorFamily` 枚举 `CommonColor`/`CrystalColor`，`DQuickControlColor` 有 `common`/`crystal` | grep enum + Q_PROPERTY | `dquickcontrolpalette_p.h` |
| 3.15 | `DciIcon` QML 类型注册存在，类型名为 `DciIcon`（非 `DciIconImage`） | 核对 `qmlRegisterType`/`QML_NAMED_ELEMENT` | `qmlplugin_plugin.cpp` |
| 3.16 | `DciIcon` 属性 `name`(QString)/`mode`(ControlState)/`theme`(ColorType)/`palette`(DDciIconPalette)/`sourceSize`(QSize)/`mirror`(bool)/`fallbackToQIcon`(bool)/`asynchronous`(bool)/`cache`(bool)/`fillMode`(QQuickImage::FillMode) 全部存在 | 核对 Q_PROPERTY | `dquickdciiconimage_p.h` |
| 3.17 | `DciIcon` 属性 `retainWhileLoading`(bool) 存在（Qt >= 6.8.0） | grep Q_PROPERTY | `dquickdciiconimage_p.h` |
| 3.18 | `D.DTK.makeIconPalette()` 函数在 QML 全局对象中存在，接收 `palette` 参数（Qt5: QPalette，Qt6: QQuickPalette*） | grep `makeIconPalette` | `dqmlglobalobject_p.h` + `dqmlglobalobject.cpp` |
| 3.19 | `makeIconPalette` 实现正确映射：foreground←WindowText, background←Window, highlight←Highlight, highlightForeground←HighlightedText | 核对实现 | `dqmlglobalobject.cpp` |

---

## 模块 4：config（配置系统）— 来源 dtkcore + dde-app-services

**参考文档：** `references/config/index.md`, `references/config/concepts.md`, `references/config/dconfig-cpp.md`, `references/config/dconfig-dbus.md`, `references/config/dconfig-debug.md`

**源码位置：** `~/dtk/dtkcore/include/global/` + `~/dtk/dde-app-services/dconfig-center/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 4.1 | `DConfig` 类存在 | grep `class DConfig` | `dtkcore/include/global/dconfig.h` |
| 4.2 | `DConfig` 静态方法 `create(appId, name, subpath, parent)` 和 `createGeneric(name, subpath, parent)` | 核对签名 | 同上 |
| 4.3 | `DConfig` 构造函数 `DConfig(name, subpath, parent)`（无 appId） | 核对 | 同上 |
| 4.4 | `DConfig` 实例方法：`value(key, fallback)`/`setValue(key, value)`/`keyList()`/`isValid()`/`isDefaultValue(key)`/`isReadOnly(key)`/`reset(key)` | 逐个核对 | 同上 |
| 4.5 | `DConfig` 信号 `valueChanged(const QString &)` | grep signal | 同上 |
| 4.6 | `DConfig::setAppId()` 和 `DConfig::globalThread()` 静态方法 | 核对 | 同上 |
| 4.7 | dconfig2cpp 工具存在：`dtkcore/tools/dconfig2cpp/main.cpp` | glob 检查 | `tools/dconfig2cpp/` |
| 4.8 | dconfig2cpp 生成的类有 `create(appId, subpath, parent)` 工厂方法 | grep `static.*create` | `tools/dconfig2cpp/main.cpp` |
| 4.9 | 生成类信号 `configInitializeSucceed(DConfig*)` / `configInitializeFailed()` | grep signals | 同上 |
| 4.10 | 生成类状态方法：`isInitializeSucceeded()`（新接口）/ `isInitializeSucceed()`（deprecated） | grep `isInitializeSucceed` | 同上 |
| 4.11 | CMake `dtk_add_config_meta_files()` 宏定义 | grep macro/function | `dtkcore/cmake/DtkDConfig/DtkDConfigConfig.cmake` |
| 4.12 | CMake `dtk_add_config_to_cpp()` 宏定义 | grep macro/function | `dtkcore/cmake/DtkTools/DtkDConfigMacros.cmake` |
| 4.13 | meta 文件 `magic` 值 `"dsg.config.meta"` 与 dconfig2cpp 校验一致 | grep `dsg.config.meta` | `tools/dconfig2cpp/main.cpp` |
| 4.14 | dde-dconfig CLI 支持 `-s <subpath>` 选项 | 运行 `dde-dconfig --help` | `dde-app-services/dconfig-center/dde-dconfig/` |
| 4.15 | dde-dconfig-daemon systemd service 用户为 `deepin-daemon` | grep `User=` | `dde-dconfig-daemon/services/dde-dconfig-daemon.service` |
| 4.16 | systemd service `StateDirectory=dde-dconfig-daemon` + `LogsDirectory=deepin` | grep | 同上 |
| 4.17 | daemon 中 `setCachePathPrefix()` 调用：global 为 `configPrefixPath() + "/global"`，用户为 `configPrefixPath() + "/{uid}"` | grep `setCachePathPrefix` | `dde-dconfig-daemon/dconfigresource.cpp` |
| 4.18 | daemon `configPrefixPath()` 优先 `STATE_DIRECTORY` 环境变量 | grep `STATE_DIRECTORY` | `dde-dconfig-daemon/dconfig_global.h` |
| 4.19 | DSMG 概念：`DSettingsDialog` 属 dtkwidget 而非 config 模块，已在 `widgets/dialog.md` 中描述 | 确认文件位置 | `widgets/dialog.md` |

---

## 模块 5：utilities（工具类）— 来源 dtkcore + dtkgui/dtkwidget

**参考文档：** `references/utilities/index.md`, `references/utilities/log.md`, `references/utilities/util.md`, `references/utilities/singleton.md`

**源码位置：** `~/dtk/dtkcore/include/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 5.1 | `DStandardPaths` 类存在，`writableLocation(StandardLocation)` 方法 | grep class + method | `include/filesystem/dstandardpaths.h` |
| 5.2 | `DStandardPaths` 枚举值 `AppConfigLocation`/`AppDataLocation`/`CacheLocation`/`TempLocation` 存在 | grep enum | 同上 |
| 5.3 | `DFileWatcher` 类存在，构造函数 + `addPath` 方法 + `fileChanged` 信号 | grep class + methods | `include/filesystem/dfilewatcher.h` |
| 5.4 | `DTrashManager` 类存在，静态方法 `moveToTrash`/`emptyTrash` | grep class + methods | `include/filesystem/dtrashmanager.h` |
| 5.5 | `DDBusInterface` 类存在，构造函数 `(service, path, connection)` + `call` 方法 + `signal` 信号 | grep class + methods | `include/util/ddbusinterface.h` |
| 5.6 | `DDBusSender` 类存在，builder 方法 `service`/`path`/`interface`/`signal`/`arg`/`publish` 全部存在且返回 `DDBusSender&` | 逐个核对 | `include/util/ddbussender.h` |
| 5.7 | `DNotifySender` 类存在，builder 方法 `appName`/`appIcon`/`appBody`/`replaceId`/`timeOut`/`actions`/`hints`/`call` | grep class + methods | `include/util/dnotifysender.h` |
| 5.8 | `DObject`/`DSingleton`/`DError` 基类存在 | grep class | `include/base/` |
| 5.9 | `DLogManager` 类存在，`registerConsoleAppender`/`registerFileAppender`/`registerJournalAppender`/`setlogFilePath`/`setLogFormat` 方法 | grep class + method | `include/log/LogManager.h` |
| 5.10 | `DDciFile` 类存在（dci 文件解析，来自 dtkcore） | grep `class DDciFile` | `include/dci/ddcifile.h` |
| 5.11 | dtklog 日志宏 `dDebug`/`dInfo`/`dWarning`/`dError`/`dFatal` 存在 | grep 宏定义 | `dtklog/include/dloggerdefs.h` |
| 5.12 | dtklog `Logger` 类存在，`LogLevel` 枚举 `Trace`/`Debug`/`Info`/`Warning`/`Error`/`Fatal` | grep class + enum | `dtklog/include/Logger.h` |
| 5.13 | `DSysInfo` 类存在，枚举 `ProductType`/`DeepinType`/`UosType`/`UosEdition`/`Arch` 等 | grep class + enum | `dtkcore/include/global/dsysinfo.h` |
| 5.14 | `DSysInfo` 静态方法：`productType()`/`isDeepin()`/`isDDE()`/`deepinVersion()`/`uosEditionType()`/`computerName()`/`cpuModelName()`/`memoryInstalledSize()`/`uptime()`/`arch()` | grep static | 同上 |
| 5.15 | 拼音函数存在：`Chinese2Pinyin()`/`pinyin()`/`firstLetters()`（自由函数，非类成员） | grep function | `dtkcore/include/util/dpinyin.h` |
| 5.16 | `ToneStyle` 枚举 `TS_NoneTone`/`TS_Tone`/`TS_ToneNum` | grep enum | 同上 |

---

## 模块 6：log（已合并到模块 5 utilities）

日志文档已合并到 `references/utilities/index.md`，原 `references/log/` 目录已删除。原模块 7 的验证项已合并到模块 5（5.11-5.14）。

---

## 模块 7：平台集成（qt5integration + qt5platform-plugins）

**参考文档：** `SKILL.md` 中的"仓库依赖关系"和"核心库 vs 平台集成库"说明

**源码位置：** `~/dtk/qt5integration/` + `~/dtk/qt5platform-plugins/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 7.1 | SKILL.md 声称 dtkwidget 运行时依赖 qt5integration（Chameleon 风格） | 确认 `ChameleonStyle` 继承 `DStyle` | `qt5integration/styleplugins/chameleon/chameleonstyle.h` |
| 7.2 | SKILL.md 声称 qt5integration 运行时依赖 qt5platform-plugins | 确认两者有关联（检查 cmake 或代码引用） | 两项目源码 |
| 7.3 | SKILL.md 声称 dtkwidget 编译不依赖 qt5integration/qt5platform-plugins | 确认 dtkwidget 的 CMakeLists 不引用这两个项目 | `dtkwidget/CMakeLists.txt` |
| 7.4 | SKILL.md 声称 `DDciFile` 来自 dtkcore，`DDciIcon` 来自 dtkgui | 确认类所在项目 | 已在 1.1 和 6.11 验证 |
| 7.5 | SKILL.md 依赖图：dtkcommon→dtkcore, dtkcommon→dtkgui, dtkcore→dtklog, dtkcore→dtkgui, dtkcore→dtkwidget, dtkcore→dtkdeclarative, dtkgui→dtkdeclarative, dtkgui→qt5platform-plugins | 逐个检查 CMakeLists 中的 `find_package` | 各项目 `CMakeLists.txt` |

---

## 模块 8：跨文档一致性验证

**说明：** 在逐模块验证过程中发现的文档内部不一致问题需要集中确认和修正。

| # | 验证项 | 不一致描述 | 涉及文档 |
|---|--------|-----------|----------|
| 8.1 | `DNotifySender` API 形态 | index.md 描述 builder 链模式 `.call()` | `utilities/index.md` |
| 8.2 | QML `StackView` vs `StackLayout` | index.md 列 `StackView`，controls.md 用 `StackLayout`（controls.md 已删除，此条已废弃） | `declarative/index.md` |
| 8.3 | `DciIcon` 属性完整性和 `ColorSelector` 配合使用方式 | 文档 `dci-icon.md` 需包含所有 Q_PROPERTY 属性及 `ColorSelector` 配合示例 | `declarative/dci-icon.md` vs 源码 `dquickdciiconimage_p.h` |

---

## 模块 9：architecture（核心架构）— 来源全部项目

**参考文档：** `references/architecture.md`

**源码位置：** `~/dtk/dtkgui/`、`~/dtk/dtkwidget/`、`~/dtk/dtkdeclarative/`、`~/dtk/qt5integration/`、`~/dtk/qt5platform-plugins/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 9.1 | 调色板系统：`DPalette` 类存在，`DGuiApplicationHelper::standardPalette()` 方法 | grep class + method | `dtkgui/include/kernel/dguiapplicationhelper.h` |
| 9.2 | 调色板系统：`DStyleHelper::getColor()` 方法存在 | grep method | `dtkwidget/include/widgets/dstyle.h` |
| 9.3 | 字体系统：`DFontManager` 类存在，`t1()`-`t11()` 方法，`SizeType` 枚举 T1-T11 | grep class + enum | `dtkgui/include/util/dfontmanager.h` |
| 9.4 | 字体系统：`DFontSizeManager` 类存在，`bind(QWidget*, SizeType)` 方法 | grep class + method | `dtkwidget/include/widgets/dstyleoption.h` |
| 9.5 | 字体系统：`D.DTK.fontManager` QML 属性存在 | grep `fontManager` | `dtkdeclarative/src/private/dqmlglobalobject_p.h` |
| 9.6 | 图标系统：`DDciIcon`/`DIconTheme`/`DDciIconPlayer` 类存在 | grep class | `dtkgui/include/util/ddciicon.h`、`dicontheme.h` |
| 9.7 | 平台抽象：`DPlatformHandle` 类存在，属性 `windowRadius`/`shadowRadius`/`enableBlurWindow` 等 | grep class + Q_PROPERTY | `dtkgui/include/kernel/dplatformhandle.h` |
| 9.8 | 平台抽象：`DPlatformTheme` 类存在，属性 `fontName`/`activeColor`/`iconThemeName` 等 | grep class + Q_PROPERTY | `dtkgui/include/kernel/dplatformtheme.h` |
| 9.9 | 平台抽象：`DPlatformWindowInterface` 抽象基类存在 | grep class | `dtkgui/src/private/dplatformwindowinterface_p.h` |
| 9.10 | 平台分发：`DXCBPlatformWindowInterface`/`DTreeLandPlatformWindowInterface` 存在 | grep class | `dtkgui/src/plugins/platform/xcb/`、`treeland/` |
| 9.11 | QPA 层：`DPlatformIntegration`/`DWaylandIntegration` 存在 | grep class | `qt5platform-plugins/xcb/`、`wayland/` |
| 9.12 | 平台检测：`DGuiApplicationHelper::IsXWindowPlatform`/`IsWaylandPlatform` 属性存在 | grep enum Attribute | `dtkgui/include/kernel/dguiapplicationhelper.h` |

## 模块 10：platform-abstraction（平台抽象层）— 来源 dtkgui + qt5platform-plugins

**参考文档：** `references/platform-abstraction.md`

**源码位置：** `~/dtk/dtkgui/` + `~/dtk/qt5platform-plugins/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 10.1 | `DPlatformHandle` 属性全部存在：`windowRadius`/`borderWidth`/`borderColor`/`shadowRadius`/`shadowOffset`/`shadowColor`/`clipPath`/`frameMask`/`frameMargins`/`translucentBackground`/`enableSystemResize`/`enableSystemMove`/`enableBlurWindow`/`autoInputMaskByClipPath`/`realWindowId` | 核对 Q_PROPERTY | `dplatformhandle.h` |
| 10.2 | `DPlatformHandle::EffectScene` 枚举值 `EffectNoRadius`/`EffectNoShadow`/`EffectNoBorder`/`EffectNoStart`/`EffectNoClose`/`EffectNoMaximize`/`EffectNoMinimize` | grep enum | 同上 |
| 10.3 | `DPlatformHandle::EffectType` 枚举值 `EffectNormal`/`EffectCursor`/`EffectTop`/`EffectBottom`/`EffectOut` | grep enum | 同上 |
| 10.4 | `DPlatformHandle::WMBlurArea` 结构体存在，`dMakeWMBlurArea()` 辅助函数 | grep struct + inline | 同上 |
| 10.5 | `DPlatformHandle::setWindowBlurAreaByWM()` 静态方法存在（2 个重载） | grep method | 同上 |
| 10.6 | `DPlatformHandle::setEnabledNoTitlebarForWindow()`/`isEnabledNoTitlebar()` 静态方法 | grep method | 同上 |
| 10.7 | `DPlatformTheme` 属性全部存在：字体（fontName/monoFontName/fontPointSize/gtkFontName）、主题（themeName/iconThemeName/soundThemeName/activeColor/darkActiveColor）、输入（cursorBlink* / doubleClick* / dndDragThreshold）、sizeMode/scrollBarPolicy | 核对 Q_PROPERTY | `dplatformtheme.h` |
| 10.8 | 平台分发：`createWindowInterface()` 函数按 `IsXWindowPlatform`/`IsWaylandPlatform` 分发 | 核对代码逻辑 | `dplatformhandle.cpp:307-328` |
| 10.9 | `DPlatformWindowInterface` 抽象基类虚函数完整 | grep virtual | `dplatformwindowinterface_p.h` |
| 10.10 | Treeland 实现通过 `treeland_personalization_manager_v1` Wayland 协议通信 | grep protocol | `dtkgui/src/plugins/platform/treeland/personalizationwaylandclientextension.h` |
| 10.11 | `qt5platform-plugins` 包含 `xcb/` 和 `wayland/` 两个 QPA 插件目录 | ls 目录结构 | `qt5platform-plugins/` |
| 10.12 | 窗口拖拽 X11 实现：`DNoTitlebarWindowHelper` 类存在，`windowEvent()`/`startMoveWindow()`/`updateMoveWindow()` 方法 | grep class + methods | `qt5platform-plugins/xcb/dnotitlebarwindowhelper.h` |
| 10.13 | 窗口拖拽 X11 底层：`Utility::startWindowSystemMove()` 发送 `_NET_WM_MOVERESIZE_MOVE`，`updateMousePointForWindowMove()` 发送 `_DEEPIN_MOVE_UPDATE` | grep methods | `qt5platform-plugins/xcb/utility_x11.cpp` |
| 10.14 | 窗口拖拽 Treeland 实现：`MoveWindowHelper` 类存在（dtkgui 内），`windowEvent()` 拦截鼠标事件并调用 `QPlatformWindow::startSystemMove()` | grep class + method | `dtkgui/src/plugins/platform/treeland/dtreelandplatformwindowinterface.cpp` |
| 10.15 | 窗口拖拽 dwayland 实现：`DNoTitlebarWlWindowHelper` 类存在，`startMoveWindow()` 调用 `QWaylandWindow::startSystemMove()` | grep class + method | `qt5platform-plugins/wayland/dwayland/dnotitlebarwindowhelper_wl.h` |

---

## 模块 11：核心类（已合并至 utilities）— 来源 dtkcore/dtkgui/dtkwidget

**参考文档：** `references/utilities/index.md`, `references/utilities/gui-helper.md`, `references/utilities/font-manager.md`, `references/utilities/sysinfo.md`, `references/utilities/dbus.md`, `references/utilities/window-manager.md`, `references/utilities/desktop-services.md`, `references/widgets/application.md`, `references/widgets/blur-effect.md`, `references/declarative/dtk-global.md`, `references/declarative/dwindow.md`

**源码位置：** `~/dtk/dtkgui/include/kernel/` + `~/dtk/dtkcore/include/` + `~/dtk/dtkwidget/include/widgets/` + `~/dtk/dtkdeclarative/src/`

### 11.1 DGuiApplicationHelper（gui-helper.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 11.1.1 | `ColorType` 枚举有 `UnknownType`/`LightType`/`DarkType` | grep enum | `dguiapplicationhelper.h` |
| 11.1.2 | `SizeMode` 枚举有 `NormalMode`/`CompactMode` | grep enum | `dguiapplicationhelper.h` |
| 11.1.3 | `Attribute` 枚举有 `UseInactiveColorGroup`/`ColorCompositing`/`DontSaveApplicationTheme`/`IsWaylandPlatform`/`HasAnimations`/`HasInWindowBlur` | grep enum | `dguiapplicationhelper.h` |
| 11.1.4 | `instance()` 静态方法存在 | grep | `dguiapplicationhelper.h` |
| 11.1.5 | `themeTypeChanged`/`paletteTypeChanged`/`newProcessInstance`/`fontChanged`/`applicationPaletteChanged`/`sizeModeChanged` 信号 | grep Q_SIGNALS | `dguiapplicationhelper.h` |
| 11.1.6 | `adjustColor`/`blendColor`/`toColorType`/`standardPalette`/`generatePaletteColor`/`generatePalette` 静态方法 | 逐个核对 | `dguiapplicationhelper.h` |
| 11.1.7 | `setSingleInstance`/`setSingleInstanceInterval` 静态方法 | grep | `dguiapplicationhelper.h` |
| 11.1.8 | `isCompactMode()` 内联静态方法 | grep | `dguiapplicationhelper.h` |

### 11.2 DFontSizeManager/DFontManager（font-manager.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 11.2.1 | `DFontSizeManager::instance()` 存在 | grep | `dstyleoption.h` |
| 11.2.2 | `SizeType` 枚举有 `T1`~`T11`/`NSizeTypes` | grep enum | `dstyleoption.h` + `dfontmanager.h` |
| 11.2.3 | `bind(QWidget*, SizeType)`/`unbind(QWidget*)` 方法 | grep | `dstyleoption.h` |
| 11.2.4 | `get(SizeType)`/`t1()`~`t10()` 便捷方法 | grep | `dstyleoption.h` |
| 11.2.5 | `DFontManager` 通过 `DGuiApplicationHelper::instance()->fontManager()` 访问 | grep fontManager | `dguiapplicationhelper.h` |
| 11.2.6 | 像素大小数组 `{40,30,24,20,16,14,13,12,11,10,8}` | 核对 dtkgui 和 dtkwidget 的私有实现 | `dfontmanager_p.h` + `dstyleoption.cpp` |

### 11.3 DSysInfo（sysinfo.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 11.3.1 | `ProductType` 枚举有 `Deepin`/`Uos`/`ArchLinux` 等 14 值 | grep enum | `dsysinfo.h` |
| 11.3.2 | `DeepinType` 枚举有 `DeepinDesktop`/`DeepinProfessional`/`DeepinServer` 等 | grep enum | `dsysinfo.h` |
| 11.3.3 | `UosType` 枚举有 `UosDesktop`/`UosServer`/`UosDevice`/`UosSmart` | grep enum | `dsysinfo.h` |
| 11.3.4 | `UosEdition` 枚举有 `UosProfessional`/`UosHome`/`UosCommunity` 等 12 值 | grep enum | `dsysinfo.h` |
| 11.3.5 | `isDeepin()`/`isDDE()`/`isCommunityEdition()` 静态方法 | grep | `dsysinfo.h` |
| 11.3.6 | `uosEditionType()`/`uosType()`/`majorVersion()`/`minorVersion()` 静态方法 | grep | `dsysinfo.h` |

### 11.4 DDBusSender（dbus.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 11.4.1 | `DDBusSender` 类存在，流畅构建器模式 `service()`/`path()`/`interface()`/`method()`/`call()` | grep class + methods | `ddbussender.h` |
| 11.4.2 | `DDBusSender::system()` 静态工厂方法 | grep | `ddbussender.h` |
| 11.4.3 | `DDBusProperty` 的 `get()`/`set()` 方法 | grep | `ddbussender.h` |
| 11.4.4 | `DDBusInterface` 继承 `QDBusAbstractInterface`，有 `serviceValid()`/`serviceValidChanged` | grep | `ddbusinterface.h` |

### 11.5 DWindowManagerHelper（window-manager.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 11.5.1 | `MotifFunction` 枚举有 `FUNC_RESIZE`/`FUNC_MOVE`/`FUNC_MINIMIZE`/`FUNC_MAXIMIZE`/`FUNC_CLOSE`/`FUNC_ALL` | grep enum | `dwindowmanagerhelper.h` |
| 11.5.2 | `MotifDecoration` 枚举有 `DECOR_BORDER`/`DECOR_TITLE`/`DECOR_ALL` 等 | grep enum | `dwindowmanagerhelper.h` |
| 11.5.3 | `WMName` 枚举有 `OtherWM`/`DeepinWM`/`KWinWM` | grep enum | `dwindowmanagerhelper.h` |
| 11.5.4 | `instance()`/`hasBlurWindow()`/`hasComposite()`/`setMotifFunctions()`/`setMotifDecorations()` | 逐个核对 | `dwindowmanagerhelper.h` |

### 11.6 DDesktopServices（desktop-services.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 11.6.1 | `SystemSoundEffect` 枚举有 `SSE_Notifications`/`SEE_Screenshot`（拼写错误）/`SSE_Error` 等 | grep enum | `ddesktopservices.h` |
| 11.6.2 | `showFolder()`/`showFileItem()`/`showFileItemProperty()`/`trash()` 静态方法 | grep | `ddesktopservices.h` |
| 11.6.3 | `playSystemSoundEffect()`/`previewSystemSoundEffect()` 静态方法 | grep | `ddesktopservices.h` |

### 11.7 DApplication（application.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 11.7.1 | `DApplication` 继承 `QApplication`，`qApp` 宏重定义 | grep class + macro | `dapplication.h` |
| 11.7.2 | `setSingleInstance()`/`loadTranslator()` 方法 | grep | `dapplication.h` |
| 11.7.3 | `productName()`/`productIcon()`/`applicationDescription()`/`applicationHomePage()`/`applicationLicense()` | grep | `dapplication.h` |
| 11.7.4 | `newInstanceStarted`/`iconThemeChanged`/`screenDevicePixelRatioChanged` 信号 | grep Q_SIGNALS | `dapplication.h` |
| 11.7.5 | `buildDtkVersion()`/`runtimeDtkVersion()`/`buildVersion()` 静态方法 | grep | `dapplication.h` |

### 11.8 DBlurEffectWidget（blur-effect.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 11.8.1 | `BlendMode` 枚举有 `InWindowBlend`/`BehindWindowBlend`/`InWidgetBlend` | grep enum | `dblureffectwidget.h` |
| 11.8.2 | `MaskColorType` 枚举有 `DarkColor`/`LightColor`/`AutoColor`/`CustomColor` | grep enum | `dblureffectwidget.h` |
| 11.8.3 | `radius`/`blendMode`/`maskColor`/`maskAlpha`/`blurEnabled` 属性 | grep Q_PROPERTY | `dblureffectwidget.h` |
| 11.8.4 | `setMaskPath()`/`setSourceImage()` 方法 | grep | `dblureffectwidget.h` |

### 11.9 D.DTK QML 全局对象（dtk-global.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 11.9.1 | `DTK` QML 单例注册（`QML_NAMED_ELEMENT(DTK)` + `QML_SINGLETON`） | grep | `dqmlglobalobject_p.h` |
| 11.9.2 | `fontManager`/`themeType`/`hasBlurWindow`/`hasComposite`/`hasAnimation` 属性 | grep Q_PROPERTY | `dqmlglobalobject_p.h` |
| 11.9.3 | `makeIconPalette()`/`makeColor()`/`blendColor()`/`toColorType()`/`selectColor()` Q_INVOKABLE 方法 | grep | `dqmlglobalobject_p.h` |
| 11.9.4 | `ControlState` 枚举有 `NormalState`/`HoveredState`/`PressedState`/`DisabledState`/`InactiveState` | grep enum | `dqmlglobalobject_p.h` |
| 11.9.5 | `DColor` 值类型有 `Type` 枚举（`Invalid`/`Highlight`/`HighlightedText`）+ `lightness()`/`opacity()`/`saturation()`/`hue()` 方法 | grep | `dqmlglobalobject_p.h` |

### 11.10 D.DWindow QML 附加属性（dwindow.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 11.10.1 | `DWindow` QML 附加属性注册（`QML_ATTACHED(DQuickWindowAttached)`） | grep | `dquickwindow.h` |
| 11.10.2 | `enabled`/`windowRadius`/`borderWidth`/`borderColor`/`shadowRadius`/`shadowOffset`/`shadowColor` 属性 | grep Q_PROPERTY | `dquickwindow.h` |
| 11.10.3 | `enableBlurWindow`/`enableSystemResize`/`enableSystemMove`/`translucentBackground` 属性 | grep Q_PROPERTY | `dquickwindow.h` |
| 11.10.4 | `themeType` 属性（Qt6 only）+ `windowEffect`/`windowStartUpEffect` 属性 | grep Q_PROPERTY | `dquickwindow.h` |
| 11.10.5 | `popupSystemWindowMenu()`/`showMinimized()`/`showMaximized()`/`showFullScreen()`/`showNormal()` slots | grep | `dquickwindow.h` |

---

## 执行策略

### 并行分组

建议将 10 个模块分为以下并行执行组（每组分配一个 explore agent）：

| 执行组 | 包含模块 | 预估项数 |
|--------|----------|---------|
| Group A | 模块 1（theme，含图标+调色板） | 29 |
| Group B | 模块 2（widgets，2.1-2.5） | ~25 |
| Group C | 模块 2（widgets，2.6-2.10） | ~20 |
| Group D | 模块 3（declarative） | 19 |
| Group E | 模块 4（config） | 15 |
| Group F | 模块 5（utilities，含日志+系统信息+拼音） | 18 |
| Group G | 模块 7（平台集成）+ 模块 8（跨文档一致性） | 10 |
| Group H | 模块 9（architecture）+ 模块 10（platform-abstraction） | 27 |
| Group I | 模块 11（core，核心类+高频接口） | ~40 |

### 执行方式

每组的 explore agent 将收到：

1. 该组所有模块的详细验证项列表（含表号）
2. 对应文档路径（用于读取文档声称的 API 列表）
3. 对应源码路径（用于 grep 验证）
4. 指令：对每项输出 PASS / FAIL / NOT FOUND，完成后返回汇总

### 汇总

所有组完成后，汇总生成一份验证报告，列出所有 FAIL（不一致）和 NOT FOUND（缺失）项，作为 skill 文档修正的依据。
