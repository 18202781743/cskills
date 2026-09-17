# 工时系统接口记录

来源：用户提供的 `oa.uniontech.com.har`，浏览器抓包于 2026-09-17。这里只记录接口结构与状态转换，不保存任何身份、凭据或工作内容。接口可能随系统升级变化，执行时以当前登录页面为准。

2026-09-17 的实际填报纠错还确认：同一项目任务的工作内容框可能显示上周文字；直接追加当天内容会把跨周文字一并提交。下述按周过滤规则来自该次实际操作，接口字段及状态转换仍以 HAR 为依据。

考勤日历字段另据用户提供的本机 HAR 核对。原始 HAR 含敏感会话及个人数据，不随 skill 分发。下面只记录字段名、类型与用户给定的计算规则。

## 入口与认证

OA 页面打开 `/wui/ChanYanWorkHour.html` 后跳转到 `https://bi.uniontech.com/oa_work_hours/cy?gh=...`。BI 请求带 `token` 请求头；登录接口为 `POST /oa-bi/sys/workHourUser`，请求体包含 `loginName`，响应包含 `token`。不要从历史 HAR 提取并重放这些值。

## 共享认证流程

Codex 命令进程不会自动获得浏览器 Cookie。`uos-pms-bug-workflow-trigger` 的实现使用 `UNIONTECH_OA_CONFIG_DIR` 指定目录，默认 `~/.config/uniontech-oa`；其中 `key.bin` 是 Fernet 密钥，`default.json` 含 `loginid` 和 `password_encrypted`。本 skill 的 `scripts/auth_session.py` 兼容该存储格式，只在内存中解密，绝不输出账号密码或将 token 写入磁盘。

先运行 `python scripts/auth_session.py check`：读取共享凭据，`POST https://oa.uniontech.com/api/hrm/login/checkLogin` 重新登录，`GET /api/portal/account/getAccount` 验证 OA 会话，`GET /api/uniontech/marketbudget/getUserRedirectBi?flags=1` 取得本次加密登录参数，再 `POST https://bi.uniontech.com/oa-bi/sys/workHourUser` 换取 BI token。调用端在同一进程中执行 `authenticate_shared()`，返回 OA Session、BI token、用户信息；OA 请求用 Session，BI 请求加 `token` 头。两者不能互换。每次使用前重新认证和验证，不把浏览器 Cookie 或历史 HAR token 当成可复用凭据。

共享凭据不存在、解密失败或登录失败时，在有交互终端运行 `python scripts/auth_session.py setup`。它用 `getpass` 获取 OA/LDAP 密码，只有 OA 和 BI 均认证成功才写入与 PMS 兼容的加密凭据文件，权限 `0600`。终端不可安全交互时请用户自行完成这一步；不要让用户把密码发到聊天或写进命令行参数。当前环境的通用 HTTPS 代理会导致内部 OA TLS 失败，脚本默认直连，必要时可通过 `AI_UT_PROXY` 指定可用代理。网络或证书错误不能靠禁用证书校验掩盖。

## 读取

| 方法 | 路径 | 用途/参数 |
| --- | --- | --- |
| GET | `/oa-bi/sys/sysholidaylessonwork/selectHolidayList` | `startDate`, `endDate`，查询节假日 |
| GET | `/oa-bi/sys/sysworkhour/getWorkHourAttendance` | `startDate`, `endDate`，查询考勤 |
| GET | `/oa-bi/sys/sysworkhour/getWorkHourWeekOrLastWeek` | `sourceType`, `flag`, `startDate`, `endDate`，查询周工时；结果每个任务包含 `one` 至 `seven` 的日记录 |
| GET | `/oa-bi/sys/workHourReportForm/getCalendarWorkHourGroupByUserAndDate` | `startDate`, `endDate`, `sourceType`，查询每日应填、已填、草稿和审批小时数 |
| POST | `/oa-bi/sys/sysworkhour/getProjectTaskFromOA` | JSON 查询项目任务；抓包包含 `pageSize`, `pageIndex`, `taskName`, `projectName`, `projectStageName`, `approveNameOne`, `taskIds`, `taskStatus` |
| GET | `/oa-bi/sys/sysworkapproverecord/list` | `pageIndex`, `pageSize`, `startDate`, `endDate`, `flag`, `sourceType`，查询审批记录 |
| POST | `https://oa.uniontech.com/api/kq/myattendance/getHrmKQMonthReportInfo` | 表单字段 `typevalue=YYYY-MM`, `loaddata=1`, `type=2` 是本次 HAR 样本；读取考勤月历，参数须以当前会话请求为准 |

BI 工时接口响应外层为 `code`, `msg`，成功样本是 `code: 0`, `msg: "success"`。项目任务查询的 `result.list` 包含项目和任务 ID、代码、名称、阶段、默认工作内容、审批人等字段；选择时以当前响应为准。OA 考勤月历使用 `api_status` 表示请求状态，不能用 BI 的 `code=0` 判定。

