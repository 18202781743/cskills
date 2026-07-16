---
name: uos-pms-bug-workflow-trigger
description: 自动触发禅道 PMS bug 的解决、激活、关闭等流程。适用于用户想直接通过脚本提交 bug 流程，而不是在网页里手动点击，并且希望表单字段支持默认值和命令行覆盖的场景。
---

# UOS PMS Bug Workflow Trigger

这个 skill 用于直接触发 PMS bug 页面里的流程操作，默认覆盖：

- `resolve`：解决 bug
- `activate`：激活 bug
- `close`：关闭 bug

## 快速路由

| 场景 | 操作 |
|------|------|
| 配置 PMS 连接 | `python3 scripts/trigger_pms_bug_flow.py config` |
| 解决 bug | `python3 scripts/trigger_pms_bug_flow.py --url <url> --action resolve` |
| 激活 bug | `python3 scripts/trigger_pms_bug_flow.py --url <url> --action activate` |
| 关闭 bug | `python3 scripts/trigger_pms_bug_flow.py --url <url> --action close` |
| 预览提交字段 | `python3 scripts/trigger_pms_bug_flow.py --url <url> --action resolve --dry-run` |
| 查看表单字段 | `python3 scripts/trigger_pms_bug_flow.py --url <url> --action resolve --dump-form` |

详细文档见 SKILL.md 主体内容。

## Evals 测试

验证 skill 有效性的测试用例，按功能场景分类组织，见 [evals/README.md](evals/README.md)。

### 测试分类

| 目录 | 覆盖范围 | 数量 |
|------|----------|------|
| config/ | 配置相关 | 2 |
| workflow/ | 工作流相关 | 5 |

**总计**: 7 个 evals
