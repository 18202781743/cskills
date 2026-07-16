# Eval: 自动监控编译

## 任务

用户希望本地修改代码后自动同步到远程编译。

指导用户启动 watch 模式自动同步编译。

## 期望输出

回答应：
1. 展示 watch --auto 命令
2. 说明防抖机制
3. 说明编译期间变化排队
4. 说明 Ctrl+C 停止

## 验证要点

- [ ] python scripts/remote_dev.py watch -p <name> --auto
- [ ] 防抖 2 秒收集变化
- [ ] 编译期间变化排队等待
- [ ] Ctrl+C 停止监控
