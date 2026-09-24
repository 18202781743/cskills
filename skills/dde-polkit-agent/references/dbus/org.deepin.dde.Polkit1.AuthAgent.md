# org.deepin.dde.Polkit1.AuthAgent 接口参考

该接口提供 polkit 认证代理窗口 ID 设置能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Polkit1.AuthAgent` |
| Object path | `/com/deepin/dde/Polkit1/AuthAgent` |
| Interface | `org.deepin.dde.Polkit1.AuthAgent` |
| Bus | Session |

### 认证代理方法

#### setWIdForAction

为指定动作设置窗口 ID。

- **输入参数**: `action_id`（string, 类型 `s`）：动作 ID；`window_id`（uint64, 类型 `t`）：窗口 ID
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.Polkit1.AuthAgent \
  --object-path /com/deepin/dde/Polkit1/AuthAgent \
  --method org.deepin.dde.Polkit1.AuthAgent.setWIdForAction "org.example.action" 12345
```

## 兼容性说明

dde-polkit-agent 当前注册的唯一 D-Bus 服务为 `org.deepin.dde.Polkit1.AuthAgent`（对象路径 `/com/deepin/dde/Polkit1/AuthAgent`），这是 V23 接口改造后启用的接口，所有示例均使用此接口。

旧版接口（V23 改造前）使用的服务名为 `com.deepin.Polkit1AuthAgent`（对象路径 `/com/deepin/Polkit1AuthAgent`），已在 V23 接口改造适配（commit f610246）中替换为新接口名，当前代码中不再注册旧服务名，不存在兼容别名。旧接口仅作历史记录，不再可用。
