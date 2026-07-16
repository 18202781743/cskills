# Eval: 解决 Bug

## 任务

用户需要通过脚本触发 PMS bug 的解决流程，bug URL 为 https://pms.uniontech.com/bug-view-353781.html。

指导用户执行解决流程。

## 期望输出

回答应：
1. 展示 --url 和 --action resolve 命令
2. 说明默认字段值
3. 说明 --dry-run 预览
4. 说明 --field 覆盖字段

## 验证要点

- [ ] --url "https://pms.uniontech.com/bug-view-353781.html"
- [ ] --action resolve
- [ ] 默认 resolution=fixed
- [ ] --dry-run 预览不提交
- [ ] --field key=value 覆盖字段
