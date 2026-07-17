# DConfig 配置系统

DConfig 是 DTK 跨进程配置管理方案，支持持久化存储、跨应用共享和 OEM 覆盖。

## 触发关键词

DConfig、应用配置、持久化存储、跨进程配置、OEM 默认值

---

## 核心 API

```cpp
#include <DConfig>

// 创建配置实例
auto *config = DConfig::create("org.deepin.myapp", "example", "", this);

// 读写
bool value = config->value("key", defaultValue).toBool();
config->setValue("key", newValue);

// 监听变化
connect(config, &DConfig::valueChanged, [](const QString &key) { });

// 重置为默认值
config->reset("key");
```

---

## 配置文件路径

```
/usr/share/dsg/appid/configs/<name>.json          # 元数据（权限、类型）
/var/lib/dsg/appid/configs/<name>.json            # 系统级覆盖
~/.config/dsg/appid/configs/<name>.json           # 用户配置
```

---

## 元数据 JSON

```json
{
  "version": "1.0",
  "permissions": ["read", "write"],
  "define": {
    "key1": {
      "type": "bool",
      "default": true
    },
    "key2": {
      "type": "string",
      "default": "value"
    }
  }
}
```

---

## 常用方法

| 方法 | 说明 |
|------|------|
| `value(key, fallback)` | 读取配置值 |
| `setValue(key, value)` | 写入配置值 |
| `keyList()` | 获取所有键 |
| `isValid()` | 是否有效 |
| `isDefaultValue(key)` | 是否为默认值 |
| `isReadOnly(key)` | 是否只读 |
| `reset(key)` | 重置为默认值 |

---

## 调试

```bash
# 查看配置文件
cat ~/.config/dsg/appid/configs/example.json

# 查看元数据
cat /usr/share/dsg/appid/configs/example.json

# DConfig 命令行工具
dconf dump /dsg/appid/
```

---

## 相关文档

- [utilities.md](utilities.md) — DDBusSender 等工具类
