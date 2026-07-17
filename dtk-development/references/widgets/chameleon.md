# QWidget Chameleon 风格

## 概述

QWidget 控件外观由两层组成：
- `DStyle`（dtkwidget）：DTK 扩展风格类，定义图元、像素度量、状态画刷
- `ChameleonStyle`（qt5integration）：实际绘制实现

## 实现结构

```
QCommonStyle
└── DStyle                         dtkwidget
    └── ChameleonStyle             qt5integration

QStylePlugin
└── ChameleonStylePlugin
    └── create("chameleon") → ChameleonStyle
```

## 动态指定风格

```bash
# 命令行
./my-widget-app -style chameleon
./my-widget-app -style fusion

# 环境变量
QT_STYLE_OVERRIDE=chameleon ./my-widget-app
```

代码方式：

```cpp
QApplication::setStyle("chameleon");
```

## 调试

```bash
# 插件诊断
QT_DEBUG_PLUGINS=1 ./my-widget-app -style chameleon

# 检查当前风格
qInfo() << "current style:" << QApplication::style()->objectName();
qInfo() << "available styles:" << QStyleFactory::keys();
```

## 自定义控件复用 DTK 风格

详见 [style.md](style.md)。

## 相关文档

- [style.md](style.md) — DStyle 控件绘制指南
- [../theme/palette.md](../theme/palette.md) — DPalette 语义色
