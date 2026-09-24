# org.deepin.dde.LangSelector1 接口参考

该接口提供系统语言选择和切换能力，包括获取区域列表、设置当前区域、添加/删除区域、生成区域等。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.LangSelector1` |
| Object path | `/org/deepin/dde/LangSelector1` |
| Interface | `org.deepin.dde.LangSelector1` |
| Bus | Session |

### 语言选择属性

#### CurrentLocale（属性）

当前区域设置。

| 属性 | 值 |
|------|------|
| 类型 | `s` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.LangSelector1 \
  --object-path /org/deepin/dde/LangSelector1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.LangSelector1 CurrentLocale
```

#### Locales（属性）

已安装的区域列表。

| 属性 | 值 |
|------|------|
| 类型 | `as` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.LangSelector1 \
  --object-path /org/deepin/dde/LangSelector1 \
  --method org.freedesktop.DBus.Properties.Get \
  org.deepin.dde.LangSelector1 Locales
```

### 语言选择方法

#### GetLocaleList

获取支持的区域列表。

- **输入参数**: 无
- **返回值**: `locales`（`as`，string 数组）：区域列表

```bash
gdbus call --session \
  --dest org.deepin.dde.LangSelector1 \
  --object-path /org/deepin/dde/LangSelector1 \
  --method org.deepin.dde.LangSelector1.GetLocaleList
```

#### SetLocale

设置当前区域。

- **输入参数**: `locale`（string, 类型 `s`）：区域名称
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.LangSelector1 \
  --object-path /org/deepin/dde/LangSelector1 \
  --method org.deepin.dde.LangSelector1.SetLocale "zh_CN.UTF-8"
```

#### AddLocale

添加区域。

- **输入参数**: `locale`（string, 类型 `s`）：区域名称
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.LangSelector1 \
  --object-path /org/deepin/dde/LangSelector1 \
  --method org.deepin.dde.LangSelector1.AddLocale "en_US.UTF-8"
```

#### DeleteLocale

删除区域。

- **输入参数**: `locale`（string, 类型 `s`）：区域名称
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.LangSelector1 \
  --object-path /org/deepin/dde/LangSelector1 \
  --method org.deepin.dde.LangSelector1.DeleteLocale "en_US.UTF-8"
```

#### GenLocale

生成指定区域。

- **输入参数**: `locale`（string, 类型 `s`）：区域名称
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.LangSelector1 \
  --object-path /org/deepin/dde/LangSelector1 \
  --method org.deepin.dde.LangSelector1.GenLocale "en_US.UTF-8"
```

#### GetLocaleDescription

获取区域的描述信息。

- **输入参数**: `locale`（string, 类型 `s`）：区域名称
- **返回值**: `description`（string, 类型 `s`）：区域描述

```bash
gdbus call --session \
  --dest org.deepin.dde.LangSelector1 \
  --object-path /org/deepin/dde/LangSelector1 \
  --method org.deepin.dde.LangSelector1.GetLocaleDescription "zh_CN.UTF-8"
```

#### GetLanguageSupportPackages

获取指定区域的语言包列表。

- **输入参数**: `locale`（string, 类型 `s`）：区域名称
- **返回值**: `packages`（`as`，string 数组）：语言包列表

```bash
gdbus call --session \
  --dest org.deepin.dde.LangSelector1 \
  --object-path /org/deepin/dde/LangSelector1 \
  --method org.deepin.dde.LangSelector1.GetLanguageSupportPackages "zh_CN.UTF-8"
```

#### Reset

重置语言设置为默认值。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.deepin.dde.LangSelector1 \
  --object-path /org/deepin/dde/LangSelector1 \
  --method org.deepin.dde.LangSelector1.Reset
```
