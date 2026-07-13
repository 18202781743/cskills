# DStyledItemDelegate 列表项委托

## 1. 概述与适用场景

`DStyledItemDelegate`（dtkwidget）提供 DTK 风格的列表项绘制，**使用频率 15 次**。配合 DListView/DTreeView 使用，提供圆角背景、间距、统一项大小等 DTK 样式。

`DStandardItem` 和 `DViewItemAction` 提供列表项的 DTK 扩展数据模型。

**适用场景：**
- DListView/DTreeView 的列表项样式
- 需要圆角背景的列表
- 列表项带图标/操作按钮

## 2. BackgroundType 枚举

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | `NoBackground` | 无背景 |
| 1 | `ClipCornerBackground` | 裁剪圆角背景 |
| 2 | `RoundedBackground` | 圆角背景 |
| 0x100 | `NoNormalState` | 禁用 Normal 状态 |

## 3. DStyledItemDelegate 用法

### 3.1 基本用法

```cpp
#include <DStyledItemDelegate>
#include <DListView>

auto *listView = new DListView(this);
auto *delegate = new DStyledItemDelegate(listView);
listView->setItemDelegate(delegate);
```

### 3.2 设置背景类型

```cpp
// 圆角背景（最常用）
delegate->setBackgroundType(DStyledItemDelegate::RoundedBackground);

// 裁剪圆角（首尾项圆角）
delegate->setBackgroundType(DStyledItemDelegate::ClipCornerBackground);

// 无背景
delegate->setBackgroundType(DStyledItemDelegate::NoBackground);
```

### 3.3 设置间距和大小

```cpp
delegate->setMargins(QMargins(10, 5, 10, 5));
delegate->setItemSize(QSize(300, 50));
delegate->setItemSpacing(5);
```

## 4. DStandardItem 用法

### 4.1 基本列表项

```cpp
#include <DStandardItem>

auto *item = new DStandardItem("列表项");
item->setForegroundRole(DPalette::TextTitle);
```

### 4.2 添加操作按钮

```cpp
auto *editAction = new DViewItemAction(Qt::AlignRight, QSize(16, 16), QSize(), true);
editAction->setIcon(DIconTheme::findQIcon("edit"));
editAction->setClickAreaMargins(QMargins(5, 5, 5, 5));

auto *deleteAction = new DViewItemAction(Qt::AlignRight, QSize(16, 16), QSize(), true);
deleteAction->setIcon(DIconTheme::findQIcon("delete"));

item->setActionList(Qt::RightEdge, {editAction, deleteAction});
```

### 4.3 设置 DCI 图标

```cpp
DDciIcon dciIcon = DDciIcon::fromTheme("my-icon");
item->setDciIcon(dciIcon);
```

### 4.4 设置文本颜色

```cpp
// 使用 DPalette 颜色类型
item->setTextColorRole(DPalette::TextWarning);

// 使用 QPalette 颜色角色
item->setTextColorRole(QPalette::Highlight);
```

## 5. DViewItemAction 详解

| 方法 | 说明 |
|------|------|
| `setAlignment(Qt::Alignment)` | 设置对齐方式 |
| `setIconSize(QSize)` | 设置图标大小 |
| `setMaximumSize(QSize)` | 设置最大尺寸 |
| `setClickAreaMargins(QMargins)` | 设置点击区域边距 |
| `setTextColorRole(DPalette::ColorType)` | 设置文本颜色类型 |
| `setFontSize(DFontSizeManager::SizeType)` | 设置字体大小 |
| `setClickable(bool)` | 设置是否可点击 |
| `setWidget(QWidget*)` | 设置自定义控件 |
| `setDciIcon(DDciIcon)` | 设置 DCI 图标 |

## 6. 常见错误与避坑

### 错误 1：不设置 DStyledItemDelegate

```cpp
// ❌ 错误：DListView 缺少 DTK 样式
auto *listView = new DListView(this);

// ✅ 正确：设置 DStyledItemDelegate
auto *listView = new DListView(this);
listView->setItemDelegate(new DStyledItemDelegate(listView));
```

## 7. 相关文档

- [view.md](view.md) - 视图控件
- [label.md](label.md) - DLabel
- [../theme/palette.md](../theme/palette.md) - 调色板规范
