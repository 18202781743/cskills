# Eval: 配置 PMS 连接

## 任务

用户需要首次配置 PMS 连接，包括 base_url 和认证信息。

指导用户使用 config 子命令配置。

## 期望输出

回答应：
1. 展示 config 子命令
2. 说明认证流程
3. 说明配置文件路径
4. 说明 LDAP 登录

## 验证要点

- [ ] python3 scripts/trigger_pms_bug_flow.py config
- [ ] 配置文件: ~/.config/uos-pms-bug-workflow-trigger/config.json
- [ ] 认证使用 LDAP 用户名和密码
- [ ] 凭证加密保存到 ~/.config/uniontech-oa/default.json
