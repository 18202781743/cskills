# org.deepin.dde.Search1 接口参考

该接口提供系统搜索和搜索字典管理能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Search1` |
| Object path | `/org/deepin/dde/Search1` |
| Interface | `org.deepin.dde.Search1` |
| Bus | Session |
### 搜索方法

#### NewSearchWithStrDict

使用字符串字典创建搜索。

- **输入参数**: `dict`（字典, 类型 `a{ss}`）：搜索字典
- **返回值**: `o`（object path）：搜索句柄

```bash
gdbus call --session \
  --dest org.deepin.dde.Search1 \
  --object-path /org/deepin/dde/Search1 \
  --method org.deepin.dde.Search1.NewSearchWithStrDict {"key":"value"}
```

#### NewSearchWithStrList

使用字符串列表创建搜索。

- **输入参数**: `list`（string 数组, 类型 `as`）：搜索列表
- **返回值**: `o`（object path）：搜索句柄

```bash
gdbus call --session \
  --dest org.deepin.dde.Search1 \
  --object-path /org/deepin/dde/Search1 \
  --method org.deepin.dde.Search1.NewSearchWithStrList ["item1","item2"]
```

#### SearchStartWithString

使用字符串开始搜索。

- **输入参数**: `str`（string, 类型 `s`）：搜索字符串
- **返回值**: `o`（object path）：搜索句柄

```bash
gdbus call --session \
  --dest org.deepin.dde.Search1 \
  --object-path /org/deepin/dde/Search1 \
  --method org.deepin.dde.Search1.SearchStartWithString "keyword"
```

#### SearchString

搜索字符串。

- **输入参数**: `str`（string, 类型 `s`）：搜索字符串
- **返回值**: `as`（string 数组）：搜索结果

```bash
gdbus call --session \
  --dest org.deepin.dde.Search1 \
  --object-path /org/deepin/dde/Search1 \
  --method org.deepin.dde.Search1.SearchString "keyword"
```

