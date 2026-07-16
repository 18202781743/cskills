# Eval: 配置全局远程机器信息

## 任务

用户有两台机器，本机做开发，远程机器 192.168.1.50 (用户名 devuser) 做编译。需要配置远程编译环境。

指导用户使用 setup --global 配置全局远程信息。

## 期望输出

回答应：
1. 展示 setup --global 命令
2. 展示全局配置文件结构
3. 说明全局配置的作用范围
4. 说明所有项目共享全局配置

## 验证要点

- [ ] python scripts/remote_dev.py setup --global
- [ ] 配置文件: ~/.config/remote-dev/config.json
- [ ] 配置项: remote_host, sudo_password, retry
- [ ] 说明项目配置可覆盖全局配置
