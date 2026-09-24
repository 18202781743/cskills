# org.deepin.dde.Polkit1.AuthAgent 接口参考

## 接口信息

该接口在 **Session 总线**上注册，提供 polkit 认证代理窗口 ID 设置能力，供外部应用调用以关联认证窗口。

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Polkit1.AuthAgent` |
| Object path | `/com/deepin/dde/Polkit1/AuthAgent` |
| Interface | `org.deepin.dde.Polkit1.AuthAgent` |
| Bus | Session |

## 方法

### setWIdForAction

为指定 polkit 动作设置窗口 ID。

- **功能**：将调用方应用的窗口 ID 关联到指定的 polkit 动作（action_id），使认证对话框能够正确关联到发起认证请求的窗口。
- **触发条件**：当外部应用需要在执行特权操作前，将自身窗口 ID 传递给认证代理时调用此方法。
- **使用场景**：应用在发起需要 polkit 认证的操作前，调用此方法将窗口 ID 传递给认证代理，使认证对话框能与发起窗口正确关联（如窗口居中、窗口归属设置）。
- **输入参数**：
  - `action_id`（string, 类型 `s`）：polkit 动作 ID，对应 `/usr/share/polkit-1/actions/` 下 `.policy` 文件中定义的 action id
  - `window_id`（uint64, 类型 `t`）：窗口 ID（X11 Window ID 或 Wayland window ID）
- **返回值**：无

## 示例

```bash
gdbus call --session \
  --dest org.deepin.dde.Polkit1.AuthAgent \
  --object-path /com/deepin/dde/Polkit1/AuthAgent \
  --method org.deepin.dde.Polkit1.AuthAgent.setWIdForAction "org.example.action" 12345
```

## 兼容性说明

当前接口 `org.deepin.dde.Polkit1.AuthAgent`（对象路径 `/com/deepin/dde/Polkit1/AuthAgent`）是 V23 接口改造后启用的唯一 D-Bus 接口，所有示例均使用此接口。

旧版接口（V23 改造前）使用服务名 `com.deepin.Polkit1AuthAgent`（对象路径 `/com/deepin/Polkit1AuthAgent`），已在 V23 接口改造中替换为新接口名，当前不再注册，属于**废弃**接口，仅作历史记录。
