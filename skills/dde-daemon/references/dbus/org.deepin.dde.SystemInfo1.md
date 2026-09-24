# org.deepin.dde.SystemInfo1 接口参考

该接口提供系统硬件和软件信息查询能力。该接口仅导出属性，无导出方法，属性通过 `org.freedesktop.DBus.Properties.Get` 访问。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.SystemInfo1` |
| Object path | `/org/deepin/dde/SystemInfo1` |
| Interface | `org.deepin.dde.SystemInfo1` |
| Bus | System |

### 系统信息属性

以下属性通过 `org.freedesktop.DBus.Properties.Get` 访问，均为只读。

| 属性 | 类型 | 说明 |
|------|------|------|
| `MemorySize` | `t`（uint64） | 内存大小（字节） |
| `MemorySizeHuman` | `s`（string） | 内存大小（人类可读，如 `16.00GB`） |
| `CurrentSpeed` | `t`（uint64） | CPU 当前频率（MHz） |
| `DisplayDriver` | `s`（string） | 显卡驱动 |
| `VideoDriver` | `s`（string） | 视频驱动 |
| `DMIInfo` | `(ssssssssssss)`（结构体） | DMI 信息（厂商、型号等） |

#### 读取内存大小

```bash
gdbus call --system \
  --dest org.deepin.dde.SystemInfo1 \
  --object-path /org/deepin/dde/SystemInfo1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.SystemInfo1 MemorySize
```

#### 读取 CPU 当前频率

```bash
gdbus call --system \
  --dest org.deepin.dde.SystemInfo1 \
  --object-path /org/deepin/dde/SystemInfo1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.SystemInfo1 CurrentSpeed
```

#### 读取内存大小（人类可读）

```bash
gdbus call --system \
  --dest org.deepin.dde.SystemInfo1 \
  --object-path /org/deepin/dde/SystemInfo1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.SystemInfo1 MemorySizeHuman
```

#### 读取所有属性

```bash
gdbus call --system \
  --dest org.deepin.dde.SystemInfo1 \
  --object-path /org/deepin/dde/SystemInfo1 \
  --method org.freedesktop.DBus.Properties.GetAll \
  org.deepin.dde.SystemInfo1
```