OA 考勤月历的响应结构与 BI 工时接口不同：`result` 以当月日期数字字符串为键；每日记录有 `date`、`isWorkDay`、`signInfo`、`workflow`。`signInfo` 中的 `title` 为“上班打卡”或“下班打卡”，`signTime` 可为 `HH:MM:SS`，也可能为“未打卡”。`workflow` 可能含请假/调休流程，`title` 可是 HTML 链接；只提取可见流程类型，不能将链接或内部 ID 写入汇报。`getWorkHourAttendance` 只用于核对 BI 应填/请假等数据，不替代 OA 月历的实际打卡时间。

## 考勤打卡与工时计算

对每个目标工作日，按 `date` 找到月历记录，要求 `isWorkDay=true`，且能唯一取得有效的上班与下班打卡。本次 HAR 的 `signInfo` 只有各一条；若未来出现多条、跨日或无法识别的记录，先请用户确认，不能自行择取。

用户给定规则将正常下班时间视为上班打卡后 9 小时（8 小时工作 + 1 小时午休）。设 `span = 下班打卡 - 上班打卡`，`extra = span - 9 小时`：

| 条件 | 拟填工作时长 | 处理 |
| --- | --- | --- |
| 缺任一打卡、`未打卡`、顺序异常、非工作日 | 不计算 | 核查请假/漏卡并请用户明确 |
| `span < 9h` | 不计算 | 查看当日 `workflow` 是否有请假/调休；提醒用户并请其明确实际工时 |
| 当日有请假/调休记录 | 不自动计算 | 即使打卡完整也先核对实际工时 |
| `9h ≤ span < 12h` | `8.0h` | 距正常下班未满 3 小时，不计加班 |
| `span ≥ 12h` | `8h + (extra - 1h)` | 距正常下班满 3 小时才计加班，再扣 1 小时吃饭 |

“超过 3 小时”的边界按用户给出的 09:00—21:00 示例解释为**满 3 小时（含）**：09:00—21:00 的跨度为 12 小时，正常下班 18:00，额外 3 小时扣 1 小时吃饭，拟填 `10.0h`。09:00—20:59 仍拟填 `8.0h`。最终工作时长用十进制四舍五入到 1 位小数；例如跨度 12 小时 5 分钟，拟填 `10.1h`。此为用户指定的填报规则，遇系统节假日、排班或考勤校验冲突时先停下核实，不绕过系统限制。

可用 `scripts/calculate_hours.py --date YYYY-MM-DD` 从**当前 API 响应的标准输入**计算候选值。脚本只输出指定日期的打卡时间、候选工时或复核原因，不输出流程链接、请求 ID 或身份字段。若输出 `status=review`，不能直接保存该日，需用户明确实际工时。

若用户原先给出的小时数与考勤计算值不同，预览同时列出两者并请用户确认。确认异常日期的实际工时后可以采用用户明确给出的值，注明“用户确认”；不得把异常自动归为 8 小时。

## 保存与提交

两次页面操作均调用 `POST /oa-bi/sys/sysworkhour/save`，JSON 顶层是数组。一次保存包含同一任务对应周内多天的条目；抓包中的两条有时长，两条周末空值。不要把空值条目当成已填工时，也不要推断发送部分数组是否会影响同周其他条目；优先由页面生成请求。

单条抓包字段：`id`, `submitNew`, `approveIdOne`, `approveNameOne`, `projectId`, `projectCode`, `projectName`, `taskId`, `taskName`, `taskCode`, `taskType`, `workContent`, `projectStageType`, `projectStageName`, `sourceType`, `workHourDay`, `hours`, `firstDayWeek`, `lastDayDeek`, `processCode`, `status`, `startLog`, `saveUpdateFlag`。其中 `lastDayDeek` 是页面实际字段名，不要改拼写。周范围为周一到周日。

观察到的状态转换：

| 操作 | `id` | `status` | `startLog` | `saveUpdateFlag` | 回读 |
| --- | --- | ---: | ---: | ---: | --- |
| 首次保存 | `null` | 0 | 0 | 0 | `one` 至 `seven` 对应日期出现新 `id`，状态 `"0"` |
| 随后提交 | 保存后得到的 `id` | 1 | 1 | 1 | 同一 `id` 的状态变为 `"1"` |

两次写请求的成功响应均为 `{"msg":"success","code":0}`。提交请求中已有记录的小时数是字符串，例如 `"8.00"`；首次保存时是数值。`submitNew` 在样本中为 `"new"`；`sourceType` 在首次保存为数字 `0`，提交时已有记录为字符串 `"0"`。这些是抓包观察值，不代表所有项目、来源或页面版本的固定要求。不要凭本记录推断其他状态码的含义。

## 重复记录排查

2026-09-17 的实际调用出现过：以 `id=null` 保存项目 2454、任务 4176、日期 2026-09-17 时，接口返回 `code=500` 且提示该项目/任务/日期不允许重复；随后某些周查询及按日期查询返回空列表。这说明新建请求被拒绝，**不能仅凭空列表判断数据库不一致**，也不能重复发送相同的新建请求。空列表可能受 `sourceType`、`flag`、日期范围、审批状态或接口用法影响；当前证据尚未确定具体原因。

