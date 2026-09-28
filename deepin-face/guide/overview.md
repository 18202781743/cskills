# deepin-face 二次开发文档 · 概览

## 项目定位

deepin-face 是 DDE 人脸识别服务，基于 SeetaFace 引擎，以 DBus 服务方式运行在系统总线上，提供人脸注册、人脸验证和人脸特征删除能力。使用方通过 DBus 接口与之交互。

## 术语与缩写

- **SeetaFace**：deepin-face 所使用的人脸检测、关键点定位、活体检测、追踪和识别引擎。
- **特征（chara）**：一段已注册的人脸特征数据，以字符串标识，用于后续验证和删除。
- **特征类型（charaType）**：区分不同特征来源或用途的整型标记。
- **DBus 属性**：远端接口上的具名值，使用方可读取或监听变化。
- **actionId**：调用方传入的标识字符串，用于关联一次注册或验证会话的启动与停止操作。

## 导出类型

[导出类型介绍](modules.md)是本项目唯一的类型参考文档。以 DBus 接口名为章节，说明其定位、功能能力和使用场景。

## 全局约定

deepin-face 是纯 DBus 服务，不安装 C++ 公共头文件，不导出 CMake 配置文件或库目标。使用方通过 DBus 连接访问其功能。DBus 服务名、对象路径和接口名均为 `org.deepin.dde.Face1`，运行在系统总线上。

## 按功能查阅

- 将 deepin-face 引入使用方工程：参见[集成与构建配置](integration.md)。
- 执行人脸注册或验证：参见 [org.deepin.dde.Face1](modules.md#orgdeepinddeface1)。
