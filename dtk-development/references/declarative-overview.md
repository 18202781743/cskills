# QML 控件概览

dtkdeclarative 对 Qt Quick Controls 进行 DTK 主题封装，用于 DDE Shell 插件和 QML 应用。

## 触发关键词

QML 按钮/对话框/输入框、QML 菜单/列表/进度条、org.deepin.dtk、DTK QML 控件

## 控件选择决策树

```
需要什么类型的 QML 控件？
    │
    ├─ 窗口 → ApplicationWindow / DialogWindow
    ├─ 按钮 → Button / RecommandButton / WarningButton / IconButton
    ├─ 选择 → CheckBox / RadioButton / Switch
    ├─ 输入 → TextField / LineEdit / SearchEdit / PasswordEdit / SpinBox
    ├─ 菜单 → Menu / MenuItem / ThemeMenu
    ├─ 对话框 → DialogWindow / AboutDialog
    ├─ 列表 → ItemDelegate / CheckDelegate
    ├─ 进度 → ProgressBar / WaterProgressBar
    └─ 滑动 → Slider / TipsSlider
```

---

## 导入模块

```qml
import org.deepin.dtk 1.0 as D
```

---

## 窗口

### ApplicationWindow

```qml
import org.deepin.dtk 1.0 as D

D.ApplicationWindow {
    width: 800
    height: 600
    visible: true
    
    D.TitleBar { }
}
```

### DialogWindow

```qml
D.DialogWindow {
    title: "对话框"
    width: 400
    height: 300
}
```

---

## 按钮

### Button / RecommandButton / WarningButton

```qml
D.Button { text: "普通" }
D.RecommandButton { text: "推荐" }  // 蓝色
D.WarningButton { text: "警告" }    // 红色
```

### IconButton

```qml
D.IconButton {
    icon.name: "icon-name"
    icon.width: 24
    icon.height: 24
}
```

---

## 输入控件

### TextField / LineEdit

```qml
D.TextField {
    placeholderText: "请输入"
    onTextChanged: { }
}
```

### SearchEdit / PasswordEdit

```qml
D.SearchEdit { placeholderText: "搜索..." }
D.PasswordEdit { }
```

---

## DCI 图标

### DciIcon

```qml
D.DciIcon {
    name: "icon-name"
    sourceSize: Qt.size(32, 32)
    palette: D.DTK.makeIconPalette(D.DTK.palette)
}
```

**关键属性：**
- `name`: dci 图标名称
- `mode`: NormalState / HoveredState / PressedState / DisabledState
- `theme`: LightType / DarkType

---

## D.DTK 全局对象

| 属性/方法 | 说明 |
|-----------|------|
| `D.DTK.themeType` | 当前主题类型 |
| `D.DTK.fontManager` | 字体管理器 |
| `D.DTK.palette` | 应用调色板 |
| `D.DTK.makeIconPalette(palette)` | 创建图标调色板 |
| `D.DTK.makeColor(role)` | 创建语义化颜色 |

### 监听主题切换

```qml
Connections {
    target: D.DTK
    function onThemeTypeChanged() {
        console.log("Theme:", D.DTK.themeType)
    }
}
```

---

## 列表项

### ItemDelegate

```qml
D.ItemDelegate {
    text: "列表项"
    onClicked: { }
}
```

---

## 进度与滑动

```qml
D.ProgressBar { value: 0.5 }
D.WaterProgressBar { value: 50 }  // 水波进度
D.Slider { from: 0; to: 100; value: 50 }
```

---

## ColorSelector 取色器

ColorSelector 是附加属性，自动根据控件状态选择颜色：

```qml
D.Button {
    property D.Palette backgroundColor: D.Palette {
        normal: "#ffffff"
        hovered: "#f0f0f0"
    }
    
    background: Rectangle {
        color: backgroundColor.D.ColorSelector.color
    }
}
```

**Palette 属性：** `normal` / `hovered` / `pressed` / `disabled`（每个支持 `normalDark` 等暗色版本）

---

## 常见错误

| 错误 | 正确做法 |
|------|----------|
| 使用 Qt Quick Controls 原生控件 | 导入 `org.deepin.dtk` 使用 DTK 控件 |
| 硬编码颜色 | 使用 `Palette` + `ColorSelector` |
| 图标不跟随主题 | 使用 `DciIcon` 或设置 `palette` |

---

## 相关文档

- [widgets-overview.md](widgets-overview.md) — QWidget 控件
- [theme-system.md](theme-system.md) — 主题系统
