# builtin 图标规范

## 1. 概述与适用场景

**builtin 图标**是 DTK 内置在资源文件中的图标集合，特点：

- **内置资源**：随 dtkgui/dtkwidget 打包，无需额外文件
- **主题感知**：自动适配 Light/Dark 主题
- **即用即得**：通过图标名称直接调用，无需关心路径

**适用场景：**
- DTK 应用内的标准 UI 图标
- 对话框按钮图标（确定、取消、警告等）
- 工具栏通用图标
- 需要主题切换但无需动画的图标

**不适用场景：**
- 应用特有的自定义图标 → 使用 **dci 图标**
- 需要兼容其他桌面环境 → 使用 **icon theme 图标**

## 2. 文件格式规范

builtin 图标存储在 DTK 的 Qt 资源文件中，通过图标名称引用：

```
builtin://dialog-ok        → 确定图标
builtin://dialog-cancel    → 取消图标
builtin://dialog-warning   → 警告图标
```

实际存储路径：
- 浅色主题：`:/icons/builtin/light/`
- 深色主题：`:/icons/builtin/dark/`

## 3. API 用法

### 3.1 加载图标

```cpp
#include <DIconTheme>

// 方式 1：查找图标（优先 dci → builtin → icon theme）
QIcon icon = DIconTheme::findQIcon("dialog-ok");

// 方式 2：指定回退图标
QIcon fallback = QIcon(":/custom-ok.png");
QIcon icon = DIconTheme::findQIcon("dialog-ok", fallback);

// 方式 3：带选项查找
QIcon icon = DIconTheme::findQIcon("dialog-ok", DIconTheme::IgnoreDciIcons);
```

### 3.2 检查图标类型

```cpp
#include <DIconTheme>

QIcon icon = DIconTheme::findQIcon("dialog-ok");

// 检查是否为内置图标
if (DIconTheme::isBuiltinIcon(icon)) {
    // 这是 DTK 内置图标
}

// 检查是否为 XDG 图标主题图标
if (DIconTheme::isXdgIcon(icon)) {
    // 这是系统图标主题图标
}
```

### 3.3 使用选项控制查找行为

```cpp
#include <DIconTheme>

// 不回退到 QIcon::fromTheme
QIcon icon = DIconTheme::findQIcon("my-icon", 
    DIconTheme::DontFallbackToQIconFromTheme);

// 忽略 builtin 图标，只查找 dci 和 icon theme
QIcon icon = DIconTheme::findQIcon("my-icon", 
    DIconTheme::IgnoreBuiltinIcons);

// 忽略 dci 图标，只查找 builtin 和 icon theme
QIcon icon = DIconTheme::findQIcon("my-icon", 
    DIconTheme::IgnoreDciIcons);

// 组合选项：忽略缓存和 builtin
QIcon icon = DIconTheme::findQIcon("my-icon", 
    DIconTheme::IgnoreIconCache | DIconTheme::IgnoreBuiltinIcons);
```

### 3.4 图标缓存管理

```cpp
#include <DIconTheme>

// 获取缓存实例
auto *cache = DIconTheme::cached();

// 设置最大缓存大小
cache->setMaxCost(1024 * 1024); // 1MB

// 清除缓存
cache->clear();

// 从缓存查找
QIcon icon = cache->findQIcon("dialog-ok");

// 查找 dci 图标文件路径
QString dciPath = cache->findDciIconFile("my-icon", "deepin");
```

## 4. 完整示例

### 4.1 标准按钮图标

```cpp
#include <DIconTheme>
#include <DPushButton>

// 创建带内置图标的按钮
auto *btn = new DPushButton("确定", this);
btn->setIcon(DIconTheme::findQIcon("dialog-ok"));

auto *cancelBtn = new DPushButton("取消", this);
cancelBtn->setIcon(DIconTheme::findQIcon("dialog-cancel"));
```

### 4.2 警告对话框图标

```cpp
#include <DIconTheme>
#include <DDialog>

auto *dialog = new DDialog(this);
dialog->setIcon(DIconTheme::findQIcon("dialog-warning"));
dialog->setTitle("警告");
dialog->setMessage("确定要删除此文件吗？");
dialog->exec();
```

### 4.3 工具栏图标

```cpp
#include <DIconTheme>
#include <QToolBar>

auto *toolbar = new QToolBar(this);

// 添加 builtin 图标到工具栏
auto *newAction = toolbar->addAction(DIconTheme::findQIcon("document-new"), "新建");
auto *openAction = toolbar->addAction(DIconTheme::findQIcon("document-open"), "打开");
auto *saveAction = toolbar->addAction(DIconTheme::findQIcon("document-save"), "保存");
```

## 5. 常用 builtin 图标列表

以下为常用的 builtin 图标名称：

| 图标名称 | 用途 |
|----------|------|
| `dialog-ok` | 确定/确认 |
| `dialog-cancel` | 取消 |
| `dialog-warning` | 警告 |
| `dialog-error` | 错误 |
| `dialog-information` | 信息提示 |
| `dialog-question` | 询问 |
| `document-new` | 新建文档 |
| `document-open` | 打开文档 |
| `document-save` | 保存文档 |
| `document-save-as` | 另存为 |
| `edit-copy` | 复制 |
| `edit-cut` | 剪切 |
| `edit-paste` | 粘贴 |
| `edit-delete` | 删除 |
| `edit-find` | 查找 |
| `edit-undo` | 撤销 |
| `edit-redo` | 重做 |
| `list-add` | 添加项 |
| `list-remove` | 移除项 |
| `go-previous` | 返回 |
| `go-next` | 前进 |
| `go-up` | 向上 |
| `go-down` | 向下 |
| `view-refresh` | 刷新 |
| `view-fullscreen` | 全屏 |
| `window-close` | 关闭窗口 |
| `application-exit` | 退出应用 |
| `preferences-system` | 系统设置 |
| `help-about` | 关于 |
| `help-contents` | 帮助内容 |

## 6. 与 dci/icontheme 的选择建议

| 对比项 | builtin 图标 | dci 图标 | icon theme 图标 |
|--------|-------------|----------|----------------|
| 来源 | DTK 内置 | 应用自定义 | 系统图标主题 |
| 主题切换 | ✅ 自动 | ✅ 自动 | ⚠️ 需处理 |
| 动画 | ❌ 不支持 | ✅ 支持 | ❌ 不支持 |
| 自定义 | ❌ 仅限内置 | ✅ 完全自定义 | ✅ 主题可换 |
| XDG 兼容 | ❌ DTK 专用 | ❌ DTK 专用 | ✅ 标准规范 |

**选择建议：**
- 标准 UI 图标（按钮、对话框） → **builtin 图标**
- 应用自定义图标（Logo、特色图标） → **dci 图标**
- 需要跨桌面兼容 → **icon theme 图标**
