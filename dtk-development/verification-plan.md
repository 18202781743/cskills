# DTK Skill 验证计划

## 目标

验证 `dtk-development` skill 中每个参考文档声称的 **类名、枚举值、方法签名、QML 类型、CMake 指令** 与 `~/dtk` 源码一致，确保 skill 能真正指导开发 DTK 应用。

## 验证范围

Skill 覆盖 8 个 DTK 项目，按参考文档结构划分为 7 个功能模块 + 1 个平台集成模块 + 1 个跨文档一致性模块，共 **9 个验证模块**。

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

---

## 模块 1：icons（图标系统）— 来源 dtkgui

**参考文档：** `references/icons/index.md`, `references/icons/builtin.md`, `references/icons/dci.md`, `references/icons/icontheme.md`

**源码位置：** `~/dtk/dtkgui/include/util/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 1.1 | `DDciIcon` 类存在，构造函数 `DDciIcon(QString path)` 和 `DDciIcon(QByteArray)` | grep `class DDciIcon` + 构造函数声明 | `ddciicon.h` |
| 1.2 | `DDciIcon::Theme` 枚举有 `Light`/`Dark` | grep `enum.*Theme` | `ddciicon.h` |
| 1.3 | `DDciIcon::Mode` 枚举有 `Normal`/`Disabled`/`Hover`/`Pressed` | grep `enum.*Mode` | `ddciicon.h` |
| 1.4 | `DDciIcon::HasPalette` 属性枚举存在 | grep `HasPalette` | `ddciicon.h` |
| 1.5 | `DDciIcon::fromTheme()` 静态方法（1 参和 2 参重载） | grep `fromTheme` | `ddciicon.h` |
| 1.6 | `pixmap()`、`paint()`、`availableSizes()`、`isNull()` 方法签名 | 逐个核对 | `ddciicon.h` |
| 1.7 | `DDciIconPlayer` 类存在，方法 `setIcon`/`setIconSize`/`setTheme`/`play`/`currentImage`，信号 `updated` | grep class + 方法 | `ddciiconplayer.h` |
| 1.8 | `DDciIconPalette` 类存在，4 色构造函数，`fromQPalette`/`convertToString`/`convertFromString` 静态方法，getter/setter（foreground/background/highlight/highlightForeground） | 逐个核对 | `ddciiconpalette.h` |
| 1.9 | `DIconTheme` 类存在，静态方法 `findQIcon`（3 个重载）、`isBuiltinIcon`、`isXdgIcon`、`createIconEngine`、`findDciIconFile`（2 个重载）、`dciThemeSearchPaths`/`setDciThemeSearchPaths`、`cached` | 逐个核对 | `dicontheme.h` |
| 1.10 | `DIconTheme::Options` 枚举有 `DontFallbackToQIconFromTheme`/`IgnoreBuiltinIcons`/`IgnoreDciIcons`/`IgnoreIconCache` | grep `enum.*Options` | `dicontheme.h` |
| 1.11 | `DIconTheme::Cached` 内部类有 `findQIcon`/`findDciIconFile`/`setMaxCost`/`clear` 方法 | grep `class Cached` | `dicontheme.h` |
| 1.12 | **参数顺序差异验证**：顶层 `findQIcon(iconName, fallback, options)` vs `Cached::findQIcon(iconName, options, fallback)` — 确认文档所述参数顺序是否正确 | 核对函数签名 | `dicontheme.h` |
| 1.13 | builtin 图标资源路径 `:/icons/deepin/builtin/light/` 和 `:/icons/deepin/builtin/dark/` 存在 | 搜索 `.qrc` 文件或资源目录 | `dtkgui/src/util/icons/` 或 `dtkwidget/src/widgets/assets/` |
| 1.14 | builtin 图标名列表（如 `dialog-ok`、`window-close_round_30px`、`icon_ok_32px` 等）在资源中存在 | glob 搜索资源文件 | 同上 |
| 1.15 | CMake `find_package(DtkGui)` + `Dtk::Gui` target | 检查 cmake 配置文件 | `dtkgui/dtkgui.cmake` |

---

## 模块 2：theming（主题系统）— 来源 dtkgui/dtkwidget

**参考文档：** `references/theming/index.md`, `references/theming/palette.md`, `references/theming/style.md`, `references/theming/theme-switch.md`

**源码位置：** `~/dtk/dtkgui/include/kernel/` + `~/dtk/dtkwidget/include/widgets/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 2.1 | `DPalette` 类继承 `QPalette`，`ColorType` 枚举有全部 11 个值：`ItemBackground`/`TextTitle`/`TextTips`/`TextWarning`/`TextLively`/`LightLively`/`DarkLively`/`FrameBorder`/`PlaceholderText`/`FrameShadowBorder`/`ObviousBackground` | grep `enum.*ColorType` + 逐个值 | `dtkgui/include/kernel/dpalette.h` |
| 2.2 | `DPalette` 方法：`color(ColorType)`、`textTitle()`/`textTips()`/`textWarning()`/`itemBackground()` getter、`setColor`/`setBrush` setter | 逐个核对 | 同上 |
| 2.3 | `DGuiApplicationHelper` 类存在，`ColorType` 枚举有 `LightType`/`DarkType` | grep class + enum | `dtkgui/include/kernel/dguiapplicationhelper.h` |
| 2.4 | `DGuiApplicationHelper` 静态方法：`standardPalette(ColorType)`、`generatePaletteColor`、`generatePalette`、`adjustColor`、`blendColor`、`toColorType`、`fetchPalette` | 逐个核对签名 | 同上 |
| 2.5 | `DGuiApplicationHelper` 实例方法：`themeType()`、`applicationPalette()`（含重载）、`applicationTheme()`、`setApplicationPalette()`、`setPaletteType()` | 逐个核对 | 同上 |
| 2.6 | 信号：`themeTypeChanged(ColorType)`、`applicationPaletteChanged` | grep `Q_SIGNALS`/`signals` | 同上 |
| 2.7 | `DStyle` 类存在，继承 `QCommonStyle` | grep `class DStyle` | `dtkwidget/include/widgets/dstyle.h` |
| 2.8 | `DStyle::StandardPixmap` 枚举有 `SP_CloseButton`/`SP_IncreaseElement`/`SP_DecreaseElement`/`SP_MarkElement`/`SP_DeleteButton`/`SP_AddButton`/`SP_ArrowEnter`/`SP_ArrowLeave` | grep enum + 逐个值 | 同上 |
| 2.9 | `DStyle::PixelMetric` 枚举有 `PM_FrameRadius`/`PM_ShadowRadius`/`PM_FocusBorderWidth` | grep enum | 同上 |
| 2.10 | `DStyle::PE_ItemBackground` 原始元素存在 | grep `PE_ItemBackground` | 同上 |
| 2.11 | `DStyle` 静态方法：`standardIcon(style, SP)`、`pixelMetric(style, PM)` | 核对签名 | 同上 |
| 2.12 | `DStyleHelper` 类存在，方法 `getColor`/`generatedBrush`/`drawPrimitive` | grep class + 方法 | 同上 |
| 2.13 | `DStyle::SS_HoverState`/`SS_FocusFlag` 状态标志存在 | grep `SS_HoverState` | 同上 |
| 2.14 | `DPlatformTheme` 类存在（`fetchPalette` 参数类型） | grep `class DPlatformTheme` | `dtkgui/include/kernel/dplatformtheme.h` |

