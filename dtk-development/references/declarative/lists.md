# 列表类控件

## 1. ItemDelegate

列表项委托，继承 `T.ItemDelegate`。支持：
- 选中高亮（`HighlightPanel`）
- 级联选中（`RoundRectangle` + `cascadeSelected`）
- 勾选指示器（`menu_select` dci 图标）
- 自定义内容组件（`content`）
- 四角独立控制（`corners` 位掩码）

```qml
ListView {
    model: 10
    delegate: ItemDelegate {
        text: "列表项 " + index
        checked: index === currentIndex
        indicatorVisible: true
        backgroundVisible: true
    }
}
```

| 自定义属性 | 类型 | 说明 |
|-----------|------|------|
| `indicatorVisible` | `bool` | 是否显示勾选指示器 |
| `backgroundVisible` | `bool` | 是否显示背景（默认 true） |
| `cascadeSelected` | `bool` | 级联选中样式（子项继承父项选中状态） |
| `contentFlow` | `bool` | 内容是否填充剩余空间 |
| `content` | `Component` | 自定义内容组件 |
| `checkedTextColor` | `Palette` | 选中时文本颜色 |
| `corners` | `int` | 四角控制（`RoundRectangle.TopLeftCorner` 等位掩码） |
| `getCornersForBackground(index, count)` | 方法 | 自动计算首尾项的圆角 |

**注意事项：** 默认字体 `D.DTK.fontManager.t9`，图标通过 `D.DTK.makeIcon()` 查找 dci 路径。

## 2. CheckDelegate

可勾选委托，继承 `T.CheckDelegate`。带 `menu_select` 勾选指示器，支持自定义 `content` 内容组件和 `backgroundColor` 背景色。

```qml
ListView {
    model: ListModel { ListElement { name: "Apple" } }
    delegate: CheckDelegate {
        text: model.name
        checked: model.checked
    }
}
```

## 3. ArrowListView

带箭头按钮的列表视图，继承 `FocusScope`。当内容超过 `maxVisibleItems` 时，显示上下箭头按钮用于滚动导航。用于 Menu/ComboBox 弹出内容。

```qml
ArrowListView {
    maxVisibleItems: 6
    itemHeight: 30
    view.model: myModel
}
```

## 4. 相关文档

- [menus.md](menus.md) — Menu 菜单系统（使用 ArrowListView 和 MenuItem）
- [inputs.md](inputs.md) — ComboBox（使用 ArrowListView）
- [panels.md](panels.md) — HighlightPanel 面板
