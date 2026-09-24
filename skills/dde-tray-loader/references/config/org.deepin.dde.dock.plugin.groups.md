# org.deepin.dde.dock.plugin.groups

任务栏插件分组配置资源，管理托盘插件的分组列表，用于 `trayplugin-loader` 的 `--group` 选项按组加载插件。

## 配置项

| Key | Name | Description | 类型 | Permissions | Visibility |
|---|---|---|---|---|---|
| `selfMaintenanceTrayPlugins` | 自维护托盘插件列表 | 自维护托盘插件的路径列表，这些插件由 dde-tray-loader 自身维护，通过 `--group selfMaintenanceTrayPlugins` 加载 | string | readonly | private |
| `subprojectTrayPlugins` | 子项目托盘插件列表 | 子项目托盘插件的路径列表，通过 `--group subprojectTrayPlugins` 加载 | string | readwrite | private |
| `crashProneTrayPlugins` | 易崩溃托盘插件列表 | 易崩溃托盘插件的路径列表，通过 `--group crashProneTrayPlugins` 加载 | string | readwrite | private |

## 读写示例

```bash
# 查询子项目托盘插件列表
dde-dconfig get -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.groups -k subprojectTrayPlugins

# 设置子项目托盘插件列表
dde-dconfig set -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.groups -k subprojectTrayPlugins -v "/usr/lib/dde-tray-loader/plugins/sub1.so;/usr/lib/dde-tray-loader/plugins/sub2.so"

# 查询易崩溃托盘插件列表
dde-dconfig get -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.groups -k crashProneTrayPlugins

# 设置易崩溃托盘插件列表
dde-dconfig set -a org.deepin.dde.tray-loader -r org.deepin.dde.dock.plugin.groups -k crashProneTrayPlugins -v "/usr/lib/dde-tray-loader/plugins/crashprone.so"
```
