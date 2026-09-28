# dtkwidget 二次开发文档 · 概览

## 项目定位

dtkwidget 是基于 Qt Widgets 模块的 C++ 控件库，提供 DTK 风格的对话框、窗口、按钮、输入框、列表、视图、样式、动画效果、打印预览、设置界面和辅助工具等控件级别的功能。图形界面层面的非控件能力（调色板、DCI 图标、窗口装饰等）由下层 dtkgui 提供。

## 术语与缩写

- **DTK**：Deepin Tool Kit。
- **DTK5 / DTK6**：分别与 Qt5 / Qt6 配套的主版本。
- **DWidget**：公开头文件安装目录名，也是主要 C++ 命名空间的一部分。
- **转发头**：以公开类型名命名的无后缀头文件，转而引入实际声明所在的头文件。
- **命名空间别名**：dtkwidget 通过 `dwidgetstype.h` 将 Qt Widgets 控件类型以 `D` 前缀重新暴露在 DTK 命名空间中，如 `DPushButton`、`DLabel` 等。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。它以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。项目还提供大量 Qt 控件类型在 DTK 命名空间下的别名，便于在 DTK 工程中统一命名风格。

## 全局约定

公开头文件安装在按主版本区分的 DWidget 目录。主要公开符号位于 `Dtk::Widget` 命名空间，可使用 `DWIDGET_USE_NAMESPACE` 引入。版本判断和跨主版本构建方式见[集成与构建配置](integration.md)。

公开类型多以 `D` 开头。控件类型通常继承对应 Qt 控件并集成 DTK 主题与样式。部分类型在 DTK6 中已移除，详见对应类型章节。具体名称以公开声明为准。

## 按功能查阅

