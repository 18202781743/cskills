---
name: remote-dev-sync
description: 在本机编写代码，通过 rsync 同步到远程机器编译和测试的开发工作流。支持自动 watch 模式，文件保存即自动同步编译。当用户提到"远程编译"、"同步到远程"、"远程构建"、"远程测试"、"自动同步编译"、"watch 模式"、"文件监控"、"remote build"、"deploy to remote"、"rsync 编译"或涉及本地写代码远程编译的场景时使用此技能。适用于远程机器环境简单（只有编译工具）而本机有完整 IDE/AI 工具的双机开发模式。
tags: [remote, rsync, cmake, qmake, build, ssh, sync]
owner: yeshanshan
---

# 远程开发同步编译技能

在本机（开发环境）编写代码，通过 rsync 增量同步到远程机器（编译环境），根据工具链类型自动生成配置/编译/安装命令。支持 cmake、make、ninja、qmake 四种工具链。远程机器可能不稳定（经常崩溃/注销），技能处理连接中断并自动恢复。

## 快速路由

| 场景 | 操作 |
|------|------|
| 配置全局远程机器信息 | `python scripts/remote_dev.py setup --global` |
| 配置项目远程编译 | `python scripts/remote_dev.py setup` |
| 同步并编译项目 | `python scripts/remote_dev.py build -p <name>` |
| 监控自动同步编译 | `python scripts/remote_dev.py watch -p <name> --auto` |
| Ad-hoc 模式编译 | `python scripts/remote_dev.py build -H user@ip -r ~/path` |

详细文档见 SKILL.md 主体内容。

## Evals 测试

验证 skill 有效性的测试用例，按功能场景分类组织，见 [evals/README.md](evals/README.md)。

### 测试分类

| 目录 | 覆盖范围 | 数量 |
|------|----------|------|
| setup/ | 配置相关 | 2 |
| sync/ | 同步相关 | 1 |
| build/ | 编译相关 | 3 |
| watch/ | 监控模式 | 2 |
| git-worktree/ | Git worktree | 3 |

**总计**: 11 个 evals