---

## 模块 3：widgets（QWidget 控件）— 来源 dtkwidget

**参考文档：** `references/widgets/index.md` + 8 个子文档（`button.md`/`container.md`/`dialog.md`/`input.md`/`message.md`/`navigation.md`/`progress.md`/`view.md`/`window.md`）

**源码位置：** `~/dtk/dtkwidget/include/widgets/` + `~/dtk/dtkwidget/include/DWidget/`（转发头文件）

### 3.1 按钮类（button.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 3.1.1 | 按钮类全部存在：`DSuggestButton`/`DWarningButton`/`DIconButton`/`DToolButton`/`DSwitchButton`/`DButtonBox`/`DFloatingButton` | glob 头文件名 | `include/DWidget/` |
| 3.1.2 | `DIconButton` 构造函数：`(DStyle::StandardPixmap, parent)`、`(DDciIcon, parent)`、`(parent)` 三种重载 | 核对构造函数 | `diconbutton.h` |
| 3.1.3 | `DIconButton` 方法：`setIcon(QIcon)`/`setIcon(DStyle::StandardPixmap)`/`setIcon(DDciIcon)`/`setFlat`/`setEnabledCircle`/`dciIcon` | 逐个核对 | 同上 |
| 3.1.4 | `DSwitchButton` 方法 `setChecked` + 信号 `checkedChanged(bool)` | grep signal | `dswitchbutton.h` |
| 3.1.5 | `DButtonBox` 方法 `setButtonList(QList, bool)` | 核对签名 | `dbuttonbox.h` |
| 3.1.6 | `DFloatingButton` 构造函数 `(DStyle::StandardPixmap, parent)` + 信号 `clicked` | 核对 | `dfloatingbutton.h` |
| 3.1.7 | `DImageButton` 弃用标注（deprecated -> use `DIconButton`） | grep `deprecated`/`Q_DECL_DEPRECATED` | `dimagebutton.h` |

### 3.2 对话框类（dialog.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 3.2.1 | 对话框类全部存在：`DDialog`/`DInputDialog`/`DFileDialog`/`DAboutDialog`/`DAbstractDialog` | glob 头文件 | `include/DWidget/` |
| 3.2.2 | `DDialog` 构造函数 `(parent)` 和 `(title, message, parent)` 两种 | 核对构造函数 | `ddialog.h` |
| 3.2.3 | `DDialog` 方法：`setTitle`/`setMessage`/`setIcon`/`addButton(text,bool,ButtonType)`/`insertButton`/`addContent`/`setOnButtonClickedClose`/`exec` | 逐个核对 | 同上 |
| 3.2.4 | `DDialog::ButtonType` 枚举 `ButtonNormal`/`ButtonWarning`/`ButtonRecommend` | grep enum | 同上 |
| 3.2.5 | `DDialog` 信号 `buttonClicked(int, QString)` 和 `closed` | grep signals | 同上 |
| 3.2.6 | `DDialog::setIconPixmap` 和 `setIcon(QIcon,QSize)` 弃用标注 | grep deprecated | 同上 |
| 3.2.7 | `DInputDialog` 静态方法 `getText`/`getInt` 签名 | 核对 | `dinputdialog.h` |
| 3.2.8 | `DFileDialog` 静态方法 `getOpenFileName`/`getOpenFileNames`/`getExistingDirectory`/`getSaveFileName` | 核对 | `dfiledialog.h` |
| 3.2.9 | `DAbstractDialog::DisplayPosition` 枚举 `Center`/`TopRight` + `setDisplayPosition` 方法 | grep enum + method | `dabstractdialog.h` |

