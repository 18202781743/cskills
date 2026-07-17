# Eval: 图标按钮使用 DCI 图标

## 任务

创建一个图标按钮，要求：
1. 使用 DCI 动态图标格式
2. 图标路径为 ":/icons/action.dci"
3. 点击时输出日志

## 期望输出

代码应：
1. 创建图标按钮
2. 使用 DCI 图标格式设置图标
3. 连接点击信号

## 验证要点

- [ ] #include <DIconButton>
- [ ] #include <DDciIcon>
- [ ] DDciIcon icon(":/icons/action.dci")
- [ ] button->setIcon(icon)

## 参考

参见 [按钮控件](../../../references/widgets/button.md) 了解 DIconButton 和 DCI 图标的用法。
