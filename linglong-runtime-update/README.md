# Linglong Runtime Update Skill

用于自动化更新 `org.deepin.runtime` 和 `org.deepin.runtime.webengine` 两个 DTK 玲珑 Runtime 仓库。工作流串联 CRP 打包、Jenkins 更新仓库、GitHub 代码更新、Layer 构建和 N8N 推送。

## 主要能力

- 为 DTK 相关项目触发 CRP 打包并检查状态
- 触发 Jenkins 制作 deb 更新仓库
- 根据 DTK 包版本计算玲珑 Runtime 版本
- 更新 Runtime 与 WebEngine 仓库
- 为 Runtime 创建或复用 GitHub PR
- 触发 Runtime/WebEngine Layer 构建
- 将构建产物推送到玲珑仓库
- 缓存 CRP、Jenkins 和本地仓库所需配置

## 工作流

```text
CRP 打包
  ↓
制作 deb 更新仓库
  ↓
更新 Runtime / WebEngine 仓库
  ↓
构建玲珑 Layer
  ↓
推送 Layer
```

每一步的输出会作为后续步骤的输入，Runtime 和 WebEngine 的仓库更新方式不同，执行前应阅读 [SKILL.md](SKILL.md) 中的完整说明。

## 前置条件

- Python 3.8+，以及 `requests`、`cryptography`、`rsa`
- Go、`ll-builder`、已认证的 `gh` CLI
- 可用的 CRP 和 Jenkins 账号
- 正确配置内外网代理及 `no_proxy`

## 快速开始

```bash
# 启动交互式菜单
python3 scripts/linglong-update.py

# 查看所有命令
python3 scripts/linglong-update.py --help

# 查看某一步的参数
python3 scripts/linglong-update.py <command> --help
```

## 重要限制

CRP、Jenkins 和 N8N 均为响应较慢的内网服务：

- 主动轮询间隔不得低于 5 分钟
- Jenkins 任务触发后至少等待 2 分钟再首次查询
- CRP 打包触发后至少等待 5 分钟再首次查询
- 不要查询与当前步骤无关的任务状态

## 详细文档

- [CRP 打包](references/crp-pack.md)
- [Jenkins 交互](references/jenkins.md)
- [仓库更新与 PR](references/repo-update.md)
- [Evals 说明](evals/README.md)
