# 通知系统

## 1. DNotifySender

`DNotifySender` 采用链式构建器模式，位于 `DUtil` 命名空间。

```cpp
#include <DNotifySender>

using namespace Dtk::Core::DUtil;

// 发送简单通知
DNotifySender("下载完成")
    .appBody("文件已保存到 /home/user/Downloads")
    .call();

// 发送带图标和超时的通知
DNotifySender("操作完成")
    .appIcon("dialog-ok")
    .appBody("所有文件已同步")
    .timeOut(5000)
    .call();

// 发送带动作的通知
DNotifySender("确认删除")
    .appBody("确定要删除此文件吗？")
    .appIcon("dialog-warning")
    .actions({"open", "打开", "cancel", "取消"})
    .timeOut(10000)
    .call();

// 指定应用名称
DNotifySender("新消息")
    .appName("myapp")
    .appBody("您有一条未读消息")
    .call();
```

## 2. 链式方法说明

| 方法 | 说明 |
|------|------|
| `DNotifySender(summary)` | 构造，传入通知标题 |
| `.appName(name)` | 设置应用名称 |
| `.appIcon(icon)` | 设置图标名称 |
| `.appBody(body)` | 设置通知正文 |
| `.replaceId(id)` | 设置替换 ID（更新已有通知） |
| `.timeOut(ms)` | 设置超时时间（毫秒） |
| `.actions(list)` | 设置动作列表（成对：id, 标签） |
| `.hints(map)` | 设置额外提示 |
| `.call()` | 发送通知，返回 `QDBusPendingCall` |

## 3. 相关文档

- [index.md](index.md) - 核心工具总览
