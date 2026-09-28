# 导出类型介绍

xdg-desktop-portal-dde 通过 DBus 接口提供截图、通知、文件选择、壁纸设置、屏幕共享、远程桌面、访问控制、设置、后台运行、密钥、全局快捷键和锁定门户能力。

## org.freedesktop.impl.portal.desktop.dde

### 定位

DDE 的 XDG Desktop Portal 后端接口，面向 xdg-desktop-portal 前端，实现 freedesktop 门户规范中定义的桌面功能接口。

### 功能能力总结

实现以下门户接口：

- `org.freedesktop.impl.portal.Screenshot`：截图接口，提供屏幕截图能力。
- `org.freedesktop.impl.portal.Notification`：通知接口，提供桌面通知发送能力。
- `org.freedesktop.impl.portal.FileChooser`：文件选择接口，提供文件打开和保存对话框能力。
- `org.freedesktop.impl.portal.Wallpaper`：壁纸设置接口，提供桌面壁纸设置能力。
- `org.freedesktop.impl.portal.ScreenCast`：屏幕共享接口，提供屏幕内容共享能力。
- `org.freedesktop.impl.portal.RemoteDesktop`：远程桌面接口，提供远程桌面控制能力。
- `org.freedesktop.impl.portal.Access`：访问控制接口，提供资源访问授权能力。
- `org.freedesktop.impl.portal.Settings`：设置接口，提供桌面设置读取能力。

### 使用场景

需要通过门户规范接口在沙箱应用中执行截图、发送通知、选择文件、设置壁纸、共享屏幕、远程控制桌面、请求访问授权或读取桌面设置时。

## org.freedesktop.Notifications

### 定位

freedesktop 通知规范接口，面向需要发送桌面通知的调用者。

### 功能能力总结

提供符合 freedesktop 通知规范的通知发送能力。

### 使用场景

需要通过 freedesktop 通知规范接口发送桌面通知时。
