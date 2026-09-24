# org.deepin.dde.Pinyin1 接口参考

该接口提供中文汉字转拼音查询能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Pinyin1` |
| Object path | `/org/deepin/dde/Pinyin1` |
| Interface | `org.deepin.dde.Pinyin1` |
| Bus | Session |

> **验证说明**：该接口为 Session 总线服务，当前环境无 X11 显示，无法进行运行时内省验证。以下方法签名基于 dde-api 源码（`hans2pinyin/exported_methods_auto.go`、`hans2pinyin/main.go`）确认。

## 拼音查询方法

### Query

查询单个汉字字符串的拼音。

- **输入参数**:
  - `hans`（string, 类型 `s`）：汉字字符串
- **返回值**: `pinyin`（string 数组, 类型 `as`）：拼音列表

```bash
gdbus call --session \
  --dest org.deepin.dde.Pinyin1 \
  --object-path /org/deepin/dde/Pinyin1 \
  --method org.deepin.dde.Pinyin1.Query \
  "你好"
```

### QueryList

查询多个汉字字符串的拼音列表，返回 JSON 格式结果。

- **输入参数**:
  - `hansList`（string 数组, 类型 `as`）：汉字字符串数组
- **返回值**: `jsonStr`（string, 类型 `s`）：JSON 格式的拼音结果（键为输入汉字，值为拼音数组）

```bash
gdbus call --session \
  --dest org.deepin.dde.Pinyin1 \
  --object-path /org/deepin/dde/Pinyin1 \
  --method org.deepin.dde.Pinyin1.QueryList \
  "['你好', '世界']"
```
