# org.deepin.ds.launchpad

启动器应用配置资源，控制 dde-launchpad 自身的应用列表排序、应用显示过滤、图标缩放比例和按桌面条目 ID 搜索行为。该配置资源挂载在 appId `org.deepin.dde.shell` 下（dde-launchpad 以 dde-shell applet 形式运行），仅作用于 dde-launchpad 自身应用行为，不影响系统全局配置。

## 配置项

| Key | Name | Description | 类型 | Permissions |
|---|---|---|---|---|
| `categoryType` | 应用排序类别 | 窗口模式下应用列表的排序类别。0: 首字母分组排序，1: DDE 风格分类，2: 自由排序 | number | readwrite |
| `compulsoryAppIdList` | 核心必要应用 ID 列表 | 需要被视为核心必要应用的 desktop ID 列表 | array | readonly |
| `excludeAppIdList` | 应用排除 ID 列表 | 需要使启动器排除（避免显示）的应用 desktop ID 列表 | array | readonly |
| `frequentlyUsedAppIdList` | 常用应用 ID 列表 | 「我的常用」中默认显示的应用 desktop ID 列表 | array | readonly |
| `searchByDesktopId` | 按桌面条目 ID 搜索 | 搜索时是否允许按桌面条目 ID 进行搜索 | bool | readwrite |
| `iconScaleFactor` | 图标缩放比例 | 全屏模式下应用图标的缩放比例 | number | readwrite |

## 读写示例

```bash
# 查询应用排序类别
dde-dconfig get -a org.deepin.dde.shell -r org.deepin.ds.launchpad -k categoryType
# 设置应用排序类别（0: 首字母分组, 1: DDE 分类, 2: 自由排序）
dde-dconfig set -a org.deepin.dde.shell -r org.deepin.ds.launchpad -k categoryType -v 1

# 查询是否按桌面条目 ID 搜索
dde-dconfig get -a org.deepin.dde.shell -r org.deepin.ds.launchpad -k searchByDesktopId
# 设置是否按桌面条目 ID 搜索
dde-dconfig set -a org.deepin.dde.shell -r org.deepin.ds.launchpad -k searchByDesktopId -v true

# 查询图标缩放比例
dde-dconfig get -a org.deepin.dde.shell -r org.deepin.ds.launchpad -k iconScaleFactor
# 设置图标缩放比例
dde-dconfig set -a org.deepin.dde.shell -r org.deepin.ds.launchpad -k iconScaleFactor -v 1.2

# 查询应用排除 ID 列表
dde-dconfig get -a org.deepin.dde.shell -r org.deepin.ds.launchpad -k excludeAppIdList
```
