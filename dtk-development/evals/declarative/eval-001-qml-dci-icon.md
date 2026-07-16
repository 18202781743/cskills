# Eval: QML 中使用 dci 图标

## 任务

在 QML 中显示一个 dci 图标，要求：
1. 图标名称为 "action-icon"
2. 尺寸为 32x32
3. 自动跟随系统主题（亮/暗）

## 期望输出

代码应：
1. 使用 DciIcon 组件
2. 设置 name 和 sourceSize 属性
3. 不需要手动设置 theme，自动跟随系统

## 验证要点

- [ ] import org.deepin.dtk 1.0
- [ ] 使用 DciIcon 组件
- [ ] 设置 sourceSize: Qt.size(32, 32)
