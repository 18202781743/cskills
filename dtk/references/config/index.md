# 配置系统决策树

## 1. 概述与适用场景

DTK 提供两种配置方案：

| 方案 | 特点 | 适用场景 |
|------|------|----------|
| `DConfig` | 系统级、多进程共享、GSettings 兼容 | 系统设置、跨应用配置 |
| `DSettings` | 应用级、JSON 格式、UI 生成 | 应用设置、需要设置界面 |

## 2. 快速决策树

```
需要配置持久化？
    │
    ├─ 需要跨应用/跨进程共享？
    │   └─ 是 → DConfig
    │
    ├─ 需要系统级配置？
    │   └─ 是 → DConfig
    │
    ├─ 需要自动生成设置界面？
    │   └─ 是 → DSettings
    │
    └─ 应用内部配置？
        └─ DSettings
```

## 3. DConfig 用法

### 3.1 基本用法

```cpp
#include <DConfig>

auto *config = new DConfig("org.deepin.myapp", "myapp", this);

// 读取配置
QVariant value = config->value("key-name");

// 写入配置
config->setValue("key-name", QVariant("value"));

// 监听配置变化
connect(config, &DConfig::valueChanged, [](const QString &key) {
    qInfo() << "Config changed:" << key;
});
```

### 3.2 配置文件位置

- 系统配置：`/usr/share/dsg/appid/configs/`
- 用户配置：`~/.config/dsg/appid/configs/`

## 4. DSettings 用法

### 4.1 基本用法

```cpp
#include <DSettings>
#include <DSettingsDialog>

auto *settings = DSettings::fromJsonFile(":/settings.json");

// 读取配置
QVariant value = settings->option("group.key")->value();

// 写入配置
settings->option("group.key")->setValue(QVariant("value"));

// 显示设置对话框
auto *dialog = new DSettingsDialog(settings, this);
dialog->exec();
```

### 4.2 settings.json 格式

```json
{
    "groups": [{
        "key": "general",
        "name": "常规",
        "options": [{
            "key": "auto-start",
            "name": "开机启动",
            "type": "checkbox",
            "default": false
        }]
    }]
}
```

## 5. 相关文档

- [dconfig.md](dconfig.md) - DConfig 详细规范
- [dsettings.md](dsettings.md) - DSettings 详细规范
