# org.deepin.dde.WarningDialog1 接口参考

该接口为 D-Bus 激活型服务，用于警告对话框的进程单实例控制。服务本身不导出 D-Bus 方法，通过 D-Bus 服务激活机制启动 `dde-warning-dialog` 进程来显示警告对话框。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.WarningDialog1` |
| Object path | `/org/deepin/dde/WarningDialog1` |
| Interface | `org.deepin.dde.WarningDialog1` |
| Bus | Session |

### 服务激活

通过 D-Bus 服务激活机制启动警告对话框进程：

- **功能**: 通过 D-Bus 服务名激活机制启动 `dde-warning-dialog` 进程，实现警告对话框的进程单实例控制
- **触发条件**: 当系统组件尝试调用此 D-Bus 服务名时自动触发，D-Bus 守护进程根据 `.service` 文件自动启动对应进程
- **使用场景**: 系统检测到电池耗尽或磁盘空间不足严重警告条件时，通过此服务名激活警告对话框进程以显示警告窗口

```bash
gdbus call --session \
  --dest org.deepin.dde.WarningDialog1 \
  --object-path /org/deepin/dde/WarningDialog1 \
  --method org.freedesktop.DBus.Peer.Ping
```

> 该服务不导出业务方法，仅通过 D-Bus 服务名注册实现进程单实例控制。警告对话框窗口由 `dde-warning-dialog` 进程直接展示。
