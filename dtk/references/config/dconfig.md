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

```cpp
// 构造
DConfig(const QString &appId, const QString &name, QObject *parent = nullptr);

// 读写
QVariant value(const QString &key) const;
void setValue(const QString &key, const QVariant &value);

// 检查
bool contains(const QString &key) const;
QStringList keyList() const;

// 重置
void reset(const QString &key);
```

## 4. 完整示例

```cpp
#include <DConfig>
#include <DApplication>

int main(int argc, char *argv[]) {
    DApplication app(argc, argv);
    
    DConfig config("org.deepin.myapp", "myapp");
    
    // 检查配置是否存在
    if (!config.contains("first-run")) {
        config.setValue("first-run", false);
        // 显示欢迎界面
    }
    
    return app.exec();
}
```

## 5. 相关文档

- [index.md](index.md) - 配置系统决策树
- [dsettings.md](dsettings.md) - DSettings 规范
