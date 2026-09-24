# org.deepin.dde.Accounts1 接口参考

该接口提供用户和用户组创建、删除、查询和属性管理能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Accounts1` |
| Object path | `/org/deepin/dde/Accounts1` |
| Interface | `org.deepin.dde.Accounts1` |
| Bus | System |
### 用户管理方法

#### CreateUser

创建用户。

- **输入参数**: `name`（string, 类型 `s`）：用户名；`fullName`（string, 类型 `s`）：全名；`groupType`（int32, 类型 `i`）：用户组类型
- **返回值**: `o`（object path）：用户路径

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Accounts1 \
  --object-path /org/deepin/dde/Accounts1 \
  --method org.deepin.dde.Accounts1.CreateUser "user" "Full Name" 1
```

#### DeleteUser

删除用户。

- **输入参数**: `name`（string, 类型 `s`）：用户名；`rmHome`（bool, 类型 `b`）：是否删除主目录
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Accounts1 \
  --object-path /org/deepin/dde/Accounts1 \
  --method org.deepin.dde.Accounts1.DeleteUser "user" true
```

#### FindUserById

通过 UID 查找用户。

- **输入参数**: `uid`（int32, 类型 `i`）：用户 ID
- **返回值**: `o`（object path）：用户路径

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Accounts1 \
  --object-path /org/deepin/dde/Accounts1 \
  --method org.deepin.dde.Accounts1.FindUserById 1000
```

#### FindUserByName

通过用户名查找用户。

- **输入参数**: `name`（string, 类型 `s`）：用户名
- **返回值**: `o`（object path）：用户路径

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Accounts1 \
  --object-path /org/deepin/dde/Accounts1 \
  --method org.deepin.dde.Accounts1.FindUserByName "user"
```

#### RandUserIcon

随机获取用户图标。

- **输入参数**: 无
- **返回值**: `s`（string）：图标路径

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Accounts1 \
  --object-path /org/deepin/dde/Accounts1 \
  --method org.deepin.dde.Accounts1.RandUserIcon
```

#### IsUsernameValid

校验用户名是否合法。

- **输入参数**: `name`（string, 类型 `s`）：用户名
- **返回值**: `(bas)`（元组）：是否合法、错误信息和建议列表

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Accounts1 \
  --object-path /org/deepin/dde/Accounts1 \
  --method org.deepin.dde.Accounts1.IsUsernameValid "user"
```

#### IsPasswordValid

校验密码是否合法。

- **输入参数**: `password`（string, 类型 `s`）：密码
- **返回值**: `(bas)`（元组）：是否合法、错误信息和建议列表

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Accounts1 \
  --object-path /org/deepin/dde/Accounts1 \
  --method org.deepin.dde.Accounts1.IsPasswordValid "password"
```
### 用户组管理方法

#### CreateGroup

创建用户组。

- **输入参数**: `name`（string, 类型 `s`）：组名
- **返回值**: `o`（object path）：组路径

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Accounts1 \
  --object-path /org/deepin/dde/Accounts1 \
  --method org.deepin.dde.Accounts1.CreateGroup "group"
```

#### DeleteGroup

删除用户组。

- **输入参数**: `name`（string, 类型 `s`）：组名
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Accounts1 \
  --object-path /org/deepin/dde/Accounts1 \
  --method org.deepin.dde.Accounts1.DeleteGroup "group"
```

#### GetGroups

获取用户组列表。

- **输入参数**: 无
- **返回值**: `as`（string 数组）：组列表

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Accounts1 \
  --object-path /org/deepin/dde/Accounts1 \
  --method org.deepin.dde.Accounts1.GetGroups
```

#### GetGroupInfoByName

通过组名获取组信息。

- **输入参数**: `name`（string, 类型 `s`）：组名
- **返回值**: `a{sv}`（字典）：组信息

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Accounts1 \
  --object-path /org/deepin/dde/Accounts1 \
  --method org.deepin.dde.Accounts1.GetGroupInfoByName "group"
```

#### GetPresetGroups

获取预设用户组列表。

- **输入参数**: 无
- **返回值**: `as`（string 数组）：预设组列表

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Accounts1 \
  --object-path /org/deepin/dde/Accounts1 \
  --method org.deepin.dde.Accounts1.GetPresetGroups
```

