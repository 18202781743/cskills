# org.deepin.dde.BlackScreen1 接口参考

该接口提供黑屏显示控制能力，包括黑屏窗口的显示、隐藏、退出和抓取设备释放。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.BlackScreen1` |
| Object path | `/org/deepin/dde/BlackScreen1` |
| Interface | `org.deepin.dde.BlackScreen1` |
| Bus | Session |

### Raise

将黑屏窗口提升到最前层。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.BlackScreen1 \
  --object-path /org/deepin/dde/BlackScreen1 \
  --method org.deepin.dde.BlackScreen1.Raise
```

### Quit

退出黑屏程序。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.BlackScreen1 \
  --object-path /org/deepin/dde/BlackScreen1 \
  --method org.deepin.dde.BlackScreen1.Quit
```

### setActive

设置黑屏窗口的显示或隐藏状态。

- **输入参数**: `visible`（bool, 类型 `b`）：是否显示黑屏
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.BlackScreen1 \
  --object-path /org/deepin/dde/BlackScreen1 \
  --method org.deepin.dde.BlackScreen1.setActive true
```

### quitDBusService

注销 D-Bus 服务并退出黑屏程序。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.BlackScreen1 \
  --object-path /org/deepin/dde/BlackScreen1 \
  --method org.deepin.dde.BlackScreen1.quitDBusService
```

### blackScreenVisible

查询黑屏是否正在显示。

- **输入参数**: 无
- **返回值**: `b`（bool）：黑屏是否可见

```bash
gdbus call --session \
  --dest org.deepin.dde.BlackScreen1 \
  --object-path /org/deepin/dde/BlackScreen1 \
  --method org.deepin.dde.BlackScreen1.blackScreenVisible
```

### releaseGrabDevices

释放黑屏程序抓取的键盘和鼠标设备。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.BlackScreen1 \
  --object-path /org/deepin/dde/BlackScreen1 \
  --method org.deepin.dde.BlackScreen1.releaseGrabDevices
```

### releaseGrabDevicesHideBlack

释放抓取设备并隐藏黑屏窗口。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.BlackScreen1 \
  --object-path /org/deepin/dde/BlackScreen1 \
  --method org.deepin.dde.BlackScreen1.releaseGrabDevicesHideBlack
```
