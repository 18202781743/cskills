# Eval: 关闭 Bug

## 任务

用户需要关闭一个 bug。

指导用户执行关闭流程。

## 期望输出

回答应：
1. 展示 --action close 命令
2. 说明关闭的字段要求
3. 说明 comment 字段
4. 展示完整命令示例

## 验证要点

- [ ] --action close
- [ ] 默认沿用表单值
- [ ] 可通过 --field comment="..." 添加备注
- [ ] 返回 success 和 bug_status
