# org.deepin.dde.session-shell

会话电源行为配置资源（appId: `org.deepin.dde.session-shell`），控制认证超时、待机休眠延时、密码检查、电源操作按钮的显示与禁用行为，共 12 个配置项。

## 配置项

| Key | Name | Description | 类型 | Permissions |
|---|---|---|---|---|
| `authResetTime` | 最大认证超时时间 | 最大认证超时时间, 默认为15秒认证超时。 | int | readwrite |
| `delayTime` | 待机休眠休眠延时时间 | 待机休眠休眠延时时间, 默认为500毫秒。 | int | readwrite |
| `useDeepinAuth` | 使用Deepin认证 | 是否使用Deepin认证。 | bool | readwrite |
| `checkpwd` | 检查密码 | 是否检查密码。 | bool | readwrite |
| `sleep` | sleep | sleep，如果启用，那么待机操作显示，如果禁用，那么待机操作不显示。 | bool | readwrite |
| `hibernate` | 休眠 | 如果启用，那么休眠操作显示，如果禁用，那么休眠操作不显示。 | bool | readwrite |
| `switchUser` | 切换用户 | 0：总是显示切换用户按钮。1：按需显示切换用户按钮。2：禁用显示切换用户按钮 | int | readwrite |
| `systemSuspend` | 系统待机 | 0：启用。1：禁用。2：隐藏 | int | readwrite |
| `systemHibernate` | 系统待机 | 0：启用。1：禁用。2：隐藏 | int | readwrite |
| `systemShutdown` | 系统关机 | 0：启用。1：禁用。2：隐藏 | int | readwrite |
| `systemLock` | 系统锁屏 | 0：启用。1：禁用。2：隐藏 | int | readwrite |
| `systemReboot` | 系统重启 | 0：启用。1：禁用。2：隐藏 | int | readwrite |

## 读写示例

```bash
# 查询最大认证超时时间
dde-dconfig get -a org.deepin.dde.session-shell -r org.deepin.dde.session-shell -k authResetTime
# 设置最大认证超时时间为20秒（单位毫秒）
dde-dconfig set -a org.deepin.dde.session-shell -r org.deepin.dde.session-shell -k authResetTime -v 20000
# 查询系统关机按钮状态
dde-dconfig get -a org.deepin.dde.session-shell -r org.deepin.dde.session-shell -k systemShutdown
# 设置系统关机按钮隐藏
dde-dconfig set -a org.deepin.dde.session-shell -r org.deepin.dde.session-shell -k systemShutdown -v 2
```
