# org.freedesktop.impl.portal.FileChooser 接口参考

该接口提供文件打开和保存对话框能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.impl.portal.desktop.dde` |
| Object path | `/org/freedesktop/portal/desktop` |
| Interface | `org.freedesktop.impl.portal.FileChooser` |
| Bus | Session |

### 文件选择方法

#### OpenFile

打开文件选择对话框。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`app_id`（string, 类型 `s`）：应用 ID；`parent_window`（string, 类型 `s`）：父窗口标识；`title`（string, 类型 `s`）：标题；`options`（字典, 类型 `a{sv}`）：选项
- **返回值**: `u`（uint）：响应码；`results`（字典, 类型 `a{sv}`）：文件选择结果

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.FileChooser.OpenFile "/" "app" "" "选择文件" {}
```

#### SaveFile

打开文件保存对话框。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`app_id`（string, 类型 `s`）：应用 ID；`parent_window`（string, 类型 `s`）：父窗口标识；`title`（string, 类型 `s`）：标题；`options`（字典, 类型 `a{sv}`）：选项
- **返回值**: `u`（uint）：响应码；`results`（字典, 类型 `a{sv}`）：文件保存结果

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.FileChooser.SaveFile "/" "app" "" "保存文件" {}
```

#### SaveFiles

打开多文件保存对话框。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`app_id`（string, 类型 `s`）：应用 ID；`parent_window`（string, 类型 `s`）：父窗口标识；`title`（string, 类型 `s`）：标题；`options`（字典, 类型 `a{sv}`）：选项
- **返回值**: `u`（uint）：响应码；`results`（字典, 类型 `a{sv}`）：文件保存结果

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.FileChooser.SaveFiles "/" "app" "" "保存多个文件" {}
```
