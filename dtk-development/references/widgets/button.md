# 按钮规范

## 1. 概述与适用场景

DTK 提供多种按钮控件，按场景选择：

| 控件 | 适用场景 | 视觉风格 |
|------|----------|----------|
| `DSuggestButton` | 主要操作（保存、确认） | 蓝色高亮 |
| `DWarningButton` | 危险操作（删除、重置） | 红色高亮 |
| `DIconButton` | 图标按钮（工具栏图标） | 仅图标 |
| `DToolButton` | 工具栏按钮（图标+文字） | 扁平 |
| `DSwitchButton` | 开关切换 | 滑动开关 |
| `DButtonBox` | 对话框底部按钮组 | 标准布局 |
| `DFloatingButton` | 浮动操作按钮 | 圆形悬浮 |

## 2. 各控件用法

### 2.1 DSuggestButton — 推荐按钮

用于界面主要操作，视觉上最突出。

```cpp
#include <DSuggestButton>

auto *saveBtn = new DSuggestButton("保存", this);
connect(saveBtn, &DSuggestButton::clicked, this, &MyClass::save);
```

### 2.2 DWarningButton — 警告按钮

用于危险操作，红色视觉提示。

```cpp
#include <DWarningButton>

auto *deleteBtn = new DWarningButton("删除", this);
connect(deleteBtn, &DWarningButton::clicked, this, &MyClass::remove);
```

### 2.3 DIconButton — 图标按钮

仅显示图标，支持 `QIcon`、`DDciIcon`、`DStyle::StandardPixmap`。

```cpp
#include <DIconButton>
#include <DStyle>
#include <DDciIcon>

// 使用 DStyle 标准图标
auto *closeBtn = new DIconButton(DStyle::SP_CloseButton, this);

// 使用 DDciIcon（构造函数直接传入）
DDciIcon icon = DDciIcon::fromTheme("my-action-icon");
auto *actionBtn = new DIconButton(icon, this);

// 使用 QIcon
auto *btn = new DIconButton(this);
btn->setIcon(DIconTheme::findQIcon("icon_ok_32px"));

// 使用 DDciIcon（通过 setIcon 设置）
DDciIcon dciIcon(":/icons/custom.dci");
auto *dciBtn = new DIconButton(this);
dciBtn->setIcon(dciIcon);

// 获取当前 dci 图标
DDciIcon currentIcon = dciBtn->dciIcon();

// 扁平模式（无边框）
btn->setFlat(true);
```

### 2.4 DSwitchButton — 开关按钮

用于布尔值切换。

```cpp
#include <DSwitchButton>

auto *toggle = new DSwitchButton(this);
toggle->setChecked(true);

connect(toggle, &DSwitchButton::checkedChanged, [](bool checked) {
    qInfo() << "Switch:" << checked;
});
```

### 2.5 DButtonBox — 按钮组

用于对话框底部的标准按钮布局。

```cpp
#include <DButtonBox>
#include <DSuggestButton>

auto *buttonBox = new DButtonBox(this);

auto *okBtn = new DSuggestButton("确定");
auto *cancelBtn = new QPushButton("取消");

buttonBox->setButtonList({cancelBtn, okBtn}, false);
```

### 2.6 DFloatingButton — 浮动按钮

悬浮在界面上的操作按钮。

```cpp
#include <DFloatingButton>
#include <DStyle>

auto *fab = new DFloatingButton(DStyle::SP_IncreaseElement, this);
fab->move(300, 400);
connect(fab, &DFloatingButton::clicked, this, &MyClass::addItem);
```

## 3. 选择决策

```
需要按钮？
    │
    ├─ 只有一个主要操作？
    │   └─ 是 → DSuggestButton
    │
    ├─ 操作有破坏性？
    │   └─ 是 → DWarningButton
    │
    ├─ 只需显示图标？
    │   └─ 是 → DIconButton
    │
    ├─ 需要开关切换？
    │   └─ 是 → DSwitchButton
    │
    ├─ 对话框底部？
    │   └─ 是 → DButtonBox
    │
    └─ 浮动操作？
        └─ 是 → DFloatingButton
```

## 4. 关键参数

### DIconButton 特殊功能

| 方法 | 说明 |
|------|------|
| `setIcon(QIcon)` | 设置图标 |
| `setIcon(DStyle::StandardPixmap)` | 设置标准图标 |
| `setIcon(DDciIcon)` | 设置 dci 图标 |
| `setFlat(bool)` | 扁平模式（无边框） |
| `setEnabledCircle(bool)` | 启用圆形背景 |

### DStyle::StandardPixmap 常用图标

| 枚举值 | 说明 |
|--------|------|
| `SP_CloseButton` | 关闭按钮 |
| `SP_IncreaseElement` | 增加（+） |
| `SP_DecreaseElement` | 减少（-） |
| `SP_MarkElement` | 对勾 |
| `SP_DeleteButton` | 删除按钮 |
| `SP_AddButton` | 新增按钮 |
| `SP_ArrowEnter` | 进入箭头 |
| `SP_ArrowLeave` | 离开箭头 |

## 5. 常见错误与避坑

### 错误 1：使用废弃的 DImageButton

```cpp
// ❌ 错误：DImageButton 已废弃
auto *btn = new DImageButton(this);

// ✅ 正确：使用 DIconButton
auto *btn = new DIconButton(this);
btn->setIcon(QIcon(":/icon.png"));
```

### 错误 2：在 DIconButton 上设置文字

```cpp
// ❌ 错误：DIconButton 不支持文字
btn->setText("文字");

// ✅ 正确：使用 DPushButton 或 DToolButton
auto *btn = new DToolButton(this);
btn->setText("文字");
btn->setIcon(QIcon(":/icon.png"));
```

## 6. 相关文档

- [index.md](index.md) - 控件选择决策树
- [dialog.md](dialog.md) - 对话框规范（DButtonBox 用法）