### 3.3 输入类（input.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 3.3.1 | 输入类全部存在：`DLineEdit`/`DSearchEdit`/`DPasswordEdit`/`DTextEdit`/`DSpinBox`/`DDoubleSpinBox`/`DComboBox`/`DKeySequenceEdit` | glob 头文件 | `include/DWidget/` |
| 3.3.2 | `DLineEdit` 方法：`setPlaceholderText`/`setAlert`/`isAlert`/`showAlertMessage`/`hideAlertMessage`/`setLeftWidgets`/`setRightWidgets`/`setClearButtonEnabled`/`lineEdit`/`setSpeechToTextEnabled`/`setTextToSpeechEnabled`/`setTextToTranslateEnabled`/`text` | 逐个核对 | `dlineedit.h` |
| 3.3.3 | `DSearchEdit` 信号 `textChanged(const QString &)` | grep signal | `dsearchedit.h` |
| 3.3.4 | `DPasswordEdit` 信号 `textChanged(const QString &)` | grep signal | `dpasswordedit.h` |
| 3.3.5 | `DSpinBox` 方法 `setRange`/`setValue`/`setSingleStep` + 信号 `valueChanged(int)` | 核对 | `dspinbox.h` |
| 3.3.6 | `DComboBox` 方法 `addItems` + 信号 `currentIndexChanged(int)` | 核对 | `dcombobox.h` |
| 3.3.7 | `DKeySequenceEdit` 信号 `keySequenceChanged(const QKeySequence &)` | grep signal | `dkeysequenceedit.h` |
| 3.3.8 | `DShortcutEdit` 弃用标注（-> use `DKeySequenceEdit`） | grep deprecated | `dshortcutedit.h` |

### 3.4 消息类（message.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 3.4.1 | 消息类全部存在：`DMessageManager`/`DFloatingMessage`/`DFloatingWidget`/`DToolTip` | glob 头文件 | `include/DWidget/` |
| 3.4.2 | `DMessageManager` 静态方法 `instance()`/`sendMessage`（3 个重载：QIcon 版、DFloatingMessage 版、DDciIcon 版）/`setContentMargens` | 逐个核对 | `dmessagemanager.h` |
| 3.4.3 | `DFloatingMessage::MessageType` 枚举 `TransientType`/`ResidentType` + 构造函数 + `setMessage`/`setIcon`(2 重载)/`setWidget`/`setDuration`/`messageType` + 信号 `closeButtonClicked` | 逐个核对 | `dfloatingmessage.h` |
| 3.4.4 | `DToolTip` 静态方法 `setToolTipTextFormat`/`toolTipTextFormat` | 核对 | `dtooltip.h` |
| 3.4.5 | `DToast` 弃用标注（-> use `DMessageManager`） | grep deprecated | `dtoast.h` |

### 3.5 导航类（navigation.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 3.5.1 | 导航类全部存在：`DTabBar`/`DDrawer`/`DDrawerGroup`/`DStackWidget` | glob 头文件 | `include/DWidget/` |
| 3.5.2 | `DTabBar` 方法 `addTab` + 信号 `currentChanged(int)` | 核对 | `dtabbar.h` |
| 3.5.3 | `DDrawer` 方法 `setHeader`/`setContent`/`setExpand` + 信号 `expandChange(bool)` | 核对 | `ddrawer.h` |
| 3.5.4 | `DDrawerGroup` 方法 `addDrawer` + 信号 `drawerClicked(int)` | 核对 | `ddrawergroup.h` |
| 3.5.5 | `DBaseExpand`/`DExpandGroup` 弃用标注 | grep deprecated | 对应头文件 |

### 3.6 进度类（progress.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 3.6.1 | 进度类全部存在：`DProgressBar`/`DColoredProgressBar`/`DIndeterminateProgressBar`/`DCircleProgress`/`DWaterProgress`/`DSpinner`/`DLoadingIndicator` | glob 头文件 | `include/DWidget/` |
| 3.6.2 | `DProgressBar` 方法 `setRange`/`setValue`/`setOrientation` | 核对 | `dprogressbar.h` |
| 3.6.3 | `DIndeterminateProgressBar` 方法 `start`/`stop` | 核对 | `dindeterminateprogressbar.h` |
| 3.6.4 | `DSpinner` 方法 `start`/`stop` | 核对 | `dspinner.h` |
| 3.6.5 | `DCircleProgress` 方法 `setValue`（0-100） | 核对 | `dcircleprogress.h` |
| 3.6.6 | `DWaterProgress` 方法 `setValue`（0-100）/`start`/`stop` | 核对 | `dwaterprogress.h` |
| 3.6.7 | `DCircleProgress` 弃用标注 | grep deprecated | 同上 |

