# Eval: Ad-hoc 模式编译

## 任务

用户有个新项目在 ~/work/new-project，远程机器是 devuser@10.0.0.5，远程路径是 ~/work/new-project。没有配置过 remote-dev，需要直接同步编译。

指导用户使用 ad-hoc 模式。

## 期望输出

回答应：
1. 展示 -H 参数指定远程主机
2. 展示 -r 参数指定远程路径
3. 说明无需预配置
4. 展示完整命令

## 验证要点

- [ ] -H devuser@10.0.0.5
- [ ] -r ~/work/new-project
- [ ] 无需预配置即可执行
- [ ] python scripts/remote_dev.py build -H ... -r ...
