# 日志系统

## 1. 快速初始化

dtkcore 通过 `DLogManager` 提供便捷的日志初始化。直接使用 Qt 的 `qDebug()`/`qInfo()`/`qWarning()`/`qCritical()` 宏即可。

```cpp
#include <DLogManager>

// 一行初始化
DLogManager::registerConsoleAppender();   // 输出到控制台
DLogManager::registerFileAppender();      // 输出到文件（自动路径 ~/.cache/<org>/<app>.log）
DLogManager::registerJournalAppender();   // 输出到 systemd journal

// 自定义路径和格式
DLogManager::setlogFilePath("/var/log/myapp.log");
DLogManager::setLogFormat("%{time}{yyyy-MM-dd HH:mm:ss.zzz} [%{type}] %{message}");
```

## 2. DConfig 日志规则控制

当**没有**设置 `DTK_DISABLED_LOGGING_RULES` 或 `QT_LOGGING_RULES` 环境变量时，`DLogManager` 通过 DConfig 的 `org.deepin.dtk.preference` 配置文件的 `rules` 键来控制日志级别。

### 工作原理

```
DLogManager 构造
  → 通过 DSGApplication::id() 解析 appId
  → 创建 DConfig("org.deepin.dtk.preference", appId)
  → 读取 rules 键 → QLoggingCategory::setFilterRules()
  → 监听 rulesChanged 信号，运行时变更即时生效
```

### 优先级

1. 当前 appId 的 `rules` 非默认值（管理员自定义）
2. `DTK_LOGGING_FALLBACK_APPID` 环境变量指定的 appId 的 `rules`
3. 当前 appId 的 `rules` 默认值（`*.debug=false`，即**默认禁用 debug 日志**）

### 环境变量

| 变量 | 说明 |
|------|------|
| `DTK_DISABLED_LOGGING_RULES` | 禁用 DConfig 日志规则控制 |
| `QT_LOGGING_RULES` | Qt 原生日志规则（优先级更高，设置后 DConfig 规则无效） |
| `DTK_LOGGING_FALLBACK_APPID` | 回退 appId 用于查找 DConfig 日志规则 |
| `DTK_FORCE_CONSOLE_LOGGING` | 强制启用控制台输出（即使在 systemd 下） |

### 使用 qDebug 示例

```cpp
#include <DLogManager>
#include <QDebug>

int main(int argc, char *argv[]) {
    DLogManager::registerConsoleAppender();
    DLogManager::registerFileAppender();

    qInfo() << "应用启动";
    qDebug() << "调试信息";   // 默认被 rules 禁用，需在 DConfig 或 QT_LOGGING_RULES 中开启
}
```

## 3. 相关文档

- [index.md](index.md) — 工具类索引
- [../config/index.md](../config/index.md) — DConfig 配置系统
