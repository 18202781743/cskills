# QWidget 控件概览

DTK 提供丰富的 QWidget 控件，本文档提供控件选择决策和核心 API 速查。

## 触发关键词

创建对话框/主窗口/按钮、控件选择、输入框/下拉框/开关按钮、列表视图/树形视图、进度条/滑动条/消息提示

## 控件选择决策树

```
需要什么类型的控件？
    │
    ├─ 对话框 → DDialog（简单交互）、DInputDialog（输入）、DFileDialog（文件选择）
    │
    ├─ 窗口 → DMainWindow（主窗口）、DTitlebar（标题栏）
    │
    ├─ 按钮 → 推荐样式？→ DSuggestButton
    │         警告样式？→ DWarningButton
    │         仅图标？→ DIconButton
    │         开关？→ DSwitchButton
    │         按钮组？→ DButtonBox
    │
    ├─ 输入 → DLineEdit（单行）、DSearchEdit（搜索）、DPasswordEdit（密码）
    │         DTextEdit（多行）、DSpinBox（数值）、DComboBox（下拉）
    │
    ├─ 视图 → DListView（列表）、DTreeView（树形）、DStyledItemDelegate（项委托）
    │
    └─ 其他 → DProgressBar（进度）、DSlider（滑动）、DMessageManager（消息）
```

---

## 对话框

| 控件 | 头文件 | 用途 |
|------|--------|------|
| DDialog | `<DDialog>` | 通用对话框 |
| DInputDialog | `<DInputDialog>` | 输入对话框 |
| DFileDialog | `<DFileDialog>` | 文件选择 |

### DDialog 核心 API

```cpp
#include <DDialog>

auto *dialog = new DDialog("标题", "消息", this);
dialog->addButton("确定", true, DDialog::ButtonRecommend);
dialog->addButton("删除", false, DDialog::ButtonWarning);

if (dialog->exec() == 0) { }
```

**按钮类型：** `ButtonNormal` / `ButtonRecommend`（蓝） / `ButtonWarning`（红）

### DInputDialog

```cpp
#include <DInputDialog>

QString text = DInputDialog::getText(this, "重命名", "新名称:");
int value = DInputDialog::getInt(this, "数量", "值:", 1, 1, 100);
```

---

## 窗口

### DMainWindow

```cpp
#include <DMainWindow>

class MainWindow : public DMainWindow {
public:
    MainWindow() {
        titlebar()->setTitle("应用名称");
        titlebar()->setMenu(myMenu);
        setSidebarWidget(sidebar);
    }
};
```

### DTitlebar 常用方法

| 方法 | 说明 |
|------|------|
| `setTitle(QString)` | 设置标题 |
| `setIcon(QIcon)` | 设置图标 |
| `setMenu(QMenu*)` | 设置菜单 |
| `setMenuVisible(bool)` | 显示/隐藏菜单按钮 |

---

## 按钮

| 控件 | 头文件 | 用途 |
|------|--------|------|
| DSuggestButton | `<DSuggestButton>` | 主操作（蓝） |
| DWarningButton | `<DWarningButton>` | 危险操作（红） |
| DIconButton | `<DIconButton>` | 仅图标 |
| DSwitchButton | `<DSwitchButton>` | 开关 |
| DButtonBox | `<DButtonBox>` | 按钮组 |

### DIconButton 核心 API

```cpp
#include <DIconButton>
#include <DStyle>
#include <DDciIcon>

auto *btn = new DIconButton(DStyle::SP_CloseButton, this);
btn->setIcon(DDciIcon::fromTheme("icon-name"));
btn->setFlat(true);
```

**常用 StandardPixmap：** `SP_CloseButton` / `SP_IncreaseElement` / `SP_DecreaseElement`

### 定制按钮颜色

```cpp
#include <DPaletteHelper>

DPalette palette = DPaletteHelper::instance()->palette(button);
palette.setColor(QPalette::Button, QColor("#2F6BFF"));
DPaletteHelper::instance()->setPalette(button, palette);
```

---

## 输入控件

| 控件 | 头文件 | 用途 |
|------|--------|------|
| DLineEdit | `<DLineEdit>` | 单行输入 |
| DSearchEdit | `<DSearchEdit>` | 搜索输入 |
| DPasswordEdit | `<DPasswordEdit>` | 密码输入 |
| DSpinBox | `<DSpinBox>` | 整数输入 |
| DComboBox | `<DComboBox>` | 下拉选择 |

### DLineEdit 警告状态

```cpp
edit->setAlert(true);
edit->showAlertMessage("输入无效");
```

---

## 视图控件

### DStyledItemDelegate

```cpp
#include <DStyledItemDelegate>

auto *delegate = new DStyledItemDelegate(listView);
delegate->setBackgroundType(DStyledItemDelegate::RoundedBackground);
listView->setItemDelegate(delegate);
```

**BackgroundType：** `NoBackground` / `ClipCornerBackground` / `RoundedBackground`

---

## 进度与消息

### DProgressBar / DMessageManager

```cpp
bar->setValue(50);
DMessageManager::instance()->sendMessage(widget, DFloatingMessage::ResidentType, "消息");
```

---

## 常见错误

| 错误 | 正确做法 |
|------|----------|
| `DImageButton` 已废弃 | 使用 `DIconButton` |
| `DIconButton->setText()` 不支持文字 | 使用 `DPushButton` |
| 硬编码颜色 | 使用 `DPaletteHelper` |

---

## 相关文档

- [theme-system.md](theme-system.md) — 主题、调色板、DCI 图标
- [platform-integration.md](platform-integration.md) — 窗口装饰

---

## 详细参考

| 文档 | 内容 |
|------|------|
| [widgets-button.md](widgets-button.md) | 按钮类型、DCI 图标、颜色定制 |
| [widgets-dialog.md](widgets-dialog.md) | DDialog/DInputDialog/DFileDialog |
| [widgets-input.md](widgets-input.md) | DLineEdit/DSearchEdit/DPasswordEdit |
| [widgets-window.md](widgets-window.md) | DMainWindow/DTitlebar |
| [widgets-item-delegate.md](widgets-item-delegate.md) | DStyledItemDelegate 列表项 |
| [widgets-blur-effect.md](widgets-blur-effect.md) | DBlurEffectWidget |
| [widgets-style.md](widgets-style.md) | DStyle/ChameleonStyle 自定义绘制 |
