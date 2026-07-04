# 配置系统决策树

## 1. DConfig 适用场景

```
需要配置持久化？
    │
    ├─ 需要跨应用/跨进程共享？
    │   └─ 是 → DConfig
    │
    ├─ 需要系统级配置（所有用户共享）？
    │   └─ 是 → DConfig（flags: ["global"]）
    │
    ├─ 需要区分用户配置？
    │   └─ 是 → DConfig（默认行为）
    │
    └─ 需要 OEM/厂商预置覆盖值？
        └─ DConfig（override 机制）
```

## 2. 快速路由

| 场景 | 参考文档 |
|------|----------|
| 了解核心概念（appId/meta/override/flags/subpath） | [concepts.md](concepts.md) |
| C++ 中使用 DConfig（含 dconfig2cpp） | [dconfig-cpp.md](dconfig-cpp.md) |
| DBus 方式操作配置 | [dconfig-dbus.md](dconfig-dbus.md) |
| 调试、热加载、缓存路径 | [dconfig-debug.md](dconfig-debug.md) |
