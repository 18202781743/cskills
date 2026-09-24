# trayplugin-loader 命令参考

DDE 托盘插件加载器，负责加载和管理系统托盘区域的插件。

## 基本信息

| 字段 | 值 |
|------|------|
| 所属包名 | `dde-tray-loader` |
| 安装路径 | `/usr/libexec/trayplugin-loader` |
| DDE 角色 | 系统调用的辅助工具，由 dde-shell 在会话启动时自动拉起 |

## 用途

DDE 托盘插件加载器，负责加载和管理系统托盘区域的插件。它根据指定的插件路径和组名，将托盘插件动态加载到 DDE 面板的托盘区域中。该工具通常由 dde-shell 或面板管理进程在会话启动时自动调用，一般不需要用户直接运行。支持按组名分组加载插件，适用于多面板或多区域托盘场景。

## 用法

`/usr/libexec/trayplugin-loader [options] -p <plugin path(s)>`

> **注意**：`-p` 参数为必填项，未指定时程序将显示帮助信息并退出。该工具需要运行中的图形显示环境（Wayland 或 X11），无显示环境时无法启动。

## 参数

| 选项 | 说明 | 是否需要值 |
|------|------|------------|
| `-h, --help` | 显示命令行帮助 | 否 |
| `-v, --version` | 显示版本信息 | 否 |
| `-p <plugin path(s)>` | 插件路径，单个或多个（用 `;` 分隔） | 是（必填） |
| `-g <group name>` | 指定插件路径的组名 | 是 |

## 使用示例

```bash
# 加载单个托盘插件
/usr/libexec/trayplugin-loader -p /usr/lib/dde-tray-loader/plugins/mytray.so

# 加载多个托盘插件（用分号分隔路径）
/usr/libexec/trayplugin-loader -p /usr/lib/dde-tray-loader/plugins/tray1.so;/usr/lib/dde-tray-loader/plugins/tray2.so

# 加载插件并指定组名（用于面板分组显示）
/usr/libexec/trayplugin-loader -p /usr/lib/dde-tray-loader/plugins/mytray.so -g panel-tray

# 查看版本信息
/usr/libexec/trayplugin-loader --version
```
