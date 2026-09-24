# org.deepin.dde.Osd1 接口参考

该接口提供 OSD（On-Screen Display）提示的显示能力，支持通过 OSD 类型标识触发对应的屏幕提示显示。

dde-shell 的 OSD 面板（`OsdPanel`）在 Session 总线上注册了两个 D-Bus 接口，两者提供相同的 `ShowOSD` 方法：

- `org.deepin.dde.Osd1`（本接口）— 注册在 object path `/`，通过 `registerService` 注册独立 service name `org.deepin.dde.Osd1`，并由 `OsdDBusAdaptor` 适配。用于兼容旧版调用方。
- `org.deepin.dde.shell.osd` — 注册在 object path `/org/deepin/dde/shell/osd`，由 `OsdPanel` 对象直接通过 `ExportAllSlots` 暴露，无独立 service name（使用 dde-shell 进程的 bus name）。

## 接口信息

| 字段 | 值 |
|------|------|
| Service | `org.deepin.dde.Osd1` |
| Object path | `/` |
| Interface | `org.deepin.dde.Osd1` |
| Bus | Session |

## org.deepin.dde.shell.osd 接口

`org.deepin.dde.shell.osd` 接口由 `OsdPanel` 对象在 `init()` 中通过 `ExportAllSlots` 直接注册，无独立 service name（使用 dde-shell 进程的 bus name，通常为 `org.deepin.dde.shell`）。

| 字段 | 值 |
|------|------|
| Service | 无独立 service name（使用 dde-shell 进程的 bus name） |
| Object path | `/org/deepin/dde/shell/osd` |
| Interface | `org.deepin.dde.shell.osd` |
| Bus | Session |

该接口提供与 `org.deepin.dde.Osd1` 相同的 `ShowOSD` 方法，调用示例：

```bash
gdbus call --session \
  --dest org.deepin.dde.shell \
  --object-path /org/deepin/dde/shell/osd \
  --method org.deepin.dde.shell.osd.ShowOSD "SwitchWM3D"
```

## 方法、属性与信号

### OSD 显示

#### ShowOSD

根据 OSD 类型标识触发对应的屏幕提示显示。

- **功能**: 根据 OSD 类型标识触发对应的屏幕提示显示
- **触发条件**: 系统服务或硬件事件（如音量键、亮度键、快捷键）需要展示 OSD 时调用
- **使用场景**: 音量调节、亮度调节、WLAN 开关、飞行模式切换、电源模式切换、窗口特效切换等
- **输入参数**:
  - `text`（string, 类型 `s`）：OSD 类型标识
- **返回值**: 无

**支持的选项**（来源于 dde-shell 源码 `panels/notification/osd/` 下各 applet 的 `match()` / `types` / `osdTypeModel`）:

音频：
- `AudioUp` — 音量增大
- `AudioDown` — 音量减小
- `AudioMute` — 静音
- `AudioUpAsh` — 音量增大（置灰）
- `AudioDownAsh` — 音量减小（置灰）
- `AudioMuteAsh` — 静音（置灰）

亮度：
- `BrightnessUp` — 亮度增大
- `BrightnessDown` — 亮度减小
- `BrightnessUpAsh` — 亮度增大（置灰）
- `BrightnessDownAsh` — 亮度减小（置灰）

开关与状态：
- `WLANOn` — WLAN 开启
- `WLANOff` — WLAN 关闭
- `CapsLockOn` — 大写锁定开启
- `CapsLockOff` — 大写锁定关闭
- `NumLockOn` — 数字键盘开启
- `NumLockOff` — 数字键盘关闭
- `TouchpadOn` — 触摸板开启
- `TouchpadOff` — 触摸板关闭
- `TouchpadToggle` — 触摸板切换
- `FnToggle` — Fn 键切换
- `AirplaneModeOn` — 飞行模式开启
- `AirplaneModeOff` — 飞行模式关闭
- `AudioMicMuteOn` — 麦克风静音
- `AudioMicMuteOff` — 麦克风取消静音
- `CameraOn` — 摄像头开启
- `CameraOff` — 摄像头关闭

电源模式：
- `balance` — 平衡模式
- `powersave` — 省电模式
- `performance` — 高性能模式

窗口特效：
- `SwitchWM3D` — 窗口特效已启用
- `SwitchWM2D` — 窗口特效已关闭
- `SwitchWMError` — 窗口特效启用失败
- `SwitchWM` — 切换窗口特效

显示与布局：
- `SwitchMonitors` — 切换显示器
- `DirectSwitchLayout` — 直接切换布局
- `SwitchLayout` — 切换键盘布局

```bash
gdbus call --session \
  --dest org.deepin.dde.Osd1 \
  --object-path / \
  --method org.deepin.dde.Osd1.ShowOSD "SwitchWM3D"
```

---
