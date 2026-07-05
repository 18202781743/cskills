# 示例

DTK 各项目提供可编译运行的示例，帮助理解控件使用方式。

## QWidget 示例

dtkwidget 提供 `collections` 示例，一个包含 16 个分类、64+ 子示例的完整 Demo 应用。

**源码路径：** `dtkwidget/examples/collections/`

**构建运行：**
```bash
cd dtkwidget/examples/collections
mkdir build && cd build
cmake .. -DCMAKE_PREFIX_PATH=/path/to/dtk/install
make
./dtk-example
```

**分类总览：**

| 分类 | 演示控件 | 源文件 |
|------|----------|--------|
| Button | DPushButton, DWarningButton, DSuggestButton, DToolButton, DIconButton, DButtonBox, DFloatingButton, DSwitchButton, DRadioButton, DCheckBox, DComboBox, DFontComboBox, DSearchComboBox | `buttonexample.cpp` |
| Edit | DSearchEdit, DLineEdit, DIpv4LineEdit, DPasswordEdit, DFileChooserEdit, DSpinBox, DTextEdit, DCrumbEdit, DKeySequenceEdit | `editexample.cpp` |
| Slider | DSlider（水平/垂直、图标、刻度） | `sliderexample.cpp` |
| Menu | DMenu（右键菜单、子菜单、动画高亮） | `menuexample.cpp` |
| ListView | DListView, DStandardItem, DViewItemAction, DBackgroundGroup, DTreeView, DHeaderView, DColumnView | `listviewexample.cpp` |
| Window | DTitlebar（4 种样式）, DMainWindow, DStatusBar, DTabBar | `windowexample.cpp` |
| ToolTip | DToolTip, DArrowRectangle | `tooltipexample.cpp` |
| Spinner | DSpinner（5 种尺寸） | `spinnerexample.cpp` |
| Dialog | DDialog, DFileDialog, DMessageManager, DFloatingMessage | `dialogexample.cpp` |
| ProgressBar | DProgressBar, DWaterProgress, DColoredProgressBar, DIndeterminateProgressbar | `progressbarexample.cpp` |
| Layout | DFrame, DSplitter, DVerticalLine, DHorizontalLine | `layoutexample.cpp` |
| ScrollBar | DScrollArea | `scrollbarexample.cpp` |
| RubberBand | DRubberBand | `rubberbandexample.cpp` |
| Widget | DCalendarWidget, DTableWidget, DMPRISControl | `widgetexample.cpp` |
| LCDNumber | DLCDNumber | `lcdnumberexample.cpp` |
| ImageViewer | DImageViewer（缩放/旋转/裁剪） | `imageviewerexample.cpp` |

此外还有 `PrintPreviewSettingsPlugin` 插件示例（`examples/PrintPreviewSettingsPlugin/`），演示打印预览设置过滤。

## QML 示例

dtkdeclarative 提供两个 QML 示例应用：

### 1. Exhibition（控件画廊）

**源码路径：** `dtkdeclarative/examples/exhibition/`

**构建运行：**
```bash
cd dtkdeclarative/examples
mkdir build && cd build
cmake .. -DCMAKE_PREFIX_PATH=/path/to/dtk/install
make
./dtk-exhibition
```

完整的 DTK QML 控件展示应用，带源代码查看功能。侧边栏分类：

| 分类 | 演示内容 | QML 文件 |
|------|----------|----------|
| Buttons | 所有按钮类型、Switch、ComboBox、CheckBox、RadioButton、ButtonBox，含 CrystalColor 族 | `Button.qml` |
| Lists | ItemDelegate（背景/指示器/级联选中/四角/内容流），CheckDelegate + ButtonGroup | `ListControl.qml` |
| Menus | 右键菜单、搜索过滤菜单（ObjectModelProxy）、级联子菜单、可勾选项、分隔线、Instantiator 动态菜单 | `Menu.qml` |
| Notify | 系统通知（DTK.sendSystemMessage）、应用通知（FloatingMessage）、应用角标 | `Notify.qml` |
| Dialogs | 8 种 DialogWindow（通知/授权/警告/组合/进度/WiFi/错误/关于） | `Dialog.qml` |
| Popups | 浮动面板（勿扰/蓝牙/音量/网络）、文件属性对话框 | `Popup.qml` |
| Sliders | 水平/垂直 Slider（6 种 HandleType）、TipsSlider 刻度、highlightedPassedGroove | `Slider.qml` |
| Inputs | LineEdit（alert）、SearchEdit、IpV4LineEdit、PasswordEdit、PlusMinusSpinBox、SpinBox、TextArea | `EditControl.qml` |
| KeySequence | 快捷键编辑 | `KeySequenceEdit.qml` |
| SideBar | 侧边栏面板（收藏/书签/标签/磁盘） | `SideBar.qml` |
| Progress | BusyIndicator（多尺寸/亮暗）、ProgressBar/EmbeddedProgressBar/WaterProgressBar | `Spinner.qml`, `ProgressBar.qml` |
| ScrollBar | 水平/垂直 ScrollBar | `ScrollBar.qml` |
| Mask | 自定义窗口形状（DWindow.clipPath + PathArc） | `Mask.qml` |
| ToolBar | TitleBar 变体 + FloatingPanel 工具栏 | `ToolBar.qml` |
| Group | ControlGroup + ControlGroupItem 折叠组 | `ControlGroup.qml` |

### 2. QML Inspect（控件检查器）

**源码路径：** `dtkdeclarative/examples/qml-inspect/`

分标签页的功能测试应用：

| 标签 | 演示内容 | QML 文件 |
|------|----------|----------|
| Example_1 | 按钮/输入/选择/滑动全览 | `Example_1.qml` |
| Example_2 | 图标/特效/阴影/导航/形状 | `Example_2.qml` |
| ItemViewport | 透明度遮罩/阴影/模糊/圆角裁剪 | `Example_3.qml` |
| Config | DConfig 键值持久化 | `Example_config.qml` |
| SettingsDialog | SettingsDialog 设置界面 | `Example_settingsdialog.qml` |
| Notify | FloatingMessage 通知 | `Example_Notify.qml` |
| ColorSelector | 调色板继承/覆盖/重设父/动画 | `Example_colorselector.qml` |
| Menu | Menu（搜索过滤/级联/动态增删） | `Example_Menu.qml` |
| Popup | Popup/ArrowShapePopup 4 方向箭头 | `Example_Popup.qml` |
| Flickable | ScrollView/ProgressBar/WaterProgressBar/IpV4LineEdit/SortFilterModel | `Example_Flickable.qml` |
| GroupBox | GroupBox 分组框 | `Example_GroupBox.qml` |

## 相关文档

- [../widgets/index.md](../widgets/index.md) — QWidget 控件文档
- [../declarative/index.md](../declarative/index.md) — QML 控件文档
