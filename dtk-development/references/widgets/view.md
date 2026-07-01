# 视图控件规范

## 1. 概述与适用场景

| 控件 | 适用场景 |
|------|----------|
| `DListView` | 列表视图（带 DTK 样式） |
| `DSimpleListView` | 简单列表视图 |
| `DStyledItemDelegate` | 自定义列表项绘制 |
| `DSimpleListItem` | 简单列表项基类 |

## 2. DListView 用法

### 2.1 基本列表

```cpp
#include <DListView>

auto *listView = new DListView(this);
auto *model = new QStandardItemModel(this);

for (int i = 0; i < 10; ++i) {
    auto *item = new QStandardItem(QString("项目 %1").arg(i + 1));
    model->appendRow(item);
}

listView->setModel(model);
```

### 2.2 带 DStyledItemDelegate

```cpp
#include <DListView>
#include <DStyledItemDelegate>

auto *listView = new DListView(this);
listView->setItemDelegate(new DStyledItemDelegate(this));
```

## 3. 常见错误与避坑

### 错误 1：不设置 DStyledItemDelegate

```cpp
// ⚠️ 默认 delegate 可能缺少 DTK 样式
auto *listView = new DListView(this);

// ✅ 使用 DStyledItemDelegate 获取 DTK 样式
listView->setItemDelegate(new DStyledItemDelegate(this));
```

## 4. 相关文档

- [index.md](index.md) - 控件选择决策树
