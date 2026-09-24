# org.freedesktop.impl.portal.Background 接口参考

该接口提供后台运行请求和通知能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.impl.portal.desktop.dde` |
| Object path | `/org/freedesktop/portal/desktop` |
| Interface | `org.freedesktop.impl.portal.Background` |
| Bus | Session |

### 后台管理方法

#### EnableAutostart

设置应用是否开机自启动。

- **输入参数**: `app_id`（string, 类型 `s`）：应用 ID；`enable`（bool, 类型 `b`）：是否启用自启动；`commandline`（字符串数组, 类型 `as`）：启动命令行；`flags`（uint, 类型 `u`）：标志位
- **返回值**: `b`（bool）：是否设置成功

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Background.EnableAutostart "app" true [] 0
```

#### GetAppState

获取应用运行状态。

- **输入参数**: 无
- **返回值**: `a{sv}`（字典）：应用状态映射（应用 ID → 运行状态）

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Background.GetAppState
```

#### NotifyBackground

通知后台运行状态。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`app_id`（string, 类型 `s`）：应用 ID；`name`（string, 类型 `s`）：通知名称
- **返回值**: `u`（uint）：响应码；`results`（字典, 类型 `a{sv}`）：通知结果

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Background.NotifyBackground "/" "app" "test"
```

### 信号

#### RunnintApplicationsChanged

当运行中的应用列表发生变化时触发。

- **参数**: 无
