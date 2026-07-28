# Remote Dev Sync Skill

用于“本机编写代码、远程机器编译测试”的双机开发工作流。脚本通过 SSH 和 rsync 增量同步源码，并根据项目工具链在远程端执行配置、编译和安装命令。

## 主要能力

- 保存全局远程主机配置
- 为不同项目维护独立的远程路径和构建配置
- 增量同步代码，减少重复传输
- 支持 CMake、Make、Ninja 和 qmake 工具链
- 使用 watch 模式在文件保存后自动同步和编译
- 支持不创建项目配置的临时 Ad-hoc 构建
- 在远程连接中断后恢复同步流程
- 支持 Git worktree 开发场景

## 前置条件

- 本机安装 Python 3、SSH 和 rsync
- 本机能够通过 SSH 登录远程构建机器
- 远程机器已安装项目所需编译器和构建工具

## 快速开始

```bash
# 配置全局远程机器
python3 scripts/remote_dev.py setup --global

# 在当前项目中创建远程构建配置
python3 scripts/remote_dev.py setup

# 同步并编译指定项目
python3 scripts/remote_dev.py build -p <name>

# 监控文件变化并自动同步编译
python3 scripts/remote_dev.py watch -p <name> --auto
```

临时指定远程主机和目录：

```bash
python3 scripts/remote_dev.py build -H user@host -r ~/remote/project
```

完整的 Agent 使用说明见 [SKILL.md](SKILL.md)，命令参数以脚本的 `--help` 输出为准。

## 验证

该 skill 提供 11 个测试用例，覆盖配置、同步、构建、watch 和 Git worktree 场景。详见 [evals/README.md](evals/README.md)。
