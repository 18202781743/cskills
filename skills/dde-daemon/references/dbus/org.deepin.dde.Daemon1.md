# org.deepin.dde.Daemon1 接口参考

该接口提供系统级守护进程管理和调试能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Daemon1` |
| Object path | `/org/deepin/dde/Daemon1` |
| Interface | `org.deepin.dde.Daemon1` |
| Bus | Session |
### 守护进程方法

#### CallTrace

调用跟踪。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Daemon1 \
  --object-path /org/deepin/dde/Daemon1 \
  --method org.deepin.dde.Daemon1.CallTrace
```

#### StartPart2

启动第二阶段。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Daemon1 \
  --object-path /org/deepin/dde/Daemon1 \
  --method org.deepin.dde.Daemon1.StartPart2
```

