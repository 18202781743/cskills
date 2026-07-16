# Eval: DIconButton 使用 dci 图标

## 任务

创建一个图标按钮，要求：
1. 使用 DDciIcon 加载图标
2. 图标路径为 ":/icons/action.dci"
3. 点击时输出日志

## 期望输出

代码应：
1. 创建 DIconButton
2. 使用 setIcon(DDciIcon) 设置图标
3. 连接 clicked 信号

## 验证要点

- [ ] #include <DIconButton>
- [ ] #include <DDciIcon>
- [ ] DDciIcon icon(":/icons/action.dci")
- [ ] button->setIcon(icon)
