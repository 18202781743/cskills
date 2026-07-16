# Eval: 激活 Bug

## 任务

用户需要重新激活一个已解决的 bug。

指导用户执行激活流程。

## 期望输出

回答应：
1. 展示 --action activate 命令
2. 说明激活的默认字段
3. 说明与 resolve 的区别
4. 展示完整命令示例

## 验证要点

- [ ] --action activate
- [ ] 默认 status=active
- [ ] 可使用 --bug-id 替代 --url
- [ ] 输出 JSON 包含 bug_status
