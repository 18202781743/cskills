# org.freedesktop.ScreenSaver 接口参考

该接口提供屏幕保护管理能力，包括空闲抑制、用户活动模拟和超时设置。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.ScreenSaver` |
| Object path | `/org/freedesktop/ScreenSaver` |
| Interface | `org.freedesktop.ScreenSaver` |
| Bus | Session |
### 抑制空闲

#### Inhibit

抑制空闲计时器，使系统不再检测是否空闲。返回一个 cookie 用于后续取消抑制。

- **输入参数**: `name`（string, 类型 `s`）：抑制空闲的程序名称；`reason`（string, 类型 `s`）：抑制原因
- **返回值**: `cookie`（uint32, 类型 `u`）：此次操作对应的 ID，用于取消抑制

```bash
gdbus call --session \
  --dest org.freedesktop.ScreenSaver \
  --object-path /org/freedesktop/ScreenSaver \
  --method org.freedesktop.ScreenSaver.Inhibit "myapp" "playing video"
```

#### UnInhibit

根据 cookie 取消对应的空闲抑制操作。

- **输入参数**: `cookie`（uint32, 类型 `u`）：Inhibit 返回的操作 ID
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.freedesktop.ScreenSaver \
  --object-path /org/freedesktop/ScreenSaver \
  --method org.freedesktop.ScreenSaver.UnInhibit 1
```

### 空闲管理

#### SimulateUserActivity

模拟用户操作，让系统处于使用状态，重新开始空闲计时器。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.freedesktop.ScreenSaver \
  --object-path /org/freedesktop/ScreenSaver \
  --method org.freedesktop.ScreenSaver.SimulateUserActivity
```

#### SetTimeout

设置空闲计时器的超时时间。

- **输入参数**: `seconds`（uint32, 类型 `u`）：超时时间，以秒为单位；`interval`（uint32, 类型 `u`）：屏保模式下背景更换的间隔时间；`blank`（bool, 类型 `b`）：是否黑屏
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.freedesktop.ScreenSaver \
  --object-path /org/freedesktop/ScreenSaver \
  --method org.freedesktop.ScreenSaver.SetTimeout 300 0 false
```

### 信号

#### IdleOn

空闲定时器超时信号，当系统在给定时间内未被使用时发出。

- **参数**: 无

```bash
gdbus monitor --session \
  --dest org.freedesktop.ScreenSaver \
  --object-path /org/freedesktop/ScreenSaver
```

#### CycleActive

空闲超时时，如果设置了壁纸切换，则发出此信号。

- **参数**: 无

#### IdleOff

空闲超时后，如果系统被使用则发出此信号，重新开始空闲计时器。

- **参数**: 无
