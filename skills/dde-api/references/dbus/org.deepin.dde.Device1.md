# org.deepin.dde.Device1 接口参考

该接口提供蓝牙设备阻止状态查询和解锁能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Device1` |
| Object path | `/org/deepin/dde/Device1` |
| Interface | `org.deepin.dde.Device1` |
| Bus | System |

> **验证说明**：已通过 `gdbus introspect --system` 运行时内省验证，所有方法均可访问。

## 设备管理方法

### HasBluetoothDeviceBlocked

查询是否有蓝牙设备被阻止。

- **功能**: 检查系统中是否存在被阻止的蓝牙设备
- **触发条件**: 由应用程序通过 D-Bus 调用触发
- **使用场景**: 蓝牙管理界面显示设备阻止状态、安全策略检查

- **输入参数**: 无
- **返回值**: `has`（bool, 类型 `b`）：是否有设备被阻止

```bash
gdbus call --system \
  --dest org.deepin.dde.Device1 \
  --object-path /org/deepin/dde/Device1 \
  --method org.deepin.dde.Device1.HasBluetoothDeviceBlocked
```

### UnblockBluetoothDevices

解除所有蓝牙设备的阻止。

- **功能**: 清除所有蓝牙设备的阻止状态，使其恢复正常连接能力
- **触发条件**: 由应用程序通过 D-Bus 调用触发
- **使用场景**: 蓝牙设备管理中批量解除阻止、安全策略重置

- **输入参数**: 无
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Device1 \
  --object-path /org/deepin/dde/Device1 \
  --method org.deepin.dde.Device1.UnblockBluetoothDevices
```
