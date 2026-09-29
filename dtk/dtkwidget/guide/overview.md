# dtkwidget 二次开发文档 · 概览

## 项目定位

dtkwidget 是基于 Qt Widgets 模块的 C++ 控件库，提供 DTK 风格的对话框、窗口、按钮、输入框、列表、视图、样式、动画效果、打印预览、设置界面和辅助工具这些控件级别的功能。图形界面层面的非控件能力（调色板、DCI 图标、窗口装饰）由下层 dtkgui 提供。

## 术语与缩写

- **DTK**：Deepin Tool Kit。
- **DTK5 / DTK6**：分别与 Qt5 / Qt6 配套的主版本。
- **DWidget**：公开头文件安装目录名，也是主要 C++ 命名空间的一部分。
- **转发头**：以公开类型名命名的无后缀头文件，转而引入实际声明所在的头文件。
- **命名空间别名**：dtkwidget 通过 `dwidgetstype.h` 将 Qt Widgets 控件类型以 `D` 前缀重新暴露在 DTK 命名空间中，如 `DPushButton`、`DLabel`。

## 导出类型

[导出类型介绍](dtk6widget-dev.md)是本项目唯一的类型参考文档。它以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。项目还提供大量 Qt 控件类型在 DTK 命名空间下的别名，便于在 DTK 工程中统一命名风格。

## 全局约定

公开头文件安装在按主版本区分的 DWidget 目录。主要公开符号位于 `Dtk::Widget` 命名空间，可使用 `DWIDGET_USE_NAMESPACE` 引入。版本判断和跨主版本构建方式见[集成与构建配置](integration.md)。

公开类型多以 `D` 开头。控件类型通常继承对应 Qt 控件并集成 DTK 主题与样式。部分类型在 DTK6 中已移除，详见对应类型章节。具体名称以公开声明为准。

## 按功能查阅

