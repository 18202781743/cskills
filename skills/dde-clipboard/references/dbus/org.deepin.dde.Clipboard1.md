# org.deepin.dde.Clipboard1 接口参考

该接口用于控制 DDE 剪贴板前端服务的显示状态，提供剪贴板窗口的切换、显示和隐藏能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Clipboard1` |
| Object path | `/org/deepin/dde/Clipboard1` |
| Interface | `org.deepin.dde.Clipboard1` |
| Bus | Session |

## 方法

### Toggle

切换剪贴板窗口的显示状态：若窗口当前隐藏则显示，若当前显示则隐藏。

用例：
```bash
dbus-send --session --print-reply \
  --dest=org.deepin.dde.Clipboard1 \
  /org/deepin/dde/Clipboard1 \
  org.deepin.dde.Clipboard1.Toggle
```

### Show

显示剪贴板窗口。

用例：
```bash
dbus-send --session --print-reply \
  --dest=org.deepin.dde.Clipboard1 \
  /org/deepin/dde/Clipboard1 \
  org.deepin.dde.Clipboard1.Show
```

### Hide

隐藏剪贴板窗口。

用例：
```bash
dbus-send --session --print-reply \
  --dest=org.deepin.dde.Clipboard1 \
  /org/deepin/dde/Clipboard1 \
  org.deepin.dde.Clipboard1.Hide
```

## 属性

### clipboardVisible

剪贴板窗口当前的可见状态。

| 属性 | 值 |
|------|------|
| 类型 | bool |
| 访问权限 | read |

用例：
```bash
dbus-send --session --print-reply \
  --dest=org.deepin.dde.Clipboard1 \
  /org/deepin/dde/Clipboard1 \
  org.freedesktop.DBus.Properties.Get \
  string:"org.deepin.dde.Clipboard1" \
  string:"clipboardVisible"
```

## 信号

### clipboardVisibleChanged

剪贴板窗口可见状态发生变化时发出。

参数：
- `visible`（bool）：当前是否可见，`true` 表示可见，`false` 表示不可见

用例：
```bash
dbus-monitor --session \
  "type='signal',interface='org.deepin.dde.Clipboard1',member='clipboardVisibleChanged'"
```
