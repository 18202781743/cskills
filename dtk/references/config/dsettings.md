# DSettings 详细规范

## 1. 概述

`DSettings` 是 DTK 提供的应用级配置管理，支持：
- JSON 格式配置文件
- 自动生成设置界面
- 多种控件类型

## 2. 头文件与依赖

```cpp
#include <DSettings>
#include <DSettingsDialog>
#include <DSettingsOption>
#include <DSettingsGroup>

// CMake
find_package(DtkCore REQUIRED)
find_package(DtkWidget REQUIRED)
target_link_libraries(your_target Dtk::Core Dtk::Widget)
```

## 3. JSON 配置格式

```json
{
    "groups": [
        {
            "key": "appearance",
            "name": "外观",
            "options": [
                {
                    "key": "theme",
                    "name": "主题",
                    "type": "combobox",
                    "items": ["自动", "浅色", "深色"],
                    "default": 0
                },
                {
                    "key": "font-size",
                    "name": "字体大小",
                    "type": "spinbutton",
                    "default": 12,
                    "min": 8,
                    "max": 24
                },
                {
                    "key": "auto-save",
                    "name": "自动保存",
                    "type": "checkbox",
                    "default": true
                }
            ]
        }
    ]
}
```

## 4. 代码示例

```cpp
#include <DSettings>
#include <DSettingsDialog>

// 从 JSON 文件加载设置
auto *settings = DSettings::fromJsonFile(":/settings.json");

// 读取值
bool autoSave = settings->option("appearance.auto-save")->value().toBool();

// 写入值
settings->option("appearance.auto-save")->setValue(false);

// 显示设置对话框
auto *dialog = new DSettingsDialog(settings, this);
dialog->exec();
```

## 5. 支持的控件类型

| type | 控件 |
|------|------|
| `checkbox` | 复选框 |
| `combobox` | 下拉选择 |
| `spinbutton` | 数值调节 |
| `lineedit` | 单行输入 |
| `textedit` | 多行输入 |
| `slider` | 滑动条 |
| `colorbutton` | 颜色选择 |

## 6. 相关文档

- [index.md](index.md) - 配置系统决策树
- [dconfig.md](dconfig.md) - DConfig 规范
