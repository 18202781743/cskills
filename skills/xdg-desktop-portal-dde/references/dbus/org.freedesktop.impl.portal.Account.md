# org.freedesktop.impl.portal.Account 接口参考

该接口提供用户信息查询能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.impl.portal.desktop.dde` |
| Object path | `/org/freedesktop/portal/desktop` |
| Interface | `org.freedesktop.impl.portal.Account` |
| Bus | Session |

### 账户方法

#### GetUserInformation

获取用户信息。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`app_id`（string, 类型 `s`）：应用 ID；`window`（string, 类型 `s`）：父窗口标识；`options`（字典, 类型 `a{sv}`）：选项
- **返回值**: `u`（uint）：响应码；`results`（字典, 类型 `a{sv}`）：用户信息（包含 id、name、image 等）

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Account.GetUserInformation "/" "app" "" {}
```
