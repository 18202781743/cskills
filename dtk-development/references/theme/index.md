# 主题系统

## 1. 概述

DTK 主题系统涵盖视觉表现的各个方面：

- **图标**：dci 图标（主题感知+动画）、builtin 图标（内置资源）、icon theme 图标（XDG 标准）
- **调色板**：`DPalette` 语义化颜色、`DGuiApplicationHelper` 亮暗主题切换
- **字体**：`DFontManager` T1-T11 层级字体体系
- **控件风格**：`DStyle` / `DStyleHelper` 控件渲染与状态颜色

## 2. 快速路由

| 场景 | 参考文档 |
|------|----------|
| dci 图标完整规范 | [dci.md](dci.md) |
| builtin 图标列表与用法 | [builtin.md](builtin.md) |
| icon theme 图标（XDG） | [icontheme.md](icontheme.md) |
| 调色板（DPalette） | [palette.md](palette.md) |
| 控件风格 API 与定制 | [style.md](style.md) |
| QWidget 变色龙风格实现 | [chameleon-style.md](chameleon-style.md) |
| 监听亮暗主题切换 | [theme-switch.md](theme-switch.md) |

## 3. 主题类型

```cpp
#include <DGuiApplicationHelper>

DGuiApplicationHelper::ColorType type = DGuiApplicationHelper::instance()->themeType();

if (type == DGuiApplicationHelper::DarkType) {
    // 深色主题
} else if (type == DGuiApplicationHelper::LightType) {
    // 浅色主题
}
```

## 4. 监听主题切换

```cpp
connect(DGuiApplicationHelper::instance(),
        &DGuiApplicationHelper::themeTypeChanged,
        [](DGuiApplicationHelper::ColorType type) {
    // 刷新 UI
});
```

## 5. 图标决策树

```
需要显示图标
    │
    ├─ 需要主题切换（亮/暗）？
    │   ├─ 是 → 使用 dci 图标
    │   │       │
    │   │       ├─ 需要动画效果？
    │   │       │   ├─ 是 → dci 图标 + DDciIconPlayer
    │   │       │   └─ 否 → dci 图标（静态）
    │   │
    │   └─ 否 → 仅在 DTK 应用内使用？
    │           ├─ 是 → 使用 builtin 图标
    │           └─ 否 → 使用 icon theme 图标（兼容 XDG 规范）
```

**决策要点：**
1. **主题切换需求** → 优先 dci 图标（支持动画作为子决策）
2. **动画需求** → 使用 dci 图标 + DDciIconPlayer
3. **XDG 兼容性** → 使用 icon theme 图标
4. **DTK 内部图标** → 可用 builtin 图标

### 图标 API 速查

| 图标类型 | 类 | 头文件 | 特点 |
|----------|-----|--------|------|
| dci 图标 | `DDciIcon` | `#include <DDciIcon>` | 主题感知、支持动画、矢量格式 |
| builtin 图标 | `QIcon` + `DIconTheme::findQIcon()` | `#include <DIconTheme>` | 内置资源、无需额外文件 |
| icon theme 图标 | `QIcon::fromTheme()` | `#include <QIcon>` | XDG 标准、系统主题集成 |
| 通用辅助 | `DIconTheme` | `#include <DIconTheme>` | 图标查找、缓存管理 |

**CMake 依赖：** 详见 [app-dev-with-dtk.md](../app-dev-with-dtk.md)

```cmake
find_package(Dtk6Gui REQUIRED)
target_link_libraries(your_target Dtk6::Gui)
```

### 图标代码模板

#### dci 图标（推荐）

```cpp
#include <DDciIcon>
#include <DGuiApplicationHelper>

DDciIcon icon(":/icons/myicon.dci");
auto theme = DGuiApplicationHelper::instance()->themeType() == DGuiApplicationHelper::DarkType
             ? DDciIcon::Dark : DDciIcon::Light;
QPixmap pix = icon.pixmap(devicePixelRatio, 32, theme);
label->setPixmap(pix);
```

#### builtin 图标

```cpp
#include <DIconTheme>

QIcon icon = DIconTheme::findQIcon("dialog-ok");
button->setIcon(icon);
bool isBuiltin = DIconTheme::isBuiltinIcon(icon);
```

#### icon theme 图标

```cpp
#include <QIcon>

QIcon icon = QIcon::fromTheme("document-open");
button->setIcon(icon);
bool isXdg = DIconTheme::isXdgIcon(icon);
```

## 6. 相关文档

- [palette.md](palette.md) — 调色板规范
- [style.md](style.md) — 控件风格规范
- [theme-switch.md](theme-switch.md) — 主题切换机制
- [dci.md](dci.md) — dci 图标完整规范
- [builtin.md](builtin.md) — builtin 图标列表与用法
- [icontheme.md](icontheme.md) — icon theme 图标系统
