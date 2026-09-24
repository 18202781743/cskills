# org.freedesktop.impl.portal.Inhibit 接口参考

该接口提供会话抑制能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.impl.portal.desktop.dde` |
| Object path | `/org/freedesktop/portal/desktop` |
| Interface | `org.freedesktop.impl.portal.Inhibit` |
| Bus | Session |

### 属性

| 属性名 | 类型 | 权限 | 说明 |
|--------|------|------|------|
| `version` | `u` | read | 接口版本号 |

### 抑制方法

#### Inhibit

抑制会话行为（如锁屏、挂起等）。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`app_id`（string, 类型 `s`）：应用 ID；`window`（string, 类型 `s`）：窗口标识；`flags`（uint, 类型 `u`）：抑制标志位；`options`（字典, 类型 `a{sv}`）：选项
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Inhibit.Inhibit "/" "app" "" 0 {}
```
