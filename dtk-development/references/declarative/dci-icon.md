# QML 中使用 dci 图标

## 1. 概述

在 QML 中使用 dci 图标，可通过 `DciIconImage` 组件（对应 C++ 后端 `DQuickDciIconImage`）。

> **注意**：`DciIconImage` 是 dtkdeclarative 的公开 QML 组件名，其 C++ 实现类为 `DQuickDciIconImage`（私有 API）。在 QML 中应使用 `DciIconImage`。

## 2. 使用方式

### 2.1 DciIconImage

```qml
import org.deepin.dtk 1.0
import QtQuick 2.15

DciIconImage {
    source: "qrc:/icons/my-icon.dci"
    width: 32
    height: 32
}
```

### 2.2 在按钮中使用

```qml
import org.deepin.dtk 1.0

Button {
    icon.source: "qrc:/icons/action-icon.dci"
    icon.width: 24
    icon.height: 24
    text: "操作"
}
```

## 3. 主题切换

```qml
import org.deepin.dtk 1.0

DciIconImage {
    id: iconImage
    source: "qrc:/icons/my-icon.dci"
    width: 32
    height: 32
    // DciIconImage 自动跟随系统主题切换
}
```

## 4. 相关文档

- [../icons/dci.md](../icons/dci.md) - dci 图标完整规范
- [index.md](index.md) - QML 控件选择
