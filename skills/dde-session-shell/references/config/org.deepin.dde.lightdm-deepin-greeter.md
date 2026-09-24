# org.deepin.dde.lightdm-deepin-greeter

登录界面配置资源（appId: `org.deepin.dde.lightdm-deepin-greeter`），控制登录界面的桌面环境切换、小键盘状态、缩放比例、认证插件、第三方定制行为，共 31 个配置项。

## 配置项

| Key | Name | Description | 类型 | Permissions |
|---|---|---|---|---|
| `useSolidBackground` | 使用纯色背景 | 是否使用纯色背景，默认为否。开启配置时，那么将不会加载背景图片，降低内存占用。禁用设置时，加载背景图片，比较美观，但是会增加内存占用。 | bool | readwrite |
| `allowSwitchingToWayland` | 允许用户切换到wayland | 是否允许用户切换到wayland，默认为否。开启配置时，如果用户安装了wayland和其它桌面环境，登录界面会显示桌面环境切换按钮，点击后用户可以选择wayland桌面环境。关闭配置时，就算用户安装了wayland环境，也会默认隐藏起来，不让用户切换到wayland环境 | bool | readwrite |
| `defaultSession` | 默认桌面环境名称 | 默认的桌面环境名称，默认为deepin。新建用户首次登录的时候，默认的桌面由此配置决定 | string | readwrite |
| `numLockState` | 数字键盘状态 | 用户的小键盘状态，True为打开，False为关闭，与用户绑定，格式为："用户名:状态"，例如"uos:True"。当用户改变状态时会记录下来，切换用户时会跟随用户改变。 | array | readwrite |
| `hideOnboard` | 隐藏屏幕键盘 | 登录界面隐藏屏幕键盘；false：不隐藏，true：隐藏。默认值为false； | bool | readwrite |
| `enableOneKeyLogin` | 是否加载华为自动登录插件 | 华为了电脑一键登录是否加载插件；false：不加载，true：加载。默认值为false； | bool | readwrite |
| `defaultScaleFactors` | 登录页面默认缩放 | 配置greeter界面默认的缩放比例 | int | readwrite |
| `showTopTip` | 是否显示顶部的提示信息，默认不开启 | 顶部提示信息一般用于定制项目，主线默认不开启 | bool | readwrite |
| `topTipText` | 顶部的提示信息的文案 | 顶部的提示信息的文案，不支持多语言 | string | readwrite |
| `showUserName` | 锁屏是否展示用户名 | 锁屏是否展示用户名，默认不展示 | bool | readwrite |
| `changePasswordForNormalUser` | 密码过期后普通用户是否可以在登录界面修改密码 | 密码过期后普通用户是否可以在登录界面修改密码，默认允许 | bool | readwrite |
| `topTipTextFont` | 顶部的提示信息的文案的字体大小 | 顶部的提示信息的文案的字体大小，默认为5，有效值为0~9，数字越大字体越小。 | int | readwrite |
| `userFrameMaxWidth` | 用户名界面最大宽度 | 显示用户名界面的最大宽度，默认为226，小于226不生效。开启后根据用户名长度调整宽度，如果无法完整显示则用省略号补充。 | int | readwrite |
| `fullNameFont` | 全名的字体大小 | 设置全名的字体大小，默认为5，有效值为0~9，数字越大字体越小。 | int | readwrite |
| `defaultGreeterSession` | Greeter以x还是wayland的模式启动 | Greeter以x还是wayland的模式启动，目前仅x和wayland两种模式.部分机型不适用，修改后可能导致登录黑屏，谨慎修改 | string | readwrite |
| `enableLighterGreeter` | 是否启用轻量Greeter | 是否启用轻量Greeter | bool | readwrite |
| `lastUser` | 上一次登录的用户 | 上一次登录的用户，LighterGreeter登录后会保存登录的用户到此配置项目中(避免对外部服务依赖，自行存储)，用于下次登录时选择为默认用户 | string | readwrite |
| `pluginBlackList` | 插件黑名单 | 插件黑名单（包括托盘插件和认证插件），在加载插件的阶段进行判断。系统级配置，默认为空，需要重启电脑。数据结构为数组，内部填充字符串（插件的key值） | array | readwrite |
| `customLogoPath` | 第三方系统logo水印路径 | 第三方系统logo水印路径,图片最大不超过500k | string | readwrite |
| `customLogoPos` | 第三方系统logo水印位置 | 第三方系统logo水印位置，系统LOGO右上角为原点,(10,0)表示 OEM LOGO 在系统LOGO右侧水平间隔10像素 | string | readwrite |
| `showSystemVersion` | 是否显示系统版本 | 系统版本显示；false：不显示，true：显示。默认值为true； | bool | readwrite |
| `systemVersionText` | 自定义系统版本信息 | 登录/锁屏界面左下角logo右侧显示的系统版本及类型信息；为空时显示系统默认的版本号+系统类型，不为空时显示配置的文本内容。 | string | readwrite |
| `designatedLoginPlugin` | 指定的认证插件 | 指定使用哪一种认证插件，优先级最高。默认为空，重启后生效。（**deprecated**）此配置不推荐使用，使用 designatedLoginPlugins 配置替代 | string | readwrite |
| `defaultLoginPlugin` | 默认的认证插件 | 默认使用的认证插件，默认为空，重启后生效。（**deprecated**）此配置不推荐使用，使用 defaultLoginPlugins 配置替代 | string | readwrite |
| `designatedLoginPlugins` | 指定的认证插件 | 指定使用的认证插件，优先级最高，会覆盖 defaultLoginPlugins 的值。类型：字符串数组，内部填充插件的 key 值。默认值：空数组。生效时机：重启后生效 | array | readwrite |
| `defaultLoginPlugins` | 默认的认证插件 | 默认使用的认证插件，优先级次于 designatedLoginPlugins。类型：字符串数组，内部填充插件的 key 值。默认值：空数组。生效时机：重启后生效 | array | readwrite |
| `loginPluginsDisplayOrder` | 认证插件的优先级 | 认证插件的显示顺序。类型：字符串数组，内部填充插件的 key 值。默认值：空数组。生效时机：重启后生效 | array | readwrite |
| `loginPluginsAuthOrder` | 认证插件的优先级 | 认证插件的认证优先级，此配置优先级最高，会覆盖其它的优先级设置。类型：字符串数组，内部填充插件的 key 值。默认值：空数组。生效时机：重启后生效 | array | readwrite |
| `showMediaWidget` | 是否显示多媒体控制界面 | 是否显示多媒体控制界面，true-显示，false-隐藏 | bool | readwrite |
| `accountExpression` | 账户名命名规则 | 账户名命名规则 | string | readwrite |
| `longPressDisplayPassword` | 是否长按小眼睛显示密码 | 是否长按小眼睛显示密码，true-鼠按长按小眼睛才显示密码，false-鼠标点击一下就一直显示密码 | bool | readwrite |

## 读写示例

```bash
# 查询是否允许切换到wayland
dde-dconfig get -a org.deepin.dde.lightdm-deepin-greeter -r org.deepin.dde.lightdm-deepin-greeter -k allowSwitchingToWayland
# 设置允许切换到wayland
dde-dconfig set -a org.deepin.dde.lightdm-deepin-greeter -r org.deepin.dde.lightdm-deepin-greeter -k allowSwitchingToWayland -v true
# 查询默认桌面环境名称
dde-dconfig get -a org.deepin.dde.lightdm-deepin-greeter -r org.deepin.dde.lightdm-deepin-greeter -k defaultSession
# 设置默认桌面环境名称
dde-dconfig set -a org.deepin.dde.lightdm-deepin-greeter -r org.deepin.dde.lightdm-deepin-greeter -k defaultSession -v deepin
```
