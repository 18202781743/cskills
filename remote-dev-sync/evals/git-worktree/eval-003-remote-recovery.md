# Eval: 远程机器崩溃恢复

## 任务

远程机器好像挂了，SSH 连不上。用户希望等它恢复后重新同步编译。配置在 ~/.config/remote-dev/ 里。

指导用户处理远程机器中断恢复。

## 期望输出

回答应：
1. 说明自动重试机制
2. 说明 retry 配置项
3. 说明恢复后增量同步
4. 说明从编译步骤继续

## 验证要点

- [ ] 检测连接失败自动等待
- [ ] retry.max_attempts 和 retry.wait_seconds
- [ ] 恢复后 rsync 增量修正
- [ ] 从 cmake --build 增量编译继续
