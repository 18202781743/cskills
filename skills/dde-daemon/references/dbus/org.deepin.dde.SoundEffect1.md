# org.deepin.dde.SoundEffect1 接口参考

该接口提供系统声音效果管理能力，包括播放声音、启用/禁用声音效果、获取声音文件路径等。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.SoundEffect1` |
| Object path | `/org/deepin/dde/SoundEffect1` |
| Interface | `org.deepin.dde.SoundEffect1` |
| Bus | Session |

### 声音效果方法

#### PlaySound

播放指定声音效果。

- **输入参数**: `name`（string, 类型 `s`）：声音名称
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.SoundEffect1 \
  --object-path /org/deepin/dde/SoundEffect1 \
  --method org.deepin.dde.SoundEffect1.PlaySound "message"
```

#### PlaySystemSound

播放指定系统声音效果。

- **输入参数**: `name`（string, 类型 `s`）：声音名称
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.SoundEffect1 \
  --object-path /org/deepin/dde/SoundEffect1 \
  --method org.deepin.dde.SoundEffect1.PlaySystemSound "message"
```

#### EnableSound

启用或禁用指定声音效果。

- **输入参数**:
  - `name`（string, 类型 `s`）：声音名称
  - `enabled`（bool, 类型 `b`）：是否启用
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.SoundEffect1 \
  --object-path /org/deepin/dde/SoundEffect1 \
  --method org.deepin.dde.SoundEffect1.EnableSound "message" true
```

#### IsSoundEnabled

检查指定声音效果是否启用。

- **输入参数**: `name`（string, 类型 `s`）：声音名称
- **返回值**: `enabled`（bool, 类型 `b`）：是否启用

```bash
gdbus call --session \
  --dest org.deepin.dde.SoundEffect1 \
  --object-path /org/deepin/dde/SoundEffect1 \
  --method org.deepin.dde.SoundEffect1.IsSoundEnabled "message"
```

#### GetSoundFile

获取指定声音效果的文件路径。

- **输入参数**: `name`（string, 类型 `s`）：声音名称
- **返回值**: `file`（string, 类型 `s`）：声音文件路径

```bash
gdbus call --session \
  --dest org.deepin.dde.SoundEffect1 \
  --object-path /org/deepin/dde/SoundEffect1 \
  --method org.deepin.dde.SoundEffect1.GetSoundFile "message"
```

#### GetSystemSoundFile

获取指定系统声音效果的文件路径。

- **输入参数**: `name`（string, 类型 `s`）：声音名称
- **返回值**: `file`（string, 类型 `s`）：声音文件路径

```bash
gdbus call --session \
  --dest org.deepin.dde.SoundEffect1 \
  --object-path /org/deepin/dde/SoundEffect1 \
  --method org.deepin.dde.SoundEffect1.GetSystemSoundFile "message"
```

#### GetSoundEnabledMap

获取所有声音效果的启用状态。

- **输入参数**: 无
- **返回值**: `result`（`a{sb}`，map[string]bool）：声音名称到启用状态的映射

```bash
gdbus call --session \
  --dest org.deepin.dde.SoundEffect1 \
  --object-path /org/deepin/dde/SoundEffect1 \
  --method org.deepin.dde.SoundEffect1.GetSoundEnabledMap
```
