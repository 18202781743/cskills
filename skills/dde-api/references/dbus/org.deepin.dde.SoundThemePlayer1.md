# org.deepin.dde.SoundThemePlayer1 接口参考

该接口提供系统声音主题播放控制能力，包括播放指定事件声音、桌面登录音效、关机音效准备、音频状态保存以及声音主题和启用状态的设置。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.SoundThemePlayer1` |
| Object path | `/org/deepin/dde/SoundThemePlayer1` |
| Interface | `org.deepin.dde.SoundThemePlayer1` |
| Bus | System |

> **验证说明**：已通过 `gdbus introspect --system` 运行时内省验证，所有方法均可访问。

## 声音播放方法

### Play

播放指定主题和事件的声音。

- **输入参数**:
  - `theme`（string, 类型 `s`）：声音主题名称
  - `event`（string, 类型 `s`）：事件名称（如 `desktop-login`、`system-shutdown` 等）
  - `device`（string, 类型 `s`）：音频设备（如 `default` 或 `plughw:CARD=card,DEV=device`）
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --system \
  --dest org.deepin.dde.SoundThemePlayer1 \
  --object-path /org/deepin/dde/SoundThemePlayer1 \
  --method org.deepin.dde.SoundThemePlayer1.Play \
  "deepin" "desktop-login" "default"
```

### PlaySoundDesktopLogin

播放桌面登录音效。

- **输入参数**: 无
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --system \
  --dest org.deepin.dde.SoundThemePlayer1 \
  --object-path /org/deepin/dde/SoundThemePlayer1 \
  --method org.deepin.dde.SoundThemePlayer1.PlaySoundDesktopLogin
```

### PrepareShutdownSound

为指定用户准备关机音效配置。

- **输入参数**:
  - `uid`（int32, 类型 `i`）：用户 UID
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --system \
  --dest org.deepin.dde.SoundThemePlayer1 \
  --object-path /org/deepin/dde/SoundThemePlayer1 \
  --method org.deepin.dde.SoundThemePlayer1.PrepareShutdownSound \
  1000
```

### SaveAudioState

保存指定用户的音频播放状态。

- **输入参数**:
  - `activePlayback`（dict<string, variant>, 类型 `a{sv}`）：音频播放状态字典，包含 `card`、`device`、`mute`、`volume` 等字段
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --system \
  --dest org.deepin.dde.SoundThemePlayer1 \
  --object-path /org/deepin/dde/SoundThemePlayer1 \
  --method org.deepin.dde.SoundThemePlayer1.SaveAudioState \
  "{'card': <'PCH'>, 'device': <'PCH'>, 'mute': <false>, 'volume': <1.0>}"
```

### EnableSound

启用或禁用指定事件的声音。

- **输入参数**:
  - `name`（string, 类型 `s`）：事件名称（空字符串表示整体开关，`desktop-login` 表示登录音效，`system-shutdown` 表示关机音效）
  - `enabled`（bool, 类型 `b`）：是否启用
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --system \
  --dest org.deepin.dde.SoundThemePlayer1 \
  --object-path /org/deepin/dde/SoundThemePlayer1 \
  --method org.deepin.dde.SoundThemePlayer1.EnableSound \
  "desktop-login" true
```

### EnableSoundDesktopLogin

启用或禁用桌面登录音效。

- **输入参数**:
  - `enabled`（bool, 类型 `b`）：是否启用
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --system \
  --dest org.deepin.dde.SoundThemePlayer1 \
  --object-path /org/deepin/dde/SoundThemePlayer1 \
  --method org.deepin.dde.SoundThemePlayer1.EnableSoundDesktopLogin \
  true
```

### SetSoundTheme

设置声音主题。

- **输入参数**:
  - `theme`（string, 类型 `s`）：声音主题名称
- **返回值**: 无（出错时返回 dbus.Error）

```bash
gdbus call --system \
  --dest org.deepin.dde.SoundThemePlayer1 \
  --object-path /org/deepin/dde/SoundThemePlayer1 \
  --method org.deepin.dde.SoundThemePlayer1.SetSoundTheme \
  "deepin"
```
