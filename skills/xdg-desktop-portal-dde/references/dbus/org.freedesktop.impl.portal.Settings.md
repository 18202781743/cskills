# org.freedesktop.impl.portal.Settings 接口参考

该接口提供桌面环境设置读取能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.impl.portal.desktop.dde` |
| Object path | `/org/freedesktop/portal/desktop` |
| Interface | `org.freedesktop.impl.portal.Settings` |
| Bus | Session |

### 属性

| 属性名 | 类型 | 权限 | 说明 |
|--------|------|------|------|
| `version` | `u` | read | 接口版本号 |

### 信号

#### SettingChanged

当设置值发生变化时触发。

- **参数**: `group`（string, 类型 `s`）：设置组名；`key`（string, 类型 `s`）：键名；`value`（variant, 类型 `v`）：设置值

### 设置方法

#### ReadAll

读取所有指定设置组的设置。

- **输入参数**: `groups`（字符串数组, 类型 `as`）：设置组名列表
- **返回值**: 设置键值映射

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Settings.ReadAll []
```

#### Read

读取指定设置组和键的值。

- **输入参数**: `group`（string, 类型 `s`）：设置组名；`key`（string, 类型 `s`）：键名
- **返回值**: 设置值

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Settings.Read "org.freedesktop.appearance" "background-uris"
```
