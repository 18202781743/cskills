# org.deepin.dde.Osd1 接口参考

该接口提供 OSD（屏幕显示）面板的显示控制能力，包括音量、亮度等系统 OSD 提示的显示。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Osd1` |
| Object path | `/` |
| Interface | `org.deepin.dde.Osd1` |
| Bus | Session |

### ShowOSD

显示指定的 OSD 提示。

- **输入参数**: `osd`（string, 类型 `s`）：OSD 提示类型名称
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Osd1 \
  --object-path / \
  --method org.deepin.dde.Osd1.ShowOSD "AudioVolumeUp"
```
