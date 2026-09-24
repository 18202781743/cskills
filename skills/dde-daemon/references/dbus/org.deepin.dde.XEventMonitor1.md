# org.deepin.dde.XEventMonitor1 接口参考

该接口提供 X 事件区域监控能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.XEventMonitor1` |
| Object path | `/org/deepin/dde/XEventMonitor1` |
| Interface | `org.deepin.dde.XEventMonitor1` |
| Bus | Session |
### X 事件监控方法

#### RegisterArea

注册监控区域。

- **输入参数**: `x`（int32, 类型 `i`）：X 坐标；`y`（int32, 类型 `i`）：Y 坐标；`width`（int32, 类型 `i`）：宽度；`height`（int32, 类型 `i`）：高度；`flags`（int32, 类型 `i`）：标志
- **返回值**: `i`（int32）：区域 ID

```bash
gdbus call --session \
  --dest org.deepin.dde.XEventMonitor1 \
  --object-path /org/deepin/dde/XEventMonitor1 \
  --method org.deepin.dde.XEventMonitor1.RegisterArea 0 0 100 100 0
```

#### UnregisterArea

取消注册监控区域。

- **输入参数**: `id`（int32, 类型 `i`）：区域 ID
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.XEventMonitor1 \
  --object-path /org/deepin/dde/XEventMonitor1 \
  --method org.deepin.dde.XEventMonitor1.UnregisterArea 1
```

