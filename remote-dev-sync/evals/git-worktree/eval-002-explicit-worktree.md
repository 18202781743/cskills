# Eval: 显式指定 Worktree 目录

## 任务

用户给 dde-shell 开了个 worktree：~/worktrees/dde-shell/fix-crash，想用这个目录做同步源。

指导用户显式指定 worktree 目录。

## 期望输出

回答应：
1. 展示 --project-dir 参数
2. 说明指定目录作为同步源
3. 说明覆盖配置中的主目录
4. 展示完整命令

## 验证要点

- [ ] --project-dir ~/worktrees/dde-shell/fix-crash
- [ ] 使用指定目录作为同步源
- [ ] 不使用配置中的主目录
- [ ] 启动 watch 或 build
