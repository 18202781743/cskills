# org.deepin.ds.Dock 接口参考

该接口是提供给外部控制 Dock 的服务接口，允许外部程序控制 Dock 的显示控制与属性管理能力，包括 Dock 的显示调用、插件重载，以及位置、几何区域和是否在主屏显示属性的读取与设置。
## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.ds.Dock` |
| Object path | `/org/deepin/ds/Dock` |
| Interface | `org.deepin.ds.Dock` |
| Bus | Session |
## 兼容接口

Dock 面板服务除当前使用的 `org.deepin.ds.Dock` 外，还注册了两个历史别名服务，各自注册在独立的对象路径上，用于向后兼容不同版本的调用方：

- `org.deepin.ds.Dock`（`/org/deepin/ds/Dock`）— 当前服务名。
- `org.deepin.dde.Dock1`（`/org/deepin/dde/Dock1`）— 旧版前端接口别名。
- `org.deepin.dde.daemon.Dock1`（`/org/deepin/dde/daemon/Dock1`）— 旧版守护进程接口别名。

新代码应优先使用 `org.deepin.ds.Dock`。

## 方法、属性与信号

### 显示与插件管理

#### callShow

调用 Dock 显示。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.ds.Dock \
  --object-path /org/deepin/ds/Dock \
  --method org.deepin.ds.Dock.callShow
```

#### ReloadPlugins

重新加载 Dock 插件。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.ds.Dock \
  --object-path /org/deepin/ds/Dock \
  --method org.deepin.ds.Dock.ReloadPlugins
```

### Dock 属性

#### geometry（属性）

Dock 的几何区域。

| 属性 | 值 |
|------|------|
| 类型 | `(iiii)`（QRect: x, y, width, height） |
| 读写权限 | read |

```bash
gdbus call --session \
  --dest org.deepin.ds.Dock \
  --object-path /org/deepin/ds/Dock \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.ds.Dock geometry
```

#### position（属性）

Dock 位置。

| 属性 | 值 |
|------|------|
| 类型 | `i`（int32） |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.ds.Dock \
  --object-path /org/deepin/ds/Dock \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.ds.Dock position
```

设置示例：

```bash
gdbus call --session \
  --dest org.deepin.ds.Dock \
  --object-path /org/deepin/ds/Dock \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.ds.Dock position "<int32 0>"
```

#### showInPrimary（属性）

是否在主屏显示 Dock。

| 属性 | 值 |
|------|------|
| 类型 | `b`（bool） |
| 读写权限 | readwrite |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.ds.Dock \
  --object-path /org/deepin/ds/Dock \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.ds.Dock showInPrimary
```

设置示例：

```bash
gdbus call --session \
  --dest org.deepin.ds.Dock \
  --object-path /org/deepin/ds/Dock \
  --method org.freedesktop.DBus.Properties.Set \
  org.deepin.ds.Dock showInPrimary "<true>"
```

---
