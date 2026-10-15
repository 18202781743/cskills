# Eval: DTK 模块关系

## 任务

面向 v25 理解 DTK 四个核心模块的关系：
1. 解释 dtkcore/dtkgui/dtkwidget/dtkdeclarative 的职责划分
2. 说明模块之间的依赖关系
3. 解释 dtkgui 作为基础层如何为控件层提供抽象

## 期望输出

回答应：
1. 正确描述每个模块的职责
2. 正确说明依赖方向（dtkgui → dtkwidget/dtkdeclarative）
3. 解释控件层如何复用基础层的抽象

## 验证要点

- [ ] dtkcore：核心工具类（DBus、日志、单实例等）
- [ ] dtkgui：主题/调色板/图标/字体/平台抽象
- [ ] dtkwidget：QWidget 控件实现
- [ ] dtkdeclarative：QML 控件实现
- [ ] 依赖方向：dtkgui 提供抽象，dtkwidget/dtkdeclarative 使用

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，回答准确覆盖 DTK 架构层次 |
| ⚠️ **PARTIAL** | 核心架构理解正确，但部分细节或层次关系有偏差 |
| ❌ **FAIL** | 架构理解错误，或混淆了不同 DTK 层次/模块的职责 |

## 反模式检查

- [ ] 未混淆 dtkgui/dtkwidget/dtkdeclarative 的职责边界
- [ ] 未将平台插件层与控件层混为一谈
