# Eval: 覆盖多个字段

## 任务

用户需要在解决 bug 时覆盖多个字段值，包括 resolution、assignedTo、comment。

指导用户使用 --field 和 --field-json 参数。

## 期望输出

回答应：
1. 展示多个 --field 参数
2. 展示 --field-json 处理多值字段
3. 说明字段优先级
4. 展示完整命令示例

## 验证要点

- [ ] --field resolution=fixed
- [ ] --field assignedTo=zhangsan
- [ ] --field comment="脚本自动触发"
- [ ] --field-json '{"openedBuild[]":["trunk"]}'
- [ ] 优先级: 命令行 > 配置文件 > 表单默认
