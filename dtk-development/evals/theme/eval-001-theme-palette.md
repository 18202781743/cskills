# Eval: 控件颜色跟随主题切换

## 任务

创建一个自定义标签，要求：
1. 背景色使用 DPalette::ItemBackground
2. 前景色使用 DPalette::TextTitle
3. 当系统主题切换时自动更新颜色

## 期望输出

代码应：
1. 使用 DPalette 获取语义颜色
2. 使用 DGuiApplicationHelper 监听主题切换
3. 在主题切换时更新控件颜色

## 验证要点

- [ ] 使用 #include <DPalette> 和 #include <DGuiApplicationHelper>
- [ ] 连接 themeTypeChanged 信号
- [ ] 使用 DPalette::ItemBackground 和 DPalette::TextTitle
