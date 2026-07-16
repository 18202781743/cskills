# Eval: 自动识别 Git Worktree

## 任务

用户在 dde-shell 的一个 git worktree 目录里开发，目录是 ~/worktrees/dde-shell/feature-a。主项目之前已配过 remote-dev。

指导用户自动识别 worktree 目录。

## 期望输出

回答应：
1. 说明自动识别机制
2. 说明当前目录反查已配置项目
3. 说明 worktree 共享 Git common dir
4. 说明执行同步编译

## 验证要点

- [ ] 在 worktree 目录执行命令
- [ ] 自动识别并匹配已配置项目
- [ ] 使用 worktree 作为本地同步源
- [ ] 无需显式指定 --project-dir
