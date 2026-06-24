# 主题系统索引

## 1. 概述

DTK 主题系统包含：
- **调色板**：`DPalette` 语义化颜色
- **风格**：`DStyle` 控件渲染风格
- **主题切换**：`DGuiApplicationHelper` 主题管理

## 2. 快速路由

| 场景 | 参考文档 |
|------|----------|
| 获取/设置颜色 | [palette.md](palette.md) |
| 控件风格定制 | [style.md](style.md) |
| 监听主题切换 | [theme-switch.md](theme-switch.md) |

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

## 5. 相关文档

- [palette.md](palette.md) - 调色板规范
- [style.md](style.md) - 风格规范
- [theme-switch.md](theme-switch.md) - 主题切换机制
