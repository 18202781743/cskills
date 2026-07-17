# 平台集成与窗口装饰

DTK 平台抽象层提供跨平台窗口装饰能力，支持 X11/Wayland/Treeland。

## 触发关键词

窗口圆角、窗口阴影、窗口模糊、无边框窗口、CSD、DPlatformHandle

---

## DPlatformHandle 核心 API

```cpp
#include <DPlatformHandle>

// 为 QWindow 启用 DTK 平台支持
DPlatformHandle handle(window);
```

### 窗口装饰属性

| 属性 | 说明 |
|------|------|
| `windowRadius` | 窗口圆角半径 |
| `borderWidth` / `borderColor` | 边框宽度和颜色 |
| `shadowRadius` / `shadowColor` | 阴影半径和颜色 |
| `translucentBackground` | 半透明背景 |
| `enableBlurWindow` | 窗口模糊效果 |

### 设置圆角和阴影

```cpp
handle.setWindowRadius(8);
handle.setBorderWidth(1);
handle.setBorderColor(QColor(0, 0, 0, 30));
handle.setShadowRadius(20);
handle.setShadowColor(QColor(0, 0, 0, 80));
```

---

## 窗口模糊效果

```cpp
#include <DPlatformHandle>

// 矩形区域模糊
DPlatformHandle::WMBlurArea area = dMakeWMBlurArea(0, 0, 200, 100, 8, 8);
DPlatformHandle::setWindowBlurAreaByWM(window, {area});

// 路径区域模糊
QPainterPath path;
path.addRoundedRect(QRectF(0, 0, 200, 100), 8, 8);
DPlatformHandle::setWindowBlurAreaByWM(window, {path});
```

---

## 无标题栏窗口（CSD）

```cpp
// 启用客户端自绘标题栏
DPlatformHandle::setEnabledNoTitlebarForWindow(window, true);

// 检查是否启用
bool noTitlebar = DPlatformHandle::isEnabledNoTitlebar(window);
```

---

## DBlurEffectWidget 模糊控件

```cpp
#include <DBlurEffectWidget>

auto *blurWidget = new DBlurEffectWidget(parent);
blurWidget->setBlurRectXRadius(8);
blurWidget->setBlurRectYRadius(8);
blurWidget->setBlendMode(DBlurEffectWidget::BehindWindowBlend);
```

---

## 窗口动效

```cpp
// 取消动效
handle.setWindowEffects(DPlatformHandle::EffectNoShadow | 
                        DPlatformHandle::EffectNoBorder);
```

**EffectScene 枚举：** `EffectNoRadius` / `EffectNoShadow` / `EffectNoBorder` / `EffectNoStart` / `EffectNoClose`

---

## 平台判断

```cpp
#include <DGuiApplicationHelper>

bool isWayland = helper->testAttribute(DGuiApplicationHelper::IsWaylandPlatform);
bool isX11 = helper->testAttribute(DGuiApplicationHelper::IsXWindowPlatform);
```

---

## 相关文档

- [widgets-overview.md](widgets-overview.md) — DMainWindow 窗口
- [theme-system.md](theme-system.md) — 主题系统
