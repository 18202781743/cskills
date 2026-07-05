# QWidget 控件选择决策树

DTK 提供丰富的 QWidget 控件，本文档帮助您快速选择正确的控件。

## 1. 快速决策树

```
需要什么类型的控件？
    │
    ├─ 对话框 → DDialog（简单交互）、DInputDialog（输入）、DDialog（文件选择）
    │
    ├─ 窗口 → DMainWindow（主窗口）、DTitlebar（标题栏）
    │
    ├─ 按钮 → 需要推荐样式？
    │           ├─ 是 → DSuggestButton
    │           └─ 否 → 需要警告样式？
    │                     ├─ 是 → DWarningButton
    │                     └─ 否 → 仅显示图标？
    │                               ├─ 是 → DIconButton
    │                               └─ 否 → DPushButton / DToolButton
    │
    ├─ 输入 → 单行文本？
    │           ├─ 是 → 需要搜索？
    │           │         ├─ 是 → DSearchEdit
    │           │         └─ 否 → 需要密码？
    │           │                   ├─ 是 → DPasswordEdit
    │           │                   └─ 否 → DLineEdit
    │           └─ 否 → 多行文本 → DTextEdit
    │                     或 数值 → DSpinBox / DDoubleSpinBox
    │                     或 快捷键 → DKeySequenceEdit
    │
    ├─ 开关 → DSwitchButton
    │
    └─ 选择 → 下拉选择 → DComboBox
              或 多选 → DCheckBox
              或 单选 → DRadioButton
```

## 2. API 速查表

### 2.1 对话框

| 控件 | 头文件 | 用途 |
|------|--------|------|
| `DDialog` | `#include <DDialog>` | 通用对话框（按钮交互、自定义内容） |
| `DAbstractDialog` | `#include <DAbstractDialog>` | 对话框基类（自定义对话框继承） |
| `DInputDialog` | `#include <DInputDialog>` | 输入对话框 |
| `DFileDialog` | `#include <DFileDialog>` | 文件选择对话框 |
| `DAboutDialog` | `#include <DAboutDialog>` | 关于对话框 |
| `DSettingsDialog` | `#include <DSettingsDialog>` | 设置对话框（JSON 驱动，配合 DSettings 使用） |

**CMake 依赖：**
```cmake
find_package(DtkWidget REQUIRED)
target_link_libraries(your_target Dtk::Widget)
```

### 2.2 窗口

| 控件 | 头文件 | 用途 |
|------|--------|------|
| `DMainWindow` | `#include <DMainWindow>` | 主窗口（含标题栏、侧边栏） |
| `DTitlebar` | `#include <DTitlebar>` | 标题栏（菜单、按钮） |

### 2.3 按钮

| 控件 | 头文件 | 用途 |
|------|--------|------|
| `DSuggestButton` | `#include <DSuggestButton>` | 推荐按钮（主要操作） |
| `DWarningButton` | `#include <DWarningButton>` | 警告按钮（危险操作） |
| `DIconButton` | `#include <DIconButton>` | 图标按钮（仅图标） |
| `DToolButton` | `#include <DToolButton>` | 工具按钮（工具栏） |
| `DSwitchButton` | `#include <DSwitchButton>` | 开关按钮 |
| `DButtonBox` | `#include <DButtonBox>` | 按钮组（对话框底部） |
| `DFloatingButton` | `#include <DFloatingButton>` | 浮动按钮（FAB） |

### 2.4 输入

| 控件 | 头文件 | 用途 |
|------|--------|------|
| `DLineEdit` | `#include <DLineEdit>` | 单行输入 |
| `DSearchEdit` | `#include <DSearchEdit>` | 搜索输入（含清除按钮） |
| `DPasswordEdit` | `#include <DPasswordEdit>` | 密码输入（含显示/隐藏） |
| `DTextEdit` | `#include <DTextEdit>` | 多行文本输入 |
| `DSpinBox` | `#include <DSpinBox>` | 整数输入（含增减按钮） |
| `DDoubleSpinBox` | `#include <DDoubleSpinBox>` | 浮点数输入 |
| `DComboBox` | `#include <DComboBox>` | 下拉选择 |
| `DKeySequenceEdit` | `#include <DKeySequenceEdit>` | 快捷键输入 |

