# QML 控件详细规范

## 1. 基础控件

### 1.1 Button

```qml
Button {
    text: "确定"
    icon.source: "qrc:/icons/icon.dci"
    onClicked: console.log("clicked")
}
```

### 1.2 TextField

```qml
TextField {
    placeholderText: "请输入..."
    onTextChanged: console.log(text)
}
```

### 1.3 ComboBox

```qml
ComboBox {
    model: ["选项1", "选项2", "选项3"]
    onCurrentIndexChanged: console.log(currentIndex)
}
```

## 2. 导航控件

### 2.1 TabBar

```qml
TabBar {
    id: tabBar
    TabButton { text: "常规" }
    TabButton { text: "高级" }
    onCurrentIndexChanged: stackView.currentIndex = currentIndex
}

StackView {
    id: stackView
    currentIndex: tabBar.currentIndex
    Item { /* 常规页 */ }
    Item { /* 高级页 */ }
}
```

## 3. 相关文档

- [index.md](index.md) - QML 控件选择
- [dci-icon.md](dci-icon.md) - dci 图标使用
