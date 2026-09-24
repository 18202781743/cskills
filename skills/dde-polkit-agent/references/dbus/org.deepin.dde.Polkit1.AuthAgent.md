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

dde-polkit-agent 仅注册唯一的 D-Bus 服务 `org.deepin.dde.Polkit1.AuthAgent`，不存在为兼容旧版接口而保留的别名或废弃接口。该接口为当前正在使用的唯一 D-Bus 接口，无历史兼容接口。
