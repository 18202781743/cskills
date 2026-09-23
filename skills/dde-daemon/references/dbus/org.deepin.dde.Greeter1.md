# org.deepin.dde.Greeter1 接口参考

该接口提供 Greeter 主题更新能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Greeter1` |
| Object path | `/org/deepin/dde/Greeter1` |
| Interface | `org.deepin.dde.Greeter1` |
| Bus | System |
### Greeter 方法

#### UpdateGreeterQtTheme

更新 Greeter Qt 主题。

- **输入参数**: 无
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Greeter1 \
  --object-path /org/deepin/dde/Greeter1 \
  --method org.deepin.dde.Greeter1.UpdateGreeterQtTheme
```

