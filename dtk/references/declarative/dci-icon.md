# QML 中使用 dci 图标

## 1. 概述

在 QML 中使用 dci 图标，需要使用 `DciIcon` 或 `DciIconImage` 组件。

## 2. 使用方式

### 2.1 DciIconImage

```qml
import org.deepin.dtk 1.0
import QtQuick 2.15

DciIconImage {
    source: "qrc:/icons/my-icon.dci"
    width: 32
    height: 32
    theme: DGuiApplicationHelper.DarkType  // 或 LightType
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
import org.deepin.dtk.private 1.0 as D

DciIconImage {
    id: iconImage
    source: "qrc:/icons/my-icon.dci"
    theme: DGuiApplicationHelper.instance.themeType === DGuiApplicationHelper.DarkType
           ? DciIcon.Dark : DciIcon.Light
}
```

## 4. 相关文档

- [../icons/dci.md](../icons/dci.md) - dci 图标完整规范
- [index.md](index.md) - QML 控件选择