### 3.7 视图类（view.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 3.7.1 | 视图类全部存在：`DListView`/`DSimpleListView`/`DStyledItemDelegate`/`DSimpleListItem` | glob 头文件 | `include/DWidget/` |
| 3.7.2 | `DListView` 方法 `setModel`/`setItemDelegate` | 核对 | `dlistview.h` |
| 3.7.3 | `DStyledItemDelegate` 构造函数 `(parent)` | 核对 | `dstyleditemdelegate.h` |

### 3.8 窗口类（window.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 3.8.1 | 窗口类全部存在：`DMainWindow`/`DTitlebar`/`DApplication`/`DPlatformWindowHandle` | glob 头文件 | `include/DWidget/` |
| 3.8.2 | `DMainWindow` 方法：`titlebar()`/`setCentralWidget`/`setSidebarWidget`/`setSidebarWidth`/`setSidebarVisible`/`setSidebarExpanded`/`sidebarVisible`/`setWindowRadius`/`setBorderWidth`/`setBorderColor`/`setShadowRadius`/`setShadowOffset`/`setShadowColor`/`setTranslucentBackground`/`setEnableBlurWindow`/`sendMessage`(2 重载)/`isDXcbWindow` | 逐个核对 | `dmainwindow.h` |
| 3.8.3 | `DTitlebar` 方法：`setTitle`/`setIcon`/`setMenu`/`setMenuVisible`/`setSwitchThemeMenuVisible`/`addWidget`/`setCustomWidget`/`setDisableFlags`/`setFullScreenButtonVisible`/`setSplitScreenEnabled` | 逐个核对 | `dtitlebar.h` |
| 3.8.4 | `DApplication` 构造函数 `(argc, argv)` | 核对 | `dapplication.h` |

### 3.9 容器类（container.md）

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 3.9.1 | 容器类全部存在：`DFrame`/`DBackgroundGroup`/`DHeaderLine`/`DLine`/`DHorizontalLine`/`DVerticalLine` | glob 头文件 | `include/DWidget/` |
| 3.9.2 | `DFrame` 方法 `setFrameRounded`/`setBackgroundRole` | 核对 | `dframe.h` |
| 3.9.3 | `DBackgroundGroup` 方法 `setBackgroundRole` | 核对 | `dbackgroundgroup.h` |
| 3.9.4 | `DHeaderLine` 方法 `setTitle` | 核对 | `dheaderline.h` |
| 3.9.5 | `DLine` 方法 `setOrientation` | 核对 | `dline.h` |

### 3.10 CMake 验证

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 3.10.1 | CMake `find_package(DtkWidget)` + `Dtk::Widget` target | 检查 cmake | `dtkwidget/dtkwidget.cmake` |

---

## 模块 4：declarative（QML 控件）— 来源 dtkdeclarative

**参考文档：** `references/declarative/index.md`, `references/declarative/controls.md`, `references/declarative/color-selector.md`, `references/declarative/dci-icon.md`, `references/declarative/effects.md`

