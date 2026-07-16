# Eval: qmake 项目远程编译

## 任务

用户有一个 qmake 项目，需要同步到远程编译，4 线程，不安装。

指导用户使用 qmake 工具链编译。

## 期望输出

回答应：
1. 展示 -t qmake 参数
2. 展示 -j 4 参数
3. 展示 --no-install 参数
4. 展示完整命令

## 验证要点

- [ ] -t qmake 指定工具链
- [ ] -j 4 指定线程数
- [ ] --no-install 跳过安装
- [ ] qmake6 + make 流程
