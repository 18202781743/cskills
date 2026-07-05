# CSkills Agent 工作流

## Skill 维护流程

修改任何 skill 文档时，遵循以下流程：

### 1. 探索源码

从对应的源码项目中查找实际 API、类、枚举值，与文档声称对照。

### 2. 修改文档

根据源码验证结果修改 `references/` 下的文档，确保：

- 类名、方法签名、枚举值与头文件一致
- 代码示例可编译运行
- 概念描述与官方文档/源码注释一致
- 相关文档交叉引用正确

### 3. 更新验证计划

修改 `verification-plan.md` 中对应模块的验证项，确保计划与实际文档结构匹配。

### 4. 验证

按 `verification-plan.md` 逐项验证，对照源码头文件确认：

- **PASS** — 文档与源码一致
- **FAIL** — 文档与源码不一致（修正文档）
- **NOT FOUND** — 源码中未找到（检查是否已移除或重命名）

重复步骤 2-4 直到全部验证项 PASS。

### 5. 提交推送

验证完成后提交并推送，提交信息格式参照 git-commit-workflow 规范。
提交时若用户未提供 PMS 和 GitHub Issue 编号，直接跳过对应的 `PMS:` 和 `Issue:` 行。

## 项目结构

```
cskills/
├── AGENTS.md              # 本文件，agent 工作流
├── dtk-development/        # DTK 开发指南 skill
├── dde-shell-development/  # DDE Shell 开发 skill
├── dde-tray-development/   # DDE 托盘开发 skill
├── dde-control-center-development/  # DDE 控制中心开发 skill
└── .opencode/             # opencode 配置
```

## DTK Skill 源码映射

| 文档模块 | 对应源码项目 | 关键目录 |
|----------|-------------|----------|
| config | dtkcore + dde-app-services | `dtkcore/include/global/` + `dde-app-services/dconfig-center/` |
| icons | dtkgui | `dtkgui/include/util/` |
| theming | dtkgui + dtkwidget | `dtkgui/include/kernel/` + `dtkwidget/include/widgets/` |
| widgets | dtkwidget | `dtkwidget/include/widgets/` + `dtkwidget/include/DWidget/` |
| declarative | dtkdeclarative | `dtkdeclarative/qmlplugin/` + `dtkdeclarative/src/` |
| core | dtkcore | `dtkcore/include/` |
| log | dtklog | `dtklog/include/` |

## DDE Control Center Skill 源码映射

| 文档模块 | 对应源码项目 | 关键目录 |
|----------|-------------|----------|
| architecture + plugin-development | dde-control-center | `include/dccfactory.h` + `src/dde-control-center/plugin/` + `misc/` |
| dccobject-api + dccapp-api | dde-control-center | `src/dde-control-center/plugin/dccobject.h` + `dccapp.h` + `dccmanager.h` |
| qml-components | dde-control-center | `src/dde-control-center/plugin/*.qml` + `*.h` |
| data-binding + dbus-integration | dde-control-center + 各个 plugin-*/ | `src/dde-control-center/plugin/dccquickdbusinterface.h` + `src/plugin-*/operation/` |
| dconfig-integration | dde-control-center + dde-app-services | 根 `CMakeLists.txt` + `dde-app-services/dconfig-center/` |
| debian-packaging | dde-control-center | `debian/` |
| translation | dde-control-center | `misc/DdeControlCenterPluginMacros.cmake` |
| plugin-example-walkthrough | dde-control-center | `examples/plugin-example/` |
| debugging | dde-control-center | `src/dde-control-center/main.cpp` (--spec) + `dccpluginloader.h/cpp` |
