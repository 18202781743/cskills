# xdg-desktop-portal-dde 命令参考

xdg-desktop-portal-dde 自身的后台服务进程，为沙箱应用（如 Flatpak）提供访问系统资源（文件选择、屏幕截图、屏幕共享）的 DBus 接口。

## 基本信息

| 字段 | 值 |
|------|------|
| 所属包名 | `xdg-desktop-portal-dde` |
| 安装路径 | `/usr/libexec/xdg-desktop-portal-dde` |
| DDE 角色 | 沙箱应用访问系统资源的 Portal 后端 |

## 用途

xdg-desktop-portal-dde 自身的后台服务进程，为沙箱应用（如 Flatpak）提供访问系统资源（文件选择、屏幕截图、屏幕共享）的 DBus 接口。它由 DBus 在沙箱应用请求系统服务时自动激活，是 DDE 沙箱应用生态的门户组件，一般不需要用户直接运行。

## 用法

`/usr/libexec/xdg-desktop-portal-dde [options]`

> 注：该二进制不在默认 PATH 中，需使用完整路径执行。

## 选项

| 选项 | 说明 | 是否需要值 |
|------|------|------------|
| `-h, --help` | 显示帮助信息 | 否 |
| `-v, --version` | 显示版本信息 | 否 |

## 使用示例

```bash
# 查看版本信息
/usr/libexec/xdg-desktop-portal-dde --version

# 查看帮助信息
/usr/libexec/xdg-desktop-portal-dde --help
```

> 注意：`xdg-desktop-portal-dde` 是 Portal 后端守护进程，由 DBus 在沙箱应用请求系统服务时自动激活，通常无需手动运行。
