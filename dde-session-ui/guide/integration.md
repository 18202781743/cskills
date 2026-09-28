# 集成与构建配置

dde-session-ui 以独立可执行程序方式运行，不安装公共开发头文件，不导出 CMake 配置文件或库目标。使用方无需安装本项目的开发包，通过命令行调用各组件即可。

## 开发包

dde-session-ui 不提供开发包。使用方只需确保运行环境中已安装 dde-session-ui，通过命令行调用各组件程序。

## 引用公开接口

使用方通过命令行调用各组件可执行程序：

- `dde-blackwidget` — 黑屏遮罩组件
- `dde-bluetooth-dialog` — 蓝牙设备对话框
- `dde-touchscreen-dialog` — 触摸屏校准对话框
- `dde-license-dialog` — 许可证对话框
- `dde-pixmix` — 图片混合工具
- `dde-wm-chooser` — 窗口管理器选择器
- `dde-hints-dialog` — 提示对话框
- `dde-welcome` — 欢迎页面
- `dde-suspend-dialog` — 挂起确认对话框
- `dde-osd` — OSD 通知
- `dde-lowpower` — 低电量警告
- `dde-warning-dialog` — 警告对话框
- `dde-switchtogreeter` — 切换到 Greeter
- `dmemory-warning-dialog` — 内存警告对话框

## 关联文档

- 导出类型的能力与使用场景见[导出类型介绍](modules.md)。
