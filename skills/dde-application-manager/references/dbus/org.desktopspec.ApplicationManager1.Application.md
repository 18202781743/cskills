# org.desktopspec.ApplicationManager1.Application 接口参考

该接口提供单个应用的启动、桌面操作和属性查询能力。动态对象路径由 ApplicationManager1.List 返回。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.desktopspec.ApplicationManager1` |
| Object path | `<dynamic>` |
| Interface | `org.desktopspec.ApplicationManager1.Application` |
| Bus | Session |

> **核验状态**：已通过源码 D-Bus 内省 XML（`api/dbus/org.desktopspec.ApplicationManager1.Application.xml`）核验，接口名称、对象路径、方法签名和属性类型均与源码一致。

### 应用操作

#### Launch

启动应用。

- **输入参数**:
  - `action`（string, 类型 `s`）：动作标识符，对应桌面文件中 `[Desktop Action xxx]` 的 `xxx`，空字符串表示默认动作
  - `fields`（数组, 类型 `as`）：传递给应用的文件路径或 URI 列表
  - `options`（字典, 类型 `a{sv}`）：启动选项，支持的键包括：
    - `uid`（uint）：以指定用户 ID 运行，可能需要 polkit 认证
    - `env`（数组 `as`）：传递环境变量，如 `['LANG=en_US', 'PATH=xxx:yyy']`
    - `unsetEnv`（数组 `as`）：取消设置的环境变量名列表
    - `path`（string）：设置工作目录（绝对路径）
- **返回值**: `o`（object path）：任务对象路径，可用于跟踪启动进度

```bash
gdbus call --session \
  --dest org.desktopspec.ApplicationManager1 \
  --object-path <dynamic> \
  --method org.desktopspec.ApplicationManager1.Application.Launch \
  "" "[]" "{}"
```

#### SendToDesktop

将应用快捷方式发送到桌面。

- **输入参数**: 无
- **返回值**: `b`（boolean）：是否成功

```bash
gdbus call --session \
  --dest org.desktopspec.ApplicationManager1 \
  --object-path <dynamic> \
  --method org.desktopspec.ApplicationManager1.Application.SendToDesktop
```

#### RemoveFromDesktop

从桌面移除应用快捷方式。

- **输入参数**: 无
- **返回值**: `b`（boolean）：是否成功

```bash
gdbus call --session \
  --dest org.desktopspec.ApplicationManager1 \
  --object-path <dynamic> \
  --method org.desktopspec.ApplicationManager1.Application.RemoveFromDesktop
```


### 应用属性

#### ID（属性）

应用 ID（桌面文件 ID）。

| 属性 | 值 |
|------|------|
| 类型 | `s` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.desktopspec.ApplicationManager1 \
  --object-path <dynamic> \
  --method org.freedesktop.DBus.Properties.Get \
  org.desktopspec.ApplicationManager1.Application ID
```

#### Name（属性）

应用名称。键为语言代码，值为对应语言的名称。

| 属性 | 值 |
|------|------|
| 类型 | `a{ss}` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.desktopspec.ApplicationManager1 \
  --object-path <dynamic> \
  --method org.freedesktop.DBus.Properties.Get \
  org.desktopspec.ApplicationManager1.Application Name
```

#### GenericName（属性）

应用通用名称。键为语言代码，值为对应语言的名称。

| 属性 | 值 |
|------|------|
| 类型 | `a{ss}` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.desktopspec.ApplicationManager1 \
  --object-path <dynamic> \
  --method org.freedesktop.DBus.Properties.Get \
  org.desktopspec.ApplicationManager1.Application GenericName
```

#### Categories（属性）

应用分类列表。

| 属性 | 值 |
|------|------|
| 类型 | `as` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.desktopspec.ApplicationManager1 \
  --object-path <dynamic> \
  --method org.freedesktop.DBus.Properties.Get \
  org.desktopspec.ApplicationManager1.Application Categories
```

#### Icons（属性）

应用图标。键为动作标识符，值为图标内容。

| 属性 | 值 |
|------|------|
| 类型 | `a{ss}` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.desktopspec.ApplicationManager1 \
  --object-path <dynamic> \
  --method org.freedesktop.DBus.Properties.Get \
  org.desktopspec.ApplicationManager1.Application Icons
```

#### Actions（属性）

应用动作标识符列表。

| 属性 | 值 |
|------|------|
| 类型 | `as` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.desktopspec.ApplicationManager1 \
  --object-path <dynamic> \
  --method org.freedesktop.DBus.Properties.Get \
  org.desktopspec.ApplicationManager1.Application Actions
```

#### ActionName（属性）

动作名称映射。键为动作标识符，值为语言-名称映射。

| 属性 | 值 |
|------|------|
| 类型 | `a{sa{ss}}` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.desktopspec.ApplicationManager1 \
  --object-path <dynamic> \
  --method org.freedesktop.DBus.Properties.Get \
  org.desktopspec.ApplicationManager1.Application ActionName
```

#### Execs（属性）

应用执行命令。键为动作标识符，值为对应的执行命令。

| 属性 | 值 |
|------|------|
| 类型 | `a{ss}` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.desktopspec.ApplicationManager1 \
  --object-path <dynamic> \
  --method org.freedesktop.DBus.Properties.Get \
  org.desktopspec.ApplicationManager1.Application Execs
```

#### Terminal（属性）

是否在终端中运行。

| 属性 | 值 |
|------|------|
| 类型 | `b` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.desktopspec.ApplicationManager1 \
  --object-path <dynamic> \
  --method org.freedesktop.DBus.Properties.Get \
  org.desktopspec.ApplicationManager1.Application Terminal
```
