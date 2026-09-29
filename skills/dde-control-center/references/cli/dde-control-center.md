# dde-control-center 命令参考

DDE 控制中心主程序，是 DDE 桌面环境中用于系统设置管理的核心图形应用。

## 基本信息

| 字段 | 值 |
|------|------|
| 所属包名 | `dde-control-center` |
| 安装路径 | `/usr/libexec/deepin/dde-control-center` |
| DDE 角色 | 用户直接使用的系统设置 GUI 工具；同时被包括 dde-shell 在内的组件通过 DBus 调用以打开特定设置页 |

## 关于包装器与实际二进制

系统中存在两个与控制中心相关的可执行文件：

- **`/usr/bin/dde-control-center`**：bash 包装器脚本，通过 `deepin-security-loader` 启动控制中心，以获得调用受保护系统服务的授权。这是用户正常启动控制中心的入口。
- **`/usr/libexec/deepin/dde-control-center`**：真正的 ELF 二进制文件，是控制中心的实际程序。

通过包装器运行 `--help`、`--help-all`、`-v` 命令时不产生终端输出（security loader 在 Qt 初始化之前拦截）。如需获取完整的帮助或版本输出，应直接运行实际二进制文件：

```bash
/usr/libexec/deepin/dde-control-center --help
/usr/libexec/deepin/dde-control-center --help-all
/usr/libexec/deepin/dde-control-center -v
```

## 用途

DDE 控制中心主程序，是 DDE 桌面环境中用于系统设置管理的核心图形应用。它集成了数十个设置模块（显示、声音、网络、个性化、账户、电源、键盘鼠标、日期时间、更新），为用户提供统一的系统配置入口。在 DDE 中，它既是用户直接通过桌面快捷方式启动的 GUI 应用，也支持命令行参数来指定打开特定模块、以 DBus 模式运行或进行启动耗时调试。控制中心还支持插件机制，允许从指定目录加载第三方设置插件。

## 用法

`/usr/bin/dde-control-center [options]`

## 参数

| 选项 | 说明 | 是否需要值 |
|------|------|------------|
| `-h, --help` | 显示命令行帮助 | 否 |
| `--help-all` | 显示所有选项，包括 Qt 通用选项 | 否 |
| `-v, --version` | 显示版本信息 | 否 |
| `-s, --show` | 显示控制中心（默认隐藏） | 否 |
| `-t, --toggle` | 切换控制中心可见性 | 否 |
| `-d, --dbus` | 以 DBus 模式启动 | 否 |
| `-m <module>` | 指定要显示的模块 ID | 是 |
| `-p <page>` | 指定模块页面 | 是 |
| `-z, --time` | 显示控制中心启动耗时 | 否 |
| `-l, --logging-module <loggingModule>` | 仅输出指定模块的日志 | 是 |
| `--spec <plugindir>` | 从指定目录加载插件 | 是 |
| `--fd1 <fd1>` | fd1 from security loader | 是 |
| `--fd2 <fd2>` | fd2 from security loader | 是 |

## 使用示例

```bash
# 显示控制中心主界面
/usr/bin/dde-control-center -s

# 切换控制中心可见性（若已显示则隐藏，反之亦然）
/usr/bin/dde-control-center -t

# 直接打开"显示"设置模块
/usr/bin/dde-control-center -m display

# 打开"网络"模块的特定页面
/usr/bin/dde-control-center -m network -p 1

# 以 DBus 模式启动（供其他程序通过 DBus 调用控制中心）
/usr/bin/dde-control-center -d

# 显示启动耗时（用于性能调试）
/usr/bin/dde-control-center -s -z

# 仅输出 network 模块的日志（用于调试特定模块）
/usr/bin/dde-control-center -s -l network

# 从自定义目录加载插件
/usr/bin/dde-control-center --spec /opt/my-plugins/

# 查看命令行帮助（需使用实际二进制，包装器不产生输出）
/usr/libexec/deepin/dde-control-center --help

# 查看所有选项（包括 Qt 通用选项）
/usr/libexec/deepin/dde-control-center --help-all

# 查看版本信息
/usr/libexec/deepin/dde-control-center -v
```

> 注意：
> - `dde-control-center` 是图形应用，GUI 启动类操作（`-s`、`-t`、`-m`、`-d` 这些）需要图形显示环境（X11/Wayland），在无 DISPLAY 的终端中运行会报 Qt platform plugin 错误。
> - `/usr/bin/dde-control-center` 是 bash 包装器脚本，通过 `deepin-security-loader` 启动控制中心。通过包装器运行 `--help`、`--help-all`、`-v` 命令时不产生终端输出（security loader 在 Qt 初始化之前拦截），需使用 `/usr/libexec/deepin/dde-control-center` 获取完整的帮助和版本输出。
> - `QT_QPA_PLATFORM=offscreen` 环境变量无法解决包装器的输出问题，因为 security loader 在 Qt 初始化之前即拦截。
