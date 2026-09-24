# org.deepin.dde.SoundEffect1 接口参考

该接口提供系统声音效果管理能力。

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

#### EnableAllSound

启用所有声音效果。

- **输入参数**: `enabled`（bool, 类型 `b`）：是否启用
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.SoundEffect1 \
  --object-path /org/deepin/dde/SoundEffect1 \
  --method org.deepin.dde.SoundEffect1.EnableAllSound true
```

