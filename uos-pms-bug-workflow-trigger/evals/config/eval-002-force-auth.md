# Eval: 强制重新认证

## 任务

用户需要重新输入账号密码，覆盖已有凭证缓存。

指导用户使用 --force-auth 参数。

## 期望输出

回答应：
1. 展示 --force-auth 命令
2. 说明忽略缓存重新认证
3. 说明适用场景
4. 说明凭证更新

## 验证要点

- [ ] python3 scripts/trigger_pms_bug_flow.py --force-auth
- [ ] 忽略共享凭证缓存
- [ ] 重新输入 loginid 和密码
- [ ] 更新加密凭证文件
