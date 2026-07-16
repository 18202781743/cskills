# Eval: CMake 项目远程编译

## 任务

用户需要将本地项目同步到远程并使用 cmake 编译。

指导用户执行完整的同步编译流程。

## 期望输出

回答应：
1. 展示 sync + build 命令
2. 展示 cmake configure 和 build
3. 说明并行编译参数
4. 说明编译失败处理

## 验证要点

- [ ] python scripts/remote_dev.py build -p <name>
- [ ] cmake 配置 + cmake --build
- [ ] -j N 并行编译
- [ ] 编译失败不执行 install
