# uos-pms-bug-workflow-trigger Evals

本目录包含 PMS Bug 流程触发技能的验证测试用例，按功能场景分类。

## 目录结构

```
evals/
├── config/           # 配置相关 evals
├── workflow/         # 工作流相关 evals
└── eval-template.md  # 模板文件
```

## Evals 列表

### config (2 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | setup-config | 配置 PMS 连接 |
| eval-002 | force-auth | 强制重新认证 |

### workflow (5 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | resolve-bug | 解决 Bug |
| eval-002 | activate-bug | 激活 Bug |
| eval-003 | close-bug | 关闭 Bug |
| eval-004 | dump-form | 查看表单字段 |
| eval-005 | field-override | 覆盖多个字段 |

## 总计

共 **7** 个 evals，覆盖 PMS Bug 流触发的核心场景。
