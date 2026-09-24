# org.deepin.dde.lock

锁屏界面配置资源（appId: `org.deepin.dde.lock`），控制锁屏界面的背景、按钮显示、认证插件、提示信息、第三方定制行为，共 30 个配置项。

## 配置项

| Key | Name | Description | 类型 | Permissions |
|---|---|---|---|---|
| `useSolidBackground` | 使用纯色背景 | 是否使用纯色背景，默认为否。开启配置时，那么将不会加载背景图片，降低内存占用。禁用设置时，加载背景图片，比较美观，但是会增加内存占用。 | bool | readwrite |
| `autoExit` | 自动退出 | 是否自动退出，默认为否。开启配置时，那么隐藏界面一分钟就dde-lock进程将自动退出，降低内存占用。关闭配置时，应用将一直驻留在内存中，每次开启速度较快。 | bool | readwrite |
| `hideLogoutButton` | 隐藏注销按钮 | 锁屏界面隐藏注销按钮；false：不隐藏，true：隐藏。默认值为false，修改后即时生效。 | bool | readwrite |
| `hideOnboard` | 隐藏屏幕键盘 | 锁屏界面隐藏屏幕键盘；false：不隐藏，true：隐藏。默认值为false，修改后即时生效。 | bool | readwrite |
| `enableOneKeyLogin` | 是否加载华为自动登录插件 | 华为了电脑一键登录是否加载插件；false：不加载，true：加载。默认值为false； | bool | readwrite |
| `enableShortcutForLock` | 锁屏下启用的快捷键 | 锁屏下需要启用一些快捷键，修改后非即时生效 | array\<string\> | readonly |
| `showTopTip` | 是否显示顶部的提示信息，默认不开启 | 顶部提示信息一般用于定制项目，主线默认不开启 | bool | readwrite |
| `topTipText` | 顶部的提示信息的文案 | 顶部的提示信息的文案，不支持多语言 | string | readwrite |
| `showUserName` | 锁屏是否展示用户名 | 锁屏是否展示用户名，默认不展示 | bool | readwrite |
| `topTipTextFont` | 顶部的提示信息的文案的字体大小 | 顶部的提示信息的文案的字体大小，默认为5，有效值为0~9，数字越大字体越小。 | int | readwrite |
| `userFrameMaxWidth` | 用户名界面最大宽度 | 显示用户名界面的最大宽度，默认为226，小于226不生效。开启后根据用户名长度调整宽度，如果无法完整显示则用省略号补充。 | int | readwrite |
| `fullNameFont` | 全名的字体大小 | 设置全名的字体大小，默认为5，有效值为0~9，数字越大字体越小。 | int | readwrite |
| `pluginBlackList` | 插件黑名单 | 插件黑名单（包括托盘插件和认证插件），在加载插件的阶段进行判断。系统级配置，默认为空，需要重启电脑。数据结构为数组，内部填充字符串（插件的key值） | array | readwrite |
| `customLogoPath` | 第三方系统logo水印路径 | 第三方系统logo水印路径,图片最大不超过500k | string | readwrite |
| `customLogoPos` | 第三方系统logo水印位置 | 第三方系统logo水印位置，系统LOGO右上角为原点,(10,0)表示 OEM LOGO 在系统LOGO右侧水平间隔10像素 | string | readwrite |
| `showSystemVersion` | 是否显示系统版本 | 系统版本显示；false：不显示，true：显示。默认值为true； | bool | readwrite |
| `systemVersionText` | 自定义系统版本信息 | 登录/锁屏界面左下角logo右侧显示的系统版本及类型信息；为空时显示系统默认的版本号+系统类型，不为空时显示配置的文本内容。 | string | readwrite |
| `delayInhibitIgnoreList` | 延迟关机忽略列表 | 延迟关机忽略列表内的应用不在阻止关机列表中显示 | array | readwrite |
| `designatedLoginPlugin` | 指定的认证插件 | 指定使用哪一种认证插件，优先级最高。默认为空，重启后生效。（**deprecated**）此配置不推荐使用，使用 designatedLoginPlugins 配置替代 | string | readwrite |
| `defaultLoginPlugin` | 默认的认证插件 | 默认使用的认证插件，默认为空，重启后生效。（**deprecated**）此配置不推荐使用，使用 defaultLoginPlugins 配置替代 | string | readwrite |
| `designatedLoginPlugins` | 指定的认证插件 | 指定使用的认证插件，优先级最高，会覆盖 defaultLoginPlugins 的值。类型：字符串数组，内部填充插件的 key 值。默认值：空数组。生效时机：重启后生效 | array | readwrite |
| `defaultLoginPlugins` | 默认的认证插件 | 默认使用的认证插件，优先级次于 designatedLoginPlugins。类型：字符串数组，内部填充插件的 key 值。默认值：空数组。生效时机：重启后生效 | array | readwrite |
| `loginPluginsDisplayOrder` | 认证插件展示的顺序 | 认证插件的显示顺序。类型：字符串数组，内部填充插件的 key 值。默认值：空数组。生效时机：重启后生效 | array | readwrite |
| `loginPluginsAuthOrder` | 认证插件认证的顺序 | 认证插件的认证优先级，此配置优先级最高，会覆盖其它的优先级设置。类型：字符串数组，内部填充插件的 key 值。默认值：空数组。生效时机：重启后生效 | array | readwrite |
| `enableShellBlack` | 是否打开shell的黑屏模式 | 是否打开shell的黑屏模；false：不开，true：开启。默认值为true； | bool | readwrite |
| `visibleShutdownWhenRebootOrShutdown` | 是否在shutdown页面点击关机或重启时隐藏shutdown页面 | 是否在shutdown页面点击关机或重启时，隐藏shutdown页面；false：隐藏，true：不隐藏。默认值为true； | bool | readwrite |
| `showMediaWidget` | 是否显示多媒体控制界面 | 是否显示多媒体控制界面，true-显示，false-隐藏 | bool | readwrite |
| `accountExpression` | 账户名命名规则 | 账户名命名规则 | string | readwrite |
| `longPressDisplayPassword` | 是否长按小眼睛显示密码 | 是否长按小眼睛显示密码，true-鼠按长按小眼睛才显示密码，false-鼠标点击一下就一直显示密码 | bool | readwrite |
| `enableShutdownBlackWidget` | 是否打开关机、重启黑屏界面 | 是否打开关机、重启黑屏界面；false：不开，true：开启。默认值为true； | bool | readwrite |

## 读写示例

```bash
# 查询锁屏是否使用纯色背景
dde-dconfig get -a org.deepin.dde.lock -r org.deepin.dde.lock -k useSolidBackground
# 设置锁屏使用纯色背景
dde-dconfig set -a org.deepin.dde.lock -r org.deepin.dde.lock -k useSolidBackground -v true
# 查询锁屏是否隐藏注销按钮
dde-dconfig get -a org.deepin.dde.lock -r org.deepin.dde.lock -k hideLogoutButton
# 设置锁屏隐藏注销按钮
dde-dconfig set -a org.deepin.dde.lock -r org.deepin.dde.lock -k hideLogoutButton -v true
```
