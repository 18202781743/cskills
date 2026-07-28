# CSkills

CSkills 是一个面向 Deepin、UOS 和 DDE 开发维护场景的 Codex Skill 集合。项目将常用的开发知识、源码参考、操作流程和自动化脚本整理为独立 skill，帮助使用人员快速完成框架开发、插件开发、远程构建和内部工作流操作。

## Skill 列表

| Skill | 功能简介 | 适用场景 |
|-------|----------|----------|
| [dtk-development](dtk-development/README.md) | DTK 桌面应用开发指南 | DTK QWidget/QML 控件、主题、图标、DConfig、系统集成、构建与调试 |
| [dde-shell-development](dde-shell-development/README.md) | DDE Shell 插件开发指南 | Applet、Containment、Panel 插件和 LayerShell 窗口开发 |
| [dde-tray-development](dde-tray-development/README.md) | DDE 托盘插件开发指南 | 托盘图标、快捷面板、消息协议和右键菜单开发 |
| [dde-control-center-development](dde-control-center-development/README.md) | DDE 控制中心开发指南 | 控制中心架构、插件、C++/QML API 和加载问题排查 |
| [remote-dev-sync](remote-dev-sync/README.md) | 本地开发、远程编译同步工具 | 使用 rsync/SSH 将本地代码同步到远程机器构建和测试 |
| [linglong-runtime-update](linglong-runtime-update/README.md) | DTK 玲珑 Runtime 更新自动化 | CRP 打包、Jenkins 构建、Runtime 仓库更新和 Layer 推送 |
| [uos-pms-bug-workflow-trigger](uos-pms-bug-workflow-trigger/README.md) | UOS PMS Bug 流程触发工具 | 通过命令行解决、激活或关闭 PMS Bug |

## 项目结构

每个 skill 使用独立目录组织，通常包含以下内容：

```text
<skill-name>/
├── SKILL.md          # Agent 使用的核心说明和任务路由
├── README.md         # 面向使用人员的功能简介和快速上手
├── references/       # 按需查阅的详细参考文档
├── scripts/          # 可直接执行的自动化脚本
├── assets/           # 工作流使用的模板或资源
└── evals/            # Skill 能力验证用例
```

不同 skill 会根据实际需要只保留其中一部分目录。

## 如何使用

1. 从上方列表选择与任务匹配的 skill。
2. 阅读对应目录的 `README.md`，了解能力范围、前置条件和常用入口。
3. 将需要的 skill 安装或加载到支持 Skill 的 Agent 环境。
4. 使用自然语言描述任务；Agent 会根据 `SKILL.md` 路由到相关参考文档或脚本。

例如：

```text
使用 dtk-development 帮我创建一个支持深色主题的 DTK6 设置窗口。
```

```text
使用 remote-dev-sync 把当前项目同步到远程开发机并用 CMake 编译。
```

## 维护说明

修改 skill 文档时，应以对应源码项目中的实际 API、类、枚举和构建配置为准，并同步更新验证计划。详细维护流程见 [AGENTS.md](AGENTS.md)。
