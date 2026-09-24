# org.freedesktop.impl.portal.Wallpaper 接口参考

该接口提供壁纸设置能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.impl.portal.desktop.dde` |
| Object path | `/org/freedesktop/portal/desktop` |
| Interface | `org.freedesktop.impl.portal.Wallpaper` |
| Bus | Session |

### 壁纸方法

#### SetWallpaperURI

设置壁纸 URI。

- **输入参数**: `handle`（object path, 类型 `o`）：请求句柄；`app_id`（string, 类型 `s`）：应用 ID；`parent_window`（string, 类型 `s`）：父窗口标识；`uri`（string, 类型 `s`）：壁纸 URI；`options`（字典, 类型 `a{sv}`）：壁纸选项
- **返回值**: `u`（uint）：响应码

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop \
  --method org.freedesktop.impl.portal.Wallpaper.SetWallpaperURI "/" "app" "" "file:///usr/share/wallpapers/deepin/desktop.jpg" {}
```
