# org.deepin.dde.EventLog1 接口参考

该接口提供系统事件日志记录能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.EventLog1` |
| Object path | `/org/deepin/dde/EventLog1` |
| Interface | `org.deepin.dde.EventLog1` |
| Bus | Session |
### 事件日志方法

#### Enable

启用或禁用事件日志记录。

- **功能**：启用 GRUB2 引导菜单，开机时显示引导选择界面。
- **触发条件**：当用户在控制中心开启 GRUB2 引导菜单时调用。
- **使用场景**：控制中心引导设置开启 GRUB2 菜单。

- **输入参数**: `enable`（bool, 类型 `b`）：是否启用事件日志记录
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.EventLog1 \
  --object-path /org/deepin/dde/EventLog1 \
  --method org.deepin.dde.EventLog1.Enable true
```

#### ReportLog

上报事件日志。

- **功能**：上报日志信息。
- **触发条件**：当应用商店需要记录操作日志时调用。
- **使用场景**：应用商店操作日志记录。

- **输入参数**: `log`（string, 类型 `s`）：事件 JSON 字符串
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.EventLog1 \
  --object-path /org/deepin/dde/EventLog1 \
  --method org.deepin.dde.EventLog1.ReportLog "{}"
```