**源码位置：** `~/dtk/dtkdeclarative/qmlplugin/`（Qt5）+ `~/dtk/dtkdeclarative/qt6/`（Qt6）+ `~/dtk/dtkdeclarative/src/qml/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 4.1 | QML 模块 URI `org.deepin.dtk` 正确 | 检查 `qmldir` 文件 | `qmlplugin/qmldir` |
| 4.2 | QML 控件类型全部注册：`ApplicationWindow`/`Button`/`RoundButton`/`DelayButton`/`TextField`/`TextArea`/`SpinBox`/`ComboBox`/`CheckBox`/`RadioButton`/`Switch`/`TabBar`/`TabButton`/`StackView`/`Drawer`/`ProgressBar`/`BusyIndicator`/`Dialog`/`ToolTip`/`Popup`/`ListView`/`ScrollView` | 在 qmldir 或 QML 文件目录中逐个确认 | `qmldir` + `src/qml/` |
| 4.3 | `DciIconImage` QML 类型注册（文档用此名，源码注册名可能是 `DciIcon`） | grep `DciIconImage` 或 `DciIcon` in 注册代码 | `qmlplugin/qmlplugin_plugin.cpp` |
| 4.4 | `DciIconImage` 属性 `source`/`width`/`height` 存在 | 检查 C++ 实现类 `DQuickDciIconImage` 的 Q_PROPERTY | `src/private/dquickdciiconimage_p.h` |
| 4.5 | 效果类型全部注册：`Blur`/`InWindowBlur`/`BehindWindowBlur`/`Glow`/`ColorOverlay`/`OpacityMask`/`WaterProgress` | 在 qmldir 或注册代码中确认 | `qmldir` + `qmlplugin_plugin.cpp` |
| 4.6 | `InWindowBlur` 属性 `source`/`radius` 存在 | 检查 `DQuickInWindowBlur` Q_PROPERTY | `src/private/` |
| 4.7 | `Button` 的 `icon.source`/`icon.width`/`icon.height` 属性可用 | 检查 QML Button 实现 | `src/qml/Button.qml` 或 `chameleon/` |
| 4.8 | `StackLayout` 类型存在（controls.md 中使用，注意 index.md 列的是 `StackView`） | grep `StackLayout` in qmldir | `qmldir` |
| 4.9 | CMake `find_package(DtkDeclarative)` + `Dtk::Declarative` | 检查 cmake | `dtkdeclarative/cmake/` |
| 4.10 | **文档一致性**：index.md 列出 21 个 QML 类型，controls.md 额外提到 `StackLayout`，确认是否遗漏或不一致 | 交叉比对 | - |
| 4.11 | `ColorSelector` 类型为附加属性（`QML_ATTACHED` + `QML_UNCREATABLE`） | grep `ColorSelector` in 注册代码 | `src/private/dquickcontrolpalette_p.h` |
| 4.12 | `ColorSelector` 属性 `control`/`controlTheme`/`controlState`/`family`/`hovered`/`pressed`/`disabled`/`inactived` 存在 | 核对 Q_PROPERTY | `dquickcontrolpalette_p.h` |
| 4.13 | `ColorSelector::controlState` 枚举值 `NormalState`/`HoveredState`/`PressedState`/`DisabledState`/`InactiveState` 存在 | grep `ControlState` 枚举 | `dqmlglobalobject_p.h` |
| 4.14 | `ColorSelector` 信号 `colorPropertyChanged(QByteArray name)` 存在 | 核对 SIGNAL | `dquickcontrolpalette_p.h` |
| 4.15 | `Palette` 类型可创建（`QML_NAMED_ELEMENT(Palette)`） | grep `Palette` in 注册代码 | `dquickcontrolpalette_p.h` |
| 4.16 | `Palette` 属性 `enabled`/`normal`/`normalDark`/`hovered`/`hoveredDark`/`pressed`/`pressedDark`/`disabled`/`disabledDark` 存在 | 核对 Q_PROPERTY | `dquickcontrolpalette_p.h` |
| 4.17 | `Palette::ColorFamily` 枚举有 `CommonColor`/`CrystalColor` | grep `enum ColorFamily` | `dquickcontrolpalette_p.h` |
| 4.18 | `Palette::ColorGroup` 枚举有 `Light`/`Dark`/`Normal`/`Hovered`/`Pressed`/`Disabled` | grep `enum ColorGroup` | `dquickcontrolpalette_p.h` |
| 4.19 | `DQuickControlColor` 类型有 `common`/`crystal` 属性（支持分组语法 `normal { common: ...; crystal: ... }`） | 核对 Q_PROPERTY | `dquickcontrolpalette_p.h` |

---

## 模块 5：config（配置系统）— 来源 dtkcore + dde-app-services

**参考文档：** `references/config/index.md`, `references/config/concepts.md`, `references/config/dconfig-cpp.md`, `references/config/dconfig-dbus.md`, `references/config/dconfig-debug.md`

**源码位置：** `~/dtk/dtkcore/include/global/` + `~/dtk/dde-app-services/dconfig-center/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 5.1 | `DConfig` 类存在 | grep `class DConfig` | `dtkcore/include/global/dconfig.h` |
| 5.2 | `DConfig` 静态方法 `create(appId, name, subpath, parent)` 和 `createGeneric(name, subpath, parent)` | 核对签名 | 同上 |
| 5.3 | `DConfig` 构造函数 `DConfig(name, subpath, parent)`（无 appId） | 核对 | 同上 |
| 5.4 | `DConfig` 实例方法：`value(key, fallback)`/`setValue(key, value)`/`keyList()`/`isValid()`/`isDefaultValue(key)`/`isReadOnly(key)`/`reset(key)` | 逐个核对 | 同上 |
| 5.5 | `DConfig` 信号 `valueChanged(const QString &)` | grep signal | 同上 |
| 5.6 | `DConfig::setAppId()` 和 `DConfig::globalThread()` 静态方法 | 核对 | 同上 |
| 5.7 | dconfig2cpp 工具存在：`dtkcore/tools/dconfig2cpp/main.cpp` | glob 检查 | `tools/dconfig2cpp/` |
| 5.8 | dconfig2cpp 生成的类有 `create(appId, subpath, parent)` 工厂方法 | grep `static.*create` | `tools/dconfig2cpp/main.cpp` |
| 5.9 | 生成类信号 `configInitializeSucceed(DConfig*)` / `configInitializeFailed()` | grep signals | 同上 |
| 5.10 | 生成类状态方法：`isInitializeSucceeded()`（新接口）/ `isInitializeSucceed()`（deprecated） | grep `isInitializeSucceed` | 同上 |
| 5.11 | CMake `dtk_add_config_meta_files()` 宏定义 | grep macro/function | `dtkcore/cmake/DtkDConfig/DtkDConfigConfig.cmake` |
| 5.12 | CMake `dtk_add_config_to_cpp()` 宏定义 | grep macro/function | `dtkcore/cmake/DtkTools/DtkDConfigMacros.cmake` |
| 5.13 | meta 文件 `magic` 值 `"dsg.config.meta"` 与 dconfig2cpp 校验一致 | grep `dsg.config.meta` | `tools/dconfig2cpp/main.cpp` |
| 5.14 | dde-dconfig CLI 支持 `-s <subpath>` 选项 | 运行 `dde-dconfig --help` | `dde-app-services/dconfig-center/dde-dconfig/` |
| 5.15 | dde-dconfig-daemon systemd service 用户为 `deepin-daemon` | grep `User=` | `dde-dconfig-daemon/services/dde-dconfig-daemon.service` |
| 5.16 | systemd service `StateDirectory=dde-dconfig-daemon` + `LogsDirectory=deepin` | grep | 同上 |
| 5.17 | daemon 中 `setCachePathPrefix()` 调用：global 为 `configPrefixPath() + "/global"`，用户为 `configPrefixPath() + "/{uid}"` | grep `setCachePathPrefix` | `dde-dconfig-daemon/dconfigresource.cpp` |
| 5.18 | daemon `configPrefixPath()` 优先 `STATE_DIRECTORY` 环境变量 | grep `STATE_DIRECTORY` | `dde-dconfig-daemon/dconfig_global.h` |
| 5.19 | DSMG 概念：`DSettingsDialog` 属 dtkwidget 而非 config 模块，已在 `widgets/dialog.md` 中描述 | 确认文件位置 | `widgets/dialog.md` |

