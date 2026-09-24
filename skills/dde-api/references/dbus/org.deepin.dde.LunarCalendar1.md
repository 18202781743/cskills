# org.deepin.dde.LunarCalendar1 接口参考

该接口提供农历日历查询能力，用于获取农历日期信息。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.LunarCalendar1` |
| Object path | `/org/deepin/dde/LunarCalendar1` |
| Interface | `org.deepin.dde.LunarCalendar1` |
| Bus | Session |

## 兼容性说明

该接口为历史遗留接口，其 `.service` 激活文件（`misc/services/org.deepin.dde.LunarCalendar1.service`）中的 `Exec` 行已被注释掉，当前无法通过 D-Bus 自动激活。dde-api 仓库中已无对应的源码实现目录，表明该功能已废弃。保留 `.service` 文件仅供兼容性参考，不建议在新代码中使用。
