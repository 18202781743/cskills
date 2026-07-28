# cskills

`cskills` 是 [deepin-skills](https://gitlabwh.uniontech.com/ut000020/deepin-skills) 的下游维护仓库，集中维护 Deepin、UOS 和 DDE 研发场景所需的技能。

本仓库中的技能遵循 `deepin-skills` 的组织和发布约定。技能在这里完成开发、源码校验和测试后，再按 `deepin-skills` 的流程同步或合入，供其支持的技能发现、安装和发布体系使用。

## 当前技能

| Skill | 功能简介 | 适用场景 |
|-------|----------|----------|
| [dtk-development](dtk-development/SKILL.md) | DTK 桌面应用开发指南 | QWidget/QML 控件、主题、图标、DConfig、系统集成、构建与调试 |
| [dde-shell-development](dde-shell-development/SKILL.md) | DDE Shell 开发指南 | Applet、Containment、Panel 插件和 LayerShell 窗口开发 |
| [dde-tray-development](dde-tray-development/SKILL.md) | DDE 托盘插件开发指南 | 托盘图标、快捷面板、消息协议和右键菜单开发 |
| [dde-control-center-development](dde-control-center-development/SKILL.md) | DDE 控制中心开发指南 | 控制中心架构、插件、C++/QML API 和加载问题排查 |
| [remote-dev-sync](remote-dev-sync/SKILL.md) | 本地开发、远程编译同步工具 | 使用 rsync 和 SSH 将本地代码同步到远程机器构建和测试 |
| [linglong-runtime-update](linglong-runtime-update/SKILL.md) | DTK 玲珑 Runtime 更新自动化 | CRP 打包、Jenkins 构建、Runtime 仓库更新和 Layer 推送 |
| [uos-pms-bug-workflow-trigger](uos-pms-bug-workflow-trigger/SKILL.md) | UOS PMS Bug 流程触发工具 | 通过命令行解决、激活或关闭 PMS Bug |

## 与 deepin-skills 的关系

- `deepin-skills` 是面向研发内部公共技能的主仓库和发布入口。
- `cskills` 聚焦 Deepin、UOS、DDE 和 DTK 相关技能的开发与维护。
- 技能目录结构、元数据和发布要求以 `deepin-skills` 的约定为准。
- 本仓库根目录的 `README.md` 用于介绍下游仓库，不放入具体 skill 目录，也不作为 skill 内容发布。

## Skill 目录结构

每个 skill 至少包含一个 `SKILL.md`，并按实际需要携带参考资料、脚本和资源：

```text
<skill-name>/
├── SKILL.md          # 技能入口、适用场景和执行流程
├── references/       # 按需加载的参考资料
├── scripts/          # 可执行的自动化脚本
└── assets/           # 模板、补丁或静态资源
```

仓库内的 `evals/` 和 `verification-plan.md` 用于开发阶段验证。发布内容和目录处理方式应遵循 `deepin-skills` 的同步发布流程。

## 维护流程

修改技能文档时：

1. 从对应源码项目核对实际 API、类、枚举和构建配置。
2. 修改技能文档及相关交叉引用。
3. 更新对应验证计划。
4. 按验证计划逐项检查，直到全部通过。
5. 提交变更，并按 `deepin-skills` 的流程同步或合入。

详细规则见 [AGENTS.md](AGENTS.md)。
