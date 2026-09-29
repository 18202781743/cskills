# dtkcore 二次开发文档 · 概览

## 项目定位

dtkcore 是基于 Qt 的 C++ 基础库，提供配置与设置、日志、文件与目录、系统信息、DBus 通信、通知、文本处理和线程调度能力。界面控件与视觉主题由上层库提供。

## 术语与缩写

- **DTK**：Deepin Tool Kit。
- **DTK5 / DTK6**：分别与 Qt5 / Qt6 配套的主版本。
- **DCore**：公开头文件安装目录名，也是主要 C++ 命名空间的一部分。
- **DSG**：配置及应用数据相关的目录和环境变量前缀。
- **XDG**：用户数据、配置和缓存目录的约定。
- **DCI**：将多份图标数据组织在单个文件中的格式。
- **公开接口载体**：本库对外发布、供调用者引入的头文件。
- **转发头**：以公开类型名命名的无后缀头文件，转而引入实际声明所在的头文件。
- **后端**：为配置或设置模型承担实际持久化的实现，可由调用者按接口选择或替换。
- **DBus 属性**：远端接口上的具名值，与 C++ 类的成员属性不同。
- **待完成的调用**：已经异步发起、尚未取得结果的 DBus 调用句柄。
- **单位换算基数**：相邻容量单位之间的换算比例，可由容量格式化类型设置。

## 导出类型

[导出类型介绍](dtk6core-dev.md)是本项目唯一的类型参考文档。它以类型名为章节，逐一说明对外导出类型的定位、功能能力和使用场景。

## 全局约定

公开头文件安装在按主版本区分的 DCore 目录。主要公开符号位于 `Dtk::Core`，另有全局作用域的 `DUtil`。版本判断和跨主版本构建方式见[集成与构建配置](integration.md)。

公开类型多以 `D` 开头，头文件通常以类型名首字母小写后的形式命名；部分类型还提供与类型同名的无后缀转发头。与 Qt 类型职责相近但行为不同的类型可用 `D` 前缀区分。枚举项通常用英文描述状态或事件，部分枚举以数量项收尾；宏一般使用大写字母和下划线。具体名称以公开声明为准。

## 按功能查阅

- 将 dtkcore 引入 CMake、qmake 或 pkg-config 工程：参见[集成与构建配置](integration.md)。
- 管理配置或设置：参见 [DConfig](dtk6core-dev.md#dconfig) 与 [DSettings](dtk6core-dev.md#dsettings)。
- 监视文件、查询系统信息或与 DBus 服务交互：参见 [DFileWatcher](dtk6core-dev.md#dfilewatcher)、[DSysInfo](dtk6core-dev.md#dsysinfo) 与 [DDBusCaller](dtk6core-dev.md#ddbuscaller)。
- 读取 DCI 资源、探测文本编码或换算容量：参见 [DDciFile](dtk6core-dev.md#ddcifile)、[DTextEncoding](dtk6core-dev.md#dtextencoding) 与 [DDiskSizeFormatter](dtk6core-dev.md#ddisksizeformatter)。
- 在 DTK5 与 DTK6 之间迁移构建配置：参见[集成与构建配置](integration.md)；迁移公开类型：参见对应的[导出类型介绍](dtk6core-dev.md)。
