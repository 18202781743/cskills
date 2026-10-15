# Eval: 字体系统架构

## 任务

理解 DTK 字体系统的架构：
1. 说明 T1-T11 字体大小层级
2. 解释 DFontManager 的作用
3. 说明 DFontSizeManager 如何绑定控件

## 期望输出

回答应：
1. 描述字体大小层级体系
2. 说明系统字体变化的传播路径
3. 解释控件如何自动更新字体

## 验证要点

- [ ] T1-T11 层级，T6(14px) 为基准
- [ ] DFontManager 管理 T1-T11 计算
- [ ] DFontSizeManager::bind() 绑定控件
- [ ] 数据流：系统字体 → DFontManager → DFontSizeManager → 控件

## 评分标准

| 等级 | 条件 |
|------|------|
| ✅ **PASS** | 所有验证要点全部满足，回答准确覆盖 DTK 架构层次 |
| ⚠️ **PARTIAL** | 核心架构理解正确，但部分细节或层次关系有偏差 |
| ❌ **FAIL** | 架构理解错误，或混淆了不同 DTK 层次/模块的职责 |

## 反模式检查

- [ ] 未混淆 dtkgui/dtkwidget/dtkdeclarative 的职责边界
- [ ] 未将平台插件层与控件层混为一谈
