# org.freedesktop.impl.portal.Screenshot 接口参考

该接口提供屏幕截图和取色能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.impl.portal.desktop.dde` |
| Object path | `/org/freedesktop/portal/desktop` |
| Interface | `org.freedesktop.impl.portal.Screenshot` |
| Bus | Session |

### 截图方法

#### Screenshot

进行屏幕截图。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`app_id`（string, 类型 `s`）：应用 ID；`parent_window`（string, 类型 `s`）：父窗口标识；`options`（字典, 类型 `a{sv}`）：截图选项
- **返回值**: `u`（uint）：响应码；`results`（字典, 类型 `a{sv}`）：截图结果（包含 URI 等信息）

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Screenshot.Screenshot "/" "app" "" {}
```

#### PickColor

进行屏幕取色。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`app_id`（string, 类型 `s`）：应用 ID；`parent_window`（string, 类型 `s`）：父窗口标识；`options`（字典, 类型 `a{sv}`）：取色选项
- **返回值**: `u`（uint）：响应码；`results`（字典, 类型 `a{sv}`）：取色结果（包含 color 等信息）

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Screenshot.PickColor "/" "app" "" {}
```
