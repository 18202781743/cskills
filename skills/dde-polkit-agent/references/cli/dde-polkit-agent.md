# dde-polkit-agent 命令参考

DDE 的 PolicyKit 认证代理，负责在用户执行需要特权的操作时弹出认证对话框。

## 基本信息

| 字段 | 值 |
|------|------|
| 所属包名 | `dde-polkit-agent` |
| 安装路径 | `/usr/lib/polkit-1-dde/dde-polkit-agent` |
| DDE 角色 | PolicyKit 图形化认证代理 |

## 用途

DDE 的 PolicyKit 认证代理，负责在用户执行需要特权的操作时弹出认证对话框。它监听 polkit 的认证请求，通过图形界面收集用户密码或指纹认证信息，是 DDE 权限管理的前端组件。该程序在用户会话启动时自动运行，由 DBus 激活。

## 用法

`/usr/lib/polkit-1-dde/dde-polkit-agent [options]`

> 注：该二进制不在默认 PATH 中，需使用完整路径执行。

## 选项

| 选项 | 说明 | 是否需要值 |
|------|------|------------|
| `-h, --help` | 显示帮助信息 | 否 |
| `-v, --version` | 显示版本信息 | 否 |

## 使用示例

```bash
# 查看版本信息
/usr/lib/polkit-1-dde/dde-polkit-agent --version

# 查看帮助信息
/usr/lib/polkit-1-dde/dde-polkit-agent --help
```

> 注意：`dde-polkit-agent` 是图形认证代理守护进程，需要图形显示环境（X11/Wayland），通常由会话管理器自动启动，无需手动运行。在无 DISPLAY 的终端中直接启动会失败。
