# DConfig 详细规范

## 1. 概述

`DConfig` 是 DTK 提供的系统级配置管理，支持：
- 多进程共享配置
- GSettings 兼容
- 实时同步

## 2. 头文件与依赖

```cpp
#include <DConfig>

// CMake
find_package(DtkCore REQUIRED)
target_link_libraries(your_target Dtk::Core)
```

## 3. 基本 API

### 3.1 创建方式

```cpp
// 推荐：静态方法创建（需要 appId）
DConfig *DConfig::create(const QString &appId, const QString &name,
                          const QString &subpath = QString(),
                          QObject *parent = nullptr);

// 构造函数创建（仅 name，无 appId）
explicit DConfig(const QString &name, const QString &subpath = QString(),
                 QObject *parent = nullptr);

// 通用配置（无 appId）
static DConfig *createGeneric(const QString &name, const QString &subpath = QString(),
                               QObject *parent = nullptr);
```

### 3.2 读写与查询

```cpp
// 读写
QVariant value(const QString &key, const QVariant &fallback = QVariant()) const;
void setValue(const QString &key, const QVariant &value);

// 查询
QStringList keyList() const;
bool isValid() const;
bool isDefaultValue(const QString &key) const;
bool isReadOnly(const QString &key) const;

// 重置
void reset(const QString &key);
```

## 4. 完整示例

### 4.1 使用静态方法创建（推荐）

```cpp
#include <DConfig>

auto *config = DConfig::create("org.deepin.myapp", "myapp", "", this);
if (!config->isValid()) {
    qWarning() << "DConfig is not valid";
    return;
}

// 读取配置
bool firstRun = config->value("first-run", true).toBool();

// 写入配置
config->setValue("first-run", false);

// 监听配置变化
connect(config, &DConfig::valueChanged, [](const QString &key) {
    qInfo() << "Config changed:" << key;
});
```

### 4.2 使用构造函数创建

```cpp
#include <DConfig>

auto *config = new DConfig("myapp", "", this);

QVariant value = config->value("key-name");
config->setValue("key-name", QVariant("value"));
```

## 5. 相关文档

- [index.md](index.md) - 配置系统决策树
- [dsettings.md](dsettings.md) - DSettings 规范
