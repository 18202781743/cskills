# dde-polkit-agent 命令参考

DDE 的 PolicyKit 认证代理守护进程，负责在用户执行需要特权的操作时弹出图形认证对话框，收集用户密码或指纹认证信息，是 DDE 权限管理的前端组件。

## 基本信息

| 字段 | 值 |
|------|------|
| 所属包名 | `dde-polkit-agent` |
| 安装路径 | `/usr/lib/polkit-1-dde/dde-polkit-agent` |
| DDE 角色 | PolicyKit 图形化认证代理 |

## 启动方式

`dde-polkit-agent` 由 systemd 用户服务 `dde-polkit-agent.service` 在用户会话初始化时自动启动，无需手动运行。该服务在 `dde-session-initialized.target` 之前启动，依赖于 `dde-session-core.target`。

服务单元文件位于 `/usr/lib/systemd/user/dde-polkit-agent.service`，`ExecStart` 指向 `/usr/lib/polkit-1-dde/dde-polkit-agent`。

## 用法

`/usr/lib/polkit-1-dde/dde-polkit-agent [options]`

> 注：该二进制不在默认 PATH 中，需使用完整路径执行。

## 选项

| 选项 | 说明 | 是否需要值 |
|------|------|------------|
| `-h, --help` | 显示帮助信息（DApplication 标准选项） | 否 |
| `-v, --version` | 显示版本信息（DApplication 标准选项） | 否 |

> 注意：`--help` 和 `--version` 是 DApplication 框架提供的标准命令行选项。由于 `dde-polkit-agent` 在启动时会先注册 polkit 监听器，注册成功后才进入事件循环处理命令行参数，因此在非图形会话环境（无 DISPLAY）中直接运行时，程序会在监听器注册阶段失败退出，无法正常处理这两个选项。

## 使用示例

```bash
# 查看版本信息（需要在图形会话环境中运行）
/usr/lib/polkit-1-dde/dde-polkit-agent --version

# 查看帮助信息（需要在图形会话环境中运行）
/usr/lib/polkit-1-dde/dde-polkit-agent --help
```

> 注意：`dde-polkit-agent` 是图形认证代理守护进程，需要图形显示环境（X11/Wayland）和有效的用户会话。通常由 systemd 用户服务自动启动，无需手动运行。在无图形显示的终端中直接启动会因 polkit 监听器注册失败而退出。
