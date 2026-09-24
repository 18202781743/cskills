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

#### WriteEventLog

写入事件日志。

- **输入参数**: `event`（string, 类型 `s`）：事件 JSON 字符串
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.EventLog1 \
  --object-path /org/deepin/dde/EventLog1 \
  --method org.deepin.dde.EventLog1.WriteEventLog "{}"
```

