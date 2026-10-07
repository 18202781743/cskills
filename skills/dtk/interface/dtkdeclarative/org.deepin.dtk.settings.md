# org.deepin.dtk.settings QML 模块

org.deepin.dtk.settings 是 dtkdeclarative 提供的设置界面 QML 模块，为 DTK 应用提供开箱即用的设置对话框框架。模块内置导航栏与内容区的联动布局，支持从配置模型自动生成复选框、下拉框、文本输入等配置项控件，统一遵循 DTK 主题样式。

## 集成

### 使用方式

QML 模块 URI 为 `org.deepin.dtk.settings`，版本为 1.0，其插件随对应的 dtkdeclarative 运行时包安装。DTK6 使用 Qt6 与 `libdtk6declarative`，DTK5 使用 Qt5 与 `libdtkdeclarative5`；使用 Chameleon 风格时还需对应 Qt 主版本的 Chameleon QML 样式包。

```qml
import org.deepin.dtk 1.0 as D
import org.deepin.dtk.settings 1.0 as Settings
```

用 `Settings.SettingsGroup` 和 `Settings.SettingsOption` 声明配置模型，在 `Settings.SettingsDialog` 中关联 `config` 与 `groups`。配置对象可使用主模块的 `D.Config`，其键名须与选项的 `key` 对应。颜色与尺寸取自主模块或 `org.deepin.dtk.style` 的 `Style.settings`；本设置模块不导出独立的 `Style` 类型。图标、主题与配置对象详见 [org.deepin.dtk](org.deepin.dtk.md)。

## 设置模型

### SettingsOption

#### 定位

单个配置选项及其显示委托。

#### 功能能力总结

通过 key、name、value 和 delegate 声明选项，value 与所属容器的 config 同步，重置时恢复配置默认值。delegate 是默认内容属性；在选项委托中通过 SettingsOption 附加属性访问当前选项。

#### 使用场景

需要把一个配置键映射为设置行，或编写自定义选项委托时。


---

### SettingsGroup

#### 定位

设置选项的分组与层级。

#### 功能能力总结

通过 key、name、visible 声明分组，默认 options 保存选项，children 保存子组，background 可替换分组背景。提供只读 level 和 index；标题和内容委托可通过 SettingsGroup 附加属性访问所属分组。

#### 使用场景

需要将配置项组织为导航分组或嵌套分组时。


---

### SettingsContainer

#### 定位

把配置对象和分组声明转为设置界面模型。

#### 功能能力总结

通过 config 关联配置对象，以默认 groups 接收分组，生成 contentModel 与 navigationModel，并允许替换内容标题、内容背景及导航标题委托。支持按组键读写可见性及 resetSettings 恢复设置。

#### 使用场景

需要使用标准设置对话框，或自行组合导航与内容界面时。


---


## 设置项控件

### OptionDelegate

#### 定位

设置项的通用行布局。

#### 功能能力总结

继承 RowLayout，左侧标签读取 SettingsOption.name，leftVisible 控制标签可见性；子内容可通过 SettingsOption 附加属性读写当前配置值。

#### 使用场景

需要为文件选择、数值输入或其他设置项实现自己的委托时。


---

### CheckBox

#### 定位

布尔配置项的编辑委托。

#### 功能能力总结

继承 OptionDelegate，使用复选框显示 SettingsOption.name 和 value，checked 变化时回写选项；默认隐藏独立左侧标签以避免重复文字。

#### 使用场景

配置值为布尔类型，需要用勾选方式启停功能时。


---

### ComboBox

#### 定位

候选值配置项的编辑委托。

#### 功能能力总结

继承 OptionDelegate，以 model 提供候选数据，valueRole 指定对象中的取值角色；匹配 SettingsOption.value 决定当前索引，用户 activated 后将选中值回写。impl 暴露内部 ComboBox。

#### 使用场景

需要从字符串或对象数组中选择一个配置值时。


---

### LineEdit

#### 定位

文本配置项的编辑委托。

#### 功能能力总结

继承 OptionDelegate，文本绑定 SettingsOption.value，在 editingFinished 时回写输入；名称标签和布局由基类提供。

#### 使用场景

需要编辑字符串配置，并在编辑完成后保存时。


---


## 对话框与分组外观

### SettingsDialog

#### 定位

设置窗口及导航、内容联动框架。

#### 功能能力总结

继承 DialogWindow，通过 groups 和 config 声明设置，container 负责配置同步与模型生成。navigationView 和 contentView 暴露两侧视图，当前组索引双向联动，恢复默认值按钮调用容器的 resetSettings。

#### 使用场景

需要以声明式分组和选项创建应用设置窗口时。


---

### NavigationTitle

#### 定位

导航栏中的分组标题。

#### 功能能力总结

读取 SettingsGroup.name，checked 控制选中配色，clicked 通知用户选择分组；字体和尺寸使用 Style.settings 的导航参数。

#### 使用场景

替换 SettingsContainer 的导航标题委托时。


---

### ContentTitle

#### 定位

内容区域的分组标题。

#### 功能能力总结

读取 SettingsGroup.name 和 level，根据层级选择字体与左右边距，提供明确的分组层次。

#### 使用场景

替换 SettingsContainer 的内容标题委托时。


---

### ContentBackground

#### 定位

设置内容的分组背景。

#### 功能能力总结

继承 Rectangle，根据 SettingsGroup.level 设置背景区域的左右边距，使用主题背景色与圆角呈现分组内容。

#### 使用场景

替换 SettingsContainer 的内容背景委托时。


---
