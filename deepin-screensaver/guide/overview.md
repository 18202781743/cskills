# deepin-screensaver 二次开发文档 · 概览

## 项目定位

deepin-screensaver 是 DDE 屏幕保护程序，以 DBus 服务方式运行，提供屏保启动、屏保停止、屏保预览、屏保封面获取、自定义配置启动、可配置项列表查询、屏保可配置性判断和屏保列表刷新能力。使用方通过 DBus 接口与之交互。

## 术语与缩写

- **屏保（ScreenSaver）**：屏幕保护程序，deepin-screensaver 管理其启动、停止和预览。
- **屏保封面（ScreenSaverCover）**：屏保的预览封面图路径。
- **可配置项（ConfigurableItems）**：指定屏保支持的配置参数列表。
- **DBus 属性**：远端接口上的具名值，使用方可读取、写入或监听变化。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以 DBus 接口名为章节，说明其定位、功能能力和使用场景。

## 全局约定

deepin-screensaver 是纯 DBus 服务，不安装 C++ 公共头文件，不导出 CMake 配置文件或库目标。使用方通过 DBus 连接访问其功能。DBus 服务名和对象路径均为 `com.deepin.ScreenSaver`。

## 按功能查阅

- 将 deepin-screensaver 引入使用方工程：参见[集成与构建配置](integration.md)。
- 启动、停止或预览屏保：参见 [com.deepin.ScreenSaver](modules.md#comdeepinscreensaver)。
- 查询屏保运行状态或切换当前屏保：参见 [com.deepin.ScreenSaver](modules.md#comdeepinscreensaver)。
