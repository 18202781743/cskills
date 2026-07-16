# QML Style 单例与应用级样式覆盖

## 1. 两层“style”不要混淆

dtkdeclarative 中存在两套职责不同的样式机制：

| 层次 | URI / 名称 | 职责 |
|---|---|---|
| Qt Quick Controls 风格插件 | `Chameleon` | `dtkdeclarative/chameleon/` 提供 `Button.qml`、`CheckBox.qml` 等同名映射，使标准 Qt Quick Controls 使用 DTK 控件实现 |
| DTK 样式数据单例 | `org.deepin.dtk.style 1.0` 中的 `Style` | 集中提供尺寸、间距、圆角和各状态调色板，供 `org.deepin.dtk` 控件绘制时读取 |

前者决定“标准控件由哪套 QML 实现”，后者决定 DTK 控件实现使用哪些设计参数。它们可以同时工作，但不是同一个插件。

## 2. URI 和注册过程

主插件 URI 是 `org.deepin.dtk`。Qt 5 的 `QmlpluginPlugin::registerTypes()` 还由主 URI 派生并注册 `org.deepin.dtk.style`，随后把 `Style` 注册成 QML 单例：

```cpp
const QByteArray styleUri = QByteArray(uri).append(".style");
qmlRegisterModule(styleUri.constData(), 1, 0);
qmlRegisterSingletonType(
    QUrl("qrc:/dtk/declarative/qml/style/Style.qml"),
    styleUri.constData(), 1, 0, "Style");
```

因此控件源码通常这样读取样式：

```qml
import org.deepin.dtk.style 1.0 as DS

// Button.qml
implicitHeight: DS.Style.control.implicitHeight(control)
topPadding: DS.Style.button.vPadding
spacing: DS.Style.control.spacing
```

`Style` 使用 `pragma Singleton`，同一个 QML 引擎中共享一份样式对象，避免每个控件重复创建完整的样式树。

## 3. `Style.qml` 与 `FlowStyle.qml`

默认入口 `src/qml/style/Style.qml` 很薄：

```qml
pragma Singleton
import ".."

FlowStyle {}
```

真正的默认设计参数位于 `src/qml/FlowStyle.qml`。它是一个 `QtObject`，按控件分组暴露属性：

```text
Style
├── control       通用圆角、间距、padding、边框和隐式尺寸算法
├── button        普通按钮尺寸、图标尺寸、背景和文字调色板
├── checkedButton / highlightedButton
├── textField / comboBox / menu
├── progressBar / slider / scrollBar
└── ...
```

调色板不是单个固定颜色，而是 `D.Palette`。其 `normal`、`hovered`、`pressed`、`disabled` 以及对应的 `*Dark` 属性描述亮暗主题和交互状态；`common`、`crystal` 还可区分颜色族。控件再通过 `D.ColorSelector` 根据 `hovered`、`pressed`、`checked`、`enabled` 和当前主题选择实际颜色。

这种分工使控件的背景、内容项和状态判断仍留在各控件 QML 中，而尺寸及颜色令牌集中在 `FlowStyle.qml` 中。

## 4. 应用覆盖 `Style.qml`

插件把单例固定注册到资源 URL：

```text
qrc:/dtk/declarative/qml/style/Style.qml
```

所以应用级覆盖不是在任意 import 目录放一个同名文件，而是把自己的 `Style.qml` 注册到**相同的 Qt Resource 路径**。自定义文件通常继承 `FlowStyle`，只改需要的属性，其余继续使用 DTK 默认值。

### 4.1 自定义文件

例如创建 `qml/style/Style.qml`：

```qml
pragma Singleton

import org.deepin.dtk 1.0

FlowStyle {
    // 全局几何参数
    control.radius: 10
    control.spacing: 8

    // 按钮默认尺寸
    button.width: 160
    button.height: 40
    button.iconSize: 20

    // 普通按钮的亮色状态色；未修改的暗色及其他状态沿用默认值
    button.background1.normal.common: "#f2f3f5"
    button.background1.hovered.common: "#e5e8ed"
    button.background1.pressed.common: "#d7dce3"
}
```

覆盖文件必须保留 `pragma Singleton`，并提供控件实际访问的属性路径。最稳妥的方式是继承 `FlowStyle` 后局部赋值；从空 `QtObject` 重写时，漏掉例如 `Style.control.implicitHeight()` 或 `Style.button.text` 会导致控件加载错误。

### 4.2 注册到相同资源路径

Qt 资源文件示例：

```xml
<RCC>
  <qresource prefix="/dtk/declarative/qml/style">
    <file alias="Style.qml">qml/style/Style.qml</file>
  </qresource>
</RCC>
```

将该 `.qrc` 编入应用，并确保应用资源在首次 `import org.deepin.dtk.style`、创建 DTK 控件之前完成注册。若资源位于单独的库中，可在加载 QML 前调用 `Q_INIT_RESOURCE(resource_name)`。

这是资源 URL 覆盖机制，不是 QML import path 优先级机制：仅调用 `QQmlEngine::addImportPath()`，或在应用 QML 目录放置一个普通 `Style.qml`，不会改变插件注册的上述 `qrc:` URL。

> 同一路径资源的解析与资源注册顺序有关。应用应在初始化最早阶段注册覆盖资源，并在目标 Qt/DTK 版本上验证；若打包方式无法可靠保证顺序，建议直接设置控件公开的 `Palette`、尺寸属性或封装应用自己的控件组件。

## 5. 哪种定制方式更合适

| 需求 | 建议方式 |
|---|---|
| 只修改一个控件实例 | 设置该控件公开的 `backgroundColor`、`textColor`、`palette`、`icon`、`font` 等属性 |
| 统一修改应用内一类控件 | 封装应用自己的 `AppButton.qml` 等组件 |
| 全局调整 DTK 的尺寸令牌和状态调色板 | 以 `FlowStyle` 为基类覆盖资源路径中的 `Style.qml` |
| 让标准 Qt Quick Controls 采用 DTK 实现 | 启用 `Chameleon` Qt Quick Controls 风格插件 |

`FlowStyle` 和 `Style` 属于实现级接口。升级 DTK 后可能新增控件分组或属性，因此应用覆盖文件应尽量只做局部赋值，并在升级时与当前版本 `FlowStyle.qml` 对照。

## 6. 调试覆盖是否生效

1. 打开 QML import 和插件日志：

   ```bash
   QML_IMPORT_TRACE=1 QT_DEBUG_PLUGINS=1 ./my-qml-app
   ```

2. 在自定义 `Style.qml` 中临时加入：

   ```qml
   Component.onCompleted: console.info("application Style.qml loaded")
   ```

3. 确认资源中确实存在目标路径：

   ```text
   :/dtk/declarative/qml/style/Style.qml
   ```

4. 若标准 Qt Quick Controls 的外观仍无变化，分别运行：

   ```bash
   QT_QUICK_CONTROLS_STYLE=Chameleon ./my-qml-app
   QT_QUICK_CONTROLS_STYLE=Basic ./my-qml-app
   ```

   `Basic` 生效而 `Chameleon` 不生效时，检查对应 DTK 控件是否实际读取了被修改的 `DS.Style` 属性；反之则先检查应用是否使用了标准 Controls、DTK 控件或自行实现的背景。

## 7. 相关文档

- [index.md](index.md) — QML 控件索引
- [color-selector.md](color-selector.md) — `Palette`、亮暗主题与控件状态取色
- [buttons.md](buttons.md) — 按钮实例级颜色、图标和字体定制
- [../theme/chameleon-style.md](../theme/chameleon-style.md) — QWidget/QML Chameleon 插件及动态切换对比
