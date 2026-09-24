# org.deepin.dde.MemoryWarningDialog1 接口参考

该接口提供内存警告对话框的显示控制能力，在系统内存不足时弹出警告提示窗口。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.MemoryWarningDialog1` |
| Object path | `/org/deepin/dde/MemoryWarningDialog1` |
| Interface | `org.deepin.dde.MemoryWarningDialog1` |
| Bus | Session |

### Show

显示内存警告对话框。

- **输入参数**: `launchInfo`（string, 类型 `s`）：启动信息
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.MemoryWarningDialog1 \
  --object-path /org/deepin/dde/MemoryWarningDialog1 \
  --method org.deepin.dde.MemoryWarningDialog1.Show "warning"
```

### Hide

隐藏内存警告对话框。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.MemoryWarningDialog1 \
  --object-path /org/deepin/dde/MemoryWarningDialog1 \
  --method org.deepin.dde.MemoryWarningDialog1.Hide
```
