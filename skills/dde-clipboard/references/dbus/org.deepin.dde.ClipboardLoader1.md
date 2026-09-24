# org.deepin.dde.ClipboardLoader1 接口参考

该接口提供剪贴板守护进程的剪贴板数据接收与恢复能力。dde-clipboard-daemon 监听系统剪贴板变化，将新数据通过 `dataComing` 信号发送给前端；前端可通过 `dataReborned` 方法将指定数据恢复到系统剪贴板。

> 注意：`dataComing` 信号和 `dataReborned` 方法传输的 `buf` 参数为 `QByteArray` 类型，内部为 dde-clipboard 组件自定义的序列化格式，包含剪贴板条目的格式映射、类型、URL、图片、文本、创建时间信息，非标准数据格式。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.ClipboardLoader1` |
| Object path | `/org/deepin/dde/ClipboardLoader1` |
| Interface | `org.deepin.dde.ClipboardLoader1` |
| Bus | Session |

## 方法

### dataReborned

将指定的剪贴板数据恢复到系统剪贴板。参数为 dde-clipboard 组件内部序列化格式的字节数组。

参数：
- `buf`（QByteArray）：剪贴板条目数据的序列化字节数组

用例：
```bash
dbus-send --session --print-reply \
  --dest=org.deepin.dde.ClipboardLoader1 \
  /org/deepin/dde/ClipboardLoader1 \
  org.deepin.dde.ClipboardLoader1.dataReborned \
  array:byte:
```

## 信号

### dataComing

系统剪贴板数据发生变化时发出，携带新的剪贴板条目数据。

参数：
- `buf`（QByteArray）：剪贴板条目数据的序列化字节数组

用例：
```bash
dbus-monitor --session \
  "type='signal',interface='org.deepin.dde.ClipboardLoader1',member='dataComing'"
```
