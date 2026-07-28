# UOS PMS Bug Workflow Trigger Skill

通过命令行直接触发 UOS 禅道 PMS Bug 的流程操作，适合需要自动化提交解决、激活或关闭表单的场景。

## 主要能力

- 配置 PMS 服务地址和认证信息
- 触发 Bug 解决流程
- 重新激活已解决或已关闭的 Bug
- 关闭 Bug
- 使用默认字段减少重复输入
- 通过命令行参数覆盖表单字段
- 在提交前预览请求内容或查看页面表单结构

## 前置条件

- Python 3
- 安装 [requirements.txt](requirements.txt) 中的依赖
- 可以访问 PMS 服务并拥有目标 Bug 的操作权限

## 快速开始

```bash
# 配置 PMS 连接
python3 scripts/trigger_pms_bug_flow.py config

# 解决 Bug
python3 scripts/trigger_pms_bug_flow.py --url <bug-url> --action resolve

# 激活 Bug
python3 scripts/trigger_pms_bug_flow.py --url <bug-url> --action activate

# 关闭 Bug
python3 scripts/trigger_pms_bug_flow.py --url <bug-url> --action close
```

提交前检查：

```bash
# 预览将要提交的字段，不执行流程
python3 scripts/trigger_pms_bug_flow.py --url <bug-url> --action resolve --dry-run

# 输出页面中识别到的表单字段
python3 scripts/trigger_pms_bug_flow.py --url <bug-url> --action resolve --dump-form
```

完整的 Agent 使用说明见 [SKILL.md](SKILL.md)，具体参数以脚本的 `--help` 输出为准。

## 参考与验证

- [已验证的解决流程示例](references/bug-280627-resolve-flow.md)
- [配置示例](references/config.example.json)
- [Evals 说明](evals/README.md)
