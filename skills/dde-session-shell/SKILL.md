---
name: dde-session-shell
description: 提供锁屏程序启动、登录界面显示设置、登录界面亮度初始化、登录欢迎界面运行、手势密码重置的 CLI 命令，锁屏界面显示控制、关机界面显示控制、电源操作的 D-Bus 接口，快速登录开关的 DConfig 配置项
Categories:
  - Settings
---

# dde-session-shell

dde-session-shell 是 DDE 登录锁屏组件，提供锁屏程序、登录界面、关机界面的 CLI 命令工具，通过 Session 总线提供锁屏界面显示控制、关机界面显示控制和电源操作能力，并通过 DConfig 暴露快速登录开关配置。

## CLI 命令

### dde-lock

DDE 锁屏程序，是 DDE 桌面环境中负责屏幕锁定和用户切换的核心组件。

详见 [dde-lock.md](references/cli/dde-lock.md)

### reset-pattern-dialog

重置登录手势密码对话框，位于 `dde-session-shell/plugins/login-gesture/reset-pattern-dialog`。

详见 [reset-pattern-dialog.md](references/cli/reset-pattern-dialog.md)

### lightdm-deepin-greeter

DDE 登录界面（LightDM Greeter），是 deepin 定制的 LightDM 欢迎程序。

详见 [lightdm-deepin-greeter.md](references/cli/lightdm-deepin-greeter.md)

### greeter-display-setting

登录界面显示设置工具，用于在 LightDM 登录阶段配置显示相关参数（如分辨率、缩放）。

详见 [greeter-display-setting.md](references/cli/greeter-display-setting.md)

### lightdm-deepin-greeter-lighter

LightDM Deepin Greeter 的辅助程序，用于在登录过程中处理亮度调节初始化操作。

详见 [lightdm-deepin-greeter-lighter.md](references/cli/lightdm-deepin-greeter-lighter.md)


## D-Bus 接口

### 锁屏界面控制

提供锁屏界面显示、用户列表显示、认证状态控制和电源操作能力。

详见 [org.deepin.dde.LockFront1.md](references/dbus/org.deepin.dde.LockFront1.md)

### 关机界面控制

提供关机界面显示和电源操作能力。

详见 [org.deepin.dde.ShutdownFront1.md](references/dbus/org.deepin.dde.ShutdownFront1.md)

### 兼容接口

dde-session-shell 通过 Dual Q_CLASSINFO 机制同时注册新旧两套 D-Bus 服务名，旧版接口作为兼容别名保留，与新版接口共享同一实现，提供完全相同的功能。旧版接口仅供历史应用向后兼容使用，新代码应优先使用上述 `org.deepin.dde.LockFront1` 和 `org.deepin.dde.ShutdownFront1` 接口。

| 兼容服务名 | 对象路径 | 接口名 | 对应新版接口 | 说明 |
|---|---|---|---|---|
| `com.deepin.dde.lockFront` | `/com/deepin/dde/lockFront` | `com.deepin.dde.lockFront` | `org.deepin.dde.LockFront1` | 锁屏前端旧版兼容别名 |
| `com.deepin.dde.shutdownFront` | `/com/deepin/dde/shutdownFront` | `com.deepin.dde.shutdownFront` | `org.deepin.dde.ShutdownFront1` | 关机前端旧版兼容别名 |

## DConfig 配置项

dde-session-shell 通过 DConfig 暴露快速登录功能的开关配置。该配置由 lightdm-deepin-greeter 读取应用，非系统全局账户配置。

### 快速登录开关

控制是否启用快速登录功能，开启时开机后自动登录并进入锁屏状态。

详见 [org.deepin.dde.daemon.accounts](references/config/org.deepin.dde.daemon.accounts.md)
