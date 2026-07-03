# QML 中使用 dci 图标

## 1. 概述

在 QML 中使用 dci 图标，可通过 `DciIcon` 组件（对应 C++ 后端 `DQuickDciIconImage`）。

## 2. 使用方式

### 2.1 DciIcon

```qml
import org.deepin.dtk 1.0

DciIcon {
    name: "my-icon"
    sourceSize: Qt.size(32, 32)
}
```

### 2.2 在按钮中使用

```qml
import org.deepin.dtk 1.0

Button {
    icon.name: "action-icon"
    icon.width: 24
    icon.height: 24
    text: "操作"
}
```

## 3. 主题切换

```qml
import org.deepin.dtk 1.0

DciIcon {
    id: iconImage
    name: "my-icon"
    sourceSize: Qt.size(32, 32)
    // DciIcon 自动跟随系统主题切换
}
```

## 4. 相关文档

- [../icons/dci.md](../icons/dci.md) - dci 图标完整规范
- [index.md](index.md) - QML 控件选择
