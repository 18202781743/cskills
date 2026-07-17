# QML Chameleon 风格

## 概述

QML Chameleon 是 Qt Quick Controls 2 Style 插件，将 Qt Quick Controls 控件映射到 DTK QML 控件实现。

## 插件结构

`dtkdeclarative/chameleon/` 包含：
- `Button.qml` → `D.Button`
- `CheckBox.qml` → `D.CheckBox`
- `TextField.qml` → `D.TextField`
- 等 Qt Quick Controls 同名 QML 文件

**注意：** QML 风格名是 `Chameleon`（大小写敏感），与 QWidget 的 `chameleon` 不同。

## 启用方式

```bash
# 环境变量
QT_QUICK_CONTROLS_STYLE=Chameleon ./my-qml-app

# 命令行
./my-qml-app -style Chameleon
```

代码方式：

```cpp
QQuickStyle::setStyle("Chameleon");
```

必须在加载 QML 前调用。

## 调试

```bash
QT_DEBUG_PLUGINS=1 QT_QUICK_CONTROLS_STYLE=Chameleon ./my-qml-app
```

## Style 单例

DTK QML 控件通过 `org.deepin.dtk.style` URI 的 `Style` 单例读取尺寸和状态调色板。

详见 [style.md](style.md)。

## 不能混用的 API

| QWidget | QML |
|---------|-----|
| `QApplication::setStyle("chameleon")` | `QQuickStyle::setStyle("Chameleon")` |
| `QStyleOption::state` | `hovered` / `pressed` / `checked` / `enabled` |
| `QPalette` / `DPaletteHelper` | QML Palette / ColorSelector |
| `drawControl()` / `QPainter` | `background` / `contentItem` |

## 相关文档

- [style.md](style.md) — QML Style 单例
- [color-selector.md](color-selector.md) — QML 取色器