## 3. 代码模板

### 3.1 DDialog 通用对话框

```cpp
#include <DDialog>
#include <DSuggestButton>

auto *dialog = new DDialog(this);
dialog->setTitle("确认删除");
dialog->setMessage("此操作不可撤销，确定继续吗？");
dialog->setIcon(DIconTheme::findQIcon("icon_warning_32px"));

int okBtn = dialog->addButton("确定", true, DDialog::ButtonWarning);
int cancelBtn = dialog->addButton("取消", false, DDialog::ButtonNormal);

if (dialog->exec() == okBtn) {
    // 用户点击确定
}
```

### 3.2 DMainWindow 主窗口

```cpp
#include <DMainWindow>
#include <DTitlebar>

class MainWindow : public DMainWindow {
public:
    MainWindow() {
        titlebar()->setTitle("我的应用");
        titlebar()->setMenu(new QMenu(this));
    }
};
```

### 3.3 按钮类型选择

```cpp
#include <DSuggestButton>
#include <DWarningButton>
#include <DIconButton>
#include <DSwitchButton>

// 推荐按钮（主要操作）
auto *saveBtn = new DSuggestButton("保存", this);

// 警告按钮（危险操作）
auto *deleteBtn = new DWarningButton("删除", this);

// 图标按钮（工具栏）
auto *settingsBtn = new DIconButton(this);
settingsBtn->setIcon(DIconTheme::findQIcon("icon_ok_32px"));

// 开关按钮
auto *toggle = new DSwitchButton(this);
connect(toggle, &DSwitchButton::checkedChanged, [](bool checked) {
    qInfo() << "Toggled:" << checked;
});
```

### 3.4 DLineEdit 带警告

```cpp
#include <DLineEdit>

auto *edit = new DLineEdit(this);
edit->setPlaceholderText("请输入邮箱");

// 验证失败时显示警告
if (!isValidEmail(edit->text())) {
    edit->setAlert(true);
    edit->showAlertMessage("邮箱格式不正确");
}

// 清除警告
edit->setAlert(false);
```

## 4. 关键参数说明

### DDialog::ButtonType

| 值 | 说明 |
|----|------|
| `ButtonNormal` | 普通按钮 |
| `ButtonWarning` | 警告按钮（红色） |
| `ButtonRecommend` | 推荐按钮（蓝色） |

### DAbstractDialog::DisplayPosition

| 值 | 说明 |
|----|------|
| `Center` | 屏幕中央 |
| `TopRight` | 屏幕右上角 |

## 5. 常见错误与避坑

### 错误 1：使用废弃的控件

```cpp
// ❌ 错误：DSegmentedControl 已废弃
auto *segment = new DSegmentedControl(this);

// ✅ 正确：使用 DButtonBox
auto *buttonBox = new DButtonBox(this);
buttonBox->setButtonList({new QPushButton("选项1"), new QPushButton("选项2")});
```

### 错误 2：对话框未设置父窗口

```cpp
// ❌ 错误：对话框无父窗口，可能被遮挡
auto *dialog = new DDialog();
dialog->exec();

// ✅ 正确：设置父窗口
auto *dialog = new DDialog(this);
dialog->exec();
```

### 错误 3：忽略按钮返回值

```cpp
// ❌ 错误：忽略按钮索引
dialog->addButton("确定");
dialog->addButton("取消");
if (dialog->exec()) { /* 不确定点击了哪个按钮 */ }

// ✅ 正确：检查具体按钮索引
int okIdx = dialog->addButton("确定");
dialog->addButton("取消");
if (dialog->exec() == okIdx) { /* 点击了确定 */ }
```

## 6. 相关文档

- [dialog.md](dialog.md) — 对话框详细规范
- [window.md](window.md) — 窗口详细规范
- [button.md](button.md) — 按钮详细规范
- [input.md](input.md) — 输入控件详细规范
- [container.md](container.md) — 容器控件
- [navigation.md](navigation.md) — 导航控件
- [progress.md](progress.md) — 进度与状态
- [message.md](message.md) — 消息与通知
- [view.md](view.md) — 视图控件
