# org.deepin.dde.LockService1 接口参考

该接口提供锁屏和用户切换能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.LockService1` |
| Object path | `/org/deepin/dde/LockService1` |
| Interface | `org.deepin.dde.LockService1` |
| Bus | System |
### 锁屏服务方法

#### CurrentUser

获取当前用户。

- **输入参数**: 无
- **返回值**: `s`（string）：当前用户名

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.LockService1 \
  --object-path /org/deepin/dde/LockService1 \
  --method org.deepin.dde.LockService1.CurrentUser
```

#### SwitchToUser

切换到指定用户。

- **输入参数**: `name`（string, 类型 `s`）：用户名
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.LockService1 \
  --object-path /org/deepin/dde/LockService1 \
  --method org.deepin.dde.LockService1.SwitchToUser "user"
```

