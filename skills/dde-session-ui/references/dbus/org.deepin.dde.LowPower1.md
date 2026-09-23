# org.deepin.dde.LowPower1 接口参考

该接口提供低电量提示窗口的显示控制能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.LowPower1` |
| Object path | `/org/deepin/dde/LowPower1` |
| Interface | `org.deepin.dde.LowPower1` |
| Bus | Session |

### Raise

将低电量提示窗口提升到最前层。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.LowPower1 \
  --object-path /org/deepin/dde/LowPower1 \
  --method org.deepin.dde.LowPower1.Raise
```

### Quit

退出低电量提示程序。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.LowPower1 \
  --object-path /org/deepin/dde/LowPower1 \
  --method org.deepin.dde.LowPower1.Quit
```
