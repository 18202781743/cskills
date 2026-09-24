---
name: deepin-face
description: 提供系统级人脸录入、验证、列出、重命名、删除及默认设备与服务设置的 D-Bus 接口
Categories:
  - Settings
---

# deepin-face

deepin-face 是 DDE 的人脸识别组件，通过 System 总线提供系统级人脸录入、验证、列出、重命名、删除及默认设备与服务设置能力。其中录入、重命名、删除操作需要 polkit 提权。

## D-Bus 接口

### 人脸识别管理

提供人脸录入、验证、列出、重命名、删除及默认设备与服务设置能力，所有接口面向系统全局用户的人脸数据管理。

详见 [com.deepin.daemon.Authenticate.Face.md](references/dbus/com.deepin.daemon.Authenticate.Face.md)
