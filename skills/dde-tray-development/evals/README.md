# dde-tray-development Evals

本目录包含 DDE 托盘插件开发的验证测试用例，按 references 文档结构分类。

## 目录结构

```
evals/
├── tray-plugin-spec/      # 托盘插件接口规范 evals
├── quick-panel/           # 快捷面板插件 evals
├── message-protocol/      # 消息协议 evals
├── context-menu/          # 右键菜单 evals
├── trigger-evals.json     # 触发评估（全部）
├── trigger-evals-train.json
├── trigger-evals-validation.json
└── eval-template.md       # 模板文件
```

## 评分标准

每个 eval 包含四段结构：

| 节 | 说明 |
|----|------|
| 任务 | 具体的开发任务描述 |
| 期望输出 | 代码应具备的特征 |
| 验证要点 | 检查清单 |
| 评分标准 | PASS / PARTIAL / FAIL 三级评分 + 反模式检查 |

## Evals 列表

### tray-plugin-spec (4 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | basic-plugin | 基础托盘插件创建 |
| eval-002 | flags-config | PluginFlags 配置 |
| eval-003 | proxy-interface | PluginProxyInterface 使用 |
| eval-004 | position-change | 任务栏位置变化处理 |

### quick-panel (3 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | quick-plugin | 快捷面板插件创建 |
| eval-002 | panel-size | 控件尺寸设置 |
| eval-003 | detail-page | 子页面显示 |

### message-protocol (3 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | message-handler | 消息处理实现 |
| eval-002 | support-flag | 插件可用性通知 |
| eval-003 | active-state | 激活状态报告 |

### context-menu (3 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | menu-data | 菜单数据格式 |
| eval-002 | checkable-menu | 可勾选菜单项 |
| eval-003 | open-control-center | 打开控制中心 |


### cross-skill (1 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | dtk-dependency | 使用 DTK DPalette 主题适配的跨 skill 依赖加载 |

## 触发评估

`trigger-evals.json` 包含 30 条触发测试（17 正例 + 13 反例），其中 1 条为跨 skill 测试（同时涉及 DConfig、Dtk6 CMake、DIconTheme 等 DTK 关键词，验证 `$dtk-development` 交叉触发）。

## 总计

共 **15** 个 output-quality evals（含 eval-template.md），覆盖 DDE 托盘插件开发的核心场景。
