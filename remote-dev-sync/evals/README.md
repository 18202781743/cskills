# remote-dev-sync Evals

本目录包含远程开发同步编译技能的验证测试用例，按功能场景分类。

## 目录结构

```
evals/
├── setup/            # 配置相关 evals
├── sync/             # 同步相关 evals
├── build/            # 编译相关 evals
├── watch/            # 监控模式 evals
├── git-worktree/     # Git worktree 相关 evals
└── eval-template.md  # 模板文件
```

## Evals 列表

### setup (2 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | global-config | 全局远程机器配置 |
| eval-002 | project-config | 项目配置 |

### sync (1 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | incremental-sync | 增量同步代码 |

### build (3 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | cmake-build | CMake 项目编译 |
| eval-002 | qmake-build | qmake 项目编译 |
| eval-003 | adhoc-build | Ad-hoc 模式编译 |

### watch (2 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | auto-watch | 自动监控编译 |
| eval-002 | confirm-mode | 确认模式监控 |

### git-worktree (3 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | auto-worktree | 自动识别 Worktree |
| eval-002 | explicit-worktree | 显式指定 Worktree |
| eval-003 | remote-recovery | 远程崩溃恢复 |

## 总计

共 **11** 个 evals，覆盖远程开发同步编译的核心场景。
