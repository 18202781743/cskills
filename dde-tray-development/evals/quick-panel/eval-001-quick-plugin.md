# Eval: 创建快捷面板插件

## 任务

用户想创建一个快捷面板插件，同时有托盘图标和快捷面板控件。

指导用户使用 Type_Quick 标志和 QUICK_ITEM_KEY。

## 期望输出

回答应：
1. 展示 flags() 设置 Type_Quick | Quick_Panel_Full
2. 展示 itemWidget 处理 QUICK_ITEM_KEY
3. 展示控件尺寸设置
4. 说明配置文件注册

## 验证要点

- [ ] flags() 使用 Type_Quick（非 Type_Tray）
- [ ] Quick_Panel_Single/Multi/Full 布局标志
- [ ] itemWidget(Dock::QUICK_ITEM_KEY) 返回快捷面板控件
- [ ] setFixedHeight(Dock::QUICK_ITEM_HEIGHT)
- [ ] pluginName 添加到 quickPlugins 配置
