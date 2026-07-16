# Eval: 配置项目远程编译

## 任务

用户的项目在 /home/devuser/work/dde-file-manager，远程机器上同样的路径。需要配置项目，cmake 要加 -DCMAKE_BUILD_TYPE=Debug 参数，用 8 个线程编译。

指导用户配置项目并执行同步编译。

## 期望输出

回答应：
1. 展示 setup 命令
2. 展示项目配置文件结构
3. 展示 cmake 配置和 build 配置
4. 展示执行同步编译命令

## 验证要点

- [ ] python scripts/remote_dev.py setup
- [ ] 配置文件: ~/.config/remote-dev/projects/<name>.json
- [ ] cmake.tool: cmake, cmake.extra_args, build.parallel_jobs
- [ ] python scripts/remote_dev.py build -p <name>
