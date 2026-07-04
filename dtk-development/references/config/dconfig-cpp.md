# DConfig C++ 使用

## 1. 直接使用 DConfig

### 1.1 头文件与 CMake

```cpp
#include <DConfig>

// CMake
find_package(DtkCore REQUIRED)
target_link_libraries(your_target Dtk::Core)
```

### 1.2 基本用法

```cpp
auto *config = DConfig::create("org.deepin.myapp", "example", "", this);
if (!config->isValid()) {
    qWarning() << "DConfig is not valid";
    return;
}

// 读取
bool canExit = config->value("canExit", true).toBool();

// 写入
config->setValue("canExit", false);

// 监听变化
connect(config, &DConfig::valueChanged, [](const QString &key) {
    qInfo() << "Config changed:" << key;
});

// 重置为默认值
config->reset("canExit");

// 查询是否为默认值
config->isDefaultValue("canExit");
```

### 1.3 创建方式

```cpp
// 推荐：指定 appId
static DConfig *create(const QString &appId, const QString &name,
                       const QString &subpath = QString(),
                       QObject *parent = nullptr);

// 构造函数（无 appId，自动使用 QCoreApplication::applicationName）
explicit DConfig(const QString &name, const QString &subpath = QString(),
                 QObject *parent = nullptr);

// 应用无关配置
static DConfig *createGeneric(const QString &name,
                              const QString &subpath = QString(),
                              QObject *parent = nullptr);

// 全局设置
static void setAppId(const QString &appId);
static QThread *globalThread();
```

> **注意**：不指定 appId 时自动使用 `QCoreApplication::applicationName`，可能和预期不一致，推荐使用 `create()` 显式指定。

### 1.4 实例方法

```cpp
// 读写
QVariant value(const QString &key, const QVariant &fallback = QVariant()) const;
void setValue(const QString &key, const QVariant &value);

// 查询
QStringList keyList() const;
bool isValid() const;
bool isDefaultValue(const QString &key) const;
bool isReadOnly(const QString &key) const;

// 属性
QString name() const;
QString subpath() const;

// 重置
void reset(const QString &key);
```

### 1.5 信号

```cpp
Q_SIGNALS:
    void valueChanged(const QString &key);
```

### 1.6 带 subpath 使用

```cpp
// subpath 用于配置分层，格式以 / 开头
auto *configV1 = DConfig::create("org.deepin.myapp", "settings", "", this);
auto *configV2 = DConfig::create("org.deepin.myapp", "settings", "/v2", this);
```

## 2. dconfig2cpp：JSON 生成类型安全的 C++ 类

### 2.1 工具用法

```bash
dconfig2cpp -c MyConfig -o my_config.hpp configs/example.json
```

选项：

| 选项 | 说明 |
|------|------|
| `-c` / `--class-name` | 生成类名（默认 `dconfig_` + 文件名） |
| `-o` / `--output` | 输出头文件路径 |
| `--force-request-thread` | 强制传入 QThread 参数 |
| `--no-comment` | 不生成注释 |

### 2.2 生成类特性

- 每个配置项对应一个 `Q_PROPERTY`，类型自动推导：`bool` / `qlonglong` / `double` / `QString` / `QList<QVariant>` / `QVariantMap`
- `create(appId, subpath, parent)` / `createGeneric(subpath, parent)` 等工厂方法
- 线程安全的异步初始化（`DConfig::globalThread()`）
- `valueChanged(key, value)` 和各属性 `xxxChanged()` 信号
- `isInitializeSucceeded()` / `isInitializeFailed()` / `isInitializing()` 状态查询

### 2.3 使用生成类

```cpp
#include "my_config.hpp"

class MyWindow : public QWidget {
    MyConfig *m_cfg;
    void initConfig() {
        // 创建（异步初始化）
        m_cfg = MyConfig::create("org.deepin.myapp");

        // 连接初始化信号，receiver 为 m_cfg 自身
        connect(m_cfg, &MyConfig::configInitializeSucceed, m_cfg, [this]() {
            qInfo() << "Config ready, canExit:" << m_cfg->canExit();
        });
        connect(m_cfg, &MyConfig::configInitializeFailed, m_cfg, [this]() {
            qWarning() << "Config init failed";
        });

        // 监听属性变化
        connect(m_cfg, &MyConfig::canExitChanged, m_cfg, [this]() {
            qInfo() << "canExit changed:" << m_cfg->canExit();
        });
        connect(m_cfg, &MyConfig::valueChanged, m_cfg,
                [this](const QString &key, const QVariant &value) {
            qInfo() << key << "->" << value;
        });
    }

    void saveConfig() {
        if (!m_cfg->isInitializeSucceeded())
            return;

        // 类型安全读写
        m_cfg->setCanExit(false);

        // 重置
        m_cfg->resetCanExit();

        // 获取底层 DConfig 对象
        auto *dconfig = m_cfg->config();
    }
};
```

> **注意**：`configInitializeSucceed` 信号回调中使用 `m_cfg` 而非信号参数中的 `DConfig*` 指针。信号确保回调执行时配置已完全初始化，直接通过生成的属性读写即可。

### 2.4 CMake 集成

```cmake
find_package(DtkCore REQUIRED)

dtk_add_config_to_cpp(GENERATED_SOURCES
    ${CMAKE_SOURCE_DIR}/configs/example.json
    CLASS_NAME MyConfig
    OUTPUT_FILE_NAME my_config.hpp)
```

### 2.5 生成类状态机

```
Invalid → Initializing → Succeeded  (初始化成功)
                       → Failed     (初始化失败)
                       → Destroyed  (对象销毁)
```

- 初始化中可安全销毁对象
- 初始化完成前读取属性返回 meta 中定义的默认值
- 初始化后 `config()` 方法返回底层 `DConfig` 对象

## 3. 相关文档

- [concepts.md](concepts.md) - 核心概念
- [dconfig-dbus.md](dconfig-dbus.md) - DBus 方式
- [dconfig-debug.md](dconfig-debug.md) - 调试
