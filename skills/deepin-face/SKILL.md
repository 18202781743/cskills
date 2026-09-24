---
name: deepin-face
description: deepin-face 是 DDE 的人脸识别组件，通过 System 总线提供全局的人脸录入、验证、列出、重命名、删除及默认设备与服务设置的 D-Bus 接口。其中录入、重命名、删除操作需要 polkit 提权
Categories:
  - Settings
---

# deepin-face

deepin-face 是 DDE 的人脸识别组件，通过 System 总线提供全局的人脸录入、验证、列出、重命名、删除及默认设备与服务设置能力。所有接口面向系统全局用户的人脸数据管理，其中录入、重命名、删除操作需要 polkit 提权。

## D-Bus 接口

### 人脸识别管理

提供全局的人脸录入、验证、列出、重命名、删除及默认设备与服务设置能力，面向系统全局用户的人脸数据管理。其中录入、重命名、删除操作需要 polkit 提权。

详见 [org.deepin.dde.Authenticate1.Face.md](references/dbus/org.deepin.dde.Authenticate1.Face.md)
