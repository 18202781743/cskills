---
name: uniontech-workhours
description: 通过统信 OA 考勤和 BI 工时接口整理、补填或批量填写工时。用户说“帮我写今天的周报”、提供工作事项要求填报、要求保存草稿或提交工时时使用；信息完整后直接保存草稿并回读，不询问是否保存；提交前单独取得用户确认。
---

# 统信 OA 工时填报

处理用户指定日期和任务的工时，从工作事项整理到草稿回读；符合提交条件时再提交并回读。默认使用 `scripts/workhours.py` 完成查询、组装、写入和回读，不再为每次任务临时编写 API 脚本。接口字段、计算边界和请求顺序见 [接口记录](references/har-contract.md)；执行写请求前读该文件的“保存与提交”“按周工作内容”“API 执行顺序”。

## 默认流程

1. **认证并读取。** 运行 `python3 scripts/auth_session.py check`，再运行 `python3 scripts/workhours.py inspect --start YYYY-MM-DD --end YYYY-MM-DD`。该命令一次返回未填日期、OA 考勤计算结果、近期有效任务和网页版地址；默认结束日期为 Asia/Shanghai 的昨天。没有共享凭据时，在交互终端运行 `python3 scripts/auth_session.py setup`；不能安全交互就告知用户如何完成，不收集聊天中的密码。认证格式和接口见 [共享认证流程](references/har-contract.md#共享认证流程)。
2. **整理逐日记录并沿用任务。** 依据 `Asia/Shanghai` 确定相对日期和周一至周日。每天一条 `YYYY-MM-DD 工作内容，`，同一天的多个事项用分号合并；内容无须拆成逐小时记录。用户未指定改任务时，优先沿用 `inspect` 返回且此前确认的项目/任务；不要依据“V20”“Qt 6”等工作内容关键词另选任务或要求用户分配各事项的小时数。用户明确指定多个任务时，才分别确定工时。计划中的 `hours` 可省略，`workhours.py` 会从当前 OA 考勤按 [考勤打卡与工时计算](references/har-contract.md#考勤打卡与工时计算) 自动计算；返回需复核时先解决缺项。
3. **解决真正的缺项。** 只有既无用户指定任务也无可信的已确认默认任务、多个明确任务缺少各自工时、缺下班卡、请假、异常打卡或脚本返回 `status=review` 时，才请用户补充必要信息。用户给的当天总时长与有效考勤计算值不符时，报告差异并请其确认；已确认的异常工时无需重复询问。已提交、审批中或已审批的记录不直接改写。查询不全或请求字段无法确认时不写入。
4. **生成计划并预览。** 按 [计划文件示例](assets/workhours-plan.example.json) 创建临时 JSON，只写 `project_id`、`task_id` 和逐日 `date` / `content` / 可选 `hours`。先运行 `python3 scripts/workhours.py save-drafts --input PLAN.json`；脚本会按周保留有效旧条目、过滤跨周行、同日去重，并输出完整待写内容。核对预览后，如果缺项已经解决，同一轮继续执行，不因展示预览暂停等待用户回复。
5. **直接保存或续写草稿并回读。** 运行 `python3 scripts/workhours.py save-drafts --input PLAN.json --apply`。脚本会沿用已有可编辑草稿 ID，无记录才新建，并在成功响应后重新查询日期、ID、小时数、整周内容和状态；回读不一致即失败。若接口报重复，按 [重复记录排查](references/har-contract.md#重复记录排查) 处理，不要继续以 `id=null` 重试。
6. **提交前确认。** 草稿回读成功后报告结果。只有用户随后明确确认提交，才运行 `python3 scripts/workhours.py submit --input PLAN.json --apply --confirm-submit` 并回读。用户在初始请求中说“保存并提交”或“直接提交”时，也先保存草稿并回读，然后单独询问是否提交；“仅保存”请求到草稿为止。
7. **回复结果和验证入口。** 列出日期、项目任务、逐日小时数、完整工作内容及实际保存/提交状态，并提供 `[打开 OA 工时填报页面](https://oa.uniontech.com/wui/ChanYanWorkHour.html)` 供网页版核验。所有 CLI 命令的 JSON 也包含 `web_url`。不要输出工号、审批人 ID、Cookie、token 或其他身份信息。

## 关键边界

- “帮我写今天的周报，内容是……”也进入上述 OA 填报流程。当天尚无下班卡时，先请用户给出实际工时；不能默认 8 小时。
- 同一任务可以持续数周或数月；默认只编辑目标周内容。目标周文本中的跨周默认行可以清除，目标周已有有效内容须保留。用户要求改写目标周既有条目或已提交记录时，先验证当前记录的可编辑状态和接口契约；本 skill 的接口记录未验证撤回 API，不能猜测撤回请求。
- 认证后的 OA Session 只用于 OA 请求，BI token 只放在 BI 请求的 `token` 头。历史 HAR 仅供契约核对，不从中重放 token、工号或个人数据，也不把当前响应落盘。
- 本地机的通用 HTTPS 代理可能使内部 OA TLS 失败；认证脚本默认直连，可用 `AI_UT_PROXY` 指定代理。不要禁用证书校验。
- `workhours.py` 的写命令默认只预览；草稿必须显式 `--apply`，提交还必须显式 `--confirm-submit`。不要绕过这两个闸门直接自行拼装写请求，除非脚本无法覆盖且已按接口记录查明原因。