---

## 模块 6：core（核心工具）— 来源 dtkcore

**参考文档：** `references/core/index.md`, `references/core/dbus.md`, `references/core/filesystem.md`, `references/core/notify.md`

**源码位置：** `~/dtk/dtkcore/include/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 6.1 | `DStandardPaths` 类存在，`writableLocation(StandardLocation)` 方法 | grep class + method | `include/filesystem/dstandardpaths.h` |
| 6.2 | `DStandardPaths` 枚举值 `AppConfigLocation`/`AppDataLocation`/`CacheLocation`/`TempLocation` 存在 | grep enum | 同上 |
| 6.3 | `DFileWatcher` 类存在，构造函数 + `addPath` 方法 + `fileChanged` 信号 | grep class + methods | `include/filesystem/dfilewatcher.h` |
| 6.4 | `DTrashManager` 类存在，静态方法 `moveToTrash`/`emptyTrash` | grep class + methods | `include/filesystem/dtrashmanager.h` |
| 6.5 | `DDBusInterface` 类存在，构造函数 `(service, path, connection)` + `call` 方法 + `signal` 信号 | grep class + methods | `include/util/ddbusinterface.h` |
| 6.6 | `DDBusSender` 类存在，builder 方法 `service`/`path`/`interface`/`signal`/`arg`/`publish` 全部存在且返回 `DDBusSender&` | 逐个核对 | `include/util/ddbussender.h` |
| 6.7 | `DNotifySender` 类存在 | grep `class DNotifySender` | `include/util/dnotifysender.h` |
| 6.8 | **文档不一致验证**：index.md 描述 `DNotifySender::Message` 结构体 + `instance()->sendMessage()` 单例模式；notify.md 描述构造函数 `DNotifySender("summary")` + builder 链 + `.call()`。确认实际 API 是哪种 | 仔细阅读头文件完整 API | 同上 |
| 6.9 | `DNotifySender` builder 方法（如 notify.md 所述）：`appName`/`appIcon`/`appBody`/`replaceId`/`timeOut`/`actions`/`hints`/`call` | 逐个核对 | 同上 |
| 6.10 | `DObject`/`DSingleton`/`DError` 基类存在 | grep class | `include/base/` |
| 6.11 | `DDciFile` 类存在（dci 文件解析，来自 dtkcore） | grep `class DDciFile` | `include/dci/ddcifile.h` |

---

## 模块 7：log（日志系统）— 来源 dtklog

**参考文档：** `references/log/index.md`

**源码位置：** `~/dtk/dtklog/include/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 7.1 | `Logger` 类存在，`globalInstance()` 静态方法 | grep class + method | `include/Logger.h` |
| 7.2 | `Logger::LogLevel` 枚举有 `Trace`/`Debug`/`Info`/`Warning`/`Error`/`Fatal` | grep enum + 逐个值 | 同上 |
| 7.3 | `Logger` 方法：`registerAppender`/`registerCategoryAppender`/`unregisterAppender`/`levelToString`/`levelFromString` | 逐个核对 | 同上 |
| 7.4 | `AbstractAppender` 类存在（基类） | grep class | `include/AbstractAppender.h` |
| 7.5 | `ConsoleAppender` 类存在，无参构造函数 | grep class + ctor | `include/ConsoleAppender.h` |
| 7.6 | `FileAppender` 类存在，构造函数接受文件路径 `QString` | grep class + ctor | `include/FileAppender.h` |
| 7.7 | `RollingFileAppender` 类存在，构造函数接受文件路径，继承 `FileAppender` | grep class + ctor + inherits | `include/RollingFileAppender.h` |
| 7.8 | 日志宏 `dDebug`/`dInfo`/`dWarning`/`dError`/`dFatal` 存在 | grep 宏定义 | `include/dloggerdefs.h` |
| 7.9 | CMake `find_package(DtkLog)` + `Dtk::Log` target | 检查 cmake | `dtklog/CMakeLists.txt` 或 `cmake/` |
| 7.10 | 头文件名 `#include <Logger>`/`<FileAppender>`/`<ConsoleAppender>`/`<RollingFileAppender>` 可用（无 `.h` 后缀的转发头文件） | glob 检查 | `include/` |