- 将 dtkwidget 引入 CMake、pkg-config 或 qmake 工程：参见[集成与构建配置](integration.md)。
- 使用对话框：参见 [DDialog](dtk6widget-dev.md#ddialog)、[DAbstractDialog](dtk6widget-dev.md#dabstractdialog)、[DAboutDialog](dtk6widget-dev.md#daboutdialog)、[DFileDialog](dtk6widget-dev.md#dfiledialog)、[DInputDialog](dtk6widget-dev.md#dinputdialog)、DMessageBox、DColorDialog、DFontDialog、DErrorMessage、[DLicenseDialog](dtk6widget-dev.md#dlicensedialog)、[DFeatureDisplayDialog](dtk6widget-dev.md#dfeaturedisplaydialog)、[DSettingsDialog](dtk6widget-dev.md#dsettingsdialog)、[DPrintPreviewDialog](dtk6widget-dev.md#dprintpreviewdialog)。
- 使用窗口与标题栏：参见 [DMainWindow](dtk6widget-dev.md#dmainwindow)、[DTitlebar](dtk6widget-dev.md#dtitlebar)、[DPlatformWindowHandle](dtk6widget-dev.md#dplatformwindowhandle)、[DWindowCloseButton](dtk6widget-dev.md#dwindowclosebutton)、[DWindowMaxButton](dtk6widget-dev.md#dwindowmaxbutton)、[DWindowMinButton](dtk6widget-dev.md#dwindowminbutton)、[DWindowOptionButton](dtk6widget-dev.md#dwindowoptionbutton)、[DWindowQuitFullButton](dtk6widget-dev.md#dwindowquitfullbutton)、[DTabletWindowOptionButton](dtk6widget-dev.md#dtabletwindowoptionbutton)。
- 使用按钮：参见 DPushButton、[DIconButton](dtk6widget-dev.md#diconbutton)、[DSuggestButton](dtk6widget-dev.md#dsuggestbutton)、[DWarningButton](dtk6widget-dev.md#dwarningbutton)、DRadioButton、DCheckBox、[DToolButton](dtk6widget-dev.md#dtoolbutton)、[DCommandLinkButton](dtk6widget-dev.md#dcommandlinkbutton)、[DSwitchButton](dtk6widget-dev.md#dswitchbutton)、[DButtonBox](dtk6widget-dev.md#dbuttonbox)、[DFloatingButton](dtk6widget-dev.md#dfloatingbutton)、[DArrowButton](dtk6widget-dev.md#darrowbutton)。
- 使用输入控件：参见 [DLineEdit](dtk6widget-dev.md#dlineedit)、[DPasswordEdit](dtk6widget-dev.md#dpasswordedit)、[DSearchEdit](dtk6widget-dev.md#dsearchedit)、[DIpv4LineEdit](dtk6widget-dev.md#dipv4lineedit)、[DFileChooserEdit](dtk6widget-dev.md#dfilechooseredit)、[DKeySequenceEdit](dtk6widget-dev.md#dkeysequenceedit)、[DCrumbEdit](dtk6widget-dev.md#dcrumbedit)、[DTextEdit](dtk6widget-dev.md#dtextedit)、[DSpinBox](dtk6widget-dev.md#dspinbox)、[DDoubleSpinBox](dtk6widget-dev.md#ddoublespinbox)、[DSlider](dtk6widget-dev.md#dslider)、[DComboBox](dtk6widget-dev.md#dcombobox)、[DSearchComboBox](dtk6widget-dev.md#dsearchcombobox)、[DFontComboBox](dtk6widget-dev.md#dfontcombobox)。
- 使用列表与视图：参见 [DListView](dtk6widget-dev.md#dlistview)、[DSimpleListView](dtk6widget-dev.md#dsimplelistview)、[DSimpleListItem](dtk6widget-dev.md#dsimplelistitem)、[DStandardItem](dtk6widget-dev.md#dstandarditem)、[DStyledItemDelegate](dtk6widget-dev.md#dstyleditemdelegate)、DTreeView、DTableView、DHeaderView。
- 使用样式与主题：参见 [DStyle](dtk6widget-dev.md#dstyle)、[DStyleHelper](dtk6widget-dev.md#dstylehelper)、[DStyleOption](dtk6widget-dev.md#dstyleoption)、[DStyledIconEngine](dtk6widget-dev.md#dstylediconengine)、[DStylePainter](dtk6widget-dev.md#dstylepainter)、[DApplication](dtk6widget-dev.md#dapplication)、[DPaletteHelper](dtk6widget-dev.md#dpalettehelper)、[DSizeMode](dtk6widget-dev.md#dsizemode)、[DFontSizeManager](dtk6widget-dev.md#dfontsizemanager)、[DWaterMarkHelper](dtk6widget-dev.md#dwatermarkhelper)。
- 使用效果与动画：参见 [DBlurEffectWidget](dtk6widget-dev.md#dblureffectwidget)、[DClipEffectWidget](dtk6widget-dev.md#dclipeffectwidget)、[DGraphicsClipEffect](dtk6widget-dev.md#dgraphicsclipeffect)、[DGraphicsDropShadowEffect](dtk6widget-dev.md#dgraphicsdropshadoweffect)、[DBounceAnimation](dtk6widget-dev.md#dbounceanimation)、[DSpinner](dtk6widget-dev.md#dspinner)、[DWaterProgress](dtk6widget-dev.md#dwaterprogress)、[DIndeterminateProgressbar](dtk6widget-dev.md#dindeterminateprogressbar)、[DPageIndicator](dtk6widget-dev.md#dpageindicator)。
- 使用容器与布局：参见 [DFrame](dtk6widget-dev.md#dframe)、[DHorizontalLine](dtk6widget-dev.md#dhorizontalline)、[DVerticalLine](dtk6widget-dev.md#dverticalline)、[DBackgroundGroup](dtk6widget-dev.md#dbackgroundgroup)、[DShadowLine](dtk6widget-dev.md#dshadowline)、[DDrawer](dtk6widget-dev.md#ddrawer)、[DDrawerGroup](dtk6widget-dev.md#ddrawergroup)、DToolBox、DStackedWidget、DSplitter、DScrollArea、DGroupBox、DTabWidget、[DTabBar](dtk6widget-dev.md#dtabbar)。
- 使用浮层与提示：参见 [DFloatingWidget](dtk6widget-dev.md#dfloatingwidget)、[DFloatingMessage](dtk6widget-dev.md#dfloatingmessage)、[DMessageManager](dtk6widget-dev.md#dmessagemanager)、[DTipLabel](dtk6widget-dev.md#dtiplabel)、[DToolTip](dtk6widget-dev.md#dtooltip)、[DAlertControl](dtk6widget-dev.md#dalertcontrol)。
- 使用设置界面：参见 [DSettingsDialog](dtk6widget-dev.md#dsettingsdialog)、[DSettingsWidgetFactory](dtk6widget-dev.md#dsettingswidgetfactory)。
- 使用打印预览：参见 [DPrintPreviewDialog](dtk6widget-dev.md#dprintpreviewdialog)、[DPrintPreviewSettingInfo](dtk6widget-dev.md#dprintpreviewsettinginfo)、[DPrintPreviewSettingInterface](dtk6widget-dev.md#dprintpreviewsettinginterface)。
- 在 DTK5 与 DTK6 之间迁移构建配置：参见[集成与构建配置](integration.md)；迁移公开类型：参见对应的[导出类型介绍](dtk6widget-dev.md)。
