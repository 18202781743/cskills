# org.deepin.dde.dock.plugin.sound

任务栏音量插件配置资源，管理音量滑动条显示和无输出端口时的音量调节。

## 配置项

| Key | Name | Description | 类型 | Permissions | Visibility |
|---|---|---|---|---|---|
| `soundOutputSlider` | 音量滑动条 | 音量滑动条显示状态，0-Enabled（启用），1-Disabled（禁用），2-Hidden（隐藏） | number | readwrite | private |
| `enableAdjustVolumeNoCard` | 无输出端口时允许调节音量 | 全局配置，控制在没有音频输出端口时是否允许调节音量 | bool | readwrite | private |

## 读写示例

```bash
# 查询音量滑动条状态
dde-dconfig get -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.sound -k soundOutputSlider
```

输出示例：

```
0
```

```bash
# 设置音量滑动条为隐藏
dde-dconfig set -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.sound -k soundOutputSlider -v "2"
```

```bash
# 查询无输出端口时是否允许调节音量
dde-dconfig get -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.sound -k enableAdjustVolumeNoCard
```

输出示例：

```
false
```
