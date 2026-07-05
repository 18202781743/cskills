# QML 控件选择决策树

## 1. 概述

dtkdeclarative 提供符合 DTK 设计规范的 QML 控件，用于 Qt Quick 应用。

**适用场景：**
- DDE Shell 插件
- QML 应用
- 需要动态 UI 的场景

**CMake 依赖（仅当使用 dtkdeclarative 的 C++ API 时需要）：**
```cmake
find_package(DtkDeclarative REQUIRED)
target_link_libraries(your_target Dtk::Declarative)
```

纯 QML 应用通过 `import org.deepin.dtk 1.0` 即可，运行时由 QML 引擎自动查找，不需要 CMake 依赖。

## 2. 快速决策树

```
需要什么类型的 QML 控件？
    │
    ├─ 窗口 → ApplicationWindow
    │
    ├─ 按钮 → Button / RoundButton / DelayButton
    │
    ├─ 输入 → TextField / TextArea / SpinBox / ComboBox
    │
    ├─ 选择 → CheckBox / RadioButton / Switch
    │
    ├─ 导航 → TabBar / StackView / Drawer
    │
    ├─ 进度 → ProgressBar / BusyIndicator
    │
    ├─ 消息 → Dialog / ToolTip / Popup
    │
    └─ 视图 → ListView / ScrollView
```

## 3. 核心控件速查

| 控件 | 用途 |
|------|------|
| `ApplicationWindow` | 主窗口 |
| `Button` | 标准按钮 |
| `TextField` | 单行输入 |
| `TextArea` | 多行输入 |
| `ComboBox` | 下拉选择 |
| `CheckBox` | 多选框 |
| `RadioButton` | 单选按钮 |
| `Switch` | 开关 |
| `TabBar` + `TabButton` | 标签页 |
| `StackView` | 页面堆栈 |
| `ProgressBar` | 进度条 |
| `BusyIndicator` | 加载指示 |
| `Dialog` | 对话框 |
| `ListView` | 列表视图 |
| `ScrollView` | 滚动视图 |

## 4. 代码模板

### 4.1 基本窗口

```qml
import org.deepin.dtk 1.0

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "My App"
}
```

### 4.2 按钮与输入

```qml
import org.deepin.dtk 1.0
import QtQuick 2.15
import QtQuick.Layouts 1.15

ColumnLayout {
    TextField {
        placeholderText: "请输入..."
    }
    Button {
        text: "确定"
        onClicked: console.log("clicked")
    }
}
```

## 5. 相关文档

- [controls.md](controls.md) — 控件分类索引（按按钮/输入/菜单/对话框/面板/列表/进度分类）
- [color-selector.md](color-selector.md) — ColorSelector 取色器与 Palette 调色板
- [effects.md](effects.md) — QML 视觉效果（模糊/光晕/叠加/遮罩）
- [dci-icon.md](dci-icon.md) — QML 中使用 dci 图标
