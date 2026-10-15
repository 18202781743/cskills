# dde-control-center-development Evals

本目录包含控制中心插件开发的验证测试用例，按 references 文档结构分类。

## 目录结构

```
evals/
├── architecture/          # 架构相关 evals
├── plugin-development/    # 插件开发流程 evals
├── cpp-api/              # C++ API 使用 evals
├── qml-api/              # QML API 使用 evals
├── debugging/            # 调试与问题排查 evals
├── trigger-evals.json     # 触发评估（全部）
├── trigger-evals-train.json
├── trigger-evals-validation.json
└── eval-template.md      # 模板文件
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

### architecture (3 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | plugin-architecture | 插件架构与加载流程 |
| eval-002 | module-registration | 模块注册与层级结构 |
| eval-003 | search-mechanism | 搜索机制与索引 |

### plugin-development (5 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | create-plugin | 创建新插件 |
| eval-002 | cmake-config | CMake 配置 |
| eval-003 | debian-packaging | Debian 打包 |
| eval-004 | translation | 翻译集成 |
| eval-005 | plugin-install | 插件安装路径 |

### cpp-api (4 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | dccobject-basic | DccObject 基础用法 |
| eval-002 | dccapp-usage | DccApp 全局访问 |
| eval-003 | dccfactory-usage | DccFactory 工厂模式 |
| eval-004 | dccquickdbusinterface | DBus 接口绑定 |

### qml-api (4 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | dccgroupview | DccGroupView 布局 |
| eval-002 | dccrepeater | DccRepeater 动态创建 |
| eval-003 | dccdbusinterface | QML DBus 绑定 |
| eval-004 | dccobject-qml | QML 中访问 DccObject |

### debugging (5 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | plugin-debug | --spec 参数调试插件 |
| eval-002 | framework-debug | 框架代码调试环境变量 |
| eval-003 | qml-cache | QML 缓存问题 |
| eval-004 | plugin-not-show | 插件不显示排查 |
| eval-005 | dccdata-undefined | dccData undefined 问题 |


### cross-skill (1 个)

| 编号 | 文件 | 测试点 |
|------|------|--------|
| eval-001 | dtk-dependency | 使用 DTK DBlurEffectWidget 的跨 skill 依赖加载 |

## 触发评估

`trigger-evals.json` 包含 44 条触发测试（25 正例 + 19 反例），其中 1 条为跨 skill 测试（同时涉及 DConfig、DPalette、DCI 图标等 DTK 关键词，验证 `$dtk-development` 交叉触发）。

## 总计

共 **23** 个 output-quality evals（含 eval-template.md），覆盖控制中心插件开发的核心场景。
