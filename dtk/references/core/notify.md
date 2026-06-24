# 通知系统

## 1. DNotifySender

```cpp
#include <DNotifySender>

// 发送简单通知
DNotifySender::instance()->sendMessage("标题", "消息内容");

// 发送详细通知
DNotifySender::Message msg;
msg.summary = "下载完成";
msg.body = "文件已保存到 /home/user/Downloads";
msg.iconName = "dialog-ok";
msg.timeout = 5000; // 5 秒后自动关闭

DNotifySender::instance()->sendMessage(msg);

// 发送带动作的通知
msg.actions << "open" << "打开";
msg.actions << "cancel" << "取消";

connect(DNotifySender::instance(), &DNotifySender::actionInvoked,
        [](uint id, const QString &action) {
    if (action == "open") {
        // 执行打开操作
    }
});
```

## 2. 相关文档

- [index.md](index.md) - 核心工具总览
