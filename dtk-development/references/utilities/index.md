# 工具类与核心类

DTK 工具类与核心类提供主题系统、字体管理、系统信息、DBus 通信、窗口管理、日志、单实例等跨项目通用功能，主要来自 dtkcore/dtkgui/dtkwidget。

## 按使用频率排序

| 类名 | 使用频率 | 所属模块 | 文档 |
|------|---------|---------|------|
| DGuiApplicationHelper | 580 | dtkgui | [gui-helper.md](gui-helper.md) |
| DFontSizeManager | 522 | dtkgui/dtkwidget | [font-manager.md](font-manager.md) |
| DSysInfo | 93 | dtkcore | [sysinfo.md](sysinfo.md) |
| DDBusSender | 80 | dtkcore | [dbus.md](dbus.md) |
| DPaletteHelper | 59 | dtkwidget | [../widgets/palette-helper.md](../widgets/palette-helper.md) |
| DWindowManagerHelper | 49 | dtkgui | [window-manager.md](window-manager.md) |
| DDesktopServices | 27 | dtkcore/dtkgui | [desktop-services.md](desktop-services.md) |
| DLogManager | 72 | dtkcore | [log.md](log.md) |
| DSingleton | 18 | dtkcore | [singleton.md](singleton.md) |

## 快速决策树

```
需要什么功能？
    │
    ├─ 主题/调色板/平台判断？
    │   └─ DGuiApplicationHelper → [gui-helper.md](gui-helper.md)
    │
    ├─ 字体大小管理？
    │   └─ DFontSizeManager / DFontManager → [font-manager.md](font-manager.md)
    │
    ├─ 系统版本/类型判断？
    │   └─ DSysInfo → [sysinfo.md](sysinfo.md)
    │
    ├─ DBus 通信？
    │   └─ DDBusSender / DDBusInterface → [dbus.md](dbus.md)
    │
    ├─ 窗口管理器/装饰控制？
    │   └─ DWindowManagerHelper → [window-manager.md](window-manager.md)
    │
    ├─ 文件管理器/系统音效？
    │   └─ DDesktopServices → [desktop-services.md](desktop-services.md)
    │
    ├─ 日志？
    │   └─ DLogManager → [log.md](log.md)
    │
    ├─ 单实例/进程间通信？
    │   └─ DSingleton → [singleton.md](singleton.md)
    │
    └─ 拼音/文件系统/通知？
        └─ DUtil → [util.md](util.md)
```

## 相关文档

- [../theme/index.md](../theme/index.md) — 主题系统（调色板/图标/风格）
- [../config/index.md](../config/index.md) — DConfig 配置系统
- [../architecture.md](../architecture.md) — DTK 核心架构
