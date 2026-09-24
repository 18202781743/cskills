# org.deepin.dde.Grub2 接口参考

该接口提供 GRUB2 引导配置管理能力。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Grub2` |
| Object path | `/org/deepin/dde/Grub2` |
| Interface | `org.deepin.dde.Grub2` |
| Bus | System |
### GRUB2 管理方法

#### Disable

禁用 GRUB2。

- **功能**：禁用 GRUB2 引导菜单，开机时不再显示引导选择界面。
- **触发条件**：当用户在控制中心关闭 GRUB2 引导菜单时调用。
- **使用场景**：控制中心引导设置关闭 GRUB2 菜单。

- **输入参数**: 无
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.Disable
```

#### Enable

启用 GRUB2。

- **功能**：启用 GRUB2 引导菜单，开机时显示引导选择界面。
- **触发条件**：当用户在控制中心开启 GRUB2 引导菜单时调用。
- **使用场景**：控制中心引导设置开启 GRUB2 菜单。

- **输入参数**: 无
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.Enable
```

#### SkipGrub

跳过 GRUB2。

- **功能**：设置下次启动跳过 GRUB2 引导菜单一次。
- **触发条件**：当用户需要临时跳过引导菜单时调用。
- **使用场景**：引导设置临时跳过 GRUB2 菜单。

- **输入参数**: 无
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.SkipGrub
```

#### GetAvailableGfxmodes

获取可用图形模式。

- **功能**：获取 GRUB2 支持的所有可用图形分辨率模式列表。
- **触发条件**：当用户在控制中心查看可选 GRUB2 分辨率时调用。
- **使用场景**：控制中心引导设置选择 GRUB2 图形分辨率。

- **输入参数**: 无
- **返回值**: `a(ss)`（元组数组）：图形模式列表

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.GetAvailableGfxmodes
```

#### GetSimpleEntryTitles

获取简单条目标题。

- **功能**：获取 GRUB2 引导菜单中所有启动条目的标题列表。
- **触发条件**：当需要展示可选的启动条目时调用。
- **使用场景**：控制中心引导设置选择默认启动项。

- **输入参数**: 无
- **返回值**: `as`（string 数组）：标题列表

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.GetSimpleEntryTitles
```

#### PrepareGfxmodeDetect

准备图形模式检测。

- **功能**：准备 GRUB2 图形模式检测环境，使下次启动时自动检测可用分辨率。
- **触发条件**：当用户需要重新检测 GRUB2 支持的分辨率时调用。
- **使用场景**：控制中心引导设置重新检测图形模式。

- **输入参数**: 无
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.PrepareGfxmodeDetect
```

#### Reset

重置 GRUB2 配置。

- **功能**：重置 GRUB2 配置到默认状态。
- **触发条件**：当用户需要恢复 GRUB2 默认配置时调用。
- **使用场景**：控制中心引导设置恢复 GRUB2 默认配置。

- **输入参数**: 无
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.Reset
```

#### SetDefaultEntry

设置默认条目。

- **功能**：设置 GRUB2 引导菜单的默认启动条目。
- **触发条件**：当用户在控制中心选择默认启动项时调用。
- **使用场景**：控制中心引导设置选择默认启动项。

- **输入参数**: `entry`（string, 类型 `s`）：条目标题
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.SetDefaultEntry "entry"
```

#### SetEnableTheme

设置是否启用主题。

- **功能**：设置是否启用 GRUB2 主题。
- **触发条件**：当用户在控制中心开启或关闭 GRUB2 主题时调用。
- **使用场景**：控制中心引导设置开启或关闭主题。

- **输入参数**: `enable`（bool, 类型 `b`）：是否启用
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.SetEnableTheme true
```

#### SetGfxmode

设置图形模式。

- **功能**：设置 GRUB2 引导界面的图形分辨率模式。
- **触发条件**：当用户在控制中心选择 GRUB2 分辨率时调用。
- **使用场景**：控制中心引导设置选择图形分辨率。

- **输入参数**: `mode`（string, 类型 `s`）：图形模式
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.SetGfxmode "1920x1080"
```

#### SetTimeout

设置超时时间。

- **功能**：设置 GRUB2 引导菜单的等待超时时间（秒）。
- **触发条件**：当用户在控制中心修改引导菜单等待时间时调用。
- **使用场景**：控制中心引导设置修改菜单超时时间。

- **输入参数**: `timeout`（int32, 类型 `i`）：超时秒数
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.SetTimeout 5
```

#### GetBackground

获取背景图片。

- **功能**：获取当前 GRUB2 引导界面的背景图片路径。
- **触发条件**：当需要展示当前 GRUB2 背景图片时调用。
- **使用场景**：控制中心引导设置显示当前背景。

- **输入参数**: 无
- **返回值**: `s`（string）：背景图片路径

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.GetBackground
```

#### SetBackgroundSourceFile

设置背景源文件。

- **功能**：设置 GRUB2 引导界面的背景图片源文件。
- **触发条件**：当用户在控制中心选择新的背景图片时调用。
- **使用场景**：控制中心引导设置更换背景图片。

- **输入参数**: `file`（string, 类型 `s`）：文件路径
- **返回值**: 无

权限：
- requires_sudo: true

```bash
pkexec gdbus call --system \
  --dest org.deepin.dde.Grub2 \
  --object-path /org/deepin/dde/Grub2 \
  --method org.deepin.dde.Grub2.SetBackgroundSourceFile "/path/to/bg"
```

