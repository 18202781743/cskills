# org.deepin.dde.Launcher1 接口参考

该接口提供启动器的显示、隐藏、切换和模式控制能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Launcher1` |
| Object path | `/org/deepin/dde/Launcher1` |
| Interface | `org.deepin.dde.Launcher1` |
| Bus | Session |

> **核验说明**：本文档接口信息已与源码 D-Bus 定义（`dbus/org.deepin.dde.Launcher1.xml`、生成的 Adaptor 及 `launcheritem.cpp` 中的 `registerService`/`registerObject` 调用）核对一致。当前服务由 dde-shell 加载 dde-launchpad applet 后在 Session 总线上程序化注册（无 .service 激活文件），dde-shell 运行时即可访问。

### 启动器显示控制

#### Exit

退出启动器。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Launcher1 \
  --object-path /org/deepin/dde/Launcher1 \
  --method org.deepin.dde.Launcher1.Exit
```

#### Show

显示启动器。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Launcher1 \
  --object-path /org/deepin/dde/Launcher1 \
  --method org.deepin.dde.Launcher1.Show
```

#### Hide

隐藏启动器。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Launcher1 \
  --object-path /org/deepin/dde/Launcher1 \
  --method org.deepin.dde.Launcher1.Hide
```

#### Toggle

切换启动器显示状态。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Launcher1 \
  --object-path /org/deepin/dde/Launcher1 \
  --method org.deepin.dde.Launcher1.Toggle
```

#### ShowByMode

按指定模式显示启动器。

- **输入参数**: `mode`（int64, 类型 `x`）：显示模式
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Launcher1 \
  --object-path /org/deepin/dde/Launcher1 \
  --method org.deepin.dde.Launcher1.ShowByMode 'int64 1'
```


### 启动器属性

#### Visible（属性）

启动器是否可见。

| 属性 | 值 |
|------|------|
| 类型 | `b` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.Launcher1 \
  --object-path /org/deepin/dde/Launcher1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.Launcher1 Visible
```

### 启动器信号

#### Closed

启动器关闭时发出。

- **参数**: 无
- **触发条件**: 启动器被关闭时发出

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Launcher1 \
  --object-path /org/deepin/dde/Launcher1
```

#### Shown

启动器显示时发出。

- **参数**: 无
- **触发条件**: 启动器被显示时发出

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Launcher1 \
  --object-path /org/deepin/dde/Launcher1
```

#### VisibleChanged

启动器可见状态变化时发出。

- **参数**: `visible`（bool, 类型 `b`）：是否可见
- **触发条件**: 启动器可见状态变化时发出

```bash
gdbus monitor --session \
  --dest org.deepin.dde.Launcher1 \
  --object-path /org/deepin/dde/Launcher1
```

---

## 兼容性说明

dde-launchpad 当前仅导出 `org.deepin.dde.Launcher1` 一个 D-Bus 服务接口，这是最新的服务接口名，所有示例均使用此接口。

以下为旧版兼容性服务名，由 `dde-api-dbus-proxy-v1` 代理转发，并非 dde-launchpad 自身导出，仅作功能概述：

- `com.deepin.dde.Launcher`：旧版启动器前端服务名，通过 dde-api-dbus-proxy 兼容转发，功能与 `org.deepin.dde.Launcher1` 相同。
- `com.deepin.dde.daemon.Launcher`：旧版启动器后端服务名，通过 dde-api-dbus-proxy 兼容转发。

这些旧接口不应在新代码中使用，新代码应统一使用 `org.deepin.dde.Launcher1`。Dock 相关的历史别名接口属于 dde-shell，不在 dde-launchpad 中。
