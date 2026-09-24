# org.freedesktop.impl.portal.GlobalShortcuts 接口参考

该接口提供全局快捷键会话创建和绑定能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.impl.portal.desktop.dde` |
| Object path | `/org/freedesktop/portal/desktop` |
| Interface | `org.freedesktop.impl.portal.GlobalShortcuts` |
| Bus | Session |

### 属性

| 属性名 | 类型 | 权限 | 说明 |
|--------|------|------|------|
| `version` | `u` | read | 接口版本号 |

### 全局快捷键方法

#### CreateSession

创建全局快捷键会话。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`session_handle`（object path, 类型 `o`）：会话句柄；`app_id`（string, 类型 `s`）：应用 ID；`options`（字典, 类型 `a{sv}`）：选项
- **返回值**: `u`（uint）：响应码；`results`（字典, 类型 `a{sv}`）：会话创建结果

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.GlobalShortcuts.CreateSession "/" "/" "app" {}
```

#### BindShortCuts

绑定全局快捷键。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`session_handle`（object path, 类型 `o`）：会话句柄；`shortcuts`（字典, 类型 `a{sv}`）：快捷键描述；`parent_window`（string, 类型 `s`）：父窗口标识；`options`（字典, 类型 `a{sv}`）：选项
- **返回值**: `a{sv}`（字典）：绑定结果

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.GlobalShortcuts.BindShortCuts "/" "/" {} "" {}
```

#### ListShortCuts

列出已绑定的全局快捷键。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`session_handle`（object path, 类型 `o`）：会话句柄
- **返回值**: `a{sv}`（字典）：已绑定的快捷键列表

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.GlobalShortcuts.ListShortCuts "/" "/"
```
