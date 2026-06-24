# 图标系统决策树

DTK 提供三种图标方案：**dci 图标**、**builtin 图标**、**icon theme 图标**。本文档帮助您快速选择正确的方案。

## 1. 快速决策树

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

## 2. API 速查表

| 图标类型 | 类 | 头文件 | 特点 |
|----------|-----|--------|------|
| dci 图标 | `DDciIcon` | `#include <DDciIcon>` | 主题感知、支持动画、矢量格式 |
| builtin 图标 | `QIcon` + `DIconTheme::findQIcon()` | `#include <DIconTheme>` | 内置资源、无需额外文件 |
| icon theme 图标 | `QIcon::fromTheme()` | `#include <QIcon>` | XDG 标准、系统主题集成 |
| 通用辅助 | `DIconTheme` | `#include <DIconTheme>` | 图标查找、缓存管理 |

**CMake 依赖：**
```cmake
find_package(DtkGui REQUIRED)
target_link_libraries(your_target Dtk::Gui)
```

## 3. 代码模板

### 3.1 dci 图标（推荐）

```cpp
#include <DDciIcon>
#include <DGuiApplicationHelper>

// 加载 dci 图标
DDciIcon icon(":/icons/myicon.dci");

// 获取当前主题
auto theme = DGuiApplicationHelper::instance()->themeType() == DGuiApplicationHelper::DarkType
             ? DDciIcon::Dark : DDciIcon::Light;

// 绘制到指定尺寸
QPixmap pix = icon.pixmap(devicePixelRatio, 32, theme);
label->setPixmap(pix);
```

### 3.2 builtin 图标

```cpp
#include <DIconTheme>

// 查找内置图标
QIcon icon = DIconTheme::findQIcon("dialog-ok");
button->setIcon(icon);

// 检查是否为内置图标
bool isBuiltin = DIconTheme::isBuiltinIcon(icon);
```

### 3.3 icon theme 图标

```cpp
#include <QIcon>

// 使用系统图标主题
QIcon icon = QIcon::fromTheme("document-open");
button->setIcon(icon);

// 检查是否为 XDG 图标
bool isXdg = DIconTheme::isXdgIcon(icon);
```

## 4. 关键参数说明

### DDciIcon::Theme

| 值 | 说明 |
|----|------|
| `Light` | 浅色主题图标 |
| `Dark` | 深色主题图标 |

### DDciIcon::Mode

| 值 | 说明 |
|----|------|
| `Normal` | 正常状态 |
| `Disabled` | 禁用状态（灰显） |
| `Hover` | 悬停状态 |
| `Pressed` | 按下状态 |

### DIconTheme::Options

| 标志 | 说明 |
|------|------|
| `DontFallbackToQIconFromTheme` | 不回退到 QIcon::fromTheme |
| `IgnoreBuiltinIcons` | 忽略 builtin 图标 |
| `IgnoreDciIcons` | 忽略 dci 图标 |
| `IgnoreIconCache` | 忽略图标缓存 |

## 5. 常见错误与避坑

### 错误 1：忽略主题切换

```cpp
// ❌ 错误：硬编码主题
DDciIcon icon(":/icon.dci");
pixmap = icon.pixmap(1.0, 32, DDciIcon::Light); // 始终使用浅色

// ✅ 正确：根据当前主题动态选择
auto theme = DGuiApplicationHelper::instance()->themeType() == DGuiApplicationHelper::DarkType
             ? DDciIcon::Dark : DDciIcon::Light;
pixmap = icon.pixmap(1.0, 32, theme);
```

### 错误 2：未处理 devicePixelRatio

```cpp
// ❌ 错误：忽略高 DPI
pixmap = icon.pixmap(1.0, 32, theme); // 固定 DPR=1.0

// ✅ 正确：使用实际 DPR
qreal dpr = widget->devicePixelRatioF();
pixmap = icon.pixmap(dpr, 32, theme);
```

### 错误 3：动画图标未使用 Player

```cpp
// ❌ 错误：手动管理动画帧
while (!image.atEnd()) { /* ... */ }

// ✅ 正确：使用 DDciIconPlayer
DDciIconPlayer player;
player.setIcon(icon);
player.setIconSize(32);
connect(&player, &DDciIconPlayer::updated, [=]() {
    label->setPixmap(QPixmap::fromImage(player.currentImage()));
});
player.play(DDciIcon::Normal);
```

## 6. 相关文档

- [dci.md](dci.md) - dci 图标完整规范
- [builtin.md](builtin.md) - builtin 图标列表与用法
- [icontheme.md](icontheme.md) - 图标主题系统
- [../theming/palette.md](../theming/palette.md) - 调色板与主题配色
