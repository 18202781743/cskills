# DConfig 核心概念

## 1. 概述

DConfig 涉及 appId、配置 ID、meta 文件、override 文件等概念。先区分应用
身份和配置文件身份，再处理接口参数与安装路径。

- `appId` — 应用唯一标识
- 配置 ID（`name`）— 配置描述文件标识
- meta 文件 — 配置元信息文件
- override 文件 — OEM 覆盖值文件

## 2. 标识与命名规范

### 2.1 appId

`appId` 是应用程序的唯一 ID，也是 `dde-application-manager` 识别应用所用的
标识。它通常是 desktop 文件名去掉 `.desktop` 后缀，例如：

```text
desktop 文件：deepin-editor.desktop
appId：deepin-editor
```

新应用按应用打包和 desktop 命名规范确定 appId；若采用倒置域名，则可以是：

```text
desktop 文件：org.deepin.example.desktop
appId：org.deepin.example
```

DConfig 直接复用应用既有 appId，不另造一个 DConfig 专用 appId。appId
既可以由 desktop 文件标识确定，也可以通过 `DSG_APP_ID` 声明；两者存在时
应保持一致，并与 `dde-application-manager` 识别的应用身份一致。不要使用
应用显示名称、翻译名称、可执行文件路径或随意设置的
`QCoreApplication::applicationName()` 作为正式应用身份。

默认访问方式通过 `DSGApplication::id()` 获取应用 appId。不指定 appId 时
优先使用这个默认行为；只有确需访问其他应用配置或默认身份不可用时，才使用
`DConfig::create(appId, name, ...)` 显式指定。

### 2.2 配置 ID（name）

配置 ID 是配置描述文件的唯一标识，即 JSON 文件名去掉 `.json` 后缀。
生产配置使用稳定的倒置域名，避免 `settings`、`example` 等全局泛化名称：

```text
meta 文件：org.deepin.editor.json
配置 ID：org.deepin.editor
```

一个应用提供多份配置时，可在应用命名空间后增加稳定的职责后缀：

```text
org.deepin.editor.window
org.deepin.editor.shortcuts
```

配置 ID 一旦发布就构成配置身份。重命名会改变 meta、缓存和 override 的匹配
关系，应作为配置迁移处理。

### 2.3 两层标识的对应关系

appId 与配置 ID 可以使用相同字符串，但语义仍然不同。历史应用也常出现两者
不同的情况：

| 项目 | 历史命名示例 | 倒置域名示例 |
|------|--------------|--------------|
| desktop 文件 | `deepin-editor.desktop` | `org.deepin.example.desktop` |
| appId | `deepin-editor` | `org.deepin.example` |
| meta 文件 | `org.deepin.editor.json` | `org.deepin.example.settings.json` |
| 配置 ID（name） | `org.deepin.editor` | `org.deepin.example.settings` |

对应的安装与调用关系是：

```text
/usr/share/dsg/configs/{appId}/{configId}.json
/etc/dsg/configs/overrides/{appId}/{configId}/*.json
DConfig::create(appId, configId, subpath, parent)
acquireManager(appId, configId, subpath)
```

`subpath` 是运行时配置层级，不属于 appId 或配置 ID，也不能替代配置 ID 的
命名空间。

命名和路径以 deepin 的
[配置文件规范](https://github.com/linuxdeepin/deepin-specifications/blob/master/unstable/%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E8%A7%84%E8%8C%83.md#%E5%90%8D%E8%AF%8D%E8%A7%A3%E9%87%8A)
为基础。该文档位于 `unstable`，使用前确认目标环境采用的当前版本。

## 3. meta 文件

安装包携带，描述配置项元信息和默认值。JSON 格式，`magic` 为
`"dsg.config.meta"`。完整模板见 [assets/config/org.example.settings.json](../../assets/config/org.example.settings.json)。

### contents 中每个配置项属性

| 属性 | 说明 |
|------|------|
| `value` | 默认值，支持 bool、double、string、array、object |
| `permissions` | `readwrite` 可读可写 / 为空时，只读 |
| `visibility` | `private` 仅程序内部可见 / `public` 外部程序可见 |
| `flags` | 字符串数组，可选 `nooverride`、`global`、`user-public` |
| `name` | 显示名称（可选） |
| `description` | 描述文本（可选） |

### CMake 安装

```cmake
# APPID 是应用 id；文件 basename 是配置 ID。
dtk_add_config_meta_files(
    APPID deepin-editor
    BASE ./configs
    FILES
        ./configs/org.deepin.editor.json
        ./configs/a/org.deepin.editor.json
)
```

## 4. override 文件

可选，OEM/管理员用于覆盖 meta 文件中的 `value` 和 `permissions`。`magic` 为
`"dsg.config.override"`。完整模板见 [assets/config/org.example.settings-override.json](../../assets/config/org.example.settings-override.json)。

优先级从低到高：

1. `/usr/share/dsg/configs/overrides/{appId}/{configId}/*.json`
2. `/usr/share/dsg/configs/overrides/{configId}/*.json`
3. `/etc/dsg/configs/overrides/{appId}/{configId}/*.json`（最高优先级）

配置项设置 `flags: ["nooverride"]` 后不可被 override 覆盖。

## 5. subpath

配置文件子路径，格式以 `/` 开头，如 `"/feature/v2"`。查找 meta 文件时从
子目录向上逐级查找，用于配置分层和优先级。

```cpp
auto *config = new DConfig("org.deepin.editor", "/feature/v2", this);
```

## 6. flags

| flag | 说明 |
|------|------|
| `global` | 所有用户共享同一份数据，读写忽略用户身份 |
| `nooverride` | 该配置项不可被 override 文件覆盖 |
| `user-public` | 对用户级外部可见，由 DBus 控制访问权限 |

### global 详解

- 所有用户共享同一份数据，任意用户的修改对所有用户生效
- 缓存存储在系统全局目录 `{DSG_APP_DATA}/configs/{appId}/`
- 全局目录不可写时自动降级到用户目录

实际缓存位置由 `dde-dconfig-daemon` 的版本和运行环境决定，排查时读取
[dconfig-debug.md](dconfig-debug.md)，不要在应用中硬编码。

## 7. 应用无关配置

不指定 appId 的通用配置，所有应用共享。使用 `DConfig::createGeneric()` 访问。

## 8. 配置文件路径

以下是 DConfig 元数据和 override 的系统管理路径。应用代码不应手动拼接
用户配置、缓存或持久化目录；应分别保持 appId 与配置 ID 在目录、文件名和
调用参数中的映射一致。

| 类型 | 路径 |
|------|------|
| 应用 meta 文件 | `/usr/share/dsg/configs/{appId}/{configId}.json` |
| 应用无关 meta | `/usr/share/dsg/configs/{configId}.json` |
| override 文件 | `/etc/dsg/configs/overrides/{appId}/{configId}/*.json` |
