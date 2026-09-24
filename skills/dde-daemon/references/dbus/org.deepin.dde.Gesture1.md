# org.deepin.dde.Gesture1 接口参考

该接口提供触摸手势管理能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Gesture1` |
| Object path | `/org/deepin/dde/Gesture1` |
| Interface | `org.deepin.dde.Gesture1` |
| Bus | Session |
### 手势管理信号

#### TouchSinglePressGesture

单指按下手势触发。

- **参数**: `time`（int32, 类型 `i`）：时间戳；`mode`（int32, 类型 `i`）：模式
- **触发条件**: 单指按下时发出

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Gesture1 \
  --object-path /org/deepin/dde/Gesture1
```

#### TouchLongPressGesture

长按手势触发。

- **参数**: `time`（int32, 类型 `i`）：时间戳；`mode`（int32, 类型 `i`）：模式
- **触发条件**: 长按时发出

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Gesture1 \
  --object-path /org/deepin/dde/Gesture1
```

