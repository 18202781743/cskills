---
name: dtk
description: |
  DTK (Deepin Tool Kit) 开发指南，覆盖 dtkcore/dtkgui/dtkwidget/dtkdeclarative/dtklog。
  触发场景：
  - 开发 DDE 应用需要选择 DTK 控件
  - 实现主题感知 UI（图标、配色、窗口装饰）
  - 使用 DConfig/DSettings 管理配置
  - 需要遵循 DDE 日志规范
  - 图标/主题/窗口装饰相关问题
---

# DTK 开发指南

DTK 是深度桌面环境的核心开发框架，包含控件、主题、图标、配置等完整解决方案。

## 快速路由

按问题类型定位参考文档：

| 场景 | 参考文档 |
|------|----------|
| 创建新项目/环境搭建 | [references/build-and-debug.md](references/build-and-debug.md) |
| 选择/显示图标 | [references/icons/index.md](references/icons/index.md) |
| 主题切换/配色 | [references/theming/index.md](references/theming/index.md) |
| 选择 QWidget 控件 | [references/widgets/index.md](references/widgets/index.md) |
| 选择 QML 控件 | [references/declarative/index.md](references/declarative/index.md) |
| 应用配置持久化 | [references/config/index.md](references/config/index.md) |
| 日志规范 | [references/log/index.md](references/log/index.md) |

## 高频跨域场景

- **创建新的 DTK 项目** → [build-and-debug.md](references/build-and-debug.md)（debian 依赖、CMake 配置、编译、调试环境变量，区分 DTK5/DTK6）
- **在自定义控件中使用主题图标** → 先读 [icons/index.md](references/icons/index.md)，再读 [theming/palette.md](references/theming/palette.md)
- **QML 中显示 dci 图标** → [declarative/dci-icon.md](references/declarative/dci-icon.md)
- **控件内嵌入消息提示** → [widgets/message.md](references/widgets/message.md) + [core/notify.md](references/core/notify.md)

## 仓库依赖关系

**编译强依赖（实线）：**

```
dtkgui ──→ dtkwidget
    │
    └──→ dtkdeclarative
```

**全部 8 个项目依赖图（实线=编译依赖，虚线=运行时/功能关联）：**

```
                     dtkcommon (CMake 宏/构建基础设施)
                    ╱    │    ╲
               虚线╱  虚线│  虚线╲
                 ╱      │      ╲
           dtklog   dtkcore ──→ dtkgui
                        │         │
                    虚线│     实线╱   实线╲
                        ↓     ╱         ╲
                      dtkgui ←┘    dtkdeclarative
                     ╱      ╲            │
                实线╱      实线╲    虚线╱   虚线╲
                  ╱          ╲      ╱         ╲
          dtkwidget    dtkdeclarative  │          │
             │                          │          │
        虚线╱   虚线╲              虚线↓          虚线↓
           ↓       ↓          qt5integration  qt5platform-plugins
    qt5integration  qt5platform-plugins
```

> **说明**：dtkcommon 提供 CMake 构建宏（DtkBuildHelper），不包含 C++ API。dtklog/dtkgui/dtkwidget 等通过 CMake 宏间接依赖 dtkcommon 的构建基础设施，而非编译期头文件依赖。`DDciFile`（dci 文件解析）来自 dtkcore，`DDciIcon`（dci 图标渲染）来自 dtkgui，dtkgui 依赖 dtkcore 中的 `DDciFile`。

**核心库 vs 平台集成库：**
- **核心库**（dtkcommon/dtklog/dtkcore/dtkgui/dtkwidget/dtkdeclarative）：编译期依赖，提供 API 接口
- **平台集成库**（qt5integration/qt5platform-plugins）：运行时依赖，提供风格渲染和平台窗口管理，编译不依赖

**依赖说明：**

| 项目 | 编译依赖 | 运行时/功能关联 |
|------|----------|----------------|
| dtkcommon | 无 | — |
| dtklog | 无（独立编译） | dtkcommon（CMake 构建宏） |
| dtkcore | 无（独立编译） | dtkcommon（CMake 构建宏） |
| dtkgui | dtkcore | — |
| dtkwidget | dtkgui | qt5integration（Chameleon 风格渲染） |
| dtkdeclarative | dtkgui | — |
| qt5integration | dtkgui, dtkwidget | — |
| qt5platform-plugins | dtkgui | — |

## 核心模块速览

| 模块 | 来源 | 核心功能 |
|------|------|----------|
| 图标系统 | dtkgui | DDciIcon, DIcon, DIconTheme |
| 调色板 | dtkgui/dtkwidget | DPalette, DStyle |
| QWidget 控件 | dtkwidget | 110+ 控件 |
| QML 控件 | dtkdeclarative | 33+ QML 组件 |
| 配置系统 | dtkcore | DConfig, DSettings |
| 日志系统 | dtklog | Logger, Appender |
