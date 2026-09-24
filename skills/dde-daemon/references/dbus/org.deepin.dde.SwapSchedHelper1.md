# org.deepin.dde.SwapSchedHelper1 接口参考

该接口提供交换分区调度辅助能力，用于为指定会话创建 DDE 专用 cgroup（包含 `uiapps` 和 `DE` 两个子组），以实现内存资源的隔离与调度优化。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.SwapSchedHelper1` |
| Object path | `/org/deepin/dde/SwapSchedHelper1` |
| Interface | `org.deepin.dde.SwapSchedHelper1` |
| Bus | System |

### Prepare

为指定会话创建 DDE 专用 cgroup。

- **输入参数**: `sessionID`（string, 类型 `s`）：会话 ID（对应 login1 的 SessionId）
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.SwapSchedHelper1 \
  --object-path /org/deepin/dde/SwapSchedHelper1 \
  --method org.deepin.dde.SwapSchedHelper1.Prepare "sessionID"
```