默认排查顺序：核对目标周一至周日和当前页面使用的 `sourceType`、`flag`；查询周工时中该任务的 `one` 至 `seven`，再查日历汇总、审批记录及当前页面实际使用的查询请求。对照项目/任务 ID、目标日期、记录 ID 和状态。若找到可编辑草稿，沿用该记录 ID 与当前响应字段，将本次工作内容合并到目标周文本，再调用已验证的更新形式保存并回读。不能把 `id=null` 的新建请求当作续写。若现有记录已提交、审批中、查询仍找不到 ID，或更新字段无法验证，停止写入并报告已尝试的查询及缺少的字段；不要让用户仅因一次空列表就自行查 OA。

## 按周工作内容

`workContent` 是任务行中的工作内容文本，不能假设当前显示的内容只属于所选周。同一任务可持续数周或数月；任务通常沿用此前确认的默认值，不根据工作描述中的产品名或技术词换任务。先以目标日期计算周一和周日，再按日期筛选工作内容；只保留目标周内的有效行。工作内容按**天**记录，通常使用 `YYYY-MM-DD 工作内容，`，按日期升序排列，一日一行；同日多个事项用分号合并，不要求拆成逐小时记录。用户只给出其中一天时，只写该天；不要为其余日期编造内容或工时。例如目标周为 2026-09-07 至 2026-09-13、用户只提供 9 月 7 日时：

```text
2026-09-07 DTK 中 QML 应用 V25 样式适配，
```

如果用户明确要求工作日范围，可在预览中写 2026-09-07 至 2026-09-11；接口的 `firstDayWeek` / `lastDayDeek` 仍使用完整的周一至周日。9 月 8 日至 11 日没有用户提供内容时保持空白。跨周沿用的旧文字只从**目标周将要保存的文本**中移除，不删除上周已经提交的工时记录。同一周其他日期或任务已有有效文字时，按记录 ID 和日期保留，不把整周重置成单日内容。

“帮我写今天的周报，内容是分析 v20 更新失败问题，修改 deepin-home 适配 qt6 的问题”这类说法要进入完整填报流程。以查询当日所在周为准，将当天内容规范为一行，例如：

```text
2026-09-17 分析 V20 更新失败问题；修改 deepin-home 的 Qt 6 适配问题，
```

这里的日期只是格式示例，实际执行必须按 `Asia/Shanghai` 当天日期生成。不得把“分析”写成“已解决”，也不得把“修改”扩写为未经用户说明的验收结果。同日两个事项仍可记在此前确认的同一任务下，填该日总工时；仅当用户明确要求分属不同任务时，才核对各任务的小时数。

## API 执行顺序

1. 使用当前有效会话查询 `getWorkHourAttendance`、`getWorkHourWeekOrLastWeek` 和 `getProjectTaskFromOA`；优先核对此前确认的默认任务仍有效，再用响应中的项目、任务、阶段、审批人及现有 ID 确认目标。工作内容关键词不决定任务。已提交/审批中的记录不直接覆盖。
2. 按目标周组装 `workContent` 与逐日小时数，核对周范围、日期、项目、任务、阶段、打卡起止时间、计算依据、拟填工时、异常提醒和工作内容全文。`status=review` 的日期须先取得用户明确时长。不要只展示新增的一行而隐藏同一 `workContent` 中的其他行。必要信息明确后在本轮直接保存草稿，不因展示预览暂停，也不询问是否保存；用户补充内容时重新查询并组装。

   ```text
   待填报周：YYYY-MM-DD 至 YYYY-MM-DD
   项目 / 任务 / 阶段：… / … / …
   考勤与拟填工时：YYYY-MM-DD 上班 HH:MM、下班 HH:MM、拟填 N.N 小时；…
   异常及待确认项：无 / 日期与原因
   工作内容（将原样保存）：
   YYYY-MM-DD 内容，
   已执行：保存草稿并回读
   如需提交：等待用户单独确认。
   ```
3. 先按项目、任务和日期查找已有记录。已有可编辑草稿就沿用其 ID 更新，无记录才新建；重复数据报错按“重复记录排查”处理。调用 `save` 时传入当前响应确认的完整字段，不用固定任务代码、固定审批人或不明来源的默认值。重新查询该周，核对日期、ID、小时数、工作内容全文及状态 `"0"`。回读还须确认目标周旧有效条目未丢失、仅新增本次条目且跨周文字已从目标周文本清除。
4. 草稿回读成功后报告结果；用户随后单独明确确认提交，才沿用回读得到的 ID 和当前字段，以 `status=1`、`startLog=1`、`saveUpdateFlag=1` 调用 `save`。即使原请求说“保存并提交”或“直接提交”，也先保存草稿并回读，再询问是否提交。再次查询，确认相同 ID 的状态为 `"1"`。两次写入间不能仅凭 `code=0` 继续。
5. 如需更正已提交记录，先确认当前 API 存在并允许撤回操作；本 HAR 没有记录撤回接口，因此不能凭该文档构造撤回请求。撤回后重新读取草稿，按上述步骤保存和提交。