---

## 模块 8：平台集成（qt5integration + qt5platform-plugins）

**参考文档：** `SKILL.md` 中的"仓库依赖关系"和"核心库 vs 平台集成库"说明

**源码位置：** `~/dtk/qt5integration/` + `~/dtk/qt5platform-plugins/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 8.1 | SKILL.md 声称 dtkwidget 运行时依赖 qt5integration（Chameleon 风格） | 确认 `ChameleonStyle` 继承 `DStyle` | `qt5integration/styleplugins/chameleon/chameleonstyle.h` |
| 8.2 | SKILL.md 声称 qt5integration 运行时依赖 qt5platform-plugins | 确认两者有关联（检查 cmake 或代码引用） | 两项目源码 |
| 8.3 | SKILL.md 声称 dtkwidget 编译不依赖 qt5integration/qt5platform-plugins | 确认 dtkwidget 的 CMakeLists 不引用这两个项目 | `dtkwidget/CMakeLists.txt` |
| 8.4 | SKILL.md 声称 `DDciFile` 来自 dtkcore，`DDciIcon` 来自 dtkgui | 确认类所在项目 | 已在 1.1 和 6.11 验证 |
| 8.5 | SKILL.md 依赖图：dtkcommon <- dtklog, dtkcommon <- dtkcore, dtkcore <- dtkgui, dtkgui <- dtkwidget, dtkgui <- dtkdeclarative | 逐个检查 CMakeLists 中的 `find_package` | 各项目 `CMakeLists.txt` |

---

## 模块 9：跨文档一致性验证

**说明：** 在逐模块验证过程中发现的文档内部不一致问题需要集中确认和修正。

| # | 验证项 | 不一致描述 | 涉及文档 |
|---|--------|-----------|----------|
| 9.1 | `DNotifySender` API 形态 | index.md（`Message` 结构体 + `instance()->sendMessage()` 单例模式）vs notify.md（构造函数 `DNotifySender("summary")` + builder 链 + `.call()`） | `core/index.md` vs `core/notify.md` |
| 9.2 | QML `StackView` vs `StackLayout` | index.md 列 `StackView`，controls.md 用 `StackLayout` | `declarative/index.md` vs `declarative/controls.md` |
| 9.3 | `DciIconImage` vs `DciIcon` QML 类型名 | 文档用 `DciIconImage`，源码注册名可能是 `DciIcon` | `declarative/dci-icon.md` vs 源码 |

---

## 模块 10：architecture（核心架构）— 来源全部项目

**参考文档：** `references/architecture.md`

**源码位置：** `~/dtk/dtkgui/`、`~/dtk/dtkwidget/`、`~/dtk/dtkdeclarative/`、`~/dtk/qt5integration/`、`~/dtk/qt5platform-plugins/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 10.1 | 调色板系统：`DPalette` 类存在，`DGuiApplicationHelper::standardPalette()` 方法 | grep class + method | `dtkgui/include/kernel/dguiapplicationhelper.h` |
| 10.2 | 调色板系统：`DStyleHelper::getColor()` 方法存在 | grep method | `dtkwidget/include/widgets/dstyle.h` |
| 10.3 | 字体系统：`DFontManager` 类存在，`t1()`-`t11()` 方法，`SizeType` 枚举 T1-T11 | grep class + enum | `dtkgui/include/util/dfontmanager.h` |
| 10.4 | 字体系统：`DFontSizeManager` 类存在，`bind(QWidget*, SizeType)` 方法 | grep class + method | `dtkwidget/include/widgets/dstyleoption.h` |
| 10.5 | 字体系统：`D.DTK.fontManager` QML 属性存在 | grep `fontManager` | `dtkdeclarative/src/private/dqmlglobalobject_p.h` |
| 10.6 | 图标系统：`DDciIcon`/`DIconTheme`/`DDciIconPlayer` 类存在 | grep class | `dtkgui/include/util/ddciicon.h`、`dicontheme.h` |
| 10.7 | 平台抽象：`DPlatformHandle` 类存在，属性 `windowRadius`/`shadowRadius`/`enableBlurWindow` 等 | grep class + Q_PROPERTY | `dtkgui/include/kernel/dplatformhandle.h` |
| 10.8 | 平台抽象：`DPlatformTheme` 类存在，属性 `fontName`/`activeColor`/`iconThemeName` 等 | grep class + Q_PROPERTY | `dtkgui/include/kernel/dplatformtheme.h` |
| 10.9 | 平台抽象：`DPlatformWindowInterface` 抽象基类存在 | grep class | `dtkgui/src/private/dplatformwindowinterface_p.h` |
| 10.10 | 平台分发：`DXCBPlatformWindowInterface`/`DTreeLandPlatformWindowInterface` 存在 | grep class | `dtkgui/src/plugins/platform/xcb/`、`treeland/` |
| 10.11 | QPA 层：`DPlatformIntegration`/`DWaylandIntegration` 存在 | grep class | `qt5platform-plugins/xcb/`、`wayland/` |
| 10.12 | 平台检测：`DGuiApplicationHelper::IsXWindowPlatform`/`IsWaylandPlatform` 属性存在 | grep enum Attribute | `dtkgui/include/kernel/dguiapplicationhelper.h` |

