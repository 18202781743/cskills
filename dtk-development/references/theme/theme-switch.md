# 主题切换机制

## 1. 监听主题变化

```cpp
#include <DGuiApplicationHelper>

// 监听主题类型变化
connect(DGuiApplicationHelper::instance(), 
        &DGuiApplicationHelper::themeTypeChanged,
        this, &MyWidget::onThemeChanged);

// 监听调色板变化
connect(DGuiApplicationHelper::instance(),
        &DGuiApplicationHelper::applicationPaletteChanged,
        this, &MyWidget::onPaletteChanged);
```

## 2. 响应主题切换

```cpp
void MyWidget::onThemeChanged(DGuiApplicationHelper::ColorType type) {
    // 刷新图标
    if (type == DGuiApplicationHelper::DarkType) {
        m_icon = DDciIcon::Dark;
    } else {
        m_icon = DDciIcon::Light;
    }
    update();
}
```

## 3. 手动切换主题

```cpp
#include <DGuiApplicationHelper>

// 切换到深色主题
DGuiApplicationHelper::instance()->setPaletteType(DGuiApplicationHelper::DarkType);

// 切换到浅色主题
DGuiApplicationHelper::instance()->setPaletteType(DGuiApplicationHelper::LightType);
```

## 4. 相关文档

- [palette.md](palette.md) - 调色板规范
- [Widget 控件风格](../widgets/style.md) - 风格规范
