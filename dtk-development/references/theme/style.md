# DStyle 风格规范

## 1. 概述

`DStyle` 是 DTK 的控件风格类，继承自 `QCommonStyle`，负责控件的渲染风格。

## 2. 标准图标

```cpp
#include <DStyle>

QIcon closeIcon = DStyle::standardIcon(style, DStyle::SP_CloseButton);
QIcon addIcon = DStyle::standardIcon(style, DStyle::SP_IncreaseElement);
```

## 3. 像素度量

```cpp
#include <DStyle>

int radius = DStyle::pixelMetric(style, DStyle::PM_FrameRadius);
int shadowRadius = DStyle::pixelMetric(style, DStyle::PM_ShadowRadius);
int focusBorderWidth = DStyle::pixelMetric(style, DStyle::PM_FocusBorderWidth);
```

## 4. DStyleHelper

```cpp
#include <DStyle>

DStyleHelper helper(style());

// 获取处理后的颜色
QColor color = helper.getColor(option, DPalette::TextTitle);

// 绘制图元
helper.drawPrimitive(DStyle::PE_ItemBackground, option, painter, widget);
```

## 5. 相关文档

- [chameleon-style.md](chameleon-style.md) - DStyle 与 ChameleonStyle 实现
- [palette.md](palette.md) - 调色板规范
- [theme-switch.md](theme-switch.md) - 主题切换机制
