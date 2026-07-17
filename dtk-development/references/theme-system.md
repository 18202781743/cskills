# 主题系统

DTK 主题系统包含调色板（DPalette）、图标（DDciIcon）、字体和风格（Chameleon），实现 Light/Dark 双主题自动切换。

## 触发关键词

主题切换、调色板、DPalette、DGuiApplicationHelper、亮色/暗色、dci 图标、ColorSelector

---

## 三层架构

```
DGuiApplicationHelper (主题管理)
    │
    ├─ DPalette (C++ QWidget) / Palette (QML)
    │   └─ DPaletteHelper / ColorSelector (取色)
    │
    ├─ DDciIcon (图标)
    │   └─ DDciIconPalette (着色)
    │
    └─ DStyle / ChameleonStyle (绘制)
```

---

## DGuiApplicationHelper 核心 API

### 主题类型

```cpp
#include <DGuiApplicationHelper>

auto *helper = DGuiApplicationHelper::instance();

// 获取主题类型
auto type = helper->themeType();  // LightType / DarkType

// 切换主题
helper->setPaletteType(DGuiApplicationHelper::DarkType);
```

### 监听主题切换

```cpp
connect(helper, &DGuiApplicationHelper::themeTypeChanged,
        this, [](DGuiApplicationHelper::ColorType type) {
    // 刷新 UI
});
```

### 平台判断

```cpp
// Wayland / X11 / 平板
bool isWayland = helper->testAttribute(DGuiApplicationHelper::IsWaylandPlatform);
bool isTablet = helper->testAttribute(DGuiApplicationHelper::IsTableEnvironment);
```

---

## DPalette 调色板

### DTK 扩展颜色类型

| 类型 | 用途 |
|------|------|
| `ItemBackground` | 列表项背景 |
| `TextTitle` | 标题文本 |
| `TextTips` | 提示文本 |
| `TextWarning` | 警告文本 |
| `LightLively` | 推荐按钮亮色 |
| `DarkLively` | 推荐按钮暗色 |
| `FrameBorder` | 边框颜色 |
| `PlaceholderText` | 占位符 |

### 获取/设置颜色

```cpp
#include <DPalette>
#include <DPaletteHelper>

// 获取控件调色板
DPalette palette = DPaletteHelper::instance()->palette(widget);

// 获取颜色
QColor color = palette.color(DPalette::TextTitle);

// 设置颜色
palette.setColor(DPalette::TextWarning, QColor("#FF5722"));
DPaletteHelper::instance()->setPalette(widget, palette);

// 恢复默认
DPaletteHelper::instance()->resetPalette(widget);
```

---

## DPaletteHelper 控件调色板

```cpp
#include <DPaletteHelper>

auto *helper = DPaletteHelper::instance();

// 获取/设置/恢复
DPalette palette = helper->palette(widget);
helper->setPalette(widget, palette);
helper->resetPalette(widget);
```

---

## DDciIcon 图标

dci 图标内置 Light/Dark 两套资源，自动跟随主题切换。

### 加载与显示

```cpp
#include <DDciIcon>

// 从主题加载
DDciIcon icon = DDciIcon::fromTheme("icon-name");

// 获取 pixmap
auto theme = helper->themeType() == DGuiApplicationHelper::DarkType
             ? DDciIcon::Dark : DDciIcon::Light;
QPixmap pix = icon.pixmap(dpr, 32, theme, DDciIcon::Normal);

// 在按钮中使用
button->setIcon(icon);
```

### 图标状态

`DDciIcon::Normal` / `Disabled` / `Hover` / `Pressed`

### 调色板着色

```cpp
#include <DDciIconPalette>

DDciIconPalette iconPalette;
iconPalette.setForeground(QColor("#FF5722"));
icon.pixmap(dpr, 32, theme, DDciIcon::Normal, iconPalette);
```

---

## QML 主题系统

### D.DTK 全局对象

```qml
import org.deepin.dtk 1.0 as D

// 当前主题
D.DTK.themeType  // LightType / DarkType

// 调色板
D.DTK.palette

// 图标调色板
D.DTK.makeIconPalette(palette)
```

### Palette + ColorSelector

```qml
D.Button {
    property D.Palette backgroundColor: D.Palette {
        normal: "#ffffff"
        hovered: "#f0f0f0"
        normalDark: "#303030"  // 暗色版本
        hoveredDark: "#404040"
    }
    
    background: Rectangle {
        color: backgroundColor.D.ColorSelector.color
    }
}
```

**Palette 属性：** `normal` / `hovered` / `pressed` / `disabled`（每个支持 `Dark` 后缀）

---

## DStyle 标准图标

```cpp
#include <DStyle>

// 获取标准图标
QIcon icon = DStyle::standardIcon(DStyle::SP_CloseButton, nullptr, widget);

// 常用枚举
DStyle::SP_CloseButton
DStyle::SP_IncreaseElement
DStyle::SP_DecreaseElement
DStyle::SP_DeleteButton
DStyle::SP_ArrowEnter
```

---

## 常见错误

| 错误 | 正确做法 |
|------|----------|
| 硬编码颜色值 | 使用 `DPalette` / `Palette` |
| 监听控件调色板变化 | 使用 `DPaletteHelper::paletteChanged` |
| 图标不跟随主题 | 使用 `DDciIcon` |

---

## 相关文档

- [widgets-overview.md](widgets-overview.md) — 控件颜色定制
- [declarative-overview.md](declarative-overview.md) — QML ColorSelector

---

## 详细参考

| 文档 | 内容 |
|------|------|
| [theme-palette.md](theme-palette.md) | DPalette/DPaletteHelper 完整 API |
| [theme-dci.md](theme-dci.md) | DDciIcon 图标格式与动画 |
| [theme-chameleon.md](theme-chameleon.md) | QWidget/QML Chameleon 风格 |
