# com.deepin.daemon.Authenticate.Face 接口参考

该接口提供系统级人脸录入、验证、列出、重命名、删除及默认设备与服务设置能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `com.deepin.daemon.Authenticate` |
| Object path | `/com/deepin/daemon/Authenticate/Face` |
| Interface | `com.deepin.daemon.Authenticate.Face` |
| Bus | System |

### 人脸录入

#### StartEnroll

开始人脸录入。

权限：
- requires_sudo: true

- **输入参数**: `username`（string, 类型 `s`）：用户名；`serviceName`（string, 类型 `s`）：服务名称；`faceName`（string, 类型 `s`）：人脸名称
- **返回值**: `id`（string, 类型 `s`）：录入操作 ID

```bash
pkexec gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method com.deepin.daemon.Authenticate.Face.StartEnroll \
  "testuser" "face_service" "my_face"
```

#### StopEnroll

停止人脸录入。仅允许发起录入的调用者停止。

- **输入参数**: `id`（string, 类型 `s`）：录入操作 ID
- **返回值**: 无

```bash
gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method com.deepin.daemon.Authenticate.Face.StopEnroll \
  "<enroll_id>"
```

### 人脸验证

#### StartVerify

开始人脸验证。

- **输入参数**: `username`（string, 类型 `s`）：用户名；`serviceName`（string, 类型 `s`）：服务名称；`timeout`（int32, 类型 `i`）：超时时间（秒）
- **返回值**: `id`（string, 类型 `s`）：验证操作 ID

```bash
gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method com.deepin.daemon.Authenticate.Face.StartVerify \
  "testuser" "face_service" 30
```

#### StopVerify

停止人脸验证。仅允许发起验证的调用者停止。

- **输入参数**: `id`（string, 类型 `s`）：验证操作 ID
- **返回值**: 无

```bash
gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method com.deepin.daemon.Authenticate.Face.StopVerify \
  "<verify_id>"
```

### 人脸查询与管理

#### ListFaces

列出指定用户已录入的人脸列表。

- **输入参数**: `serviceName`（string, 类型 `s`）：服务名称；`username`（string, 类型 `s`）：用户名
- **返回值**: `faces`（string 数组, 类型 `as`）：人脸名称列表

```bash
gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method com.deepin.daemon.Authenticate.Face.ListFaces \
  "face_service" "testuser"
```

#### RenameFace

重命名已录入的人脸。

权限：
- requires_sudo: true

- **输入参数**: `serviceName`（string, 类型 `s`）：服务名称；`username`（string, 类型 `s`）：用户名；`oldFace`（string, 类型 `s`）：原人脸名称；`newFace`（string, 类型 `s`）：新人脸名称
- **返回值**: 无

```bash
pkexec gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method com.deepin.daemon.Authenticate.Face.RenameFace \
  "face_service" "testuser" "old_name" "new_name"
```

#### DeleteFace

删除指定的人脸。

权限：
- requires_sudo: true

- **输入参数**: `serviceName`（string, 类型 `s`）：服务名称；`username`（string, 类型 `s`）：用户名；`faceName`（string, 类型 `s`）：人脸名称
- **返回值**: 无

```bash
pkexec gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method com.deepin.daemon.Authenticate.Face.DeleteFace \
  "face_service" "testuser" "my_face"
```

#### DeleteFaces

删除指定用户的所有人脸。

权限：
- requires_sudo: true

- **输入参数**: `serviceName`（string, 类型 `s`）：服务名称；`username`（string, 类型 `s`）：用户名
- **返回值**: 无

```bash
pkexec gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method com.deepin.daemon.Authenticate.Face.DeleteFaces \
  "face_service" "testuser"
```

### 默认设备与服务设置

#### SetDefaultDevice

设置指定服务的默认设备。

- **输入参数**: `serviceName`（string, 类型 `s`）：服务名称；`device`（string, 类型 `s`）：设备路径
- **返回值**: 无

```bash
gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method com.deepin.daemon.Authenticate.Face.SetDefaultDevice \
  "face_service" "/dev/video0"
```

#### SetDefaultService

设置默认人脸识别服务。

- **输入参数**: `serviceName`（string, 类型 `s`）：服务名称
- **返回值**: 无

```bash
gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method com.deepin.daemon.Authenticate.Face.SetDefaultService \
  "face_service"
```

### 共享内存信息

#### GetShareMemInfo

获取录入或验证操作的共享内存信息，用于读取图像数据。

- **输入参数**: `id`（string, 类型 `s`）：操作 ID
- **返回值**: `sockPath`（string, 类型 `s`）：共享内存套接字路径；`key`（string, 类型 `s`）：共享内存键；`size`（int32, 类型 `i`）：共享内存大小

```bash
gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method com.deepin.daemon.Authenticate.Face.GetShareMemInfo \
  "<operation_id>"
```

### 属性

#### DefaultDevice

当前默认设备路径。

| 属性 | 值 |
|------|------|
| 类型 | `s` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method org.freedesktop.DBus.Properties.Get \
  com.deepin.daemon.Authenticate.Face DefaultDevice
```

#### DefaultService

当前默认人脸识别服务名称。

| 属性 | 值 |
|------|------|
| 类型 | `s` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method org.freedesktop.DBus.Properties.Get \
  com.deepin.daemon.Authenticate.Face DefaultService
```

#### ServiceList

可用的人脸识别服务列表（JSON 格式字符串）。

| 属性 | 值 |
|------|------|
| 类型 | `s` |
| 读写权限 | read |

读取示例：

```bash
gdbus call --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face \
  --method org.freedesktop.DBus.Properties.Get \
  com.deepin.daemon.Authenticate.Face ServiceList
```

### 信号

#### EnrollStatus

人脸录入状态变化时发出。

- **参数**: `id`（string, 类型 `s`）：操作 ID；`user`（string, 类型 `s`）：用户名；`code`（int32, 类型 `i`）：状态码；`msg`（string, 类型 `s`）：状态消息

```bash
gdbus monitor --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face
```

#### VerifyStatus

人脸验证状态变化时发出。

- **参数**: `id`（string, 类型 `s`）：操作 ID；`user`（string, 类型 `s`）：用户名；`code`（int32, 类型 `i`）：状态码；`msg`（string, 类型 `s`）：状态消息

```bash
gdbus monitor --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face
```

#### DeviceStatus

设备状态变化时发出。

- **参数**: `serviceName`（string, 类型 `s`）：服务名称；`code`（int32, 类型 `i`）：设备状态码

```bash
gdbus monitor --system \
  --dest com.deepin.daemon.Authenticate \
  --object-path /com/deepin/daemon/Authenticate/Face
```

---
