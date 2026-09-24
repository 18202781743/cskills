# org.deepin.dde.ClipboardManager1 接口参考

该接口提供剪贴板目标管理能力，包括成为剪贴板拥有者、移除目标、保存剪贴板内容和写入内容。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.ClipboardManager1` |
| Object path | `/org/deepin/dde/ClipboardManager1` |
| Interface | `org.deepin.dde.ClipboardManager1` |
| Bus | Session |

### 剪贴板管理方法

#### BecomeClipboardOwner

成为剪贴板拥有者。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.ClipboardManager1 \
  --object-path /org/deepin/dde/ClipboardManager1 \
  --method org.deepin.dde.ClipboardManager1.BecomeClipboardOwner
```

#### RemoveTarget

移除剪贴板目标。

- **输入参数**: `target`（string, 类型 `s`）：目标名称
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.ClipboardManager1 \
  --object-path /org/deepin/dde/ClipboardManager1 \
  --method org.deepin.dde.ClipboardManager1.RemoveTarget "target"
```

#### SaveClipboard

保存当前剪贴板内容。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.ClipboardManager1 \
  --object-path /org/deepin/dde/ClipboardManager1 \
  --method org.deepin.dde.ClipboardManager1.SaveClipboard
```

#### WriteContent

写入剪贴板内容。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.ClipboardManager1 \
  --object-path /org/deepin/dde/ClipboardManager1 \
  --method org.deepin.dde.ClipboardManager1.WriteContent
```
