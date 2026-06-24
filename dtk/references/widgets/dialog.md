# 对话框规范

## 1. 概述与适用场景

DTK 提供多种对话框控件，适用于不同交互场景：

| 控件 | 适用场景 |
|------|----------|
| `DDialog` | 通用对话框（确认、警告、自定义内容） |
| `DInputDialog` | 快速获取用户输入 |
| `DFileDialog` | 文件/目录选择 |
| `DAboutDialog` | 应用关于信息 |
| `DAbstractDialog` | 自定义对话框基类 |

**不适用场景：**
- 简单的消息提示 → 使用 `DMessageManager` + `DFloatingMessage`
- 右上角通知 → 使用系统通知

## 2. DDialog 核心用法

### 2.1 基本对话框

```cpp
#include <DDialog>

auto *dialog = new DDialog(this);
dialog->setTitle("提示");
dialog->setMessage("操作已完成");
dialog->addButton("确定", true); // true = 默认按钮
dialog->exec();
```

### 2.2 带按钮交互

```cpp
#include <DDialog>
#include <DIconTheme>

auto *dialog = new DDialog("确认删除", "此操作不可撤销", this);
dialog->setIcon(DIconTheme::findQIcon("icon_warning_32px"));

int deleteBtn = dialog->addButton("删除", false, DDialog::ButtonWarning);
int cancelBtn = dialog->addButton("取消", true, DDialog::ButtonNormal);

connect(dialog, &DDialog::buttonClicked, [deleteBtn](int index, const QString &) {
    if (index == deleteBtn) {
        // 执行删除
    }
});

dialog->exec();
```

### 2.3 自定义内容

```cpp
#include <DDialog>
#include <DLineEdit>

auto *dialog = new DDialog(this);
dialog->setTitle("输入名称");

auto *input = new DLineEdit(dialog);
input->setPlaceholderText("请输入...");
dialog->addContent(input);

int okBtn = dialog->addButton("确定", true, DDialog::ButtonRecommend);
dialog->addButton("取消");

if (dialog->exec() == okBtn) {
    QString name = input->text();
}
```

### 2.4 按钮类型

```cpp
// 普通按钮
dialog->addButton("取消", false, DDialog::ButtonNormal);

// 推荐按钮（蓝色高亮）
dialog->addButton("保存", true, DDialog::ButtonRecommend);

// 警告按钮（红色）
dialog->addButton("删除", false, DDialog::ButtonWarning);
```

## 3. DInputDialog 用法

```cpp
#include <DInputDialog>

bool ok;
QString text = DInputDialog::getText(this, "重命名", "输入新名称:",
                                      QLineEdit::Normal, "", &ok);
if (ok && !text.isEmpty()) {
    // 使用输入值
}

int value = DInputDialog::getInt(this, "设置数量", "数量:", 
                                  1, 1, 100, 1, &ok);
```

## 4. DFileDialog 用法

```cpp
#include <DFileDialog>

// 选择单个文件
QString file = DFileDialog::getOpenFileName(this, "打开文件",
                                             "/home", "文本文件 (*.txt)");

// 选择多个文件
QStringList files = DFileDialog::getOpenFileNames(this, "打开文件");

// 选择目录
QString dir = DFileDialog::getExistingDirectory(this, "选择目录");

// 保存文件
QString saveFile = DFileDialog::getSaveFileName(this, "保存文件");
```

## 5. DAbstractDialog 自定义对话框

```cpp
#include <DAbstractDialog>

class CustomDialog : public DAbstractDialog {
public:
    CustomDialog(QWidget *parent = nullptr) : DAbstractDialog(parent) {
        setFixedSize(400, 300);
        setDisplayPosition(DAbstractDialog::Center);
        
        // 添加自定义内容
        auto *layout = new QVBoxLayout(this);
        layout->addWidget(new QLabel("自定义内容"));
    }
};
```

## 6. 关键 API

### DDialog 常用方法

| 方法 | 说明 |
|------|------|
| `setTitle(QString)` | 设置标题 |
| `setMessage(QString)` | 设置消息 |
| `setIcon(QIcon)` | 设置图标 |
| `addButton(text, isDefault, type)` | 添加按钮，返回索引 |
| `insertButton(index, text, isDefault, type)` | 在指定位置插入按钮 |
| `addContent(QWidget*)` | 添加自定义内容 |
| `setOnButtonClickedClose(bool)` | 点击按钮后是否关闭 |
| `exec()` | 模态执行，返回点击的按钮索引 |

### DAbstractDialog 显示位置

| 枚举值 | 说明 |
|--------|------|
| `Center` | 屏幕中央 |
| `TopRight` | 屏幕右上角 |

## 7. 常见错误与避坑

### 错误 1：使用废弃的 setIconPixmap

```cpp
// ❌ 错误：setIconPixmap 已废弃
dialog->setIconPixmap(pixmap);

// ✅ 正确：使用 setIcon
dialog->setIcon(QIcon(pixmap));
```

### 错误 2：未处理关闭信号

```cpp
// ❌ 错误：用户点击关闭按钮未处理
dialog->exec();

// ✅ 正确：检查 aboutToClose 或 closed
connect(dialog, &DDialog::closed, this, &MyClass::onDialogClosed);
```

## 8. 相关文档

- [index.md](index.md) - 控件选择决策树
- [window.md](window.md) - 窗口规范
