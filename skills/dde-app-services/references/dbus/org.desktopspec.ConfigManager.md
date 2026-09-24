# org.desktopspec.ConfigManager 接口参考

该接口提供全局的配置管理器对象获取、更新、同步能力，以及 dde-dconfig-daemon 自身的日志规则设置、用户配置数据移除和配置重新加载能力。其中配置管理器对象获取、更新、同步为全局 DConfig 管理功能；日志规则设置（enableVerboseLogging、disableVerboseLogging、setLogRules）仅用于设置 dde-dconfig-daemon 自身的日志级别与行为，而非系统全局日志。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.desktopspec.ConfigManager` |
| Object path | `/` |
| Interface | `org.desktopspec.ConfigManager` |
| Bus | System |



### 管理器对象获取

#### acquireManagerV2

获取指定用户、应用和资源的配置管理器对象（V2）。

- **输入参数**: `uid`（uint32, 类型 `u`）：用户 ID；`appid`（string, 类型 `s`）：应用 ID；`name`（string, 类型 `s`）：资源名；`subpath`（string, 类型 `s`）：子路径
- **返回值**: `o`（object path）：管理器对象路径

```bash
gdbus call --system \
  --dest org.desktopspec.ConfigManager \
  --object-path / \
  --method org.desktopspec.ConfigManager.acquireManagerV2 1000 "org.deepin.dde.daemon" "org.deepin.dde.daemon.power" ""
```

### 兼容性接口

本接口中存在新旧两个版本的管理器对象获取方法，用于向后兼容：

- `acquireManagerV2`（当前版本）：带 `uid` 参数，支持多用户场景下获取指定用户的配置管理器对象。
- `acquireManager`（旧版兼容接口）：不含 `uid` 参数（内部使用调用方的 uid），功能与 `acquireManagerV2` 相同。

两者功能一致，均为获取配置管理器对象。旧版 `acquireManager` 保留仅为兼容历史调用方，新代码应使用 `acquireManagerV2`。

### 配置更新与同步

#### update

更新指定路径的配置。

- **输入参数**: `path`（string, 类型 `s`）：管理器对象路径
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.desktopspec.ConfigManager \
  --object-path / \
  --method org.desktopspec.ConfigManager.update "/path/to/manager"
```

#### sync

同步指定路径的配置到磁盘。

- **输入参数**: `path`（string, 类型 `s`）：管理器对象路径
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.desktopspec.ConfigManager \
  --object-path / \
  --method org.desktopspec.ConfigManager.sync "/path/to/manager"
```

#### setDelayReleaseTime

设置延迟释放时间。

- **输入参数**: `time`（int32, 类型 `i`）：延迟时间（毫秒）
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.desktopspec.ConfigManager \
  --object-path / \
  --method org.desktopspec.ConfigManager.setDelayReleaseTime 5000
```

#### delayReleaseTime

获取延迟释放时间。

- **输入参数**: 无
- **返回值**: `i`（int32）：延迟时间（毫秒）

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.desktopspec.ConfigManager \
  --object-path / \
  --method org.desktopspec.ConfigManager.delayReleaseTime
```


### 日志规则设置（仅作用于 dde-dconfig-daemon 自身）

> 以下接口仅用于设置 dde-dconfig-daemon 自身的日志级别与行为，不影响系统全局日志配置。

#### enableVerboseLogging

启用详细日志。

- **输入参数**: 无
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.desktopspec.ConfigManager \
  --object-path / \
  --method org.desktopspec.ConfigManager.enableVerboseLogging
```

#### disableVerboseLogging

禁用详细日志。

- **输入参数**: 无
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.desktopspec.ConfigManager \
  --object-path / \
  --method org.desktopspec.ConfigManager.disableVerboseLogging
```

#### setLogRules

设置日志规则。

- **输入参数**: `rules`（string, 类型 `s`）：日志规则 JSON
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.desktopspec.ConfigManager \
  --object-path / \
  --method org.desktopspec.ConfigManager.setLogRules '{"rules":"*=true"}'
```


### 数据管理

#### removeUserData

移除指定用户的配置数据。

- **输入参数**: `uid`（uint32, 类型 `u`）：用户 ID
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.desktopspec.ConfigManager \
  --object-path / \
  --method org.desktopspec.ConfigManager.removeUserData 1000
```

#### reload

重新加载配置。

- **输入参数**: 无
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.desktopspec.ConfigManager \
  --object-path / \
  --method org.desktopspec.ConfigManager.reload
```

---
