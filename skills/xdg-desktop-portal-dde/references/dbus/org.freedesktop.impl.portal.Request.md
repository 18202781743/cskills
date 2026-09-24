# org.freedesktop.impl.portal.Request 接口参考

该接口提供标准 portal 请求关闭能力。Request 对象在每次 portal 请求时动态创建，对象路径不固定。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.freedesktop.impl.portal.desktop.dde` |
| Object path | 动态生成（每次请求时创建） |
| Interface | `org.freedesktop.impl.portal.Request` |
| Bus | Session |

### 请求方法

#### Close

关闭请求。

- **输入参数**: 无
- **返回值**: 无

```bash
gdbus call --session \
  --dest org.freedesktop.impl.portal.desktop.dde \
  --object-path /org/freedesktop/portal/desktop/request/<dynamic> \
  --method org.freedesktop.impl.portal.Request.Close
```
