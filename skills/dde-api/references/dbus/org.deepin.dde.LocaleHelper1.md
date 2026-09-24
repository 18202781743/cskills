# org.deepin.dde.LocaleHelper1 接口参考

该接口提供系统区域设置生成和切换能力。

> **条件编译说明**：该接口的二进制文件存在，但对应的 `.service` 文件在安装阶段被 `rm -f` 删除，因此无法通过 D-Bus activation 自动激活。实际运行时通过 systemd service 启动，而非 D-Bus 自动激活。使用者不应假设该服务可通过 D-Bus 自动拉起，需确保 systemd 服务已启动后再进行 D-Bus 调用。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.LocaleHelper1` |
| Object path | `/org/deepin/dde/LocaleHelper1` |
| Interface | `org.deepin.dde.LocaleHelper1` |
| Bus | System |

> **验证说明**：已通过 `gdbus introspect --system` 运行时内省验证，以下方法均可访问。源码中另有 `SetAllowCaller` 方法（`locale-helper/exported_methods_auto.go`），但在当前运行时内省中不可见，可能需要特定安全上下文或尚未部署到当前环境，此处不予文档化。

## 区域设置方法

### GenerateLocale

生成指定的区域设置。该方法执行完毕后会发出 `Success` 信号通知结果。

- **输入参数**:
  - `locale`（string, 类型 `s`）：区域名称（如 `zh_CN.UTF-8`）
- **返回值**: 无（出错时返回 dbus.Error）
- **信号**: 完成后发出 `Success(ok bool, reason string)` 信号

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.LocaleHelper1 \
  --object-path /org/deepin/dde/LocaleHelper1 \
  --method org.deepin.dde.LocaleHelper1.GenerateLocale \
  "zh_CN.UTF-8"
```

### SetLocale

设置系统区域。

- **输入参数**:
  - `locale`（string, 类型 `s`）：区域名称（如 `zh_CN.UTF-8`）
- **返回值**: 无（出错时返回 dbus.Error）

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.LocaleHelper1 \
  --object-path /org/deepin/dde/LocaleHelper1 \
  --method org.deepin.dde.LocaleHelper1.SetLocale \
  "zh_CN.UTF-8"
```

## 信号

### Success

`GenerateLocale` 方法执行完毕后发出此信号，通知操作结果。

- **参数**:
  - `ok`（bool, 类型 `b`）：操作是否成功
  - `reason`（string, 类型 `s`）：失败原因（成功时为空字符串）

```bash
gdbus monitor --system \
  --dest org.deepin.dde.LocaleHelper1 \
  --object-path /org/deepin/dde/LocaleHelper1
```
