# org.deepin.dde.Osd1 接口参考

该接口提供 OSD（屏幕显示）面板的显示控制能力，包括音量、亮度系统 OSD 提示的显示。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Osd1` |
| Object path | `/` |
| Interface | `org.deepin.dde.Osd1` |
| Bus | Session |

### ShowOSD

显示指定的 OSD 提示。

- **功能**: 在屏幕上弹出指定的 OSD 提示面板，显示音量、亮度、显示模式、键盘布局、窗口特效系统状态信息
- **触发条件**: 由系统组件主动调用，当音量、亮度、显示模式、键盘布局、窗口特效系统状态发生变化时触发
- **使用场景**: 用户调节音量或屏幕亮度时，系统调用此方法在屏幕上显示对应的 OSD 提示动画
- **输入参数**: `osd`（string, 类型 `s`）：OSD 提示类型名称
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Osd1 \
  --object-path / \
  --method org.deepin.dde.Osd1.ShowOSD "AudioVolumeUp"
```
