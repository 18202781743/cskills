# org.deepin.dtk QML 模块

org.deepin.dtk 是 dtkdeclarative 提供的 QML 声明式控件模块，为 DTK 应用提供一套完整的界面控件库。模块覆盖按钮、对话框与窗口、文本与数值输入、菜单与动作、列表与视图以及视觉效果与渲染等常见交互场景，所有控件统一遵循 DTK 设计规范的主题色、圆角和交互反馈风格，可与 `org.deepin.dtk.style` 样式单例和 `org.deepin.dtk.settings` 设置模块配合使用。



## 集成

### 使用方式

QML 模块 URI 为 `org.deepin.dtk`，导入版本为 1.0。模块以动态插件形式发布，使用方无需安装额外模块包，确保系统已安装 dtkdeclarative 运行时库即可。

在 QML 文件中导入：

```qml
import org.deepin.dtk 1.0
```

导入后可使用模块中的所有控件类型。样式参数通过 `org.deepin.dtk.style` 子模块的单例设置，对话框控件通过 `org.deepin.dtk.settings` 子模块配置。


---

## 接口分类

- [按钮控件](org.deepin.dtk/buttons.md) — Button、RoundButton、DelayButton、IconButton、FloatingButton、WarningButton、ToolButton、RecommandButton、ButtonBox、ButtonGroup、ButtonIndicator、ButtonPanel、AbstractButton、ActionButton、WindowButton、WindowButtonGroup、WindowQuitFullButton
- [对话框与窗口控件](org.deepin.dtk/dialogs-and-windows.md) — DialogWindow、Dialog、PopupWindow、ArrowShapePopupWindow、ArrowShapePopup、Popup、StyledArrowShapeWindow、DWindow、ApplicationWindow、TitleBar、DialogTitleBar、Drawer、AboutDialog
- [输入控件](org.deepin.dtk/input-controls.md) — TextField、TextArea、SearchEdit、PasswordEdit、IpV4LineEdit、KeySequenceEdit、LineEdit、EditPanel、PlaceholderText、SpinBox、PlusMinusSpinBox、Dial、SpinBoxIndicator、CheckBox、RadioButton、Switch、ComboBox、CheckDelegate、SwipeDelegate、Slider、SliderHandle、SliderTipItem、TipsSlider
- [菜单与动作控件](org.deepin.dtk/menus-and-actions.md) — Menu、MenuItem、MenuBar、MenuSeparator、ThemeMenu、AboutAction、HelpAction、QuitAction、Action、ActionGroup
- [列表与视图控件](org.deepin.dtk/list-and-views.md) — ScrollView、StackView、SwipeView、ItemDelegate、ArrowListView、SortFilterModel、TabBar、PageIndicator、Container、Control、DialogButtonBox、ScrollBar、ScrollIndicator
- [视觉效果与渲染控件](org.deepin.dtk/visual-effects-and-rendering.md) — BoxShadow、BoxInsetShadow、BoxPanel、FloatingPanel、RectangularShadow、HighlightPanel、ControlBackground、Frame、Pane、GroupBox、OutsideBoxBorder、InsideBoxBorder、FocusBoxBorder、BlitFramebuffer、ItemViewport、StyledBehindWindowBlur、FlowStyle、BusyIndicator、ProgressBar、WaterProgressBar、EmbeddedProgressBar、CicleSpreadAnimation、Label、ToolTip、AlertToolTip、FloatingMessage

