# 核心工具

dtkcore 提供日志、文件系统、DBus、通知等核心工具。

## 按需查阅

| 分类 | 文档 | 内容 |
|------|------|------|
| 日志 | [log.md](log.md) | DLogManager 快速初始化、DConfig 日志规则控制 |
| 工具 | [util.md](util.md) | 文件系统、DBus、通知系统 |
| 单实例 | [singleton.md](singleton.md) | 单实例应用、进程间通信、窗口激活 |

## CMake 依赖

```cmake
find_package(DtkCore REQUIRED)
target_link_libraries(your_target Dtk::Core)
```

DtkCore 自动引入 dtklog 依赖。
