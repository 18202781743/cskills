# 输入控件规范

## 1. 概述与适用场景

DTK 提供多种输入控件，按数据类型选择：

| 控件 | 适用场景 | 特殊功能 |
|------|----------|----------|
| `DLineEdit` | 单行文本输入 | 警告提示、左右扩展 |
| `DSearchEdit` | 搜索输入 | 清除按钮、搜索图标 |
| `DPasswordEdit` | 密码输入 | 显示/隐藏密码 |
| `DTextEdit` | 多行文本输入 | — |
| `DSpinBox` | 整数输入 | 增减按钮 |
| `DDoubleSpinBox` | 浮点数输入 | 增减按钮 |
| `DComboBox` | 下拉选择 | 可编辑、搜索 |
| `DKeySequenceEdit` | 快捷键输入 | 按键录制 |

## 2. 各控件用法

### 2.1 DLineEdit — 单行输入

```cpp
#include <DLineEdit>

auto *edit = new DLineEdit(this);
edit->setPlaceholderText("请输入用户名");

// 设置警告
edit->setAlert(true);
edit->showAlertMessage("用户名不能为空");

// 清除警告
edit->setAlert(false);

// 设置左右控件
auto *label = new QLabel("用户名:");
edit->setLeftWidgets({label});

auto *clearBtn = new QPushButton("清除");
edit->setRightWidgets({clearBtn});
```

### 2.2 DSearchEdit — 搜索输入

```cpp
#include <DSearchEdit>

auto *search = new DSearchEdit(this);
search->setPlaceholderText("搜索...");

connect(search, &DSearchEdit::textChanged, [](const QString &text) {
    // 执行搜索
});
```

### 2.3 DPasswordEdit — 密码输入

```cpp
#include <DPasswordEdit>

auto *pwdEdit = new DPasswordEdit(this);
pwdEdit->setPlaceholderText("请输入密码");

// 密码输入框自带显示/隐藏按钮
connect(pwdEdit, &DPasswordEdit::textChanged, [](const QString &text) {
    // 验证密码
});
```

### 2.4 DSpinBox — 数值输入

```cpp
#include <DSpinBox>

auto *spinBox = new DSpinBox(this);
spinBox->setRange(0, 100);
spinBox->setValue(50);
spinBox->setSingleStep(1);

connect(spinBox, QOverload<int>::of(&DSpinBox::valueChanged),
        [](int value) {
    qInfo() << "Value:" << value;
});
```

### 2.5 DComboBox — 下拉选择

```cpp
#include <DComboBox>

auto *combo = new DComboBox(this);
combo->addItems({"选项1", "选项2", "选项3"});

connect(combo, QOverload<int>::of(&DComboBox::currentIndexChanged),
        [](int index) {
    qInfo() << "Selected:" << index;
});
```

### 2.6 DKeySequenceEdit — 快捷键输入

```cpp
#include <DKeySequenceEdit>

auto *keyEdit = new DKeySequenceEdit(this);

connect(keyEdit, &DKeySequenceEdit::keySequenceChanged,
        [](const QKeySequence &seq) {
    qInfo() << "Shortcut:" << seq.toString();
});
```

## 3. 选择决策

```
需要输入控件？
    │
    ├─ 单行文本？
    │   ├─ 搜索？ → DSearchEdit
    │   ├─ 密码？ → DPasswordEdit
    │   └─ 通用？ → DLineEdit
    │
    ├─ 多行文本？ → DTextEdit
    │
    ├─ 数值？
    │   ├─ 整数？ → DSpinBox
    │   └─ 浮点？ → DDoubleSpinBox
    │
    ├─ 列表选择？ → DComboBox
    │
    └─ 快捷键？ → DKeySequenceEdit
```

## 4. 关键 API

### DLineEdit 警告系统

| 方法 | 说明 |
|------|------|
| `setAlert(bool)` | 设置/清除警告状态 |
| `isAlert()` | 检查是否处于警告状态 |
| `showAlertMessage(QString, duration)` | 显示警告消息（3 秒） |
| `hideAlertMessage()` | 隐藏警告消息 |

### DLineEdit 扩展

| 方法 | 说明 |
|------|------|
| `setLeftWidgets(QList<QWidget*>)` | 设置左侧控件 |
| `setRightWidgets(QList<QWidget*>)` | 设置右侧控件 |
| `setClearButtonEnabled(bool)` | 启用清除按钮 |
| `lineEdit()` | 获取内部 QLineEdit |

### DLineEdit 语音功能

| 方法 | 说明 |
|------|------|
| `setSpeechToTextEnabled(bool)` | 启用语音输入 |
| `setTextToSpeechEnabled(bool)` | 启用语音朗读 |
| `setTextToTranslateEnabled(bool)` | 启用翻译 |

## 5. 常见错误与避坑

### 错误 1：使用废弃的 DShortcutEdit

```cpp
// ❌ 错误：DShortcutEdit 已废弃
auto *edit = new DShortcutEdit(this);

// ✅ 正确：使用 DKeySequenceEdit
auto *edit = new DKeySequenceEdit(this);
```

### 错误 2：忘记清除警告状态

```cpp
// ❌ 错误：警告一直显示
if (input.isEmpty()) {
    edit->setAlert(true);
    edit->showAlertMessage("不能为空");
}
// 输入后警告仍在

// ✅ 正确：输入变化时清除警告
connect(edit->lineEdit(), &QLineEdit::textChanged, [edit]() {
    edit->setAlert(false);
});
```

### 错误 3：直接操作 QLineEdit 而非 DLineEdit

```cpp
// ❌ 错误：绕过 DLineEdit 的警告系统
edit->lineEdit()->setPlaceholderText("提示");

// ✅ 正确：使用 DLineEdit 自身方法
edit->setPlaceholderText("提示");
```

## 6. 相关文档

- [index.md](index.md) - 控件选择决策树
- [dialog.md](dialog.md) - 对话框规范（DInputDialog 用法）
