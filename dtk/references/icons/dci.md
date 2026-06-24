# dci 图标规范

## 1. 概述与适用场景

**dci** (Deepin Component Icon) 是 DTK 自有的矢量图标格式，基于 `DDciFile` 封装，支持：

- **多主题**：内置 Light/Dark 两套图标，自动适配主题切换
- **多状态**：Normal/Disabled/Hover/Pressed 四种状态
- **动画**：支持逐帧动画，通过 `DDciIconPlayer` 驱动
- **调色板着色**：通过 `DDciIconPalette` 对图标前景/背景着色

**适用场景：**
- 需要跟随主题切换的图标
- 需要动画效果的图标（如加载动画）
- 需要多状态展示的图标
- DDE 应用内的自定义图标

**不适用场景：**
- 需要兼容 XDG 图标主题规范 → 使用 `DIconTheme`
- 仅需系统标准图标 → 使用 `QIcon::fromTheme`

## 2. 文件格式规范

### 2.1 目录结构

dci 图标文件在项目中的典型布局：

```
project/
├── icons/
│   └── deepin/
│       ├── light/           ← 浅色主题图标目录
│       │   └── actions/
│       │       ├── add.dci
│       │       └── remove.dci
│       └── dark/            ← 深色主题图标目录
│           └── actions/
│               ├── add.dci
│               └── remove.dci
└── CMakeLists.txt
```

### 2.2 命名规则

- 文件名使用小写字母和连字符：`my-icon-name.dci`
- 按功能分类存放：`actions/`、`status/`、`places/`、`categories/`
- 同一图标的 Light/Dark 版本必须保持同名

### 2.3 主题搜索路径

```cpp
#include <DIconTheme>

// 查看 dci 主题搜索路径
QStringList paths = DIconTheme::dciThemeSearchPaths();

// 设置自定义搜索路径
DIconTheme::setDciThemeSearchPaths({"/usr/share/icons", ":/icons"});
```

## 3. API 用法

### 3.1 加载图标

```cpp
#include <DDciIcon>

// 方式 1：从文件路径加载
DDciIcon icon("/path/to/icon.dci");

// 方式 2：从主题名称加载（需在搜索路径中）
DDciIcon icon = DDciIcon::fromTheme("my-icon-name");

// 方式 3：从主题加载，带回退
DDciIcon fallback(":/icons/default.dci");
DDciIcon icon = DDciIcon::fromTheme("my-icon-name", fallback);

// 方式 4：从二进制数据加载
DDciIcon icon(QByteArray data);
```

### 3.2 显示图标

```cpp
#include <DDciIcon>
#include <DGuiApplicationHelper>

DDciIcon icon = DDciIcon::fromTheme("my-icon");
auto theme = DGuiApplicationHelper::instance()->themeType() == DGuiApplicationHelper::DarkType
             ? DDciIcon::Dark : DDciIcon::Light;

// 获取 QPixmap
qreal dpr = widget->devicePixelRatioF();
QPixmap pix = icon.pixmap(dpr, 32, theme, DDciIcon::Normal);
label->setPixmap(pix);

// 直接绘制
QPainter painter(this);
icon.paint(&painter, rect, dpr, theme, DDciIcon::Normal);
```

### 3.3 主题切换

```cpp
// 监听主题切换信号，刷新图标
connect(DGuiApplicationHelper::instance(), &DGuiApplicationHelper::themeTypeChanged,
        this, &MyWidget::updateIcon);

void MyWidget::updateIcon() {
    auto theme = DGuiApplicationHelper::instance()->themeType() == DGuiApplicationHelper::DarkType
                 ? DDciIcon::Dark : DDciIcon::Light;
    m_pixmap = m_icon.pixmap(devicePixelRatioF(), 32, theme);
    update();
}
```

### 3.4 调色板着色

```cpp
#include <DDciIconPalette>

// 从 QPalette 创建调色板
DDciIconPalette palette = DDciIconPalette::fromQPalette(qApp->palette());

// 自定义调色板
DDciIconPalette palette(QColor("#000000"), QColor("#ffffff"),
                        QColor("#007AFF"), QColor("#ffffff"));

// 使用调色板渲染图标
QPixmap pix = icon.pixmap(dpr, 32, theme, DDciIcon::Normal, palette);
```

### 3.5 检查图标属性

```cpp
// 获取可用尺寸
QList<int> sizes = icon.availableSizes(DDciIcon::Light, DDciIcon::Normal);

// 检查是否支持调色板
bool hasPalette = icon.isSupportedAttribute(result, DDciIcon::HasPalette);

// 检查是否为空
if (icon.isNull()) { /* 加载失败 */ }
```

## 4. 完整示例

### 4.1 静态图标

```cpp
#include <DDciIcon>
#include <DGuiApplicationHelper>
#include <QLabel>

class ThemeIconLabel : public QLabel {
public:
    ThemeIconLabel(const QString &iconName, int size = 32, QWidget *parent = nullptr)
        : QLabel(parent), m_size(size) {
        m_icon = DDciIcon::fromTheme(iconName);
        refreshPixmap();
        connect(DGuiApplicationHelper::instance(), &DGuiApplicationHelper::themeTypeChanged,
                this, &ThemeIconLabel::refreshPixmap);
    }
    void refreshPixmap() {
        auto theme = DGuiApplicationHelper::instance()->themeType()
                     == DGuiApplicationHelper::DarkType ? DDciIcon::Dark : DDciIcon::Light;
        setPixmap(m_icon.pixmap(devicePixelRatioF(), m_size, theme));
    }
private:
    DDciIcon m_icon; int m_size;
};
```

### 4.2 动态图标（动画）

```cpp
#include <DDciIcon>
#include <DDciIconPlayer>
#include <DGuiApplicationHelper>
#include <QLabel>

class AnimatedIconLabel : public QLabel {
public:
    AnimatedIconLabel(const QString &iconName, int size = 32, QWidget *parent = nullptr)
        : QLabel(parent) {
        auto *player = new DDciIconPlayer(this);
        player->setIcon(DDciIcon::fromTheme(iconName));
        player->setIconSize(size);
        auto theme = DGuiApplicationHelper::instance()->themeType()
                     == DGuiApplicationHelper::DarkType ? DDciIcon::Dark : DDciIcon::Light;
        player->setTheme(theme);
        connect(player, &DDciIconPlayer::updated, this, [=]() {
            setPixmap(QPixmap::fromImage(player->currentImage()));
        });
        player->play(DDciIcon::Normal);
    }
};
```

## 5. 与 builtin/icontheme 的选择建议

| 对比项 | dci 图标 | builtin 图标 | icon theme 图标 |
|--------|----------|-------------|----------------|
| 主题切换 | ✅ 内置支持 | ✅ 内置支持 | ⚠️ 需手动处理 |
| 动画 | ✅ 支持 | ❌ 不支持 | ❌ 不支持 |
| 调色板着色 | ✅ 支持 | ❌ 不支持 | ❌ 不支持 |
| 多状态 | ✅ 4 种状态 | ❌ 2 种状态 | ❌ 2 种状态 |
| XDG 兼容 | ❌ DTK 专用 | ❌ DTK 专用 | ✅ 标准规范 |
| 图标来源 | 需提供 .dci 文件 | DTK 内置 | 系统图标主题 |
| 适用场景 | DDE 应用自定义图标 | DTK 标准 UI 图标 | 跨桌面兼容图标 |

**选择建议：**
- DDE 应用内的功能性图标 → **dci 图标**
- DTK 标准控件图标（如对话框按钮） → **builtin 图标**
- 需要兼容其他桌面环境 → **icon theme 图标**
