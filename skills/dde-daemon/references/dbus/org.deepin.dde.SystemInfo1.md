# org.deepin.dde.SystemInfo1 接口参考

该接口提供系统硬件和软件信息查询能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.SystemInfo1` |
| Object path | `/org/deepin/dde/SystemInfo1` |
| Interface | `org.deepin.dde.SystemInfo1` |
| Bus | Session |
### 系统信息方法

#### GetSystemVersion

获取系统版本。

- **输入参数**: 无
- **返回值**: `s`（string）：版本号

```bash
gdbus call --session \
  --dest org.deepin.dde.SystemInfo1 \
  --object-path /org/deepin/dde/SystemInfo1 \
  --method org.deepin.dde.SystemInfo1.GetSystemVersion
```

#### GetProcessorModel

获取处理器型号。

- **输入参数**: 无
- **返回值**: `s`（string）：处理器型号

```bash
gdbus call --session \
  --dest org.deepin.dde.SystemInfo1 \
  --object-path /org/deepin/dde/SystemInfo1 \
  --method org.deepin.dde.SystemInfo1.GetProcessorModel
```

#### GetMemoryCapacity

获取内存容量。

- **输入参数**: 无
- **返回值**: `d`（double）：内存容量（GB）

```bash
gdbus call --session \
  --dest org.deepin.dde.SystemInfo1 \
  --object-path /org/deepin/dde/SystemInfo1 \
  --method org.deepin.dde.SystemInfo1.GetMemoryCapacity
```

