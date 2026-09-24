# org.desktopspec.MimeManager1 接口参考

该接口用于系统级 MIME 类型管理，管理所有应用的 MIME 关联，提供默认应用 MIME 类型设置能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.desktopspec.MimeManager1` |
| Object path | `/org/desktopspec/MimeManager1` |
| Interface | `org.desktopspec.MimeManager1` |
| Bus | Session |

> **核验状态**：已通过源码 D-Bus 内省 XML（`api/dbus/org.desktopspec.MimeManager1.xml`）核验，接口名称、对象路径、方法签名和信号定义均与源码一致。

### MIME 类型管理操作

#### queryDefaultApplication

查询指定内容类型的默认应用。

- **输入参数**: `content`（string, 类型 `s`）：文件绝对路径或 MIME 类型
- **返回值**: `(s, o)`（元组）：MIME 类型、应用对象路径

```bash
gdbus call --session \
  --dest org.desktopspec.MimeManager1 \
  --object-path /org/desktopspec/MimeManager1 \
  --method org.desktopspec.MimeManager1.queryDefaultApplication \
  "text/plain"
```

#### setDefaultApplication

设置 MIME 类型的默认应用。

- **输入参数**: `defaultApps`（字典, 类型 `a{ss}`）：键为 MIME 类型，值为应用 ID

```bash
gdbus call --session \
  --dest org.desktopspec.MimeManager1 \
  --object-path /org/desktopspec/MimeManager1 \
  --method org.desktopspec.MimeManager1.setDefaultApplication \
  "{'text/plain':'org.deepin.editor'}"
```

#### unsetDefaultApplication

取消设置 MIME 类型的默认应用。

- **输入参数**: `mimeTypes`（数组, 类型 `as`）：要取消的 MIME 类型列表

```bash
gdbus call --session \
  --dest org.desktopspec.MimeManager1 \
  --object-path /org/desktopspec/MimeManager1 \
  --method org.desktopspec.MimeManager1.unsetDefaultApplication \
  "['text/plain']"
```

#### listApplications

列出指定 MIME 类型的所有关联应用。

- **输入参数**: `mimeType`（string, 类型 `s`）：MIME 类型
- **返回值**: `a{oa{sa{sv}}}`（字典）：应用对象路径到属性映射的映射

```bash
gdbus call --session \
  --dest org.desktopspec.MimeManager1 \
  --object-path /org/desktopspec/MimeManager1 \
  --method org.desktopspec.MimeManager1.listApplications \
  "text/plain"
```

### MIME 类型信号

#### MimeInfoReloaded

MIME 信息重新加载时发出。

- **参数**: 无

监听示例：

```bash
gdbus monitor --session \
  --dest org.desktopspec.MimeManager1 \
  --object-path /org/desktopspec/MimeManager1
```