## 模块 11：platform-abstraction（平台抽象层）— 来源 dtkgui + qt5platform-plugins

**参考文档：** `references/platform-abstraction.md`

**源码位置：** `~/dtk/dtkgui/` + `~/dtk/qt5platform-plugins/`

| # | 验证项 | 验证方法 | 对应源码文件 |
|---|--------|----------|-------------|
| 11.1 | `DPlatformHandle` 属性全部存在：`windowRadius`/`borderWidth`/`borderColor`/`shadowRadius`/`shadowOffset`/`shadowColor`/`clipPath`/`frameMask`/`frameMargins`/`translucentBackground`/`enableSystemResize`/`enableSystemMove`/`enableBlurWindow`/`autoInputMaskByClipPath`/`realWindowId` | 核对 Q_PROPERTY | `dplatformhandle.h` |
| 11.2 | `DPlatformHandle::EffectScene` 枚举值 `EffectNoRadius`/`EffectNoShadow`/`EffectNoBorder`/`EffectNoStart`/`EffectNoClose`/`EffectNoMaximize`/`EffectNoMinimize` | grep enum | 同上 |
| 11.3 | `DPlatformHandle::EffectType` 枚举值 `EffectNormal`/`EffectCursor`/`EffectTop`/`EffectBottom`/`EffectOut` | grep enum | 同上 |
| 11.4 | `DPlatformHandle::WMBlurArea` 结构体存在，`dMakeWMBlurArea()` 辅助函数 | grep struct + inline | 同上 |
| 11.5 | `DPlatformHandle::setWindowBlurAreaByWM()` 静态方法存在（2 个重载） | grep method | 同上 |
| 11.6 | `DPlatformHandle::setEnabledNoTitlebarForWindow()`/`isEnabledNoTitlebar()` 静态方法 | grep method | 同上 |
| 11.7 | `DPlatformTheme` 属性全部存在：字体（fontName/monoFontName/fontPointSize/gtkFontName）、主题（themeName/iconThemeName/soundThemeName/activeColor/darkActiveColor）、输入（cursorBlink* / doubleClick* / dndDragThreshold）、sizeMode/scrollBarPolicy | 核对 Q_PROPERTY | `dplatformtheme.h` |
| 11.8 | 平台分发：`createWindowInterface()` 函数按 `IsXWindowPlatform`/`IsWaylandPlatform` 分发 | 核对代码逻辑 | `dplatformhandle.cpp:307-328` |
| 11.9 | `DPlatformWindowInterface` 抽象基类虚函数完整 | grep virtual | `dplatformwindowinterface_p.h` |
| 11.10 | Treeland 实现通过 `treeland_personalization_manager_v1` Wayland 协议通信 | grep protocol | `dtkgui/src/plugins/platform/treeland/personalizationwaylandclientextension.h` |
| 11.11 | `qt5platform-plugins` 包含 `xcb/` 和 `wayland/` 两个 QPA 插件目录 | ls 目录结构 | `qt5platform-plugins/` |

---

## 执行策略

### 并行分组

建议将 11 个模块分为以下并行执行组（每组分配一个 explore agent）：

| 执行组 | 包含模块 | 预估项数 |
|--------|----------|---------|
| Group A | 模块 1（icons） | 15 |
| Group B | 模块 2（theming） | 14 |
| Group C | 模块 3（widgets，3.1-3.5） | ~25 |
| Group D | 模块 3（widgets，3.6-3.10） | ~20 |
| Group E | 模块 4（declarative） | 19 |
| Group F | 模块 5（config） | 15 |
| Group G | 模块 6（core） | 11 |
| Group H | 模块 7（log） | 10 |
| Group I | 模块 8（平台集成）+ 模块 9（跨文档一致性） | 10 |
| Group J | 模块 10（architecture）+ 模块 11（platform-abstraction） | 23 |

### 执行方式

每组的 explore agent 将收到：

1. 该组所有模块的详细验证项列表（含表号）
2. 对应文档路径（用于读取文档声称的 API 列表）
3. 对应源码路径（用于 grep 验证）
4. 指令：对每项输出 PASS / FAIL / NOT FOUND，完成后返回汇总

### 汇总

所有组完成后，汇总生成一份验证报告，列出所有 FAIL（不一致）和 NOT FOUND（缺失）项，作为 skill 文档修正的依据。