- 将 dtkwidget 引入 CMake、pkg-config 或 qmake 工程：参见[集成与构建配置](integration.md)。
- 使用对话框：参见 [DDialog](modules.md#ddialog)、[DAbstractDialog](modules.md#dabstractdialog)、[DAboutDialog](modules.md#daboutdialog)、[DFileDialog](modules.md#dfiledialog)、[DInputDialog](modules.md#dinputdialog)、[DMessageBox](modules.md#dmessagebox)、[DColorDialog](modules.md#dcolordialog)、[DFontDialog](modules.md#dfontdialog)、[DErrorMessage](modules.md#derrormessage)、[DLicenseDialog](modules.md#dlicensedialog)、[DFeatureDisplayDialog](modules.md#dfeaturedisplaydialog)、[DSettingsDialog](modules.md#dsettingsdialog)、[DPrintPreviewDialog](modules.md#dprintpreviewdialog)。
- 使用窗口与标题栏：参见 [DMainWindow](modules.md#dmainwindow)、[DTitlebar](modules.md#dtitlebar)、[DPlatformWindowHandle](modules.md#dplatformwindowhandle)、[DWindowCloseButton](modules.md#dwindowclosebutton)、[DWindowMaxButton](modules.md#dwindowmaxbutton)、[DWindowMinButton](modules.md#dwindowminbutton)、[DWindowOptionButton](modules.md#dwindowoptionbutton)、[DWindowQuitFullButton](modules.md#dwindowquitfullbutton)、[DTabletWindowOptionButton](modules.md#dtabletwindowoptionbutton)。
- 使用按钮：参见 [DPushButton](modules.md#dpushbutton)、[DIconButton](modules.md#diconbutton)、[DSuggestButton](modules.md#dsuggestbutton)、[DWarningButton](modules.md#dwarningbutton)、[DRadioButton](modules.md#dradiobutton)、[DCheckBox](modules.md#dcheckbox)、[DToolButton](modules.md#dtoolbutton)、[DCommandLinkButton](modules.md#dcommandlinkbutton)、[DSwitchButton](modules.md#dswitchbutton)、[DButtonBox](modules.md#dbuttonbox)、[DFloatingButton](modules.md#dfloatingbutton)、[DArrowButton](modules.md#darrowbutton)。
- 使用输入控件：参见 [DLineEdit](modules.md#dlineedit)、[DPasswordEdit](modules.md#dpasswordedit)、[DSearchEdit](modules.md#dsearchedit)、[DIpv4LineEdit](modules.md#dipv4lineedit)、[DFileChooserEdit](modules.md#dfilechooseredit)、[DKeySequenceEdit](modules.md#dkeysequenceedit)、[DCrumbEdit](modules.md#dcrumbedit)、[DTextEdit](modules.md#dtextedit)、[DSpinBox](modules.md#dspinbox)、[DDoubleSpinBox](modules.md#ddoublespinbox)、[DSlider](modules.md#dslider)、[DComboBox](modules.md#dcombobox)、[DSearchComboBox](modules.md#dsearchcombobox)、[DFontComboBox](modules.md#dfontcombobox)。
- 使用列表与视图：参见 [DListView](modules.md#dlistview)、[DSimpleListView](modules.md#dsimplelistview)、[DSimpleListItem](modules.md#dsimplelistitem)、[DStandardItem](modules.md#dstandarditem)、[DStyledItemDelegate](modules.md#dstyleditemdelegate)、[DTreeView](modules.md#dtreeview)、[DTableView](modules.md#dtableview)、[DHeaderView](modules.md#dheaderview)。
- 使用样式与主题：参见 [DStyle](modules.md#dstyle)、[DStyleHelper](modules.md#dstylehelper)、[DStyleOption](modules.md#dstyleoption)、[DStyledIconEngine](modules.md#dstylediconengine)、[DStylePainter](modules.md#dstylepainter)、[DApplication](modules.md#dapplication)、[DPaletteHelper](modules.md#dpalettehelper)、[DSizeMode](modules.md#dsizemode)、[DFontSizeManager](modules.md#dfontsizemanager)、[DWaterMarkHelper](modules.md#dwatermarkhelper)。
- 使用效果与动画：参见 [DBlurEffectWidget](modules.md#dblureffectwidget)、[DClipEffectWidget](modules.md#dclipeffectwidget)、[DGraphicsClipEffect](modules.md#dgraphicsclipeffect)、[DGraphicsDropShadowEffect](modules.md#dgraphicsdropshadoweffect)、[DBounceAnimation](modules.md#dbounceanimation)、[DSpinner](modules.md#dspinner)、[DWaterProgress](modules.md#dwaterprogress)、[DIndeterminateProgressbar](modules.md#dindeterminateprogressbar)、[DPageIndicator](modules.md#dpageindicator)。
- 使用容器与布局：参见 [DFrame](modules.md#dframe)、[DHorizontalLine](modules.md#dhorizontalline)、[DVerticalLine](modules.md#dverticalline)、[DBackgroundGroup](modules.md#dbackgroundgroup)、[DShadowLine](modules.md#dshadowline)、[DDrawer](modules.md#ddrawer)、[DDrawerGroup](modules.md#ddrawergroup)、[DToolBox](modules.md#dtoolbox)、[DStackedWidget](modules.md#dstackedwidget)、[DSplitter](modules.md#dsplitter)、[DScrollArea](modules.md#dscrollarea)、[DGroupBox](modules.md#dgroupbox)、[DTabWidget](modules.md#dtabwidget)、[DTabBar](modules.md#dtabbar)。
- 使用浮层与提示：参见 [DFloatingWidget](modules.md#dfloatingwidget)、[DFloatingMessage](modules.md#dfloatingmessage)、[DMessageManager](modules.md#dmessagemanager)、[DTipLabel](modules.md#dtiplabel)、[DToolTip](modules.md#dtooltip)、[DAlertControl](modules.md#dalertcontrol)。
- 使用设置界面：参见 [DSettingsDialog](modules.md#dsettingsdialog)、[DSettingsWidgetFactory](modules.md#dsettingswidgetfactory)。
- 使用打印预览：参见 [DPrintPreviewDialog](modules.md#dprintpreviewdialog)、[DPrintPreviewSettingInfo](modules.md#dprintpreviewsettinginfo)、[DPrintPreviewSettingInterface](modules.md#dprintpreviewsettinginterface)。
- 在 DTK5 与 DTK6 之间迁移构建配置：参见[集成与构建配置](integration.md)；迁移公开类型：参见对应的[导出类型介绍](modules.md)。
