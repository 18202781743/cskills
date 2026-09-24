# org.deepin.dde.Gesture1 接口参考

该接口提供触摸手势管理能力，包括手势输入忽略设置和手势事件信号。该服务在 System 总线上导出。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Gesture1` |
| Object path | `/org/deepin/dde/Gesture1` |
| Interface | `org.deepin.dde.Gesture1` |
| Bus | System |

### 手势管理方法

#### SetEdgeMoveStopDuration

设置边缘移动停止的持续时间。

- **输入参数**: `duration`（int32, 类型 `i`）：持续时间
- **返回值**: 无

```bash
gdbus call --system \
  --dest org.deepin.dde.Gesture1 \
  --object-path /org/deepin/dde/Gesture1 \
  --method org.deepin.dde.Gesture1.SetEdgeMoveStopDuration 500
```

#### SetInputIgnore

设置指定输入节点是否忽略手势。

- **输入参数**:
  - `node`（string, 类型 `s`）：输入节点名称
  - `isIgnore`（bool, 类型 `b`）：是否忽略
- **返回值**: 无

```bash
gdbus call --system \
  --dest org.deepin.dde.Gesture1 \
  --object-path /org/deepin/dde/Gesture1 \
  --method org.deepin.dde.Gesture1.SetInputIgnore "/dev/input/event0" true
```

#### SetShortPressDuration

设置短按持续时间。

- **输入参数**: `duration`（int32, 类型 `i`）：持续时间
- **返回值**: 无

```bash
gdbus call --system \
  --dest org.deepin.dde.Gesture1 \
  --object-path /org/deepin/dde/Gesture1 \
  --method org.deepin.dde.Gesture1.SetShortPressDuration 300
```

### 手势事件信号

以下信号由 `org.deepin.dde.Gesture1` 接口发出，通过 `gdbus monitor` 监听。

```bash
gdbus monitor --system \
  --dest org.deepin.dde.Gesture1 \
  --object-path /org/deepin/dde/Gesture1
```

#### Event

手势事件。

- **参数**: `name`（string, 类型 `s`）：手势名称；`direction`（string, 类型 `s`）：方向；`fingers`（int32, 类型 `i`）：手指数

#### SwipeMoving

滑动移动中。

- **参数**: `fingers`（int32, 类型 `i`）：手指数；`accelX`（double, 类型 `d`）：X 轴加速度；`accelY`（double, 类型 `d`）：Y 轴加速度

#### SwipeStop

滑动停止。

- **参数**: `fingers`（int32, 类型 `i`）：手指数

#### TouchEdgeEvent

触摸边缘事件。

- **参数**: `direction`（string, 类型 `s`）：方向；`scaleX`（double, 类型 `d`）：X 坐标；`scaleY`（double, 类型 `d`）：Y 坐标

#### TouchMovementEvent

触摸移动事件。

- **参数**: `direction`（string, 类型 `s`）：方向；`fingers`（int32, 类型 `i`）：手指数；`startScaleX`（double, 类型 `d`）：起始 X；`startScaleY`（double, 类型 `d`）：起始 Y；`endScaleX`（double, 类型 `d`）：结束 X；`endScaleY`（double, 类型 `d`）：结束 Y

#### TouchMoving

触摸移动中。

- **参数**: `scalex`（double, 类型 `d`）：X 坐标；`scaley`（double, 类型 `d`）：Y 坐标

#### TouchSinglePressTimeout

触摸单指按下超时。

- **参数**: `time`（int32, 类型 `i`）：时间戳；`scaleX`（double, 类型 `d`）：X 坐标；`scaleY`（double, 类型 `d`）：Y 坐标

#### TouchPressTimeout

触摸按下超时。

- **参数**: `fingers`（int32, 类型 `i`）：手指数；`time`（int32, 类型 `i`）：时间戳；`scaleX`（double, 类型 `d`）：X 坐标；`scaleY`（double, 类型 `d`）：Y 坐标

#### TouchUpOrCancel

触摸抬起或取消。

- **参数**: `scaleX`（double, 类型 `d`）：X 坐标；`scaleY`（double, 类型 `d`）：Y 坐标

#### TouchEdgeMoveStop

触摸边缘移动停止。

- **参数**: `direction`（string, 类型 `s`）：方向；`scaleX`（double, 类型 `d`）：X 坐标；`scaleY`（double, 类型 `d`）：Y 坐标；`duration`（int32, 类型 `i`）：持续时间

#### TouchEdgeMoveStopLeave

触摸边缘移动停止并离开。

- **参数**: `direction`（string, 类型 `s`）：方向；`scaleX`（double, 类型 `d`）：X 坐标；`scaleY`（double, 类型 `d`）：Y 坐标；`duration`（int32, 类型 `i`）：持续时间

#### DbclickDown

双击按下。

- **参数**: `fingers`（int32, 类型 `i`）：手指数

#### KeyboardEvent

键盘事件。

- **参数**: `key`（uint32, 类型 `u`）：按键码；`state`（uint32, 类型 `u`）：状态

#### MouseEvent

鼠标事件。

- **参数**: `state`（uint32, 类型 `u`）：状态；`value`（uint32, 类型 `u`）：值
