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

- **功能**：启用或禁用事件日志记录功能。
- **触发条件**：当应用需要开启或关闭事件日志记录时调用。
- **使用场景**：系统服务管理事件日志记录开关。

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
- **触发条件**：当应用需要上报事件日志时调用。
- **使用场景**：系统应用上报操作日志和事件记录。

- **输入参数**: `log`（string, 类型 `s`）：事件 JSON 字符串
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.EventLog1 \
  --object-path /org/deepin/dde/EventLog1 \
  --method org.deepin.dde.EventLog1.ReportLog "{}"
```
