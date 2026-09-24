# org.freedesktop.impl.portal.Secret 接口参考

该接口提供密钥检索能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.impl.portal.desktop.dde` |
| Object path | `/org/freedesktop/portal/desktop` |
| Interface | `org.freedesktop.impl.portal.Secret` |
| Bus | Session |

### 属性

| 属性名 | 类型 | 权限 | 说明 |
|--------|------|------|------|
| `version` | `u` | read | 接口版本号 |

### 密钥方法

#### RetrieveSecret

检索密钥。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`app_id`（string, 类型 `s`）：应用 ID；`fd`（文件描述符, 类型 `h`）：文件描述符；`options`（字典, 类型 `a{sv}`）：选项
- **返回值**: `u`（uint）：响应码；`result`（字典, 类型 `a{sv}`）：密钥检索结果

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Secret.RetrieveSecret "/" "app" 0 {}
```
